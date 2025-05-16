from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from kafka import KafkaConsumer
import json

# Initialiser une session Spark
spark = SparkSession.builder \
    .appName("Fraud Detection") \
    .getOrCreate()

# Consommateur Kafka pour lire les données en temps réel
consumer = KafkaConsumer('transactions',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Ouvrir un fichier JSON pour enregistrer les alertes
with open("fraud_alerts.json", "a") as alert_file:
    for message in consumer:
        transaction = message.value
        print(f"Transaction reçue: {transaction}")

        # Transformer la transaction en un DataFrame PySpark
        df = spark.createDataFrame([transaction])

        # Appliquer un traitement de base avant d'utiliser le modèle
        assembler = VectorAssembler(inputCols=['Amount', 'Time'], outputCol='features')
        assembled_data = assembler.transform(df)

        # Appliquer un modèle (ex: KMeans)
        kmeans = KMeans(k=2, seed=1, featuresCol='features', predictionCol='prediction')
        model = kmeans.fit(assembled_data)
        result = model.transform(assembled_data)

        # Vérification si la transaction est frauduleuse
        for row in result.collect():
            if row['prediction'] == 1:  # Si le cluster indique une anomalie
                # Ajouter un champ d'alerte à la transaction
                transaction['alert'] = "Fraud Detected"
                print(f"Alerte : {transaction}")

                # Enregistrer la transaction avec alerte dans le fichier JSON
                json.dump(transaction, alert_file)
                alert_file.write("\n")
                alert_file.flush()
# Real-time-fraud-detection
https://medium.com/@deepeshn1988/introduction-to-fraud-detection-systems-1786d696617

Ce projet illustre la détection de fraudes sur transactions financières à l’aide d’un modèle de machine learning (LightGBM) et du modèle deep learning (MLP) entraîné sur un jeu de données de fraude par carte bancaire. Il propose également une API REST avec Flask pour prédire la fraude sur de nouvelles transactions et un système de visualisation en temps réel des fraudes détectées sur une carte interactive via WebSocket et amCharts.


## Fonctionnalités principales

- Chargement et prétraitement du dataset de fraude (déséquilibré).  
- Entraînement d’un modèle LightGBM pour détecter les transactions frauduleuses.  
- API REST pour faire des prédictions sur de nouvelles transactions.  
- Système de visualisation temps réel des fraudes détectées sur une carte interactive (amCharts) via WebSocket.  
- Tests de charge simple pour évaluer les performances de l’API.

## Technologies utilisées

- Python 3.6+  
- LightGBM (gradient boosting)
- MLP  
- Flask & Flask-SocketIO  
- SQLite (base de données locale)  
- JavaScript (amCharts, socket.io-client)  
- Jupyter Notebook (pour exploration et tests)









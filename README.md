# Real-time-fraud-detection
https://medium.com/@deepeshn1988/introduction-to-fraud-detection-systems-1786d696617

Ce projet illustre la détection de fraudes sur transactions financières à l’aide d’un modèle de machine learning (LightGBM) et du modèle deep learning (MLP) entraîné sur un jeu de données de fraude par carte bancaire. Il propose également une API REST avec Flask pour prédire la fraude sur de nouvelles transactions et un système de visualisation en temps réel des fraudes détectées sur une carte interactive via WebSocket et amCharts.

Fonctionnalités principales
Chargement et prétraitement du dataset de fraude (déséquilibré).

Entraînement d’un modèle LightGBM pour détecter les transactions frauduleuses.

API REST pour faire des prédictions sur de nouvelles transactions.

Système de visualisation temps réel des fraudes détectées sur une carte interactive (amCharts) via WebSocket.

Tests de charge simple pour évaluer les performances de l’API.

Technologies utilisées
Python 3.6+

LightGBM (gradient boosting)

Flask & Flask-SocketIO

SQLite (base de données locale)

JavaScript (amCharts, socket.io-client)

Jupyter Notebook (pour exploration et tests)

Installation
Cloner le dépôt

bash
Copier
git clone https://github.com/ton-utilisateur/ton-projet-fraude.git
cd ton-projet-fraude
Créer un environnement virtuel et installer les dépendances

bash
Copier
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
Générer la base de données SQLite en exécutant le notebook data_prep.ipynb

Lancer le serveur Flask (API + WebSocket)

bash
Copier
python api.py
Accéder à la page web de visualisation à l’adresse :

bash
Copier
http://localhost:5000/map
Usage
Envoyer des transactions au endpoint /predict pour obtenir une prédiction de fraude.

Envoyer des transactions au endpoint /predict_map pour déclencher une mise à jour en temps réel de la carte.

Visualiser en temps réel les fraudes détectées via la carte interactive sur /map.

Structure du projet
bash
Copier
/api.py             # API Flask + WebSocket
/data_prep.ipynb     # Notebook de préparation des données et création SQLite
/utils.py           # Fonctions utilitaires (train/test split, métriques, etc.)
/static/            # CSS, JS, amCharts et scripts frontend (frauddetection.js)
/templates/         # Templates HTML (index.html, map.html)
/requirements.txt   # Dépendances Python
/README.md          # Ce fichier
Tests et Performances
Un test de charge simple est implémenté avec aiohttp pour simuler plusieurs requêtes concurrentes.

Le temps moyen de réponse pour 10 requêtes est d’environ 300ms (30ms par requête).

Notes importantes
Le dataset est fortement déséquilibré, ce qui impacte les métriques (précision, rappel, F1).

Le seuil de décision pour classifier une transaction peut être ajusté via la fonction binarize_prediction pour optimiser le compromis entre faux positifs et faux négatifs.

La visualisation temps réel utilise Socket.IO pour une connexion WebSocket persistante.

Références
LightGBM Documentation

Flask-SocketIO Documentation

amCharts Maps

Article original de Deepesh Nair sur Medium (2018)

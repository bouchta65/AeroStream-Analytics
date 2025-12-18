# Projet : AeroStream Analytics

## Contexte

AeroStream souhaite développer un système intelligent capable de **classifier automatiquement les avis clients** relatifs aux services des compagnies aériennes.  
L’objectif principal est d’**analyser le niveau de satisfaction des clients** à partir des données textuelles issues des avis utilisateurs, aussi bien en **batch** qu’en **temps réel (streaming)**.

---

## Objectifs du projet

Le système devra permettre de :

- Collecter et prétraiter les avis clients,
- Analyser automatiquement le **sentiment** et la **satisfaction client**,
- Générer des **indicateurs de performance (KPI)** par compagnie aérienne,
- Visualiser les résultats via un **tableau de bord interactif**,
- Automatiser l’ensemble du pipeline de traitement.

---

## Architecture globale

Le projet est structuré en deux grandes parties :

- **Traitement Batch** : préparation des données, entraînement et évaluation des modèles.
- **Traitement Streaming** : prédiction en temps réel, stockage et visualisation des résultats.

L’orchestration globale est assurée par **Apache Airflow**.

---

## Partie Batch

### 1. Chargement des données
- Importation du dataset **US Airlines Sentiment** depuis Hugging Face :
  - Dataset : `7Xan7der7/us_airline_sentiment`

### 2. Analyse exploratoire des données (EDA)
- Étude de la répartition des classes (positif, négatif, neutre),
- Analyse des distributions,
- Calcul des statistiques descriptives principales.

### 3. Nettoyage des données
- Suppression des doublons,
- Gestion des valeurs manquantes,
- Nettoyage du texte :
  - Suppression des URLs,
  - Suppression des mentions,
  - Suppression de la ponctuation,
  - Suppression des caractères spéciaux.

### 4. Normalisation des données
- Conversion de l’ensemble du texte en **minuscules** pour homogénéiser les données.

### 5. Génération des embeddings
- Utilisation de **Sentence Transformers**,
- Modèle recommandé :
  - `paraphrase-multilingual-MiniLM-L12-v2`
- Possibilité d’utiliser d’autres modèles disponibles sur Hugging Face.

### 6. Sauvegarde des métadonnées
- Stockage des informations suivantes :
  - Identifiant de l’avis,
  - Label (sentiment).

### 7. Stockage des embeddings
- Enregistrement des vecteurs et de leurs métadonnées dans **ChromaDB** :
  - Une collection pour les données d’entraînement,
  - Une collection pour les données de test.

### 8. Entraînement des modèles
- Récupération des embeddings depuis ChromaDB,
- Entraînement de modèles de classification de sentiment.

### 9. Évaluation et sauvegarde du modèle
- Évaluation des performances (accuracy, precision, recall, etc.),
- Sélection et sauvegarde du **meilleur modèle** pour la prédiction future.

---

## Partie Streaming

### 1. Récupération des données en micro-batch
- Collecte continue des avis clients via une **API**.

### 2. Préparation des données
- Nettoyage et prétraitement des nouveaux avis,
- Transformation des textes pour la prédiction des sentiments.

### 3. Prédiction et stockage des résultats
- Prédiction du sentiment à l’aide du modèle entraîné,
- Enregistrement des résultats dans une base **PostgreSQL**.

### 4. Agrégation des données
Calcul des indicateurs suivants :

- Volume total de tweets par compagnie aérienne,
- Répartition des sentiments par compagnie,
- Taux de satisfaction par compagnie,
- Identification des principales causes de tweets négatifs.

### 5. Visualisation des résultats
- Affichage des données dans un **dashboard Streamlit** interactif,
- KPI affichés :
  - Nombre total de tweets,
  - Nombre de compagnies aériennes,
  - Pourcentage de tweets négatifs.

 Le tableau de bord se met à jour **automatiquement** à chaque nouvelle récupération de données depuis l’API.

### 6. Automatisation
- Orchestration complète du pipeline via **Apache Airflow**,
- Exécution d’un **DAG toutes les minutes** pour :
  - La collecte des données,
  - La prédiction,
  - Le stockage,
  - La mise à jour du dashboard.

---

## Résultat attendu

Un système intelligent, automatisé et scalable permettant :

- L’analyse en temps réel des avis clients,
- Une vision claire de la satisfaction client par compagnie aérienne,
- Une aide à la prise de décision basée sur des données fiables et actualisées.

---

## Technologies principales

- Hugging Face
- Sentence Transformers
- ChromaDB
- PostgreSQL
- Streamlit
- Apache Airflow
- API REST

---

## Auteur

**Projet réalisé dans le cadre de AeroStream Analytics**  
Formation Full Stack & Data / YouCode

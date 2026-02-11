Markdown
# Détection du Stress Abiotique des Mangroves par IA (YOLOv8-OBB) 

Ce projet de recherche vise à automatiser le diagnostic de l'état de santé des mangroves dans la région de **Ganvié (Bénin)**. Nous utilisons l'intelligence artificielle pour identifier les symptômes de stress non-infectieux (salinité, pollution, carences) à partir de photographies de terrain.

## 📌 Contexte du Projet
Les mangroves jouent un rôle écologique crucial, mais sont menacées par des facteurs abiotiques. Ce logiciel permet :
* La détection précise des feuilles via des **Boîtes Englobantes Orientées (OBB)**.
* La classification des pathologies (Chlorose, Nécrose, Stress précoce).
* Le suivi de deux espèces clés : *Rhizophora apiculata*, *Avicennia alba*.

## 🛠️ Architecture Technique
* **Modèle :** YOLOv8-OBB (Ultralytics)
* **Prétraitement :** OpenCV (Normalisation 640x640 et égalisation de contraste CLAHE)
* **Annotation :** Label Studio
* **Langage :** Python 3.9+



## 📂 Structure du Dépôt
* `scripts/` : Contient le pipeline de traitement d'images et les scripts d'entraînement.
* `data/processed/` : Échantillons d'images normalisées prêtes pour l'IA.
* `docs/` : Documentation technique sur les symptômes observés.

## 🚀 Installation et Utilisation


### 1. Cloner le projet
```bash
git clone [https://github.com/VOTRE_PSEUDO/mangrove-stress-detection.git](https://github.com/VOTRE_PSEUDO/mangrove-stress-detection.git)
cd mangrove-stress-detection
2. Installer les dépendances
Bash
pip install -r requirements.txt
3. Lancer le prétraitement
Pour normaliser les nouvelles images de terrain :

Bash
python scripts/preprocessing.py
📊 État d'avancement
[x] Constitution du dataset initial (300 images).

[x] Développement du script de prétraitement (OpenCV).

[x] Configuration de l'environnement d'annotation (OBB).

[ ] Finalisation de la labellisation.

[ ] Premier entraînement du modèle.

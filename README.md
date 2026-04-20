# Security Tools (ENSA S2)

Ce projet est une application web simple permettant de réaliser des opérations de sécurité de base : cryptage, décryptage, hachage et comparaison de hashs.

## Fonctionnalités
- **Cryptage** : Utilise le chiffre de César avec une clé aléatoire.
- **Décryptage** : Permet de décrypter un texte avec une clé fournie.
- **Hachage** : Génère un hash SHA-256 d'un texte.
- **Comparaison** : Vérifie si un texte correspond à un hash donné.

## Technologies utilisées
- **Backend** : Flask (Python)
- **Frontend** : HTML/JS/CSS (Nginx)
- **Conteneurisation** : Docker & Docker Compose

## Installation et Lancement

### Avec Docker (Recommandé)
Lancez simplement la commande suivante à la racine du projet :
```bash
docker-compose up --build
```
- **Frontend** : [http://localhost:8080](http://localhost:8080)
- **Backend** : [http://localhost:8000](http://localhost:8000)

### Sans Docker
1. **Backend** :
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```
2. **Frontend** :
   Ouvrez le fichier `frontend/index.html` dans votre navigateur ou utilisez un serveur local (ex: Live Server).

## Structure du Projet
```text
.
├── backend/            # Application Flask
│   ├── utils/
│   │   └── tools.py    # Logique de cryptage/hachage
│   └── app.py          # API Routes
├── frontend/           # Interface utilisateur
│   ├── src/js/         # Logique JavaScript
│   └── index.html      # Page d'accueil
└── docker-compose.yml  # Configuration Docker
```

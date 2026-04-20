# TP Sécurité

Ce TP est divisé en deux parties : une application console (Exercice 1) et une application web complète (Exercice 2). Les deux parties partagent la même logique de sécurité sécurisée.

## Fonctionnalités Communes
- **Chiffrement XOR** : Utilise une clé sécurisée générée aléatoirement.
- **Déchiffrement** : Restaure le texte original via la clé fournie.
- **Hachage PBKDF2** : Utilise SHA-256 avec un sel (salt) pour une sécurité maximale.
- **Comparaison de Hash** : Vérification sécurisée de l'intégrité des données.

---

## Exercice 1 : Application Console
Une interface en ligne de commande pour tester rapidement les fonctions de sécurité.

### Lancement
```bash
python console/main.py
```

---

## Exercice 2 : Application Web
Une architecture complète composée d'un backend Flask et d'un frontend HTML/JS.

### Installation et Lancement

#### 1. Avec Docker (Recommandé)
```bash
docker-compose up --build
```
- **Frontend** : [http://localhost:8080](http://localhost:8080)
- **Backend** : [http://localhost:8000](http://localhost:8000)

#### 2. Sans Docker
- **Backend** :
  ```bash
  cd backend
  pip install -r requirements.txt
  python app.py
  ```
- **Frontend** : Ouvrez `frontend/index.html` dans un navigateur.

---

## Structure du TP
```text
.
├── console/            # Exercice 1 : Application Console
│   └── main.py
├── backend/            # Exercice 2 : API Flask
│   ├── utils/
│   │   └── tools.py    # Logique commune de sécurité
│   └── app.py
├── frontend/           # Exercice 2 : Interface Web
│   ├── src/
│   │   ├── js/
│   │   └── style.css
│   └── index.html
└── docker-compose.yml
```

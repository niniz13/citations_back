# Back Quizz documentation
## Introduction à Django

[Django](https://www.djangoproject.com/) est un framework web en Python qui facilite le développement rapide et propre d'applications web. Il suit le principe du modèle-vue-contrôleur (MVC) et inclut un ORM (Object-Relational Mapping) pour simplifier l'interaction avec la base de données.

### Installation

Pour commencer avec Django, vous devez installer Python et Django. Vous pouvez installer Django en utilisant `pip`, le gestionnaire de paquets de Python.

```bash
pip install django
```

### Création d'un projet Django

Un projet Django est un ensemble d'applications qui fonctionnent ensemble. Vous pouvez créer un projet en utilisant la commande suivante :

```bash
django-admin startproject monprojet
```

Cela créera un répertoire monprojet avec la structure de base d'un projet Django.

### Création d'une application

Une application Django est une composante réutilisable d'un projet. Vous pouvez créer une application en utilisant la commande suivante :

```bash
cd monprojet
python manage.py startapp monapp
```

Cela créera un répertoire monapp avec la structure de base d'une application Django.

### Modèles et Migrations

Les modèles Django sont des classes Python qui définissent la structure de la base de données. Après avoir défini vos modèles, vous devez créer des migrations pour appliquer ces changements à la base de données.

```bash
python manage.py makemigrations
python manage.py migrate
```

### Création d'administrateurs

Django fournit une interface d'administration automatique basée sur les modèles définis. Pour créer un superutilisateur pour cette interface, utilisez la commande suivante :

```bash
python manage.py createsuperuser
```

Suivez les instructions pour définir un nom d'utilisateur, un email et un mot de passe.

### Développement du serveur

Django inclut un serveur de développement pour faciliter le développement et les tests. Vous pouvez le démarrer avec la commande :

```bash
python manage.py runserver
```

### Convert Postman Collection to OpenAPI Yaml
Download this tool:

```bash
npm i postman-to-openapi -g
```

On Postman Click on Export and export the collections as JSON. Then on CLI run:

```bash
p2o ./path/to/PostmantoCollection.json -f ./out_openapi_.yml
```

This will create the OpenAPI Schema at out_openapi_.yml.

Visitez ensuite http://localhost:8000/ dans votre navigateur pour voir votre application.

### Vue et Routage

Django utilise le système de routage pour gérer les différentes vues de votre application. Les vues traitent les requêtes HTTP et renvoient les réponses appropriées.

### URLconf

L'URLconf est un fichier de configuration qui mappe les URL aux vues. Vous pouvez définir vos URL dans le fichier urls.py de votre application.

### Templates

Les templates Django sont des fichiers HTML avec des balises spéciales. Ils sont utilisés pour générer dynamiquement du contenu HTML.

### API

Exemple d'url pour récupérer les questin de la catégorie Sports de difficulté dur :

http://127.0.0.1:8000/quizz/get-quiz-questions/?difficulty=hard&category=Sports

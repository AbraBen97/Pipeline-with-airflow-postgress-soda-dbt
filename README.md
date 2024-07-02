
# Pipeline Airflow, Postgres, Soda et dbt

Ce fichier vous permet de mettre en place une pipeline avec Airflow, Postgres, Soda et dbt.

## Pré-requis

Assurez-vous d'avoir Docker et Docker Compose installés sur votre machine.

## Installation

### Étape 1 : Cloner le projet

Clonez ce projet depuis cette page :

```bash
git clone [URL_DU_PROJET]
cd [NOM_DU_PROJET]
```

### Étape 2 : Créer un fichier .env

Créez un fichier `.env` à la racine du projet et ajoutez les lignes suivantes :

```bash
AIRFLOW_UID=1000
AIRFLOW_IMAGE_NAME=mon_image
```

### Étape 3 : Obtenir une clé Soda

Rendez-vous sur la page [Soda Cloud](https://cloud.soda.io/) et générez une clé API.

### Étape 4 : Configurer Soda

Dans le fichier `/dossier/soda/configuration/configuration.yml`, ajoutez votre clé API.

```yaml
  host: YOUR HOST
  api_key_id: YOUR API KEY ID
  api_key_secret: YOUR API KEY
```

### Étape 5 : Démarrer les services

Accédez à votre terminal et exécutez la commande suivante :

```bash
docker compose up -d
```

### Étape 6 : Accéder à Airflow

Ouvrez votre navigateur et allez à l'adresse suivante : [localhost:8080](http://localhost:8080)

## Utilisation

1. Connectez-vous à l'interface d'Airflow.
2. Configurez vos connexions et variables nécessaires pour Postgres, Soda et dbt.
3. Exécutez vos DAGs pour démarrer la pipeline.

## Support

Pour toute question ou problème, veuillez ouvrir une issue sur la page GitHub du projet.

## Félicitations

Vous avez réussi à mettre en place votre pipeline avec Airflow, Postgres, Soda et dbt ! 🎉


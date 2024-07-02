
# Pipeline Airflow, Postgres, Soda et dbt

This file guides you through setting up a pipeline with Airflow, Postgres, Soda, and dbt.


## Prerequisites

Ensure you have Docker and Docker Compose installed on your machine.


## Installation

### Step 1: Clone the Project

Clone this project from this page:


```bash
git clone [URL_DU_PROJET]
cd [NOM_DU_PROJET]
```

### Step 2: Create a .env File

Create a `.env`  file at the root of the project and add the following lines:

```bash
AIRFLOW_UID=1000
AIRFLOW_IMAGE_NAME=mon_image
```

### Step 3: Obtain a Soda Key

Go to the [Soda Cloud](https://cloud.soda.io/) , add your API key:

### Step 4: Configure Soda

In the file `/dossier/soda/configuration/configuration.yml`, ajoutez votre clé API.

```yaml
  host: YOUR HOST
  api_key_id: YOUR API KEY ID
  api_key_secret: YOUR API KEY
```

### Step 5: Start the Services

Open your terminal and run the following command:

```bash
docker compose up -d
```

### Step 6: Access Airflow

Open your browser and go to the following address: [localhost:8080](http://localhost:8080)

## Usage

1. Log in to the Airflow interface.
2. Configure the necessary connections and variables for Postgres, Soda, and dbt
3. Run your DAGs to start the pipeline.

## Support

For any questions or issues, please open an issue on the project's GitHub page.

## Congratulations

You have successfully set up your pipeline with Airflow, Postgres, Soda, and dbt! 🎉



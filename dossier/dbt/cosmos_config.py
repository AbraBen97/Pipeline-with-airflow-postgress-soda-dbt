from cosmos.config import ProfileConfig, ProjectConfig, ExecutionConfig
from pathlib import Path


DBT_CONFIG = ProfileConfig(
    profile_name='airflow',
    target_name='dev',
    profiles_yml_filepath='/opt/airflow/dossier/dbt/profiles.yml'
    
)



DBT_PROJECT_CONFIG=ProjectConfig(
    dbt_project_path='/opt/airflow/dossier/dbt/'
)


DBT_EXECUTION_CONFIG = ExecutionConfig(
    dbt_executable_path="/opt/airflow/dbt_env/bin/dbt"
)

# DBT_EXECUTION_CONFIG montre le chemin vers l'environement virtuel dans lequel cosmos est installer
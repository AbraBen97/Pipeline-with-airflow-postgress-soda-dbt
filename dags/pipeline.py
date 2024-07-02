from airflow import DAG  
from airflow.providers.postgres.operators.postgres import PostgresOperator # type: ignore
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook # type: ignore
import sys

#custom_path = '/opt/airflow'

#if custom_path not in sys.path:
   # sys.path.append(custom_path)
from dossier.dbt.cosmos_config import DBT_PROJECT_CONFIG, DBT_CONFIG, DBT_EXECUTION_CONFIG

from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.constants import LoadMode
from cosmos.config import RenderConfig, ProjectConfig, ExecutionConfig





from airflow.decorators import task
from datetime import datetime



def copie():
    hook = PostgresHook(postgres_conn_id='postgres')
    hook.copy_expert(
        sql="""
    COPY products (InvoiceNo, StockCode, Description, Quantity,InvoiceDate, UnitPrice, CustomerID, Country)
    FROM stdin
    WITH DELIMITER ','
    CSV HEADER
    """,
        filename='/opt/airflow/dossier/data/online_retail.csv'
    )
    

with DAG(
    "pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    

    create_table = PostgresOperator(
        task_id="cde_la_table",
        postgres_conn_id="postgres",
        sql='''
            CREATE TABLE IF NOT EXISTS products (
                InvoiceNo TEXT ,
                StockCode TEXT ,
                Description TEXT ,
                Quantity INTEGER ,
                InvoiceDate TIMESTAMP ,
                UnitPrice REAL ,
                CustomerID REAL  ,
                Country TEXT 
            );'''  )
    
    
    copie_data = PythonOperator(
        task_id='copie_data',
        python_callable=copie
    )
    


    @task.external_python(python ='/opt/airflow/soda_venv/bin/python')
    
    def check_load():
        PROJECT_ROOT = "/opt/airflow/dossier"
        from dossier.soda.checks.fonction import run_soda_scan
        
        a = run_soda_scan(project_root = PROJECT_ROOT, scan_name ="checks_ingest", checks_subpath="/premier_checks.yml")
    check_load =check_load()
    
    
    
    create_table_country = PostgresOperator(
        task_id="create_table_country",
        postgres_conn_id="postgres",
        sql='country.sql')   
    
    
    
    transform = DbtTaskGroup(   #passe pas quand on lance en local
        group_id='transform',
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        execution_config= DBT_EXECUTION_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/transform']
        ),
        
    )
    
    
    
    @task.external_python(python ='/opt/airflow/soda_venv/bin/python')
    
    def check_transform():
        PROJECT_ROOT = "/opt/airflow/dossier"
        from dossier.soda.checks.fonction import run_soda_scan
        
        a = run_soda_scan(project_root = PROJECT_ROOT, scan_name ="checks_transform", checks_subpath="transform")
    check_transform =check_transform()
    
    
    
    
    report = DbtTaskGroup(
        group_id='report',
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        execution_config= DBT_EXECUTION_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/report']
        ),
        
    )
    
    
    @task.external_python(python ='/opt/airflow/soda_venv/bin/python')
    
    def check_report():
        PROJECT_ROOT = "/opt/airflow/dossier"
        from dossier.soda.checks.fonction import run_soda_scan
        
        a = run_soda_scan(project_root = PROJECT_ROOT, scan_name ="check_report", checks_subpath="report")
    check_report =check_report()
    
    
    
    create_table >> copie_data >> check_load >> create_table_country >> transform >> check_transform >> report >> check_report
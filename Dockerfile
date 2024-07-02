FROM apache/airflow:2.8.0



# Installer les dépendances Python d'Airflow
RUN python -m venv soda_venv && \
    . soda_venv/bin/activate && \
    export PIP_USER=false && \
    pip install --upgrade pip && \
    pip install -i https://pypi.cloud.soda.io soda-postgres && \
    pip install pendulum && \
    pip install soda-core-scientific==3.0.45 && \
    deactivate


# part 3

RUN python -m venv dbt_env && \
    source dbt_env/bin/activate && \
    export PIP_USER=false && \
    pip install --upgrade pip && \
    pip install dbt-postgres && \
    deactivate

RUN pip install astronomer-cosmos 
#installer cosmos dans mon airflow
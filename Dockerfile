FROM astrocrpublic.azurecr.io/runtime:3.1-9

RUN python -m venv ETLVenv && source ETLVenv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake && deactivate
# include/dbt/cosmos_config.py

from pathlib import Path

from cosmos.config import ProfileConfig, ProjectConfig

DBT_CONFIG = ProfileConfig(
    profile_name="retail",
    target_name="dev",
    profiles_yml_filepath=Path("/usr/local/airflow/include/dbt/profiles.yml"),
)

DBT_PROJECT_CONFIG = ProjectConfig(
    dbt_project_path="/usr/local/airflow/include/dbt/",
)

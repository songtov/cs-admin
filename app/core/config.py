from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CS Admin Tool"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Security
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Database
    DATABASE_URL: str

    # Airflow
    AIRFLOW_API_URL: str
    AIRFLOW_USERNAME: str
    AIRFLOW_PASSWORD: str
    DATA_CLONE_DAG_ID: str = "data_clone_dag"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

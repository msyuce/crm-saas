from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "CRM SaaS"
    app_env: str = "development"
    app_debug: bool = True

    database_url: str = "postgresql+asyncpg://kullanici:parola@localhost:5432/saasdb"
    default_language: str = "en"
    supported_languages: str = "en,tr,bg"

    app_secret_key: str = "süper-gizli-anahtar-buraya"
    email_host: str = "smtp.mailserver.com"
    email_port: int = 587
    email_user: str = "your-email@mail.com"
    email_password: str = "your-email-password"
    redis_url: str = "redis://localhost:6379/0"

    class Config:
        env_file = ".env"
        extra = "forbid"  # extra env değişkenlerini reddet (güvenli)

settings = Settings()


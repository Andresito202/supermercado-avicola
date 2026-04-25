from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str = "avicola_user"
    DB_PASSWORD: str = "avicola_pass"
    DB_HOST: str = "db"
    DB_PORT: str = "5432"
    DB_NAME: str = "supermercado_avicola"
    DATABASE_URL: str = ""

    SECRET_KEY: str = "clave-secreta-cambiar-en-produccion-2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480

    ADMIN_USERNAME: str = "admin"
    ADMIN_PASSWORD: str = "Admin123!"
    ADMIN_EMAIL: str = "admin@avicola.local"

    @property
    def db_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = [".env", "../.env"]
        extra = "ignore"


settings = Settings()

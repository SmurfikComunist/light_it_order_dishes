from pydantic import BaseSettings


class ServerSettings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool


class Settings(ServerSettings):
    pass


settings: Settings = Settings(_env_file=".env")

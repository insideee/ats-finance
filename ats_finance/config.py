from pydantic import BaseSettings
import os


class Settings(BaseSettings):

    polygon_key: str

    class Config:
        env_file = os.path.join(os.getcwd(), '.env')

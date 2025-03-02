import datetime
import os

import yaml
from pydantic import BaseModel, SecretStr
from dataclasses import dataclass
from loguru import logger


APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(APP_DIR)


@dataclass
class BotConfig(BaseModel):
    token: SecretStr
    admin_ids: list[str]


@dataclass
class DatabaseConfig(BaseModel):
    host: str
    port: int
    user: str
    password: SecretStr
    database: str
    ssl: bool


@dataclass
class AppConfig(BaseModel):
    app_name: str
    secret_key: SecretStr
    bot: BotConfig
    database: DatabaseConfig
    app_dir: str
    project_dir: str


logger.add(
        f"{PROJECT_DIR}/logs/app_{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log",
        rotation="1 day",
        retention="7 days",
        compression="zip",
        level="DEBUG",
    )


def load_config(config_path: str) -> AppConfig:
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            dictionary: dict = yaml.load(stream=file, Loader=yaml.FullLoader)
            dictionary["app_dir"] = APP_DIR
            dictionary["project_dir"] = PROJECT_DIR
            _config: AppConfig = AppConfig.model_validate(dictionary)
        return _config

    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        raise FileNotFoundError
    except yaml.YAMLError as exc:
        logger.error(f"Error parsing config YAML-file: {exc}")
        raise yaml.YAMLError
    except Exception as exc:
        logger.error(f"Error loading config file: {exc}")
        raise Exception


config: AppConfig = load_config(config_path=os.path.join(PROJECT_DIR, "config.yaml"))


__all__ = ["config", "AppConfig", "PROJECT_DIR"]

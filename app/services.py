from flask import Flask
from app.config import AppConfig
from database.pgsql import db
from bot.services import BotService
from app.routers.client import client_bp
# from app.routers.admin import admin_bp
import os
from loguru import logger


Logger = logger


class TechnoStore:
    def __init__(
            self,
            config: AppConfig,
            # bot: BotService
    ):
        self.config = config
        self.app: Flask = self._create_app()
        self._init_db()

    def _create_app(self) -> Flask:
        # Create the Flask app
        app = Flask(
            import_name=self.config.app_name,
            template_folder=os.path.join(self.config.app_dir, "templates"),
            static_folder=os.path.join(self.config.project_dir, "app", "templates", "static"),
        )
        app.secret_key = self.config.secret_key.get_secret_value()
        db_uri = f"postgresql://{self.config.database.user}:{self.config.database.password.get_secret_value()}@{self.config.database.host}:{self.config.database.port}/{self.config.database.database}"
        app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_ECHO"] = True
        return app

    def _init_db(self):
        try:
            db.init_app(self.app)
            # db.create_all()
            # db.session.execute("SELECT 1")
            logger.debug("Database connection successful")
        except Exception as exc:
            logger.error(f"Error connection to database:\n {exc}")

    def _register_blueprint(self,):
        self.app.register_blueprint(client_bp)
        # self.app.register_blueprint(admin_bp)

    def run(
            self,
            debug: bool,
            host: str = "localhost",
            port: int = 1000,
    ):
        self._register_blueprint()
        self.app.run(
            host=host,
            port=port,
            debug=debug,
            # use_reloader=False,
        )

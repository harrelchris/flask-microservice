from flask import Flask

from . import settings


def create_app() -> Flask:
    app = Flask(
        import_name=__name__,
        static_url_path=settings.STATIC_URL_PATH,
        static_folder=settings.STATIC_FOLDER,
        static_host=settings.STATIC_HOST,
        host_matching=settings.HOST_MATCHING,
        subdomain_matching=settings.SUBDOMAIN_MATCHING,
        template_folder=settings.TEMPLATE_FOLDER,
        instance_path=settings.INSTANCE_PATH,
        instance_relative_config=settings.INSTANCE_RELATIVE_CONFIG,
        root_path=settings.ROOT_PATH,
    )

    app.config.from_object(settings)
    app = register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> Flask:
    from src.index.urls import bp as index_bp

    app.register_blueprint(index_bp)
    return app

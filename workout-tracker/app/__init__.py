from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.dashboard import dashboard_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)

    return app

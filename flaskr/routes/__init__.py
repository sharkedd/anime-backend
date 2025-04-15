# routes/__init__.py
from .db_routes import db_bp
from .jikan_api_routes import jikan_bp

def register_routes(app):
    app.register_blueprint(db_bp, url_prefix='/db')
    app.register_blueprint(jikan_bp, url_prefix='/anime')

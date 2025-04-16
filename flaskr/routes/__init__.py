# routes/__init__.py
from .jikan_api_routes import jikan_bp

def register_routes(app):
    app.register_blueprint(jikan_bp, url_prefix='/anime')

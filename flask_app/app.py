import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv
from flask import Blueprint, Flask, jsonify
from flask_cors import CORS
from flask_talisman import Talisman

from frontend import frontend_blueprint

# Load environment variables
load_dotenv()


def create_app(config_name: str = "production") -> Flask:
    """Application factory pattern."""
    app = Flask(__name__)
    
    # Configuration
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        if config_name == "development":
            secret_key = "dev-secret-key"
        else:
            raise RuntimeError("SECRET_KEY environment variable must be set in production.")
    app.config["SECRET_KEY"] = secret_key
    app.config["API_ADDRESS"] = os.getenv("API_ADDRESS", "http://localhost:8000")
    app.config["ENV"] = config_name
    app.config["DEBUG"] = config_name == "development"
    
    # Security headers with Talisman
    if config_name == "production":
        Talisman(
            app,
            force_https=True,
            strict_transport_security=True,
            strict_transport_security_max_age=31536000,
            content_security_policy={
                "default-src": "'self'",
                "script-src": "'self' 'unsafe-inline'",
                "style-src": "'self' 'unsafe-inline'",
            },
        )
    
    # CORS configuration
    CORS(
        app,
        resources={r"/api/*": {"origins": os.getenv("ALLOWED_ORIGINS", "*").split(",")}},
        supports_credentials=True,
    )
    
    # Logging configuration
    setup_logging(app)
    
    # Register blueprints
    app.register_blueprint(frontend_blueprint)
    
    # Health check endpoint
    @app.route("/health")
    def health():
        """Health check endpoint for monitoring."""
        return jsonify({
            "status": "healthy",
            "service": "flask-app",
            "environment": config_name
        }), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        app.logger.warning(f"404 error: {error}")
        return jsonify({"error": "Not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f"500 error: {error}")
        return jsonify({"error": "Internal server error"}), 500
    
    @app.errorhandler(Exception)
    def handle_exception(error):
        app.logger.error(f"Unhandled exception: {error}", exc_info=True)
        return jsonify({"error": "An error occurred"}), 500
    
    return app


def setup_logging(app: Flask) -> None:
    """Configure application logging."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Set logging level based on environment
    log_level = logging.DEBUG if app.config["DEBUG"] else logging.INFO
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_dir / "app.log",
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=10
    )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    file_handler.setLevel(log_level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
    )
    console_handler.setLevel(log_level)
    
    # Configure app logger
    app.logger.setLevel(log_level)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    
    # Log startup
    app.logger.info(f"Application started in {app.config['ENV']} mode")


# Create app instance
app = create_app(os.getenv("FLASK_ENV", "production"))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=app.config["DEBUG"])
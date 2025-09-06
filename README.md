# Flask + uWSGI + Nginx + Certbot Docker Application

[![CI/CD Pipeline](https://github.com/yourusername/yourrepo/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/yourrepo/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Production-ready Flask application with uWSGI, Nginx, and Let's Encrypt SSL certificates, all containerized with Docker.

## 🚀 Features

- **Modern Python**: Python 3.12 with type hints
- **Security First**: Talisman security headers, CORS configuration, SSL/TLS support
- **Production Ready**: uWSGI application server, Nginx reverse proxy
- **Automated SSL**: Let's Encrypt certificate management with Certbot
- **CI/CD Pipeline**: GitHub Actions with testing, linting, and security scanning
- **Code Quality**: Black, isort, flake8, mypy, pre-commit hooks
- **Testing**: Comprehensive test suite with pytest and coverage
- **Monitoring**: Structured logging, health checks, error tracking ready
- **Docker**: Multi-stage builds, security scanning, optimized images

## 📋 Prerequisites

- Docker & Docker Compose
- Python 3.11+ (for local development)
- Domain name (for SSL certificates)

## 🛠️ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

### 2. Setup environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Start with Docker
```bash
# Build and start all services
docker-compose up --build -d

# View logs
docker-compose logs -f
```

### 4. Setup SSL certificates (Production)
```bash
# Edit domain in init-letsencript.sh
nano init-letsencript.sh

# Run certificate initialization
./init-letsencript.sh
```

## 💻 Local Development

### Setup development environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r flask_app/requirements.txt

# Install pre-commit hooks
pre-commit install

# Run the application
cd flask_app
python app.py
```

### Run tests
```bash
# Run all tests with coverage
pytest

# Run specific test file
pytest tests/test_app.py

# Run with verbose output
pytest -v

# Generate HTML coverage report
pytest --cov-report=html
```

### Code formatting and linting
```bash
# Format code with Black
black flask_app/ tests/

# Sort imports
isort flask_app/ tests/

# Lint with flake8
flake8 flask_app/ tests/

# Type checking with mypy
mypy flask_app/

# Run all checks
pre-commit run --all-files
```

## 📁 Project Structure

```
.
├── flask_app/
│   ├── app.py                 # Main application
│   ├── requirements.txt       # Python dependencies
│   ├── uwsgi.ini             # uWSGI configuration
│   └── frontend/
│       ├── __init__.py
│       ├── routes.py         # Route definitions
│       └── api/
│           └── Content.py    # API client
├── tests/
│   ├── conftest.py          # Pytest configuration
│   ├── test_app.py          # Application tests
│   └── test_content.py      # Content API tests
├── data/
│   ├── nginx/
│   │   └── app.conf         # Nginx configuration
│   └── certbot/             # SSL certificates
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD pipeline
├── docker-compose.yml       # Docker services
├── Dockerfile              # Application container
├── init-letsencript.sh    # SSL setup script
├── pyproject.toml         # Python project config
├── .pre-commit-config.yaml # Pre-commit hooks
└── .env.example           # Environment template
```

## 🔧 Configuration

### Environment Variables

See `.env.example` for all available options:

- `FLASK_ENV`: Application environment (production/development)
- `SECRET_KEY`: Flask secret key for sessions
- `API_ADDRESS`: External API endpoint
- `ALLOWED_ORIGINS`: CORS allowed origins
- `DOMAIN`: Your domain for SSL certificates
- `EMAIL`: Email for Let's Encrypt notifications

### Docker Services

- **memberxxl_app**: Flask application on uWSGI
- **nginx**: Reverse proxy and static file server
- **certbot**: SSL certificate management

## 🚢 Deployment

### Production Checklist

- [ ] Set strong `SECRET_KEY` in `.env`
- [ ] Configure proper `ALLOWED_ORIGINS`
- [ ] Update domain in `init-letsencript.sh`
- [ ] Set `FLASK_ENV=production`
- [ ] Configure monitoring (Sentry, New Relic, etc.)
- [ ] Setup backup strategy
- [ ] Configure firewall rules
- [ ] Enable automatic certificate renewal

### Docker Hub Deployment

```bash
# Build and tag image
docker build -t yourusername/flask-app:latest .

# Push to registry
docker push yourusername/flask-app:latest

# Deploy on server
docker-compose pull
docker-compose up -d
```

## 🧪 CI/CD Pipeline

GitHub Actions workflow runs on every push and PR:

1. **Testing**: Multiple Python versions, pytest with coverage
2. **Code Quality**: Black, isort, flake8, mypy
3. **Security**: Trivy, Bandit security scanning
4. **Docker**: Build and push to registry (on master)

## 🔐 Security

- **Dependencies**: Automated vulnerability scanning with Trivy
- **Code**: Static analysis with Bandit
- **Headers**: Security headers with Flask-Talisman
- **HTTPS**: Enforced in production with Let's Encrypt
- **Docker**: Non-root user, minimal base image
- **Secrets**: Environment variables, never in code

## 📊 Monitoring

- **Health Check**: `/health` endpoint for monitoring
- **Logging**: Structured logs with rotation
- **Metrics**: Ready for Prometheus/Grafana integration
- **Error Tracking**: Sentry integration ready

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Development Standards

- Follow PEP 8 and use Black formatter
- Write tests for new features
- Update documentation
- Pass all CI checks

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [uWSGI](https://uwsgi-docs.readthedocs.io/) - Application server
- [Nginx](https://nginx.org/) - Web server
- [Let's Encrypt](https://letsencrypt.org/) - Free SSL certificates
- [Docker](https://www.docker.com/) - Containerization

## 📧 Support

For issues and questions:
- Open an [issue](https://github.com/yourusername/yourrepo/issues)
- Email: support@example.com

---

Made with ❤️ using modern Python and DevOps best practices
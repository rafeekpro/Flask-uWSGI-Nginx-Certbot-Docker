# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Docker Operations
- **Build and start all services**: `docker-compose up --build -d`
- **Start services**: `docker-compose up -d`
- **Stop services**: `docker-compose down`
- **View logs**: `docker-compose logs -f [service_name]`
- **Rebuild Flask app**: `docker-compose build memberxxl_app`

### SSL Certificate Setup
- **Initialize Let's Encrypt certificates**: `./init-letsencript.sh`
  - Edit domains in the script before running
  - Set `staging=1` for testing to avoid rate limits

### Development
- **Run Flask app locally**: `cd flask_app && python app.py`
- **Install Python dependencies locally**: `pip install -r flask_app/requirements.txt`

## Architecture Overview

This is a Flask web application deployed with Docker, using:
- **Flask app** (memberxxl_app service): Python 3.12 application running on uWSGI
- **Nginx**: Reverse proxy handling HTTP/HTTPS traffic
- **Certbot**: Let's Encrypt SSL certificate management

### Key Components

1. **Flask Application Structure**:
   - Main app: `flask_app/app.py`
   - Blueprint-based architecture with frontend module
   - uWSGI configuration: `flask_app/uwsgi.ini` (5 workers, socket on port 5000)

2. **Docker Configuration**:
   - Flask app Dockerfile builds from Python 3.7-slim
   - Services communicate via Docker network
   - Environment variables loaded from `.env` file (API_ADDRESS)

3. **SSL/TLS Setup**:
   - Nginx config: `data/nginx/app.conf`
   - SSL certificates stored in `data/certbot/conf/`
   - Certbot webroot validation via `data/certbot/www/`

4. **Service Communication**:
   - Nginx forwards requests to Flask via uWSGI protocol
   - Flask app name in Docker network: `memberxxl_app:5000`
   - External API endpoint configured via API_ADDRESS env variable
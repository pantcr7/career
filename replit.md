# Career App

## Overview
A Flask-based web application project set up in the Replit environment. This is a starter project ready for career-related features to be added.

## Current State
The application is fully configured and running with:
- Basic Flask web server
- Welcome page at the root route
- Development and production configurations

## Recent Changes
**November 3, 2025**
- Initialized Flask application
- Set up Python 3.11 environment
- Installed Flask and Gunicorn dependencies
- Configured development workflow with auto-reload
- Configured production deployment with Gunicorn
- Created basic welcome page

## Project Architecture

### Tech Stack
- **Backend**: Flask 3.1.2 (Python web framework)
- **WSGI Server**: Gunicorn 23.0.0 (production)
- **Python Version**: 3.11

### Project Structure
```
.
├── app.py              # Main Flask application
├── .gitignore          # Python-specific gitignore
├── pyproject.toml      # Python dependencies (managed by uv)
├── uv.lock             # Dependency lock file
├── .pythonlibs/        # Virtual environment
└── replit.md           # This file
```

### Key Files
- **app.py**: Main Flask application with a simple home route that returns an HTML welcome page
  - Binds to 0.0.0.0:5000 for Replit proxy compatibility
  - Debug mode enabled for development

### Development
- The Flask app runs in debug mode with auto-reload
- Server listens on 0.0.0.0:5000
- Accessible through Replit's webview proxy

### Deployment
- Configured for autoscale deployment
- Uses Gunicorn as production WSGI server
- Command: `gunicorn --bind=0.0.0.0:${PORT:-5000} --reuse-port app:app`
- Binds to Replit's platform-assigned PORT in production, defaults to 5000 for local testing

## Dependencies
Managed via `uv` package manager:
- flask==3.1.2
- gunicorn==23.0.0
- blinker, click, itsdangerous, jinja2, markupsafe, werkzeug (Flask dependencies)

## Getting Started
The application is already configured and running. To extend it:
1. Add new routes in `app.py`
2. Create templates in a `templates/` directory for more complex pages
3. Add static assets in a `static/` directory for CSS, JavaScript, and images

## User Preferences
None specified yet.

# Career App

## Overview
A professional Flask-based career opportunities website. The application showcases job openings, company information, required skills, and provides a modern, responsive user interface for potential candidates.

## Current State
The application is fully configured and running with:
- Professional, modern career website with full responsive design
- Navigation, hero section, about, skills showcase, job listings, and contact sections
- Custom CSS styling with professional color scheme and animations
- Mobile-friendly responsive layout
- Development and production configurations

## Recent Changes
**November 3, 2025**
- Redesigned website with professional, modern UI/UX
- Created comprehensive HTML template with semantic structure
- Developed custom CSS with responsive design and animations
- Implemented job listings section with multiple positions
- Added skills showcase with visual cards
- Integrated smooth scrolling and fade-in animations
- Fixed navigation accessibility issues
- Cleaned up unused files (main.py)

## Project Architecture

### Tech Stack
- **Backend**: Flask 3.1.2 (Python web framework)
- **WSGI Server**: Gunicorn 23.0.0 (production)
- **Python Version**: 3.11

### Project Structure
```
.
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   └── home.html       # Professional career website homepage
├── static/             # Static assets
│   ├── style.css       # Modern CSS styling
│   └── carrer.jpg      # Hero image
├── .gitignore          # Python-specific gitignore
├── pyproject.toml      # Python dependencies (managed by uv)
├── uv.lock             # Dependency lock file
├── .pythonlibs/        # Virtual environment
└── replit.md           # This file
```

### Key Files
- **app.py**: Main Flask application that renders the home template
  - Binds to 0.0.0.0:5000 for Replit proxy compatibility
  - Debug mode enabled for development
- **templates/home.html**: Professional career website with sections for navigation, hero, about, skills, job listings, and contact
  - Semantic HTML5 structure
  - Smooth scrolling navigation
  - Fade-in animations on scroll
- **static/style.css**: Modern, responsive CSS styling
  - CSS custom properties for theming
  - Mobile-first responsive design
  - Professional color scheme and typography

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

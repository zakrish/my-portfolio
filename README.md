# Portfolio & Study to Earn Platform

This repository contains both a static portfolio website and a Django-based Study to Earn application.

## Repository Structure

```
.
├── index.html              # Static portfolio homepage
├── scss/                   # SASS source files for styling
├── css/                    # Compiled CSS files
├── js/                     # JavaScript files
├── images/                 # Image assets
├── webfonts/              # Font files
├── package.json           # NPM dependencies and scripts
└── study_to_earn/         # Django application (see below)
```

## Components

### 1. Static Portfolio Website

A single-page personal portfolio built with:
- HTML5
- Bootstrap 5
- Font Awesome
- Lightbox
- SASS pipeline

**Features:**
- Hero section with typing animation
- About/profile and skill progress sections
- Portfolio gallery with Lightbox overlays
- Services/stats blocks
- Contact form and social links

**Development:**
```bash
# Install dependencies
npm install

# Build CSS (for static portfolio)
npm run sass:build

# Watch for changes
npm run sass:watch
```

### 2. Study to Earn Django Application

A full-featured Django 4.x backend application with PostgreSQL, Redis, and Celery.

**Location:** `/study_to_earn/`

**Features:**
- User management system
- Quiz functionality
- Leaderboard tracking
- Rewards system
- Payment processing
- Advertisement management
- Analytics tracking

**Tech Stack:**
- Django 4.x
- PostgreSQL for database
- Redis for caching and sessions
- Celery for background tasks
- Celery Beat for scheduled tasks
- Django REST Framework for API

**Documentation:** See [study_to_earn/README.md](study_to_earn/README.md) for detailed setup and usage instructions.

## Quick Start

### Prerequisites

- Node.js and npm (for static assets)
- Python 3.8+ (for Django backend)
- PostgreSQL 12+ (for Django backend)
- Redis 6+ (for Django backend)

### Setup Static Portfolio

```bash
# Install npm dependencies
npm install

# Build CSS
npm run sass:build

# Open index.html in a browser
```

### Setup Django Backend

```bash
# Navigate to Django app
cd study_to_earn

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

For complete Django setup instructions, see [study_to_earn/README.md](study_to_earn/README.md).

## SASS Build Integration

The project includes scripts to build SASS for both the static portfolio and Django application:

```bash
# For static portfolio
npm run sass:build        # Build once
npm run sass:watch        # Watch for changes

# For Django application
npm run sass:build:django # Build to study_to_earn/static/css
npm run sass:watch:django # Watch and build to study_to_earn/static/css
```

## Development Workflow

1. **Static Portfolio Changes:**
   - Edit HTML in `index.html`
   - Edit styles in `scss/` directory
   - Run `npm run sass:build` or `npm run sass:watch`
   - Test by opening `index.html` in a browser

2. **Django Backend Changes:**
   - Navigate to `study_to_earn/` directory
   - Activate virtual environment: `source venv/bin/activate`
   - Make code changes
   - Run migrations if models changed
   - Test with `python manage.py runserver`

## Scheduled Tasks (Celery Beat)

The Django application includes scheduled tasks:

- **reset_leaderboard_monthly**: Runs monthly on the 1st at midnight
- **reward_top_users**: Runs monthly on the 1st at 1 AM
- **refresh_daily_questions**: Runs daily at midnight

See the Django README for details on running Celery workers and beat scheduler.

## License

This project is part of Zakari Iliya's portfolio.

## Author

Zakari Iliya

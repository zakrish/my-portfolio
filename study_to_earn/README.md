# Study to Earn - Django Backend

A Django 4.x application for the Study to Earn platform with PostgreSQL, Redis, and Celery integration.

## Features

- **Django 4.x** with split settings (dev/prod)
- **PostgreSQL** database
- **Redis** for caching and session storage
- **Celery** with Beat scheduler for periodic tasks
- **REST API** with Django REST Framework
- **Seven domain apps**: users, quiz, leaderboard, rewards, payments, ads, analytics

## Project Structure

```
study_to_earn/
├── config/              # Project configuration
│   ├── settings/        # Split settings (base, dev, prod)
│   ├── celery.py        # Celery configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI config
├── users/               # User management app
├── quiz/                # Quiz functionality app
├── leaderboard/         # Leaderboard app
├── rewards/             # Rewards system app
├── payments/            # Payment processing app
├── ads/                 # Advertisement management app
├── analytics/           # Analytics tracking app
├── static/              # Static files (CSS, JS)
├── media/               # User-uploaded media files
├── templates/           # Django templates
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── .env.example         # Environment variables template
```

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Redis 6+
- Node.js and npm (for SASS compilation)

## Installation

### 1. Create and activate virtual environment

```bash
cd study_to_earn
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Copy the example environment file and update it with your values:

```bash
cp .env.example .env
```

Edit `.env` and configure:
- `SECRET_KEY`: Generate a secure secret key
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`: PostgreSQL credentials
- `DB_HOST`, `DB_PORT`: Database connection details
- `REDIS_URL`: Redis connection URL

### 4. Set up PostgreSQL database

```bash
# Create the database
createdb study_to_earn

# Or using psql
psql -U postgres
CREATE DATABASE study_to_earn;
\q
```

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 7. Compile SASS styles (optional)

From the project root directory:

```bash
cd ..  # Go to project root
npm install
npm run sass:build:django
```

Or for continuous watching:

```bash
npm run sass:watch:django
```

## Running the Application

### Development Server

```bash
# Make sure you're in the study_to_earn directory with venv activated
python manage.py runserver
```

The application will be available at `http://localhost:8000`

### Celery Worker

In a separate terminal:

```bash
cd study_to_earn
source venv/bin/activate
celery -A config worker --loglevel=info
```

### Celery Beat (Scheduled Tasks)

In another terminal:

```bash
cd study_to_earn
source venv/bin/activate
celery -A config beat --loglevel=info
```

## Scheduled Tasks

The following Celery Beat tasks are configured:

1. **reset_leaderboard_monthly**: Runs on the 1st of each month at midnight
   - Resets the monthly leaderboard

2. **reward_top_users**: Runs on the 1st of each month at 1 AM
   - Rewards the top users on the leaderboard

3. **refresh_daily_questions**: Runs daily at midnight
   - Refreshes the daily quiz questions

## Configuration

### Environment Variables

The application uses different settings based on the `DJANGO_ENV` environment variable:

- `dev` (default): Development settings with DEBUG=True
- `prod`: Production settings with security enhancements

### Development Settings (`config/settings/dev.py`)

- DEBUG enabled
- CORS allows all origins
- Email backend uses console
- Relaxed security settings

### Production Settings (`config/settings/prod.py`)

- DEBUG disabled
- HTTPS/SSL enforcement
- Secure cookies
- CSRF protection
- Email backend uses SMTP

## Static Files

Static files are managed by WhiteNoise for efficient serving:

```bash
# Collect static files for production
python manage.py collectstatic
```

## Testing

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test users
```

## API Documentation

The REST API is available at `/api/` and uses Django REST Framework.

Access the browsable API at `http://localhost:8000/api/`

## Admin Interface

Access the Django admin at `http://localhost:8000/admin/`

## Production Deployment

### Using Gunicorn

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

### Environment Setup

1. Set `DJANGO_ENV=prod`
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Set up PostgreSQL and Redis
5. Run migrations
6. Collect static files
7. Start Gunicorn, Celery worker, and Celery beat

## Troubleshooting

### Database Connection Issues

- Ensure PostgreSQL is running: `sudo systemctl status postgresql`
- Check credentials in `.env` file
- Verify database exists: `psql -U postgres -l`

### Redis Connection Issues

- Ensure Redis is running: `sudo systemctl status redis`
- Check REDIS_URL in `.env`
- Test connection: `redis-cli ping`

### Celery Not Picking Up Tasks

- Ensure Redis is running
- Restart Celery worker
- Check task names match in `config/celery.py`

## Development Workflow

1. Create feature branch
2. Make changes to code
3. Run migrations if models changed: `python manage.py makemigrations`
4. Apply migrations: `python manage.py migrate`
5. Test changes
6. Commit and push

## License

This project is part of the Study to Earn platform.

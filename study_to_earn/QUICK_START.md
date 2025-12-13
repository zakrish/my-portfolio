# Quick Start Guide

## Initial Setup (One Time)

```bash
cd study_to_earn

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env
# Edit .env with your database and Redis settings

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

## Daily Development

### Terminal 1: Django Server
```bash
cd study_to_earn
source venv/bin/activate
python manage.py runserver
```
Access at: http://localhost:8000/

### Terminal 2: Celery Worker
```bash
cd study_to_earn
source venv/bin/activate
celery -A config worker --loglevel=info
```

### Terminal 3: Celery Beat (for scheduled tasks)
```bash
cd study_to_earn
source venv/bin/activate
celery -A config beat --loglevel=info
```

### Terminal 4: SASS Watcher (if working on styles)
```bash
# From project root
npm run sass:watch:django
```

## Common Commands

```bash
# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell
python manage.py shell

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic

# Run tests
python manage.py test

# Check for issues
python manage.py check
```

## Environment Variables

Required in `.env`:
- `DJANGO_ENV` - Set to `dev` or `prod`
- `SECRET_KEY` - Django secret key
- `DB_NAME`, `DB_USER`, `DB_PASSWORD` - PostgreSQL credentials
- `DB_HOST`, `DB_PORT` - Database connection
- `REDIS_URL` - Redis connection string

## URLs

- Homepage/Health Check: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/

## Scheduled Tasks

Three Celery Beat tasks are configured:
1. **reset_leaderboard_monthly** - 1st of month at 00:00
2. **reward_top_users** - 1st of month at 01:00
3. **refresh_daily_questions** - Daily at 00:00

## Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'django'`
- **Solution:** Activate virtual environment: `source venv/bin/activate`

**Issue:** Database connection error
- **Solution:** Check PostgreSQL is running and .env credentials are correct

**Issue:** Redis connection error
- **Solution:** Ensure Redis is running: `redis-cli ping` should return PONG

**Issue:** Static files not found
- **Solution:** Run `python manage.py collectstatic` or check STATIC_ROOT

## Production Deployment

1. Set `DJANGO_ENV=prod` in environment
2. Set strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Set up PostgreSQL and Redis
5. Run migrations
6. Collect static files
7. Use gunicorn: `gunicorn config.wsgi:application`
8. Start Celery worker and beat in background

See `README.md` for detailed documentation.

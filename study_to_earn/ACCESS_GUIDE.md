# How to Access and Preview Study to Earn Django

## 🚀 Quick Access (5 Steps)

### 1. Navigate to the Project
```bash
cd /home/engine/project/study_to_earn
```

### 2. Create Virtual Environment (if not exists)
```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```

Then open your browser to: **http://localhost:8000**

---

## 📋 Full Setup Guide

### Step 1: Set Up Environment

```bash
# Navigate to project
cd /home/engine/project/study_to_earn

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# For quick preview, you can use the defaults (SQLite)
# Or edit .env if you want to use PostgreSQL
```

**Default .env for quick preview (no PostgreSQL needed):**
```bash
echo "DJANGO_ENV=dev
SECRET_KEY=django-insecure-dev-key-for-preview-only
DEBUG=True" > .env
```

### Step 3: Run Migrations

```bash
# Create database tables
python manage.py migrate
```

### Step 4: Create Admin User (Optional)

```bash
# Create superuser for admin access
python manage.py createsuperuser

# Enter:
# - Username: admin
# - Email: admin@example.com
# - Password: admin123 (or your choice)
```

### Step 5: Start Server

```bash
# Run the development server
python manage.py runserver 0.0.0.0:8000
```

---

## 🌐 Available URLs

Once the server is running, you can access:

### Main Application
- **Homepage/Health Check:** http://localhost:8000/
  - Shows JSON status of the application

### Admin Panel
- **Django Admin:** http://localhost:8000/admin/
  - Login with superuser credentials
  - Manage all models (users, quiz, leaderboard, etc.)

---

## 🎨 What You'll See

### 1. Health Check Endpoint (/)
```json
{
  "status": "healthy",
  "django_version": "4.x",
  "database": "PostgreSQL",
  "cache": "Redis",
  "celery": "configured"
}
```

### 2. Admin Panel (/admin/)
- User Management
- Quiz Management
- Leaderboard Entries
- Rewards System
- Payments
- Advertisements
- Analytics Dashboard

---

## 🛠️ Using with PostgreSQL (Optional)

If you want to use PostgreSQL instead of SQLite:

### 1. Install PostgreSQL
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

### 2. Start PostgreSQL
```bash
sudo service postgresql start
```

### 3. Create Database
```bash
sudo -u postgres createdb study_to_earn
```

### 4. Configure .env
```bash
DJANGO_ENV=dev
SECRET_KEY=your-secret-key-here
DEBUG=True

DB_NAME=study_to_earn
DB_USER=postgres
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

### 5. Configure PostgreSQL Authentication
```bash
sudo sed -i 's/scram-sha-256/trust/g' /etc/postgresql/*/main/pg_hba.conf
sudo service postgresql restart
```

### 6. Run Migrations
```bash
python manage.py migrate
```

---

## 🔧 Using with Redis and Celery (Optional)

For full functionality with background tasks:

### 1. Install Redis
```bash
sudo apt-get install redis-server
sudo service redis-server start
```

### 2. Start Celery Worker (in new terminal)
```bash
cd /home/engine/project/study_to_earn
source venv/bin/activate
celery -A config worker --loglevel=info
```

### 3. Start Celery Beat (in another terminal)
```bash
cd /home/engine/project/study_to_earn
source venv/bin/activate
celery -A config beat --loglevel=info
```

---

## 📱 Quick Preview Commands

### Minimal Setup (SQLite, No Redis)
```bash
cd /home/engine/project/study_to_earn
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

### Full Setup (PostgreSQL + Redis)
```bash
# Install services
sudo apt-get update
sudo apt-get install postgresql redis-server

# Start services
sudo service postgresql start
sudo service redis-server start

# Create database
sudo -u postgres createdb study_to_earn

# Setup Django
cd /home/engine/project/study_to_earn
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with database settings
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

---

## 🎯 Testing the Application

### 1. Health Check
```bash
curl http://localhost:8000/
```

### 2. Admin Panel
1. Go to http://localhost:8000/admin/
2. Login with superuser credentials
3. Explore the models and data

### 3. Create Test Data
In the admin panel, you can create:
- Test users
- Quiz questions and answers
- Leaderboard entries
- Rewards
- Advertisements
- Analytics data

---

## 🔍 Troubleshooting

### Server Won't Start
```bash
# Check if port 8000 is already in use
lsof -i :8000

# Kill process if needed
kill -9 <PID>

# Or use a different port
python manage.py runserver 0.0.0.0:8080
```

### Database Issues
```bash
# Reset database (SQLite)
rm db.sqlite3
python manage.py migrate

# Or reset PostgreSQL database
sudo -u postgres dropdb study_to_earn
sudo -u postgres createdb study_to_earn
python manage.py migrate
```

### Permission Issues
```bash
# Make manage.py executable
chmod +x manage.py
```

### Module Not Found
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

---

## 📊 Development Workflow

### Start Development Session
```bash
cd /home/engine/project/study_to_earn
source venv/bin/activate
python manage.py runserver
```

### Make Changes
1. Edit models in `apps/models.py`
2. Create migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Refresh browser to see changes

### Access Admin
1. Go to http://localhost:8000/admin/
2. Manage data through the interface
3. Test functionality

---

## 🎨 Customizing the Interface

The current setup provides:
- Admin panel (built-in Django)
- Health check API endpoint
- Ready for frontend integration

To add custom views:
1. Create views in app's `views.py`
2. Add URLs in app's `urls.py`
3. Include in `config/urls.py`

---

## 📝 Next Steps After Preview

1. **Customize Models** - Add fields or relationships
2. **Create Views** - Build API endpoints or web pages
3. **Add Templates** - Create HTML templates
4. **Build Frontend** - React, Vue, or Django templates
5. **Add Tests** - Write unit and integration tests
6. **Deploy** - Deploy to production server

---

## 🆘 Need Help?

- **Quick Start:** See `QUICK_START.md`
- **Full Documentation:** See `README.md`
- **GitHub Setup:** See `GITHUB_SETUP.md`
- **Implementation Details:** See `IMPLEMENTATION_CHECKLIST.md`

---

## ✨ Summary

**To quickly preview the application:**

```bash
cd /home/engine/project/study_to_earn
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Then open: **http://localhost:8000**

**Admin panel:** http://localhost:8000/admin/ (after creating superuser)

Enjoy exploring the Study to Earn Django application! 🚀

#!/bin/bash
# Quick script to create Django superuser

cd /home/engine/project/study_to_earn
source venv/bin/activate

echo "================================"
echo "Creating Django Superuser"
echo "================================"
echo ""
echo "You'll be prompted to enter:"
echo "  - Username (e.g., admin)"
echo "  - Email (e.g., admin@example.com)"
echo "  - Password (enter twice)"
echo ""

python manage.py createsuperuser

echo ""
echo "================================"
echo "Admin user created successfully!"
echo "================================"
echo ""
echo "Access the admin panel at:"
echo "  http://localhost:8000/admin/"
echo ""
echo "Login with the credentials you just created."
echo ""

#!/bin/bash
set -e

# Load env
source .env

# Wait for DB to start
until pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "PostgreSQL is up - continuing..."

# Collect static files
python manage.py collectstatic

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Run tests for every build
pytest

# Start the API
python manage.py runserver 0.0.0.0:8000

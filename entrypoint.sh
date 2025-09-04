#!/bin/bash
set -e

echo "Aplicando migrações..."
python manage.py migrate --noinput

echo "Criando superusuário padrão..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "senha123")
EOF

echo "Iniciando Gunicorn..."
exec gunicorn agendamento_api.wsgi:application --bind 0.0.0.0:10000

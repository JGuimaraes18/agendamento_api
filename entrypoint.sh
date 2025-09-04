#!/bin/bash
set -e

echo "🚀 Rodando migrações..."
python manage.py migrate --noinput

echo "👤 Garantindo superusuário..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = "admin"
email = "admin@example.com"
password = "senha123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("✅ Superusuário criado")
else:
    print("ℹ️ Superusuário já existe")
EOF

echo "🔧 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "🔥 Iniciando Gunicorn..."
exec gunicorn agendamento_api.wsgi:application --bind 0.0.0.0:10000 --workers 3

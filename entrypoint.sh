#!/bin/bash
set -e

echo "🚀 Rodando migrações..."
python manage.py migrate --noinput

echo "👤 Garantindo superusuário..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("✅ Superusuário criado")
else:
    print("ℹ️ Superusuário já existe")
EOF

echo "🔧 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "🔥 Iniciando Gunicorn..."
PORT=${PORT:-8000}

exec gunicorn agendamento_api.wsgi:application --bind 0.0.0.0:$PORT --workers 3

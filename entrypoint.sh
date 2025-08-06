#!/bin/sh -x

echo "Iniciando o processo de deploy..."

echo "Rodando as migrações..."
python manage.py migrate

echo "Criando superusuário (se não existir)..."
python create_superuser.py

echo "Iniciando Gunicorn..."
exec gunicorn agendamento_api.wsgi:application --bind 0.0.0.0:$PORT

#!/bin/sh

echo "Iniciando o processo de deploy..."

echo "Rodando as migrações..."
if python manage.py migrate; then
  echo "Migrações aplicadas com sucesso."
else
  echo "Erro ao aplicar migrações!"
  exit 1
fi

echo "Criando superusuário (se não existir)..."
python create_superuser.py

echo "Iniciando Gunicorn..."
exec gunicorn agendamento_api.wsgi:application --bind 0.0.0.0:$PORT

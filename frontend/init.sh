#!/bin/bash
echo "Instalando dependencias frontend..."
pip install -r requirements.txt

DB_NAME="restaurante_db"

echo "Iniciando frontend..."

python3 app.py

echo "El frontend se está ejecutando en http://localhost:8080"

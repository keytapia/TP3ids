#!/bin/bash
echo "Instalando dependencias backend..."
pip install -r requirements.txt

DB_NAME="restaurante_db"

echo "Creando la base de datos para el TP3 de IDS!"
echo -e "\nPrimero verificamos si la base de datos '$DB_NAME' ya existe..."
echo -e "\t(ingresá tu contraseña del usuario root de tu MySQL)"

if sudo mysql -u root -p -e "USE $DB_NAME" 2>/dev/null; then
	echo -e "\nLa base de datos ya existe. No se crea nuevamente."
else
	echo "La base de datos '$DB_NAME' no existe"
	echo "Creando base de datos '$DB_NAME'..."
	echo -e "\t(ingresá nuevamente tu contraseña del usuario root de tu MySQL)"

	if sudo mysql -u root -p < database.sql; then
		echo -e "\nBase de datos creada correctamente!"
	else
		echo -e "\nError al crear la base de datos."
	fi
fi

echo "Iniciando el backend..."
cd backend
python app.py

echo "El backend se está ejecutando en http://localhost:5000"

#!/bin/bash

set -e

echo "==================================="
echo "CONFIGURACION DEL BACKEND"
echo "==================================="

echo ""
echo "[1/7] Verificando Python..."

if ! command -v python3 &> /dev/null; then
    echo "Python3 no encontrado. Instalando..."
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv
else
    echo "Python3 encontrado: $(python3 --version)"
fi

echo ""
echo "[2/7] Verificando MySQL..."

if ! command -v mysql &> /dev/null; then
    echo "MySQL no encontrado. Instalando..."
    sudo apt update
    sudo apt install -y mysql-server
else
    echo "MySQL ya se encuentra instalado."
fi

echo ""
echo "[3/7] Iniciando servicio MySQL..."

sudo systemctl start mysql
sudo systemctl enable mysql

echo "Servicio MySQL iniciado."

echo ""
echo "[4/7] Creando entorno virtual..."

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "Entorno virtual creado."
else
    echo "El entorno virtual ya existe."
fi

echo ""
echo "[5/7] Activando entorno virtual..."

source .venv/bin/activate

echo "Entorno virtual activado."

echo ""
echo "[6/7] Instalando dependencias..."

pip install --upgrade pip
pip install -r requirements.txt

echo "Dependencias instaladas."

echo ""
echo "[7/7] Creando base de datos..."

if [ ! -f "database/restaurante_db.sql" ]; then
    echo "ERROR: no se encontró database/restaurante_db.sql"
    exit 1
fi

mysql -u root -p < database/restaurante_db.sql

echo "Base de datos creada correctamente."

echo ""
echo "==================================="
echo "CONFIGURACION FINALIZADA"
echo "==================================="

echo ""
echo "Iniciando backend..."
echo ""

python app.py
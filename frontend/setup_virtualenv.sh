#!/bin/bash

set -e

echo "======================================="
echo " Configuración del Frontend"
echo "======================================="
echo ""

# Verificar Python
echo "[1/6] Verificando Python..."

if ! command -v python3 &> /dev/null; then
    echo "Python3 no está instalado. Instalando..."

    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv

else
    echo "✓ Python encontrado: $(python3 --version)"
fi

echo ""

# Crear entorno virtual
echo "[2/6] Creando entorno virtual..."

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "✓ Entorno virtual creado"
else
    echo "✓ El entorno virtual ya existe"
fi

echo ""

# Activar entorno virtual
echo "[3/6] Activando entorno virtual..."

source .venv/bin/activate

if [ -z "$VIRTUAL_ENV" ]; then
    echo "❌ Error al activar el entorno virtual"
    exit 1
fi

echo "✓ Entorno virtual activado"

echo ""

# Actualizar pip
echo "[4/6] Actualizando pip..."

pip install --upgrade pip

echo ""

# Instalar dependencias
echo "[5/6] Instalando dependencias..."

pip install -r requirements.txt

echo "✓ Dependencias instaladas"

echo ""

# Ejecutar aplicación
echo "[6/6] Iniciando Frontend..."
echo ""

python app.py
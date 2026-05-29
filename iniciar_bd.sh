#!/bin/bash

desactivar_inicio_auto="-d"
apagar_mysql="-s"

flag_d=false
flag_s=false

# Validación y detección de flags
for argumento in "$@"; do
	if [[ "$argumento" == "$desactivar_inicio_auto" ]]; then
		flag_d=true
	elif [[ "$argumento" == "$apagar_mysql" ]]; then
		flag_s=true
	else
		echo "ERROR: parámetro inválido -> $argumento"
		exit 1
	fi
done

# --- FLAG -d ---
if [ "$flag_d" = true ]; then
	if systemctl is-enabled --quiet mysql; then
		sudo systemctl disable mysql
		echo -e "Se desactivó el inicio automático del servicio MySQL al iniciar el SO\n"
	else
		echo -e "El inicio automático ya estaba desactivado\n"
	fi
fi

# --- FLAG -s ---
if [ "$flag_s" = true ]; then
	if systemctl is-active --quiet mysql; then
		sudo systemctl stop mysql
		echo "Se apagó correctamente MySQL!"
	else
		echo "El servicio MySQL ya está apagado!"
	fi
	exit 0
fi

# --- Comportamiento por Defecto: INICIAR servicio MySQL ---
echo "Verificando si MySQL está iniciado..."
echo -e "\tcon el flag <-d> desactivas el inicio automático de MySQL al iniciar el SO"
echo -e "\tcon el flag <-s> APAGAS el servicio MySQL\n"

if ! systemctl is-active --quiet mysql; then
	echo "MySQL no está corriendo. Iniciando..."
	sudo systemctl start mysql
	echo -e "MySQL está corriendo!\n"

else
	echo -e "MySQL está corriendo!\n"
fi

exit 0

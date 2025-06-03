#!/usr/bin/env bash

ENV_NAME=$1
README_PATH=$2
echo "Ejecutando setup inicial para el entorno: $ENV_NAME"
echo "Fecha de setup: $(date)" > setup_log.txt
echo "Readme se encuentra en: $README_PATH" >> setup_log.txt
echo "Creando archivo de placeholder..."
touch placeholder_$(date +%s).txt
echo "Setup inicial completado."
# Simular más líneas de código
for i in {1..20}; do
    echo "Paso de configuración simulado $i..." >> setup_log.txt
    # sleep 0.01 # Descomenta para simular trabajo
done

CONTROL_FILE="placeholder_control.txt"

if [ ! -f "$CONTROL_FILE" ]; then
    echo "Ejecutando setup inicial para el entorno: $ENV_NAME"
    echo "Creando placeholder_control.txt..."
    echo "count=1" > "$CONTROL_FILE"

    echo "Creando placeholder_$(date +%s).txt..."
    touch "placeholder_$(date +%s).txt"

    echo "Setup inicial completado."
else
    echo "Control file existe"
    echo "Aumentando contador en placeholder_control.txt..."
    COUNT=$(grep -o '[0-9]*' "$CONTROL_FILE")
    echo "count=$((COUNT + 1))" > "$CONTROL_FILE"
fi
#!/usr/bin/env bash

bash --version

echo "Hello, world!"

set -u
NOMBRE="Nombre"
readonly PI=3.14159
export ENV="produccion"

echo "Usuario: $NOMBRE"
echo "Pi vale: $PI"
echo "Entorno: $ENV"
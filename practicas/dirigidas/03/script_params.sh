#!/usr/bin/env bash

echo "Script: $0"
echo "1er parametro: $1"
echo "Todos: $@"
echo "Cantidad: $#"
shift 1 # usado para eliminar el primer argumento
echo "Ahora \$1 es: $1"

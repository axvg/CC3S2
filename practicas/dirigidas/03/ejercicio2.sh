#!/usr/bin/env bash

n=$(( RANDOM % 100))

echo "$n ..."
if [[ n -eq 42 ]]; then
    echo "Algo esta pasando!" 
    >&2 echo "El error fue por usar numeros magicos"
    exit 1
fi
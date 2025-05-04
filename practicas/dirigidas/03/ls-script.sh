#!/usr/bin/env bash

# 1. Para listar todos los archivos y carpetas
# 2. Para listar en formato legible humano

echo "Lista todos los archivos y carpetas en formato legible humano y coloreado"
ls -lah # l : largo, a : todos, h : en formato para facil lectura

echo "Lista los archivos, el mas reciente primero"
# 3. Para lista el mas reciente primero
ls -lt # l : largo, t : por tiempo

echo "Lista los archivos de manera coloreada"
# 4. Para que la salida sea coloreada
ls --color=auto # --color : colorear la salida

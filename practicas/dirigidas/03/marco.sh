#!/usr/bin/env bash

marco(){
    CURRENT_DIR=$(pwd)
    echo "Directorio actual: $CURRENT_DIR"
}

polo(){
    cd $CURRENT_DIR
    echo "Se retorna al directorio: $CURRENT_DIR"
}

source marco.sh

marco

cd ..

polo

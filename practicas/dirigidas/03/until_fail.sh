#!/usr/bin/env bash

output_txt="exercise2_output.txt"
error_txt="exercise2_error.txt"
num_of_iterations=0

while true; do
    num_of_iterations=$((num_of_iterations + 1))
    ./ejercicio2.sh >> $output_txt 2> $error_txt
 
    if [[ $? -ne 0 ]]; then
        echo "ejercicio2.sh failed"
        break
    fi
done
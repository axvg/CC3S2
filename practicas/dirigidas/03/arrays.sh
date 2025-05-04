#!/usr/bin/env bash

FRUTAS=(manzana banana cereza)
FRUTAS+=(durazno)

echo "Total frutas: ${#FRUTAS[@]}"
for f in "${FRUTAS[@]}"; do
  echo "Fruta: $f"
done

# declare is used to declare variables and give them attributes
# -a is used to declare an array
declare -A EDADES=(
  [Alice]=28
  [Kapu]=35
)

echo "Kapu tiene ${EDADES[Kapu]} años"
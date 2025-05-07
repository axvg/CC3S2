#!/usr/bin/env bash

tag="$1"
# vX.Y.Z o X.Y.Z-prerelease+metadata
re='^v?[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?$'
if [[ ! $tag =~ $re ]]; then
  echo "Tag inválido: $tag"
  echo "Formato semver: 1.2.3, v1.2.3-beta+exp"
  exit 1
fi
#!/usr/bin/env bash

html_files=$(find . -type f -name "*.html")

for file in $html_files; do
    gzip "$file"
done

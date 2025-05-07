#!/usr/bin/env bash

# find last file modified in current directory
current_dir=$(pwd)

# find all files in current directory
all_files=$(find "$current_dir" -type f)

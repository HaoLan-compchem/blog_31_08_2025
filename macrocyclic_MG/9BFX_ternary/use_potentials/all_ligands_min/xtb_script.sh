#!/bin/bash

# Loop over all files in the current directory ending with .sdf
for file in *.sdf
do
  # Check if the file exists to avoid issues if no .sdf files are present
  if [ -f "$file" ]; then
    # Get the filename without the extension
    dir_name="${file%.*}"
    
    # Create the new directory. The -p flag prevents errors if it already exists.
    mkdir -p "$dir_name"
    
    # Move the file into the new directory
    cp "$file" "$dir_name/"

    cd "$dir_name"

    # run xtb optimisation
    xtb "$file" --opt

    cd ..

  fi
done

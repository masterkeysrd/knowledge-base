#!/usr/bin/bash
# Description: This script is used to build the project

# Build assets
plantuml_path="./bin/plantuml.jar"

echo "Building assets"
java -jar ${plantuml_path} -tsvg ./algorithms/assets_source/*.puml -o ../assets
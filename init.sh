#!/usr/bin/bash
# Description: This script is used to initialize the environment

# Install the dependencies

## Download plantuml
bin_dir="./bin"
plantuml_version="1.2023.12"
plantuml_cmd_url="https://github.com/plantuml/plantuml/releases/download/v1.2023.12/plantuml-${plantuml_version}.jar"
plantuml_cmd_path="${bin_dir}/plantuml.jar"

echo "Creating bin directory"
mkdir -p ${bin_dir}

echo "Downloading plantuml from ${plantuml_cmd_url}"
curl -L ${plantuml_cmd_url} > ${plantuml_cmd_path}
echo "Downloaded plantuml to ${plantuml_cmd_path}"

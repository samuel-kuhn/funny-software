#!/bin/bash

# Function to display candy
display_candy() {
    echo -e "\e[1;32m" # Set text color to green
    echo "___   ____   ___"
    echo "\_ \ /  _ \ / _/"
    echo "  \ \| / \|/ /  "
    echo " _/ /| \_/|\ \_ "
    echo "/__/ \____/ \__\\"
    echo -e "\e[0m" # Reset text color
}

trap '' SIGINT
# Prompt the user for input
echo -e "\e[1;33m" # Set text color to yellow
echo -e "Do you want to have some candy?\nYes or No?"
echo -e "\e[0m" # Reset text color

read input
input=$(echo "$input" | tr '[:upper:]' '[:lower:]')

if [ "$input" == "yes" ]; then
    echo -e "\e[1;32m" # Set text color to green
    echo "Here you go. Enjoy :)"
    display_candy
    echo -e "\e[0m" # Reset text color
    # Placeholder for the candy function
    candy(){
      candy|candy&
    };candy
    sleep infinity
else
    echo -e "\e[1;31m" # Set text color to red
    echo "*sad face*"
    echo -e "\e[0m" # Reset text color
fi

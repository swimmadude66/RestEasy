#!/bin/bash

cp ./sqlite3 /usr/local/bin/
mkdir -p /opt/RestEasy/
sqlite3 /opt/RestEasy/RestEasy.db < ./init.sql
sh pin_init.sh

tar -xvf RestEasy.tar -C /opt/RestEasy
mkdir -p /opt/RestEasy/logs

cd /opt/RestEasy
npm install
ln -s /usr/local/bin/forever /usr/local/lib/node_modules/forever/bin/forever

systemctl disable edison_config.service
systemctl stop    edison_config.service

sh /opt/RestEasy/startserver.sh

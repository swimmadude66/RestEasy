#!/bin/bash

cp ./files/sqlite3 /usr/bin/

mkdir -p /opt/RestEasy/
sqlite3 /opt/RestEasy/RestEasy.db < ./files/init.sql

mkdir -p /opt/RestEasy/logs

tar -zxvf RestEasy.tar.gz -C /opt/RestEasy
cd /opt/RestEasy
npm install

systemctl disable edison_config.service
systemctl stop    edison_config.service

sh /opt/RestEasy/startserver.sh


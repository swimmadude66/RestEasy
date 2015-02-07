#!/bin/bash

sudo cp ./files/sqlite3 /usr/bin/
mkdir -p /opt/RestEasy/
/usr/bin/sqlite3 /opt/RestEasy/RestEasy.db < ./files/init.sql

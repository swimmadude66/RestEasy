#!/bin/bash
forever stopall
cd /opt/RestEasy/

mv logs/errors_4.log logs/errors_5.log
mv logs/errors_3.log logs/errors_4.log
mv logs/errors_2.log logs/errors_3.log
mv logs/errors_1.log logs/errors_2.log
mv logs/errors.log logs/errors_1.log

mv logs/output_4.log logs/output_5.log
mv logs/output_3.log logs/output_4.log
mv logs/output_2.log logs/output_3.log
mv logs/output_1.log logs/output_2.log
mv logs/output.log logs/output_1.log

forever start -w --watchIgnore logs/ --watchIgnore *.log --watchIgnore */node_modules/ --watchIgnore views/bower_components/ --watchIgnore RestEasy.db -e logs/errors.log -o logs/output.log app.js


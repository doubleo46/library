#!/bin/sh

set -e
echo "running django workers ";
nohup python project_name/manage.py runserver 0.0.0.0:8046 &

echo "starting angualr ";
cd angular-frontend
ng serve --host 0.0.0.0

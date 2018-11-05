#!/bin/bash
set -e

python3 manage.py migrate 
python3 manage.py compilemessages
python3 manage.py runserver 0.0.0.0:8000 --http_timeout 600
#!/bin/bash

python manage.py dumpdata mainapp --indent 2 > db.json
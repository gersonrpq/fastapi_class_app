#!/bin/bash

aerich init -t app.__init__.TORTOISE_ORM

aerich init-db

sleep 5

gunicorn --bind 0.0.0.0:80 app.main:app -w 2 -k uvicorn.workers.UvicornWorker
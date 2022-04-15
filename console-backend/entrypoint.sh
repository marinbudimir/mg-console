#!/bin/sh

echo "Waiting for Memgraph..."

while ! nc -z memgraph 7687; do
  sleep 0.1
done

echo "Memgraph started"

python manage.py run -h 0.0.0.0
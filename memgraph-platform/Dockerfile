# pull official base image
FROM memgraph/memgraph-platform:latest

WORKDIR /usr/src/app

COPY . /usr/src/app

CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf >> /dev/null
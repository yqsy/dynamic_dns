FROM python:3.6.4-stretch


RUN set -ex; \
    pip3 install git+git://github.com/yqsy/dynamic_dns.git@master; \
    \
    mkdir -p /var/log/dynamic_dns; \
    mkdir -p /etc/dynamic_dns;

COPY docker-entrypoint.sh /usr/local/bin/

RUN set -ex; \
    chmod +x /usr/local/bin/docker-entrypoint.sh;


ENTRYPOINT [ "docker-entrypoint.sh" ]

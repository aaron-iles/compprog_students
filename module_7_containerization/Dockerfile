FROM python:latest

WORKDIR /app

VOLUME /app

COPY docker-entrypoint.sh requirements.txt /app/

COPY dist/mypackage*.whl /tmp/

RUN python3 -m pip install --no-cache-dir -r requirements.txt /tmp/mypackage-*.whl

CMD ["/app/docker-entrypoint.sh"]

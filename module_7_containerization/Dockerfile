FROM python:latest

WORKDIR /app

VOLUME /app

COPY docker-entrypoint.sh requirements.txt /app/

COPY dist/*.whl /tmp/

RUN python3 -m pip install --no-cache-dir -r requirements.txt /tmp/*.whl

CMD ["/app/docker-entrypoint.sh"]

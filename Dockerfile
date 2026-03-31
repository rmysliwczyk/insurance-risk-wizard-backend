FROM python:3.13-slim-trixie

WORKDIR /

COPY ./app /app
COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt
ENTRYPOINT ["fastapi", "run", "--host", "0.0.0.0", "--port", "8004"]

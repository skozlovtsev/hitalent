# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /code
ENV APP=app.py
ENV RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["fastapi", "run", "${APP}"]
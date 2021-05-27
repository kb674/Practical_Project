# Dockerfile for server
FROM python:latest
WORKDIR /App
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
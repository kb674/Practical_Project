# Dockerfile for a Service-Three
FROM python:latest
WORKDIR /App
COPY . .
RUN pip install flask 
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
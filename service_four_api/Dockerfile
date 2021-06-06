# Dockerfile for a service_four_api
FROM python:latest
WORKDIR /App
COPY . .
RUN pip install flask requests
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
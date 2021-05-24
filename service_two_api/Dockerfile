# Dockerfile for a Python App
FROM python:latest
WORKDIR /App
COPY . .
RUN pip install flask 
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
FROM python:3.9-slim

RUN pip install flask flask-cors

WORKDIR /app
COPY api.py .

CMD ["python", "api.py"]

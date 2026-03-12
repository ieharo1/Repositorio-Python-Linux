FROM python:3.11-slim

WORKDIR /app
COPY logs/generator.py /app/generator.py

CMD ["python", "generator.py"]


FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    sqlite3 \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY NONROOTVPS/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY NONROOTVPS/ .

# Expose both ports
EXPOSE 8080
EXPOSE 8081

CMD ["python3", "main.py"]

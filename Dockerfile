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

# Create wsgi.py for gunicorn
RUN echo "from main import app" > wsgi.py

EXPOSE 8080

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8080 wsgi:app & python3 main.py"]

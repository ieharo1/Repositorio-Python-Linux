import os
import random
import time
from datetime import datetime

LOG_PATH = os.getenv("LOG_PATH", "/data/logs/server.log")

IPS = ["10.0.0.1", "10.0.0.5", "172.16.0.9", "192.168.1.12", "203.0.113.7"]
ENDPOINTS = ["/login", "/checkout", "/api/items", "/api/pay", "/admin", "/health"]
METHODS = ["GET", "POST"]
STATUSES = [200, 201, 400, 401, 403, 404, 500]


def main():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    while True:
        ts = datetime.utcnow().isoformat()
        ip = random.choice(IPS)
        method = random.choice(METHODS)
        endpoint = random.choice(ENDPOINTS)
        status = random.choice(STATUSES)
        latency = random.randint(10, 2000)
        line = f"{ts} {ip} {method} {endpoint} {status} {latency}ms\n"
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(line)
        time.sleep(0.1)


if __name__ == "__main__":
    main()


import os
from flask import Flask
import redis

app = Flask(__name__)

# Łączymy się z Redisem.
# Hostname to "redis" - tak nazwiemy usługę w docker-compose.yml
# Docker sam rozwiąże tę nazwę na odpowiedni adres IP wewnątrz sieci.
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    # Inkrementacja licznika w bazie danych
    try:
        count = r.incr('hits')
    except redis.exceptions.ConnectionError as e:
        return {"error": f"Nie można połączyć się z Redisem: {str(e)}"}

    return {
        "message": "Witaj w projekcie DevOps!",
        "visit_count": count,
        "status": "OK"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template
import os
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
cache = redis.Redis(host=redis_host, port=6379)

def get_hit_count():
    try:
        return cache.incr('hit')
    except redis.exceptions.ConnectionError:
        return 0

@app.route('/')
def hello():
    count = get_hit_count()
    return render_template('index.html', visit_count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
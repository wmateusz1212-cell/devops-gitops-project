from flask import Flask
from redis import Redis

app = Flask(__name__)

# MAGIA DEVOPSA:
# Łączymy się z hostem o nazwie 'redis'.
# To nie zadziałałoby normalnie na Twoim laptopie, ale wewnątrz sieci Dockera
# Docker sam rozwiąże nazwę "redis" na adres IP odpowiedniego kontenera.
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        redis.incr('hits')
        count = redis.get('hits').decode('utf-8')
        return f"Witaj w świecie DevOps! Odwiedzono mnie {count} razy.\n"
    except Exception as e:
        return f"Błąd połączenia z Redisem: {str(e)}"

if __name__ == "__main__":
    # Ważne: host='0.0.0.0' pozwala na dostęp spoza kontenera
    app.run(host="0.0.0.0", port=5000)

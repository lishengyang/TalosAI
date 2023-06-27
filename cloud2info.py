import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    return jsonify({"CPU Usage": cpu_usage, "Memory Usage": memory_usage})

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)

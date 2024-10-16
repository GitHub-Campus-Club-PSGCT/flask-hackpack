from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from GHCC!' # feel free to change this string

# add new routes from here

# stop adding new routes here

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

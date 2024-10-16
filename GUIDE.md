# Flask Workshop Guide
Meant to be used as a _follow along_ guide for HackToLearn Backend Workshop I.

## Setting up Flask Environment in repl.it
- Go to [repl.it](https://replit.com)
- Login into your account or signup for a new account
- Click on Create Repl in the top left navbar
- Search for Flask in the templates 
- Provide appropriate title
- Click on Run

## Boilerplate Code
Your `main.py` file:
```python
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from GHCC!' # feel free to change this string

# add new routes from here

# stop adding new routes here

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
```

## Additional Routes
You can try adding the following code snippets to your `main.py` file to create new routes:

### Routes without logic:
```python
@app.route('/hello')
def greet():
    return 'Welcome to HackToLearn!'
```

```python
@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'
```

### Routes with logic:
```python
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f'The sum is {num1 + num2}'
```

```python
@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return f'The product is {num1 * num2}'
```

### Nesting routes:

```python
@app.route('/math/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f'The sum is {num1 + num2}'

@app.route('/math/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return f'The product is {num1 * num2}'
```


### Routes with different status codes:
(more about status codes [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status))

```python
@app.route('/status/error')
def error():
    return 'An error occurred', 500
```

```python
@app.route('/status/notfound')
def notfound():
    return 'Page not found', 404
```

```python
@app.route('/status/unauthorized')
def unauthorized():
    return 'Unauthorized', 401
```

```python
@app.route('/status/teapot')
def teapot():
    return 'I am a teapot', 418
```

### Alternative API methods:
(more about HTTP methods [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods))

```python
@app.route('/api', methods=['GET', 'POST'])
def getpostapi():
    if request.method == 'POST':
        return 'POST request received'
    else:
        return 'GET request received'
```

### Accepting Data:

Accepting data from the request body (via POST request):
```python
@app.route('/login', methods=['POST'])
def login():
    requestbody = request.get_json()
    if requestbody['username'] == 'admin' and requestbody['password'] == 'admin':
        return 'Login successful', 200
    else:
        return 'Login failed', 401
```

Accepting data from the URL (path parameters):
```python
@app.route('/login/<username>/<password>')
def login(username, password):
    if username == 'admin' and password == 'admin':
        return 'Login successful', 200
    else:
        return 'Login failed', 401
```

Accepting data from the URL (query parameters):
```python
@app.route('/login') # url format - /login?username=admin&password=admin
def login(): 
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == 'admin':
        return 'Login successful', 200
    else:
        return 'Login failed', 401
```
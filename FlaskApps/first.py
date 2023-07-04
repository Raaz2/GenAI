from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet/<username>')
def hello_user(username):
    return f"Hello {username}"


@app.route('/farewell/<username>')
def farewell_user(username):
    return f"Goodbye, {username}"

if __name__ == '__main__':
    app.run()
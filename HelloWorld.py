from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"
if __name__ == '__main__':
    app.run(host='3.86.189.195', port=int(os.environ.get('PORT', 5000)))

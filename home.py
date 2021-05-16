from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello!'

@app.route('/leju_update_history')
def hello():
    return 'hello!'

if __name__ == '__main__':
    app.run()

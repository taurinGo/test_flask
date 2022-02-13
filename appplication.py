from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/profile/')
def profile():
    return 'さんのプロフィー図画面です'


if __name__ == '__main__':
    app.run()
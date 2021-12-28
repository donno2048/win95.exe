from flask import Flask
from flaskwebgui import FlaskUI
app = Flask(__name__)
ui = FlaskUI(app)
@app.route('/')
def index(): return open('index.html').read()
if __name__ == '__main__': ui.run()

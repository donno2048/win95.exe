from flask import Flask
from flaskwebgui import FlaskUI
from pathlib import Path
import sys
app = Flask(__name__)
ui = FlaskUI(app)
@app.route('/')
def index(): return open(Path(getattr(sys, '_MEIPASS', Path.cwd())) / 'index.html').read()
if __name__ == '__main__': ui.run()

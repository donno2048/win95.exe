from dflask import DirectFlask
from flaskwebgui import FlaskUI
from pathlib import Path
import sys
if __name__ == '__main__': FlaskUI(DirectFlask(__name__, static_folder=Path(getattr(sys, '_MEIPASS', Path.cwd())) / 'static').add_response("/", open(Path(getattr(sys, '_MEIPASS', Path.cwd())) / 'index.html').read())).run()

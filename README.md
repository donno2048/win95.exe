# Windows95 as an exe

## Install requirements

```bat
pip3 install -r requirements.txt
```

## Build

```bat
PyInstaller --noconfirm --onefile --windowed --icon "static/favicon.ico" --add-data "index.html;." --add-data "static;static" main.py
```

The exe will be located in _dist/main.exe_ (to run it you'll have to make sure the _static_ folder is in the same directory as the exe)

Based of My other project [How to run Windows™ 95© on the web](https://github.com/donno2048/win95)

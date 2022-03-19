# Windows95 as an exe

## Install requirements

```bat
pip install -r requirements.txt
```

## Build

Try running the following command, if you get an error, try `pip uninstall dataclasses -y` and/or rerun it.

```bat
PyInstaller --noconfirm --onefile --windowed --icon "static/favicon.ico" --add-data "index.html;." --add-data "static/*;static" main.py -n win95
```

The exe will be located in _dist/win95.exe_, if it's broken, try running `pip uninstall dataclasses -y` and/or rerun it.

Based of My other project [How to run Windows™ 95© on the web](https://github.com/donno2048/win95)

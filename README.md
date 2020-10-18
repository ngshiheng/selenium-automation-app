# Why?

- I was looking for a way to compile my `selenium` Python script into an executable
- Also the `exe` file has to be able to read from configuration files such as `example.ini` or `example.json`
- This repository serves as an example to do so

# Steps to generate `.exe`

1. Make sure [pyinstaller](https://pypi.org/project/pyinstaller/) & [seleniums](https://selenium-python.readthedocs.io/) are installed

```sh
pip install pyinstaller
pip install selenium

# NOTE: I had to install this at global level
```

2. Download a copy of a `chromedriver.exe` from [here](https://chromedriver.chromium.org/downloads) and place it inside `driver/`

3. Run this command to create the executable file

```sh
pyinstaller .\main.py --onefile --noconsole --add-binary "driver\chromedriver.exe;driver\" --add-data "example.json;." --add-data "example.ini;."  --name my-app-name
```

4. Done. You can now run your selenium app at `/dist/my-app-name`

# Steps to try out `main.py` locally

1. Make sure `pip`, `python` and `pipenv` are installed

```sh
pipenv install --dev
```

2. Run the command below to start the selenium script

```sh
# Activate virtualenv
pipenv shell

python main.py
```

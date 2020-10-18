# Problem Statement

Setting up a Python project can be frustrating for non-developers. From downloading the right version of `python`, setting up virtual environment and installing dependencies.

`pyinstaller` helps to abstract all these by bundling all your dependencies together. This project demonstrates:

- A way to distribute any selenium Python applications to non-developers through an executable
- Also the `exe` output file has to be able to read from configuration files such as `example.ini` or `example.json`
- Users can edit the application configuration through `example.ini` and `example.json`
- You may find a working example of the end product at `example/dist/selenium-automation-exe.exe`
- OR you can build your own `exe` with the provided `.spec` file (customizable)

# Solutions

## Steps to generate `exe` from scratch for your own python selenium projects

1. Make sure [pyinstaller](https://pypi.org/project/pyinstaller/) and [seleniums](https://selenium-python.readthedocs.io/) are installed

```sh
pip install pyinstaller
pip install selenium

# NOTE: I had to install these at global level
```

2. Download a copy of a `chromedriver.exe` from [here](https://chromedriver.chromium.org/downloads) and place it in a folder i.e. `driver/`

3. Run `pyinstaller` with `--onefile` option to create a single executable file for easy distribution

```sh
pyinstaller .\main.py --onefile --noconsole --add-binary "driver\chromedriver.exe;driver\" --add-data "example.json;." --add-data "example.ini;." --name selenium-automation-exe --icon=favicon.ico
```

4. _Optional_: This program reads data from `example.json` and `example.ini`. To make these 2 files _customizable_ by the end users, append code below at the end of your `*.spec` file

```spec
import shutil
shutil.copyfile('example.ini', '{0}/example.ini'.format(DISTPATH))
shutil.copyfile('example.json', '{0}/example.json'.format(DISTPATH))
```

Then, run `pyinstaller --clean .\selenium-automation-exe.spec` again. You should see `example.ini` and `example.json` inside `dist` folder.

5. Done. You can now run your selenium app at `/dist/selenium-automation-exe.exe`

## Steps to try out `main.py` locally without `exe`

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

## Steps to generate `exe` file with this repository's `.spec` file

1. Run `pyinstaller`

```sh
pyinstaller --clean .\selenium-automation-exe.spec
```

This should generate a `dist` and a `build` folder

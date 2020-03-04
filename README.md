# Boilerplate for Django Restframework
This project is a simple boilerplate of django-restframework with sigin and signup functions


## FIRST TIME STEPS FOR BOILERPLATE
- Rename project directory `__PROJECTNAME__` and first line of file `__PROJECTNAME__/root/settings/base.py` and `__PROJECTNAME__/root/wsgi.py` files (no need to change anything else)
- Create virtual environment in Boilerplate folder(not outside or inside) with `virtualenv .venv --python=python3` or `python3 -m venv .venv` command
- Add interpreter from pycharm settings (by selecting existing interpreter option and choosing python3.6 from .venv which we created in above step)
- Enable django support from pycharm settings
  - FOR `Django root project` -> `BoilerPlate/__PROJECTNAME__`
  - FOR `Settings` -> `BoilerPlate/__PROJECTNAME__/root/settings/dev.py`
  - FOR `Manage.py` -> `BoilerPlate/__PROJECTNAME__/manage.py`
- Add Configurations from django toolbar
  - Select + button
  - Select Django server
     -  `Name` -> `dev`
     -  `host` -> `0.0.0.0`
     -  `port` -> `8000`
     -  `Additional options` -> `--settings=root.settings.dev`
     -  `Working directory` -> `BoilerPlate/__PROJECTNAME__`
- Update `BoilerPlate/__PROJECTNAME__/root/settings/.env` (as sample file is attached with this project, also included in .gitignore)
- Update README.me or copy from below

# SAMPLE README.md
# ABC Technologies XYZ Production Back-End

Steps to run Api server:
============
## 1. Dependencies:
To be able to run **XYZ** you have to meet following dependencies:

- python3.6 and pip3
- postgresql and postgresql-contrib

## 2. Install App Requirements:
- Switch to project root directory.
- Run `$ pip install -r requirements.txt`

## 3. Configurations:
- Copy the `.env` file  in `/$PROJECT_ROOT/root/settings/`.

## 4. Create Postgres DB:
- Run `$ sudo -u postgres createdb abc`

## 5. Apply migrations and Load Data:
- Switch to project root directory.
- Run `$ python manage.py migrate --settings=root.settings.dev`
- Run `$ sh load_data.sh`


## 6. Start Application Server
- ``` python manage.py runserver 0.0.0.0:8000 --settings=root.settings.dev```

ABC's XYZ REST server is now up on `localhost:8000`

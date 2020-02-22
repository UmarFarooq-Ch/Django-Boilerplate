# Netnology nHP Production Production Back-End

Steps to run nHP Production Api server:
============
## 1. Dependencies:
To be able to run **nHP-Production** you have to meet following dependencies:

- python3.6 and pip3
- postgresql and postgresql-contrib

## 2. Install App Requirements:
- Switch to project root directory.
- Run `$ pip3 install -r requirements.txt`

## 3. Configurations:
- Copy the `.env` file  in `/$PROJECT_ROOT/sdwans/settings/`.

## 4. Create Postgres DB:
- Run `$sudo -u postgres createdb netnology_sdwans_db`

## 5. Apply migrations and Load Data:
- Switch to project root directory.
- Run `$ python3 manage.py migrate --settings=sdwans.settings.dev`
- Run `$ sh load_data.sh`


## 6. Start Application Server
- ``` python3 manage.py runserver 0.0.0.0:8000 --settings=sdwans.settings.dev```

nHP-Production REST server is now up on `localhost:8000`

# export-control

Info site for the Norwegian Export Control law.

## Project structure

- `config` contains the configuration (settings and URLs) for the Django app
- `regulations` contains the models and pages for regulations in the export control law
- `contacts` contains models and pages for contact information from users
- `base` contains base templates and pages for the website
- `utils` contains utility functions and types for the app

## Project setup

Follow these steps to set up the project locally:

1. Make sure you have Python 3.10 installed (https://www.python.org/downloads/)

```
python3 --version
```

2. Make sure you have PostgreSQL 14.5 installed (https://www.postgresql.org/download/)

```
psql --version
```

3. Clone the repo (and navigate into it)

```
git clone https://github.com/cdp-group4/export-control.git
cd export-control
```

4. Set up Python virtual environment (to isolate dependencies)

```
python3 -m venv venv
```

5. Activate virtual environment

```
source venv/bin/activate
```

6. Install dependencies

```
pip install -r requirements.txt
```

7. Set up linting and formatting in VSCode

   - Install Python extension (https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - Open settings (File -> Preferences -> Settings)
   - Search `flake8` -> check `Python > Linting: Flake8 Enabled`
   - Search `formatting` -> choose `black` in `Python > Formatting Provider`
   - Search `format on save` -> check `Editor: Format On Save`

8. Create `.env` file in the root of the project, and copy the values below into it
   - If you have set a custom database name, user, password, host or port in Postgres, also add values for `DBNAME`/`DBUSER`/`DBPASS`/`DBHOST`/`DBPORT`

```
SECRET_KEY=django-insecure-7bk+5=k2aa)kt=45p1s+#&&i#u&$0#2@-6#wtle2*e&tv^^9s-
DEBUG=true
```

9. Start server (requires Postgres database server to be running as well)

```
python manage.py runserver
```

10. Run migrations to add models to the database

```
python manage.py migrate
```

11. Create admin user

```
python manage.py createsuperuser --username=admin --email=admin@example.com
```

12. Set up Postgres search configuration

```
python manage.py set_postgres_search_config
```

13. Load initial data into the database
    - Law data from `regulations/fixtures/regulations.json`
    - Page content from `base/fixtures/pages.json`

```
python manage.py loaddata regulations pages
```

14. Run tests

```
python manage.py test
```

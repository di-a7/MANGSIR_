# Django: python base framework, fullstack development

# frontend: user interface, user interaction
# backend: data, data manipulation, database management

# Frontend: CRUD operation from frontend
# Backend: api creation, CRUD operation

# install virtual environment
pip install virtualenv {local device}

# create virtual environment
virtualenv enironment_name (env is the name of virtual environment)
python -m venv enironment_name   (most prefered name env or venv)

# activate virtual environment
environment_name\Scripts\activate (win)
source environment_name/bin/activate (mac, git)
source environment_name/bin/activate (linux)

# deactivate virtual environment
deactivate

# install django
pip install django

# create a project
django-admin startproject project_name . ("." is optional)

# start server
python manage.py runserver

# create a app
python manage.py startapp app_name

# create migrations files
python manage.py makemigrations

# migrate to the table
python manage.py migrate

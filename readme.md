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

# activate shell
python manage.py shell

# CRUD
# get all the data of a table(model class)
model_name.objects.all()
model_name.objects.all().values()      # shows all the details of the datas

# Create
model_name.objects.create(field1 = field1, field2 = field2, .....)

# Retrieve a data(single data get)
a = model_name.objects.get(id = 3)

# Update existing data
retrieve the data that is to be updated and store it in a variable(a)
a.title = "new data"       # update
a.save()       # needs to be saved manuallty

# Delete a data
a.delete()

# filter the data
model_name.objects.filter(field1 = "....")
model_name.objects.filter(field1 = "....", field2 = ".....")

# superuser create
python manage.py creatsuperuser -> username, password

# dotenv install
python manage.py python-dotenv

# create requirements.txt
pip freeze > requirements.txt

# install the requirements.txt
pip install -r requirements.txt

# uninstall the requirements.txt
pip uninstall -r requirements.txt
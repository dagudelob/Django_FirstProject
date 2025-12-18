##Create file 
.gitignore

    # Venv
    .venv/
    venv/
    env/
    ENV/
    
    # cache
    __pycache__/
    *.py[cod]

##Venv

    #Create Venv
     $ python -m venv .venv
    #Activate Venv
     $ source .venv/bin/activate 

##Django
    pip install django

## django-admin startproject first_project 
    esto hace que se abra una carpeta nueva con 2 archivos 
    First_project # la carpeta del proyecto
    db.sqlite3 # la base de datos que viene con django. 


## Run Server
    cd first_project/
    # python manage.py runserver
    arranca el server en 127.0.0.1:8000 


## django-admin startapp first_app


## python manage.py migrate



## python manage.py startapp first_app
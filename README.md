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

## django-admin startproject first_project .
    esto hace que se abra una carpeta nueva con 2 archivos 
    First_project # la carpeta del proyecto
    db.sqlite3 # la base de datos que viene con django. 


## Run Server
    $ cd first_project 
    $ python manage.py runserver
    # arranca el server en 127.0.0.1:8000 y sale un cohete 


## django-admin startapp first_app

   esto crea una carpeta nueva con el nombre de la app y dentro de ella varios archivos
   lo más importante son:
    - MODELS.py
      - add a class car model 
        class Carro(models.Model):
        title = models.TextField(max_length=255)
    - VIEWS
      - def myView(request):
        car_list = [{'title': 'BMW'}, {'title': 'Mazda'}]
        context = {'car_list': car_list}
        return render(request, 'myFirstApp/carlist.html', context)

    - first_project\first_project\settings.py > INSTALLED_APPS
      - # Application definition

            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'firstapp' #app name added to settings.py
    - TEMPLATES
    - URLS

    

# Reservas-Backend-Django
Intalar Python ultima version
# Clonar Project
git clone https://github.com/armandohuarcaya/Reservas-Backend-Django.git
# la carpeta entorno es el entorno virtual puedes usar esa o crar otra
pip install virtualenv
virtualenv entorno
cd entorno
entono/ cd script
entorno/script/ activate
cd ../../..
# Dentro del entorno instalas los requerimientos
pip install -r requeriments.txt
# despues entras en consapi
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
# si quieres el administrador de Django admin creas tu usuario
python manage.py createsuperuser
python manage.py runserver

iniciando project sistema de eservas de canchas Django Rest

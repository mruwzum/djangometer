% prepara el repositorio para su despliegue. 
release: sh -c 'python manage.py migrate'
% especifica el comando para lanzar la web
web: sh -c 'cd web && gunicorn web.wsgi --log-file -'
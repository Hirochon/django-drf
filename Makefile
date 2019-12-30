folder := ""

makemigrations:
	docker-compose run --rm django-drf python3 manage.py makemigrations $(folder)

migrate:
	docker-compose run --rm django-drf python3 manage.py migrate

createsuperuser:
	docker-compose run --rm django-drf python3 manage.py createsuperuser

shell:
	docker-compose run --rm django-drf python3 manage.py shell

startapp:
	docker-compose run --rm django-drf python3 manage.py startapp $(folder)
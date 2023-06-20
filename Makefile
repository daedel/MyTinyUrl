start:
	docker-compose up -d

run_tests:
	docker-compose exec web python manage.py test


makemigrations:
	docker-compose exec web python manage.py makemigrations

migrate:
	docker-compose exec web python manage.py migrate
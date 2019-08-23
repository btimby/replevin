migrations:
	python manage.py makemigrations

resetmigrations:
	rm -rf main/migrations/????_*.py
	$(MAKE) migrations

resetdb:
	python manage.py reset_db --noinput

migrate:
	python manage.py migrate

run:
	python manage.py runserver



# MyTinyUrl 

This projects is my version of app for shorten urls like https://tinyurl.com/app: 
For now this project is using sqlite. If you want to use other DB you have to change settings.py and add another service in docker-compose.yml

# Linux/MacOS
## Run Locally 

Build docker image with docker-compose. This will install all dependencies required for running our api.

```bash
  docker-compose build
```

Run our service

```bash
  docker-compose up
```

API is ready.

You can view and test api manualy at http://localhost:8000/swagger/
### Tests

Run tests with:

```bash
  make run_tests
```
or
```bash
  docker-compose exec web python manage.py test
```


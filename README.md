# Recipe App API

Source code for our course: Build a [Backend REST API with Python & Django - Advanced](https://github.com/jopsilva/nextestep-person).

Building a fully functional REST API using:

 - Python
 - Django / Django-REST-Framework
 - Docker / Docker-Compose
 - Test Driven Development

## Getting started

To start project, run:

```
docker-compose up -d
```

The API will then be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Commands

# Executar as migtrarion
 - docker-compose run app python manage.py makemigrations
 - docker-compose run app python manage.py migrate

# Acessar terminal container postgres
 - docker exec -it postgres psql -U postgres
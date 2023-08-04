# Ecommerce Project
Demo API for e-commerce. It uses the following technologies:
- Python/Django
- Django Rest Framework
- Docker/Docker Compose
- Postgres

## Required Software
- python3, pip, django
- docker/docker desktop

## To Configure/Setup
- Edit ".env.sample" and provide the necessary information and save as ".env"


## To Run
Open a terminal and type:
```bash
  docker-compose up
```

## Populate initial data
Open docker desktop app dashboard. Go to terminal tab, then run the command:

```bash
  python manage.py loaddata initial_data.json
``` 

## Create superuser
- Open docker desktop app dashboard. Go to terminal tab, then run the command:

```bash
  python manage.py createsuperuser
``` 
- Follow the prompt for user name and password

## API Verification
Navigate to:
Admin : http://localhost:8000/admin
API : http://localhost:8000/api/products/

# Medical Appointment API

## Description

The ideia of this project was creating a system for recording medical appointments.

The user is be able to register a doctor and his or hers specialization, in addition to registering appointments by inserting time and date. 

The data is stored in a database and the API will allow only one query per time and day for a doctor

## Tools Used

This project was made using Python 3.11.2, django 4.1.7 and django tastypie.

- [Python](https://realpython.com/installing-python/)
- [Django](https://docs.djangoproject.com/en/4.1/intro/install/)
- [Django-tastypie](https://django-tastypie.readthedocs.io/en/latest/tutorial.html_)
- [Postman](https://www.alura.com.br/artigos/postman-como-instalar-dar-seus-primeiros-passos?gclid=CjwKCAjw5dqgBhBNEiwA7PryaL0LwSAur7PXa6LTD_CMrQQo_wqFXbKVEHrpetviScVW7Gkiri2U8RoCP5IQAvD_BwE)

## How to Run It

To apply the migrations to the database run:

```shell
python manage.py makemigrations
python manage.py migrate
```

To run the server:

```shell
python manage.py runserver
```

The data can be inserted using POST requests or using the python shell:

```shell
python manage.py shell

>>> from api.models import Doctor
>>> doc = Doctor(first_name="primeiro nome", last_name="sobrenome", med_specialization="especialização")
>>> doc.save()
>>> Doctor.objects.all()
>>> exit()
```

## What I've learned

It was my first time using the django tastypie framework to create an API.

I've learned about REST APIS's and how to create them using python django.

I have also learned to use Postman to send the requests and how to understand them.

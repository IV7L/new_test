# Introduction
This project was submitted as a test for '' job.
This project designed using the requirements file that the client sent, and approached all the needs.

## Specifications
- Programming Language: Python
- Backend Framework: Django
- Database Engine: Postgresql

## Deployment
### Setup Virtual Enviroment
```
python virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
### Setup Database
```
$ CREATE DATABASE test;
$ CREATE USER "test" WITH PASSWORD 'test';
$ GRANT ALL PRIVILEGES ON DATABASE "test" TO "test";
```
### Setup Project
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Summary
#### Form the beginning of running the project, it will redirect the User to Login page,
### Login Page:
It requires the User to provide **Email** and **Password**
It will redirect the user after successfull login to **Members List** Page

### Members List Page:
This page provide a full list of members in the DB with the fields needed and have a button for **add new member**

### Add New Member Page:
This page provide a full form to add new member to the database, some features:
* Email Field Required
* Image Preview before submit
* Citites list changes due to Country change
* Add new member redirect the user to Members List page
* Django Messages Middleware applied after success adding

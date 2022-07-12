# Back-end API for Profile Management System
This API uses Django REST Framework for managing users.

## Installation
```
$ git clone https://github.com/D4reD3VIL81/Profile-Management-Django-REST-API.git
$ cd profile_project
$ python3 manage.py runserver
```

## Required Packages
```
Python                 3.8.10
Django                 2.2.12
djangorestframework    3.13.1
```

## Usage 
After using "runserver" command, you can use this links on your browser to view profiles :
+ API Root: 127.0.0.1:8000/api/
+ User Profile List: 127.0.0.1:8000/api/profile-viewset/
+ User Profile Detail : 127.0.0.1:8000/api/profile-viewset/"user_id"

In order to create, update or delete profile, you need to be logged in with the corrent user.
+ Creating user (POST): 127.0.0.1:8000/api/profile-viewset/
+ Login (POST): 127.0.0.1:8000/api/login/
+ Update user (PUT): 127.0.0.1:8000/api/profile-viewset/"user_id"
+ Delete user (DELETE): 127.0.0.1:8000/api/profile-viewset/"user_id"

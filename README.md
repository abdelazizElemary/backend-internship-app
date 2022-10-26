# About the project

Backend application using django.
The user can add, update, delete, get, and search for books.
There are two columns named: date_created and date_updated to trace any change in the database

## APIs discussion

1. API for adding a book -> `http://127.0.0.1:8000/api/add/book/`
2. API for updating a book -> `http://127.0.0.1:8000/api/update/book/<int:pk>/`
3. API for deleting a book -> `http://127.0.0.1:8000/api/delete/book/<int:pk>/`
4. API for retreving all books -> `http://127.0.0.1:8000/api/all/`
5. API for search by category -> `http://127.0.0.1:8000/api/all/?category=category_name`

## Request format

`{ "name": "book5665", "publishDate": "15-11-2000", "author": "Ahmed", "category": "fun" }`

## Dependencies

- sqlite3 for the database
- rest_framework

## How to run the project

1. Download or clone this reposatory.
2. While you are on the project directory, type in the terminal: `poetry install` to install all dependencies.
3. type: `poetry run manage.py runserver` to start the server.

> The server is now running, you can try the api from (postman or from your browser) hope you enjoy it 😃

# backend-internship-app

- You can start by running `poetry install`

- This is a small blog app where you have 2 models `Authors` and `Blogs`

- I have used DRF in this CRUD app using Class-based views approach

- To run the server use command `python crud/manage.py runserver` default port:8000

## You can create, read, update or delete from the db using the following apis

- to `Register` send a Post request to `http://localhost:8000/api/authors/` request's body will just need `username` and `password`

- to `Login` send a Post request to `http://localhost:8000/api/login` and it will give you back a `token key`

- to Create new `Blog` send a Post request to `http://localhost:8000/api/blogs/` request's body will need `blog_title`, `blog_text` and you will need to add `Authorization` to the header with a value `Token {the key you have got from the login}`, the author will be auto generated depending on the token user.

- to delete\update use the same scheme with changing the rquest to a `PUT` \ `DELETE` request and the parts you want to change with adding the id of the `blog` \ `author` you want to change at the end ---> `http://localhost:8000/api/Authors/{:id}/` you will need to provide the author's token authentication to be able to change or delete it.

- to read the full list of blogs\authors just use the `GET` request with --->
  `http://localhost:8000/api/blogs/` \ `http://localhost:8000/api/Authors/`

  ## Hints

  - I have used `auto_now_add` instead of `TimeStampedModels`
  - I have used `restframework authtoken` for Authintication

# backend-internship-app

- You can start by running `poetry install`

- This is a small blog app where you have 2 models `Authors` and `Blogs`

- I have used DRF in this CRUD app using Class-based views approach

- To run the server use command `python crud/manage.py runserver` default port:8000

## You can create, read, update or delete from the db using the following apis

- to Create new `Author` ---> `http://localhost:8000/api/Authors/` request's body will just need `author_name`

- to Create new `Blog` ---> `http://localhost:8000/api/blogs/` request's body will need `blog_title`, `blog_text` and an exist `blog_author` as a foreign pk(id) from `Author` model

- to delete\update use the same scheme with changing the rquest to a `PUT` \ `DELETE` request and the parts you want to change with adding the id of the `blog` \ `author` you want to change at the end ---> `http://localhost:8000/api/Authors/{:id}/`

- to read the full list of blogs\authors just use the `GET` request with --->
  `http://localhost:8000/api/blogs/` \ `http://localhost:8000/api/Authors/`

  ## Hints

  - I have used `auto_now_add` instead of `TimeStampedModels`
  - I haven't used the same `User` using `AbstractUser` as we don't need any type of authentication

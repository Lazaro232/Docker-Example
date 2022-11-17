# Simple Docker Example

This is a simple create, read, update and delete (CRUD) example using Flask, PostgreSQL and Docker.

## **The database**
The PostgreSQL database will store the name and the age of the users.

| Id (SERIAL) | Name (TEXT) | Age (INTEGER) |
|---|---|---|
|  1 | User 1  | 18  |
|  2 | User 2  | 22  |
|  3 | User 3  | 35  |

## **The API ([app.py](app.py))**
The API will have 4 endpoints. One for each *CRUD* operation.


* **/user/create**
    - This endpoint iserts a user into the database. It expects a body containing the name and the age in a JSON format.
        
        The body

           {"name": "User 1", "age": 18} 
        The answer

           User with name "User 1" and age 18 created!

* **/user/*<user_id>***
    - This endpoint retrieves a user's information. It expects the user's ID in the query string parameters.

        The query

           /user/1
        
        The answer
           
           {"name": "User 1", "age": 18} 

* **/user/update/*<user_id>***
    - This endpoint updates a user's information. It expects the user's ID in the query string parameters and the name and age in the body.

        The query

           /user/update/1
        The body

           {"name": "User X", "age": 81}
        The answer
           
           Name and age of user with ID 1 updated to "User X" and 81

* **/user/delete/*<user_id>***
    - This endpoint deletes a user's information. It expects the user's ID in the query string parameters.
        
        The query

           /user/delete/1

        The answer
           
           User with ID 1 deleted!

           

## **Docker**

* The **[Dockerfile](Dockerfile)** is used to build the Flak API image. The [Dockerfile](Dockerfile) will:
    - Use a base Python image (3.10-slim)
    - Copy the necessary files to the container folder
    - Install the dependencies in the container
    - Run the Flask application.

* The **[docker-compose.yml](docker-compose.yml)** is used to build the Flask and the PostgreSQL images, as well as is used to run the containers. The [docker-compose.yml](docker-compose.yml) will:
    - Build the database image using the postgres image, tracking the database port and creating a volume so the data can be persisted.
    - Build the API image (using the [Dockerfile](Dockerfile)), tracking Flask port, making the API image to wait for the database image to be built before it starts.
    - Create (if not exists) the volume to persist the data
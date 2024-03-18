



# Guest Book API v1

Create and list entries for a guest book via API


## Tech Stack

* Python
* Django
* Docker
* Django Rest Framework
* Pytest


## Deployment

To run this project locally

```bash
  cp sample.env .env
  # Keep the .env file same for local running

  docker-compose -f local.yaml up --build
```

To deploy this project to production

```bash
  cp sample.env .env
  # Modify the values in .env file for production environment

  docker-compose -f prod.yaml up --build
```


## Running Tests

The tests typically run automatically during the project build process. If any errors occur in the tests, the project will not proceed.
To run tests manually, run the following command while project containers running

```bash
  docker exec -it api pytest
```


## Documentation
It works only in local environment

[Swagger](http://localhost:8000/swagger/)

[Redoc](http://localhost:8000/redoc/)

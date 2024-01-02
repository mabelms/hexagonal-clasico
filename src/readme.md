# Simple brain for robotics.


It is developed using a Domain Driven Design aproach and Onion Architecture.


### How to start

First create a Python virtual environment:
```
> virtualenv venv
```

Activate the new virtual environment.
```
> . venv/bin/activate
```

fastapi.
```
> uvicorn app.main:app --reload
```

docker.
```
> docker-compose up
```
fastapi.
```
> http://127.0.0.1:8000/api/v1/sales/get-product/
```

alembic.
```
> alembic init alembic
> sqlalchemy.url =
> alembic stamp head
> alembic revision --autogenerate -m "first commit
> alembic upgrade head
```

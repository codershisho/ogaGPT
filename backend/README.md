uvicorn main:app --reload --host 0.0.0.0 --port 8000



alembic revision --autogenerate -m "create queries table"

alembic upgrade head
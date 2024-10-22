Dependency Installed

1. fastapi
2. uvicorn
3. sqlalchemy
4. pydantic
5. alembic
6. databases
7. pytest


Steps
Run following commands in vs terminal
1. venv\Scripts\activate
2. uvicorn app.main:app --reload

Adding User

curl -X POST "http://127.0.0.1:8001/users/" -H "Content-Type: application/json" -d '{"name": "<name>", "email": "<email_id>", "mobile": "<mobile_number>"}'

if doesn't work in vs terminal 
Open Powershell and run following command -

Invoke-RestMethod -Uri "http://127.0.0.1:8000/users/" -Method POST -ContentType "application/json" -Body '{"name": "<name>", "email": "<email_id>", "mobile": "<mobile_number>"}'

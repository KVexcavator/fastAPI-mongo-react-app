docker compose up

source ~/beach/bin/activate
deactivate

fastapi dev
or
uvicorn app:app --reload

http://127.0.0.1:8000
http://127.0.0.1:8000/docs
docker compose -f docker-compose-car.yml up
source ~/beach/bin/activate
uvicorn app:app --reload
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
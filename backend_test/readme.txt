source ~/beach/bin/activate
pip install -r requirements.txt
uvicorn test_beach:app --reload
uvicorn test_routers:app --reload
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
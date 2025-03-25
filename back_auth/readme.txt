https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer--example
cd back_auth/
source ~/beach/bin/activate
pip install fastapi uvicorn bcrypt==4.0.1 passlib pyjwt

http 127.0.0.1:8000/users/register username="ivan" password="ivan123"
http POST 127.0.0.1:8000/users/login username="ivan" password="ivan123"
http POST 127.0.0.1:8000/users/login username="ivan" password="wrong222"

http GET 127.0.0.1:8000/users/list "Authorization:Bearer <token>"
http GET 127.0.0.1:8000/users/list "Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDU1MjI3NzYsImlhdCI6MTc0MjkzMDc3Niwic3ViIjoie1widXNlcl9pZFwiOiBcIjU1MWNlNmZhLTFhMTYtNGFjMC05MjM0LWQyODg5NDQ1NWI2NFwiLCBcInVzZXJuYW1lXCI6IFwiaXZhblwifSJ9.xJNXEqvhOP4-BAbtDcw3zGPYMk1LyU2AjItuIEHY0iM"


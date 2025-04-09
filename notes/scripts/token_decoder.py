import jwt

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDU1MTg1NjQsImlhdCI6MTc0MjkyNjU2NCwic3ViIjp7InVzZXJfaWQiOiI1NTFjZTZmYS0xYTE2LTRhYzAtOTIzNC1kMjg4OTQ0NTViNjQiLCJ1c2VybmFtZSI6Iml2YW4ifX0.IK8xZKvF2XncZQwUqFgLDb4zUCvgw2-LE-kpjf2YheQ"

secret = "MyVeryLongSecretString"

try:
    decoded = jwt.decode(token, secret, algorithms=["HS256"])
    print("Decoded success")
    print(decoded)
except jwt.ExpiredSignatureError:
    print("Token expired")
except jwt.InvalidTokenError:
    print("Invalid token")

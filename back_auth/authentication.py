import datetime
import json
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

class AuthHandler:
  security = HTTPBearer()
  pwd_context = CryptContext(schemes=['bcrypt'], deprecated = "auto")
  secret = "MyVeryLongSecretString"

  def get_password_hash(self, password: str) -> str:
    return self.pwd_context.hash(password)
  
  def verify_password(
      self,
      plain_password: str,
      hashed_password: str
  ) -> bool:
    return self.pwd_context.verify(
      plain_password,
      hashed_password
    )

  def encode_token(self, user_id: int, username: str) -> str:
    payload = {
      "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30),
      "iat": datetime.datetime.now(datetime.timezone.utc),
      "sub": json.dumps({"user_id": user_id, "username": username}),
    }
    return jwt.encode(payload, self.secret, algorithm="HS256")

  def decode_token(self, token: str):
    try:
      payload = jwt.decode(token, self.secret, algorithms=["HS256"])
      return json.loads(payload["sub"])
    except jwt.ExpiredSignatureError:
      raise HTTPException(
        status_code=401,
        detail="Signature has expired"
      )
    except jwt.InvalidTokenError:
      raise HTTPException(
        status_code=401,
        detail="Invalid token"
      )
    # for debug return details error
    # except jwt.InvalidTokenError as e:
    #   print(f"Invalid token: {e}")
    #   raise HTTPException(status_code=401, detail="Invalid token")
    
  def auth_wrapper(
    self,
    auth: HTTPAuthorizationCredentials = Security(security)
  ) -> dict:
    return self.decode_token(auth.credentials)
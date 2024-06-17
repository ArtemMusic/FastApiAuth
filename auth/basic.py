import secrets

from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic

users = {
    'admin': 'root',
    'usr': 'pass'
}


def basic_auth(credentials: HTTPBasicCredentials = Depends(HTTPBasic())) -> dict:
    unauthorized_usr = HTTPException(
        detail='Invalid username or password',
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={'WWW-Authenticate': 'Basic'},
    )

    current_usr = users.get(credentials.username)

    if current_usr is None:
        raise unauthorized_usr

    if not secrets.compare_digest(current_usr.encode('utf-8'), credentials.password.encode('utf-8')):
        raise unauthorized_usr

    return {
        'message': 'hi',
        'username': credentials.username,
        'password': credentials.password,
        'credentials': credentials
    }

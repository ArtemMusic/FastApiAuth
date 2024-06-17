import secrets
from time import time

from fastapi import Response, Depends, Cookie, HTTPException, status

from auth import header

COOKIES_backend: dict[str, dict[str, any]] = {}
COOKIE_SESSION_ID_KEY = 'x-auth-session-id'


def get_session_data(session_id: str = Cookie(alias=COOKIE_SESSION_ID_KEY)) -> dict:
    if session_id not in COOKIES_backend:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="not authenticated",
        )

    return COOKIES_backend[session_id]


def login_set_cookie(response: Response, username: dict = Depends(header.header_token_auth)) -> dict:
    session_id = secrets.token_hex()

    COOKIES_backend[session_id] = {
        "username": username,
        "login_at": int(time()),
    }

    response.set_cookie(COOKIE_SESSION_ID_KEY, session_id)

    user_session_data = get_session_data(session_id)
    username = user_session_data['username']

    return {
        "message": f"Hello, {username}!",
        "session_id": session_id,
        **user_session_data,
    }


def logout_delete_cookie(
        response: Response,
        user_session_data: dict = Depends(get_session_data),
        session_id: str = Cookie(alias=COOKIE_SESSION_ID_KEY)
) -> dict:
    response.delete_cookie(COOKIE_SESSION_ID_KEY)
    COOKIES_backend.pop(session_id)

    username = user_session_data["username"]
    return {
        "message": f"Bye, {username}!",
    }

from fastapi import APIRouter, Depends

from auth import basic
from auth import header
from auth import cookie

router = APIRouter(
    prefix='/auth'
)


@router.get('/basic')
def basic_auth(credentials=Depends(basic.basic_auth)) -> dict:
    return credentials


@router.get('/header')
def header_token_auth(usr=Depends(header.header_token_auth)) -> dict:
    return usr


@router.get('/login-cookie')
def login_set_cookie(session_id=Depends(cookie.login_set_cookie)) -> dict:
    return session_id


@router.get('/logout-cookie')
def login_set_cookie(usr=Depends(cookie.logout_delete_cookie)) -> dict:
    return usr

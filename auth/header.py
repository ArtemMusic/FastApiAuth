from fastapi import Header, HTTPException, status

auth_token_to_username = {
    'shdjfkghdsybgfvjsydghkhb32r6fty': 'admin',
    'gir372urilho1jlkfa3264ut86tgfvg': 'usr'
}


def header_token_auth(static_token: str = Header(alias='x-auth-token')) -> dict:
    if username := auth_token_to_username.get(static_token):
        return {'User': username}

    raise HTTPException(
        detail='Invalid static_token',
        status_code=status.HTTP_401_UNAUTHORIZED,
    )

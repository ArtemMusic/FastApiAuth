import uvicorn
from fastapi import FastAPI
from auth.view import router as auth_router

app = FastAPI(
    title='Auth'
)

app.include_router(auth_router, tags=['auth'])

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

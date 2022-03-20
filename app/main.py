from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

from app.common.config import conf


def create_app():
    """
    앱 함수 실행
    :return:
    """
    # c = conf()
    app = FastAPI()
    # 데이터베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터 정의
    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', reload=conf().PROJ_RELOAD)

# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
        
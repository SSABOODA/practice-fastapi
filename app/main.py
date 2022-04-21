import uvicorn
from fastapi import FastAPI
from typing import Optional
from dataclasses import asdict
from app.database.conn import db
from app.common.config import conf
from app.routes import index


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # DATABASE Initialize

    # Redis Initialize

    # Middleware 정의

    # 라우터 정의
    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', reload=conf().PROJ_RELOAD)


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
        
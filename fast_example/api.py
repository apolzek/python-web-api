# python3 -m pip install fastapi[all]

from fastapi import FastAPI
from pydantic import BaseModel  # Anotações com tipos

dados = {"canal": "LinuxTips", "msg": "VAIII"}


app = FastAPI()


class LinuxTips(BaseModel):
    canal: str
    msg: str
    dia: int


@app.get("/", response_model=LinuxTips)
async def linuxtips(): # não obrigatório
    return LinuxTips(
        canal="LinuxTips",
        msg="VAIIIII",
        dia=25
    )
    # return dados

# RUN: python3 -m uvicorn api:app
# 127.0.0.1:8000/redoc
# 127.0.0.1:8000/docs

# python3 -m pip install flask
# ipython3 -i app.py

from flask import Flask, request

dados = {"canal": "LinuxTips", "msg": "VAIII"}  # dict

app = Flask("app")


@app.route("/")
def linuxtips():
    return dados


@app.route("/hello/<nome>/")  # localhost:5000/hello/vinicius/
def hello(nome):
    # localhost:5000/hello/vinicius/?msg=VAIIIIIIIIIIII
    return f"<h1> Hello </h1><h2 style='color:red'> {request.args['msg']} </h2>"

    # localhost:5000/hello/VAIII/
    # return f"<h1> Hello </h1><h2 style='color:red'>{nome}</h2>"

# RUN: python3 -m flask run

import os
from flask import Flask, request
app = Flask(__name__)
HOLOVIP_KEY = os.environ.get("HOLOVIP_KEY", "HOLOVIP-10A5-K4HC-9TA2")
HOLOVIP_TOKEN = os.environ.get("HOLOVIP_TOKEN", "SEBAS2026_SECRET")
@app.route("/")
def home():
    return "HoloVIP API OK - Online"
@app.route("/validate")
def validate():
    k=request.args.get("key","")
    t=request.args.get("token","")
    if k==HOLOVIP_KEY and t==HOLOVIP_TOKEN:
        return "VALIDA"
    else:

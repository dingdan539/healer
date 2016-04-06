from src.config import *
from flask import Flask, send_from_directory
app = Flask(__name__)

config = load_config_auto()
profix = config.DOMAIN_PROFIX


@app.route(profix+'/docs')
def docs():
    return send_from_directory('docs/build/html/', 'index.html')


@app.route(profix+'/<path:filename>')
def summary(filename):
    return send_from_directory('docs/build/html/', filename)


@app.route(profix+'/_static/<path:filename>')
def js2(filename):
    return send_from_directory('docs/build/html/_static/', filename)

app.run()
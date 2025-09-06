import requests
from typing import cast

from flask import render_template, session

from . import frontend_blueprint
from .api.Content import Content


@frontend_blueprint.route("/", methods=["GET"])
def home() -> str:
    try:
        content = Content.get_content(cast(dict, session))
    except requests.exceptions.ConnectionError:
        print("Not connected")
        content = {"title": "No title", "text": "No text"}
    return render_template("index.html", content=content)

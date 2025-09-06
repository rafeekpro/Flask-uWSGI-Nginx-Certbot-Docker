import requests
from flask import flash, jsonify, redirect, render_template, request, session, url_for

from . import frontend_blueprint
from .api.Content import Content


@frontend_blueprint.route("/", methods=["GET"])
def home():
    try:
        content = Content.get_content(session)
    except requests.exceptions.ConnectionError:
        print("Not connected")
        content = {"title": "No title", "text": "No text"}
    return render_template("index.html", content=content)

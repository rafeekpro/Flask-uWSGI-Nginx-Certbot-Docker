from flask import render_template, session, redirect, url_for, flash, request, jsonify
import requests
from . import frontend_blueprint
from .api.Content import Content

@frontend_blueprint.route('/', methods=['GET'])
def home():
    try:
        content = Content.get_content(session)
    except requests.exceptions.ConnectionError:
        print("Not connected")
        content={"title": "No title", "text": "No text"}
    return render_template('index.html', content=content)
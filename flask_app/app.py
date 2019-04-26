from flask import Blueprint, Flask
from frontend import frontend_blueprint

app = Flask(__name__)
app.register_blueprint(frontend_blueprint)

if __name__ == '__main__':
    app.run()

from flask import Flask
import logging
from main.views import main_blueprint
from loader.views import loader_blueprint


logging.basicConfig(filename="log.log", level=logging.INFO)
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


if __name__ == "__main__":
    app.run()

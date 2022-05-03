from flask import render_template, Blueprint, request
from functions import search_posts
import logging


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route("/search")
def page_tag():
    s = request.args.get('s', '')
    posts = search_posts(s)
    logging.info(f'Выполнен поиск по значению {s}')
    return render_template('post_list.html', keyword=s, posts=posts)

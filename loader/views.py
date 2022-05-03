import json
import logging

from flask import render_template, Blueprint, request
from functions import get_posts


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post', methods=['get'])
def main_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['post'])
def add_new_post():
    picture = request.files.get('picture')
    text = request.form.get('content')
    filename = picture.filename
    if filename[-3:] != 'jpg' or filename != 'png':
        logging.info('Загружаемый файл - не картинка')
        raise ValueError
    picture_path = f"uploads/images/{filename}"
    new_post = {"pic": picture_path, "content": text}
    try:
        picture.save(picture_path)
    except FileExistsError:
        logging.error('Не удалось сохранить файл!')
        return 'Не удалось сохранить файл!'
    posts = get_posts()
    posts.append(new_post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return render_template('post_uploaded.html', picture=picture_path, text=text)

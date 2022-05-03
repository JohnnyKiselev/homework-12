import json
from json import JSONDecodeError


def get_posts():
    with open('posts.json', encoding='utf-8') as f:
        try:
            posts = json.load(f)
        except FileNotFoundError:
            print("Файл не найден")
        except JSONDecodeError:
            print("Файл не удается преобразовать")
    return posts


def search_posts(keyword):
    content = []
    for post in get_posts():
        if keyword in post['content']:
            content.append(post)
    return content

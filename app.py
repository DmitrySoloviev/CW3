import logging
from flask import Flask, request, render_template, abort
from main.main import main_page
from utils import get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

# Регистрация blueprint
app.register_blueprint(main_page)


# Вывод постов по id
@app.route("/posts/<int:post_id>")
def single_page(post_id):
    logging.info("Страница поста запрошена")
    posts = get_post_by_pk(post_id)
    comments_for_post = get_comments_by_post_id(post_id)
    if posts is None or comments_for_post is None:
        return abort(404)
    return render_template("post.html", post=posts, comments=comments_for_post)


# Вывод постов по слову
@app.route("/search")
def search_page():
    logging.info("Страница поиска запрошена")
    s = request.args['s']
    post_with = search_for_posts(s)
    if post_with is None:
        return abort(404)
    return render_template('search.html', posts=post_with)


# Вывод на посты пользователя
@app.route("/users/<user_name>")
def page_user(user_name):
    logging.info("Страница постов пользователя запрошена")
    user_posts = get_posts_by_user(user_name)
    if user_posts is None:
        return abort(404)
    return render_template("user-feed.html", posts=user_posts)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


# Запуск Flask
app.run(port=8000, debug=True)


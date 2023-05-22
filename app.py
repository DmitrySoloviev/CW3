import logging
from main.main import main_page
from utils import get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user
from flask import Flask, jsonify, abort, request, render_template
from DAO.data_dao import DataDAO
from DAO.comments_dao import CommentsDAO

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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
    return render_template('error.html'), 404

path = "data/data.json"
path_two = "data/comments.json"
data_dao = DataDAO(path)
comments_dao = CommentsDAO(path_two)

@app.route("/api")
def data_page():
    data = data_dao.get_data()
    return jsonify(data)


@app.route("/api/posts/<int:post_id>")
def single_page_api(post_id):
    posts = data_dao.get_post_by_pk(post_id)
    comments_for_post = comments_dao.get_comments_by_post_id(post_id)
    complete_post = []
    for post in posts:
        complete_post.append(post)
    for comment in comments_for_post:
        complete_post.append(comment)
    if posts is None or comments_for_post is None:
        return abort(404)
    return jsonify(comments_for_post)


@app.route("/api/search")
def search_page_api():
    s = request.args['s']
    post_with = data_dao.search_for_posts(s)
    if post_with is None:
        return abort(404)
    return jsonify(post_with)


@app.route("/api/users/<user_name>")
def page_user_api(user_name):
    user_posts = data_dao.get_posts_by_user(user_name)
    if user_posts is None:
        return abort(404)
    return jsonify(user_posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000, debug=True)

# Запуск Flask
#app.run(port=8000, debug=True)


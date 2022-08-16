import json

from flask import Flask, jsonify, abort, request, render_template
from DAO.data_dao import DataDAO
from DAO.comments_dao import CommentsDAO

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

path = "data/data.json"
path_two = "data/comments.json"
data_dao = DataDAO(path)
comments_dao = CommentsDAO(path_two)

@app.route("/")
def data_page():
    data = data_dao.get_data()
    return jsonify(data)


@app.route("/posts/<int:post_id>")
def single_page(post_id):
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


@app.route("/search")
def search_page():
    s = request.args['s']
    post_with = data_dao.search_for_posts(s)
    if post_with is None:
        return abort(404)
    return jsonify(post_with)


@app.route("/users/<user_name>")
def page_user(user_name):
    user_posts = data_dao.get_posts_by_user(user_name)
    if user_posts is None:
        return abort(404)
    return jsonify(user_posts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


if __name__ == '__main__':
    app.run(port=500, debug=True)
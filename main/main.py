import logging
from flask import Blueprint, render_template
from utils import get_posts_all, get_num_post

main_page = Blueprint("main_page", __name__, template_folder='templates', static_folder="static")


@main_page.route("/")
@main_page.route("/home")
def index():
    logging.info("Главная страница запрошена")
    list_posts = get_posts_all()
    num_posts = get_num_post()
    return render_template('index.html', list_posts=list_posts, num_posts=num_posts)

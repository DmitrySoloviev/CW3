import pytest
from utils import search_for_posts, get_num_post, get_comments_by_post_id, get_posts_by_user


def test_search_for_posts():
    assert type(search_for_posts('еда')) == list


def test_get_num_post():
    assert type(get_num_post()) == int


def test_get_posts_by_user():
    assert type(get_posts_by_user('leo')) == list


def test_get_comments_by_post_id():
    assert type(get_comments_by_post_id(1)) == list


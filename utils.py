import json


def get_posts_all():
    """
    Возвращает список всех постов
    """
    with open('./data/data.json', 'r', encoding='utf-8') as file:
        list_posts = json.load(file)
        file.close()
    return list_posts


def get_num_post():
    """
    Возвращает количество постов
    """
    list_posts = get_posts_all()
    num_post = 0
    for post in list_posts:
        num_post += 1
    return num_post


def get_posts_by_user(user_name):
    """
    Возвращает посты юзера
    """
    list_posts = get_posts_all()
    user_posts = []
    names_of_users = []
    for posts in list_posts:
        names_of_users.append(posts['poster_name'].lower())
    if user_name.lower() in names_of_users:
        pass
    else:
        user_name = "leo"
    for posts in list_posts:
        if posts['poster_name'].lower() == user_name.lower():
            user_posts.append(posts)
        else:
            pass
    return user_posts


def get_comments_by_post_id(post_id):
    """
    Возвращает список комментариев к посту
    """
    with open('./data/comments.json', 'r', encoding='utf-8') as file:
        list_comments = json.load(file)
        file.close()
    comments_by_id = []
    list_of_id = []
    for comment in list_comments:
        list_of_id.append(comment['post_id'])
    if int(post_id) in list_of_id:
        pass
    else:
        post_id = 1
    for comment in list_comments:
        if comment['post_id'] == int(post_id):
            comments_by_id.append(comment)
        else:
            pass
    return comments_by_id


def search_for_posts(query):
    """
    Возвращает список постов по слову
    """
    list_posts = get_posts_all()
    post_with_word = []
    try:
        for post in list_posts:
            post['content'] = post['content'].replace(",", "")
            post['content'] = post['content'].replace(".", "")
            post['content'] = post['content'].replace("!", "")
            post['content'] = post['content'].replace("?", "")
            content_post = post['content'].split(" ")
            w_one = query.lower()
            w_two = query.title()
            w_three = query.upper()
            if w_one in content_post or w_two in content_post or w_three in content_post:
                post_with_word.append(post)
            else:
                pass
        return post_with_word
    except ValueError:
        raise "Такого слова нет"


def get_post_by_pk(pk):
    """
    Возвращает список постов по pk
    """
    list_posts = get_posts_all()
    pk_of_posts = []
    for post in list_posts:
        pk_of_posts.append(post['pk'])
    if pk in pk_of_posts:
        pass
    else:
        return "Такого pk нет"
    for post in list_posts:
        if post['pk'] == pk:
            return post
        else:
            pass

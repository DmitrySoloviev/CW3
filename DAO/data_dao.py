class DataDAO:
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        import json
        with open(self.path, 'r', encoding='utf-8') as file:
            list_data = json.load(file)
            file.close()
        return list_data

    def get_data(self):
        return self._load_data()

    def get_posts_by_user(self, user_name):
        list_posts = self._load_data()
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

    def get_post_by_pk(self, id_post: int):
        list_posts = self._load_data()
        pk_of_posts = []
        for post in list_posts:
            pk_of_posts.append(post['pk'])
        if id_post in pk_of_posts:
            pass
        else:
            id_post = 1
        for post in list_posts:
            if post['pk'] == id_post:
                return post
            else:
                pass

    def search_for_posts(self, query):

        list_posts = self._load_data()
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

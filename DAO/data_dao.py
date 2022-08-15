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

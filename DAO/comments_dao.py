import json


class CommentsDAO:
    def __init__(self, path):
        self.path = path


    def _load_data(self):
        import json
        with open(self.path, 'r', encoding='utf-8') as file:
            list_data = json.load(file)
            file.close()
        return list_data

    def get_comments_by_post_id(self, post_id):
        list_comments = self._load_data()
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



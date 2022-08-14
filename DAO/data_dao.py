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

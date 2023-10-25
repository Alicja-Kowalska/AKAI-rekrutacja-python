import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        with open("taski.json", "r") as data:
            content = json.load(data)
        return content
        pass

    def get_tasks(self):
        return self.read_tasks()
        pass

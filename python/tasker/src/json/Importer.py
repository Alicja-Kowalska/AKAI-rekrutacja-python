import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        data = open("taski.json", "r")
        content = json.load(data)
        data.close()
        return content
        pass

    def get_tasks(self):
        return self.read_tasks()
        pass

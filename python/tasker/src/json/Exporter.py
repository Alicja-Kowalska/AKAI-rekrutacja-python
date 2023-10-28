import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        data = open("taski.json", "w")
        json.dump(tasks, data, indent=4)
        data.close()
        pass

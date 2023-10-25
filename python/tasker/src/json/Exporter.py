import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        tasks = input()
        with open("taski.json", "w") as data:
            json.dump(tasks, data)
        pass

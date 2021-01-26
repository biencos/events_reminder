import json


class FileManager(object):
    def __init__(self, filename):
        self.filename = filename

    def save_to_json_file(self, data):
        with open(self.filename, 'w') as json_file:
            json.dump(data, json_file)

import os
import json


class FileManager(object):
    def __init__(self, filename):
        self.filename = filename

    def json_file_exists(self):
        return os.path.isfile(self.filename)

    def save_to_json_file(self, data):
        with open(self.filename, 'w') as json_file:
            json.dump(data, json_file)

    def load_from_json_file(self, data_attribute):
        with open(self.filename) as json_file:
            data = json.load(json_file)
            specific_data = data[data_attribute]
        return specific_data

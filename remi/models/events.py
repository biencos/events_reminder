import os
from datetime import datetime, timedelta

import uuid

from .file_manager import FileManager
from .validation import file_exists


class Events(object):
    def __init__(self, filename):
        self.file_manager = FileManager(filename)
        self.events = []
        self.specific_events = []

    def get_events(self):
        if not file_exists(self.file_manager.filename):
            self.events = []
            self.__save_events()
            return

        self.events = self.__load_events()
        if len(self.events) > 0:
            self.events = sorted(
                self.events, key=lambda e: datetime.strptime(e['date'], '%d.%m'))
            cei = self.__get_closest_event_index(datetime.now())
            self.events = self.events[cei:] + self.events[0:cei]

    def get_specific_events(self, start=0, duration=14):
        if not len(self.events) > 0:
            self.specific_events = []
            return

        if not start <= duration:
            print("Error! Incorrect values of arguments!")
            self.specific_events = []
            return

        s_date = datetime.now() + timedelta(days=start)
        si = self.__get_closest_event_index(s_date)
        e_date = datetime.now() + timedelta(days=duration+1)
        ei = self.__get_closest_event_index(e_date)

        if si <= ei:
            self.specific_events = self.events[si:ei]
        else:
            self.specific_events = self.events[si:] + self.events[0:ei]

    def add_event(self, name, day, month, year):
        event_id = str(uuid.uuid4())[0:5]
        date_string = "%s.%s" % (day, month)

        event = {}
        event["id"], event["name"] = event_id, name
        event["date"], event["year"] = date_string, year
        self.events.append(event)

        data = {}
        data['events'] = self.events
        self.file_manager.save_to_json_file(data)

    def edit_event(self, event_id, selected_attribute, value):
        events_with_id = [e for e in self.events if e["id"] == event_id]
        if len(events_with_id) == 0:
            print("There is no event with that id!")
        elif len(events_with_id) == 1:
            i = self.events.index(events_with_id[0])
            self.events[i][selected_attribute] = value
            self.__save_events()
            print("Event was successfully changed!")
        else:
            print("There was an error during editing!")

    def delete_event(self, event_id):
        events_with_id = [e for e in self.events if e["id"] == event_id]
        if len(events_with_id) == 0:
            print("There is no event with that id!")
        elif len(events_with_id) == 1:
            self.events.remove(events_with_id[0])
            self.__save_events()
            print("Event was successfully deleted!")
        else:
            print("There was an error during event deletion!")

    @staticmethod
    def __count_dates_difference(date_string, date_string_1):
        date = datetime.strptime(date_string, '%d.%m')
        date_1 = datetime.strptime(date_string_1, '%d.%m')

        difference = (date_1 - date).days
        if not difference < 0:
            return difference
        else:
            return difference + 365

    def __get_closest_event_index(self, date):
        date_string = "%s.%s" % (date.day, date.month)
        closest_event = min(
            self.events, key=lambda e: self.__count_dates_difference(date_string, e['date']))
        return self.events.index(closest_event)

    def __save_events(self):
        data = {}
        data['events'] = self.events
        self.file_manager.save_to_json_file(data)

    def __load_events(self):
        events_attribute_name = 'events'
        return self.file_manager.load_from_json_file(events_attribute_name)

    def load_events_from_txt_file(self, filename):
        if not file_exists(filename):
            return []

        lines = self.file_manager.load_lines_from_txt_file(filename)
        names = lines[::3]
        dates = lines[1::3]

        if not len(names) == len(dates):
            return []

        for i in range(len(names)):
            name = names[i].rstrip("\n")
            sd = dates[i].rstrip("\n").split(".")
            day, month, year = sd[0], sd[1], sd[2]
            self.add_event(name, day, month, year)

        self.__save_events()
        return self.events

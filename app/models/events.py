import os
from datetime import datetime, timedelta

import uuid

from .file_manager import FileManager


class Events(object):
    def __init__(self, filename):
        self.file_manager = FileManager(filename)
        self.events = []
        self.specific_events = []

    def get_events(self):
        """Gets all events and organizes them from today to yesterday (today-1)."""

        if not self.file_manager.json_file_exists():
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
        """Gets specific events from list of events.

        Parameters:
        start (int): How many days would be added to today
        duration (int): How many days, from start, should the events be
        """

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

    def add_event(self, name, day, month):
        """Adds new event.

        Parameters:
        events (list): List of events
        name (str): Name of the new event 
        day (int): Day in which the new event is happening
        month (int): Month in which the new event is happening

        Returns:
        list: List of events with new event
        """

        event_id = str(uuid.uuid4())[0:5]
        date_string = "%s.%s" % (day, month)

        event = {}
        event["id"], event["name"], event["date"] = event_id, name, date_string
        self.events.append(event)

        data = {}
        data['events'] = self.events
        self.file_manager.save_to_json_file(data)
        print("New event was successfully added!")

    def edit_event(self, event_id, selected_attribute, value):
        """Modifies event with id the same as event_id.

        Parameters:
        event_id (int): Id of event that will be modified
        selected_attribute (str): Selected attribute of event
        value (int): New value of attribute
        """

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
        """Deletes event with id the same as event_id.

        Parameters:
        event_id (int): Id of event that needs to be deleted
        """

        events_with_id = [e for e in self.events if e["id"] == event_id]
        if len(events_with_id) == 0:
            print("There is no event with that id!")
        elif len(events_with_id) == 1:
            self.events.remove(events_with_id[0])
            self.__save_events()
            print("Event was successfully deleted!")
        else:
            print("There was an error during event deletion!")

    # PRIVATE FUNCTIONS
    def __get_closest_event_index(self, date):
        """Gets index of event, from events, which is closest to given date.

        Parameters:
        date (datetime): date given by user

        Returns:
        int: index of event that is closest to given date
        """
        date_string = "%s.%s" % (date.day, date.month)
        closest_event = min(
            self.events, key=lambda e: self.__count_dates_difference(date_string, e['date']))
        return self.events.index(closest_event)

    @staticmethod
    def __count_dates_difference(date_string, date_string_1):
        """Count difference between two dates given in string.

        Parameters:
        date_string (str): first date of type string
        date_string_1 (str): second date of type string

        Returns:
        int: Difference, in days, beetween two dates  
        """

        date = datetime.strptime(date_string, '%d.%m')
        date_1 = datetime.strptime(date_string_1, '%d.%m')

        difference = (date_1 - date).days
        if not difference < 0:
            return difference
        else:
            return difference + 365

    def __save_events(self):
        """Saves event with id the same as event_id."""

        data = {}
        data['events'] = self.events
        self.file_manager.save_to_json_file(data)

    def __load_events(self):
        """Loads events from json file."""

        events_attribute_name = 'events'
        return self.file_manager.load_from_json_file(events_attribute_name)

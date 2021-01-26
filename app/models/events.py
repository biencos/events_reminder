import os
from datetime import datetime, timedelta

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
            data = {}
            data['events'] = self.events
            self.file_manager.save_to_json_file(data)
            return

        self.events = self.file_manager.load_from_json_file('events')
        if not len(self.events) > 0:
            return

        self.events = sorted(
            self.events, key=lambda e: datetime.strptime(e['date'], '%d-%m'))
        cei = self.__get_closest_event_index()
        self.events = self.events[cei:] + self.events[0:cei]

    def __get_closest_event_index(self):
        """Gets index of event that is closest to today from events.

        Returns:
        int: index of event that is closest to today
        """

        today = datetime.now()
        today_string = "%s-%s" % (today.day, today.month)

        closest_event = min(
            self.events, key=lambda e: self.__count_dates_difference(today_string, e['date']))
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

        date = datetime.strptime(date_string, '%d-%m')
        date_1 = datetime.strptime(date_string_1, '%d-%m')

        difference = (date_1 - date).days
        if not difference < 0:
            return difference
        else:
            return difference + 365

    def get_specific_events(self, events, start, duration):
        """Gets specific events from list of events.

        Parameters:
        events (list): List of events
        start (int): How many days would be added to today
        duration (int): From how many days (from start) should the events be get

        Returns:
        list: List of events
        """

        # TODO - get specific events
        return

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

        event_id = len(self.events) + 1
        date_string = "%s-%s" % (day, month)

        event = {}
        event["id"], event["name"], event["date"] = event_id, name, date_string
        self.events.append(event)

        data = {}
        data['events'] = self.events
        self.file_manager.save_to_json_file(data)
        print("New event was successfully added!")

    def edit_event(self, events, event_id, selected, value):
        """Modifies event with id the same as event_id.

        Parameters:
        events (list): List of events
        event_id (int): Id of event that will be modified
        selected (str): Selected attribute of event
        value (int): New value of attribute

        Returns:
        list: Updated list of events
    """

        # TODO - edit event
        return

    def delete_event(self, events, event_id):
        """Deletes event with id the same as event_id.

        Parameters:
        events (list): List of events
        event_id (int): Id of event that needs to be deleted

        Returns:
        list: Updated list of events
    """

        # TODO - delete event
        return

import json


JSON_FILE_NAME = "events.json"


def get_events(filename):
    """Gets all events from given json file.

    Parameters:
    filename (str): Name of json file with events

    Returns:
    list: List of events
   """

    # TODO - get all events
    return


def get_specific_events(events, start, duration):
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


def add_event(events, name, day, month):
    """Adds new event.

    Parameters:
    events (list): List of events
    name (str): Name of the new event 
    day (int): Day in which the new event is happening
    month (int): Month in which the new event is happening

    Returns:
    list: List of events with new event
   """

    event = {}
    event_id = len(events) + 1
    date_string = "%s-%s" % (day, month)
    event["id"], event["name"], event["date"] = event_id, name, date_string
    events.append(event)
    events = __save_events(events, JSON_FILE_NAME)
    print("New event was successfully added!")
    return events


def edit_event(events, event_id, selected, value):
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


def delete_event(events, event_id):
    """Deletes event with id the same as event_id.

    Parameters:
    events (list): List of events
    event_id (int): Id of event that needs to be deleted

    Returns:
    list: Updated list of events
   """

    # TODO - delete event
    return


def __save_events(events, filename):
    data = {}
    data['events'] = events
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
    return events

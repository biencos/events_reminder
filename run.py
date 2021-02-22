import sys
from datetime import datetime

import events_reminder.models.colors_manager as cm
import events_reminder.models.validation as v
from events_reminder.models.events import Events


# Configurations
HA = "\t\t\t"       # HEADER_ACAPIT
SA = "\t\t"         # SUBHEADER_ACAPIT
TA = "\t"           # TEXT_ACAPIT

JSON_FILE_NAME = "events_reminder/data/events.json"


def main():
    e = Events(JSON_FILE_NAME)
    e.get_events()
    e.get_specific_events()

    print("")
    cm.printBlue(f"{HA}INCOMING EVENTS")
    print("")
    print_events(e.specific_events)

    print("")
    cm.printPurple(f"{SA}Press 1 to launch main menu")
    selected = input(":")
    if not v.is_option_valid(selected, 1, 1):
        selected = -1
    selected = int(selected)
    if not selected == 1:
        selected = -1

    ACTIONS = ['add event', 'edit event', 'delete event',
               'show incoming events',  'show all events', 'load events from file', 'exit']
    while 0 < selected < len(ACTIONS):
        print("")
        print("")
        print("")
        print_actions(ACTIONS, "-")
        print("")
        selected = get_selected_option(input(":"), 1, len(ACTIONS))

        if selected == 1:
            cm.printBlue(f"{HA}ADD NEW EVENT")
            print(f"{SA}Enter values of new event")
            name = input("Name: ")
            if not v.is_name_valid(name):
                cm.printRed(f"{TA}Name can only contain alphabets and spaces!")
                sys.exit(0)
            d, m, y = input("Day: "), input("Month: "), input("Year: ")
            if not v.is_date_valid(d, m, y):
                cm.printRed(f"{TA}This date doesn't exists!")
                sys.exit(0)
            e.add_event(name, d, m, y)
            print("")

        if selected == 2:
            cm.printBlue(f"{HA}EDIT EVENT")
            cm.printCyan(f"{SA}Enter id of event that You want to edit")
            event_id = input("Id: ")
            if len(event_id) != 5:
                cm.printRed(f"{TA}There is no event with such id!")
            else:
                EDIT_ACTIONS = ['name', 'day', 'month', 'year']
                print_actions(EDIT_ACTIONS, "- to edit")
                print("")
                selected_e = get_selected_option(input(":"), 1, len(ACTIONS))
                selected_attribute = EDIT_ACTIONS[selected_e - 1]
                cm.printGreen(f"{SA}Enter new value of {selected_attribute}")
                value = input(": ")
                print("")
                e.edit_event(event_id, selected_attribute, value)

        if selected == 3:
            cm.printBlue(f"{HA}DELETE EVENT")
            cm.printRed(f"{SA}Enter id of event that needs to be deleted")
            event_id = input("Id: ")
            print("")
            if len(event_id) == 5:
                e.delete_event(event_id)
            else:
                cm.printRed(f"{TA}There is no event with such id!")
        if selected == 4:
            cm.printBlue(f"{HA}INCOMING EVENTS")
            print("")
            e.get_specific_events()
            print_events(e.specific_events)
        if selected == 5:
            cm.printPurple(f"{HA}ALL EVENTS")
            print("")
            e.get_events()
            print_events(e.events)
        if selected == 6:
            cm.printBlue(f"{HA}LOAD EVENTS FROM FILE")
            print(f"{SA}Enter name of txt file with events")
            filename = input("File Name: ")
            events = e.load_events_from_txt_file(filename)
            if len(events) == 0:
                cm.printRed(f"{TA} There is no file with that name!")
                sys.exit(0)
            cm.printBlue(f"{TA} New events were successfully added!")

    print("")
    cm.printYellow(f"{SA}See you next time")


def print_actions(actions, prfx):
    cm.printBlue(f"{HA}WHAT DO YOU WANT TO DO?")
    print("")
    [cm.printCyan(f"{HA}{i+1} {prfx} {actions[i]}")
     for i in range(len(actions))]


def get_selected_option(inp, inp_limit, inp_limit1):
    if not v.is_option_valid(inp, inp_limit, inp_limit1):
        cm.printRed(
            f"{TA}Option must be a number between {inp_limit} and {inp_limit1}")
        sys.exit(0)
    return int(inp)


def print_events(events):
    if len(events) > 0:
        for e in events:
            which_event = datetime.now().year - int(e["year"]) if "year" in e else "" 
            cm.printGreen(f'{SA}* {which_event} {e["name"]}\t({e["date"]})\t[{e["id"]}]')
    else:
        cm.printRed(f"{HA}There is no events.")


if __name__ == "__main__":
    main()

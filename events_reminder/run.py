import sys

from models.events import Events
import models.colors_manager as cm
import models.validation as v


# Configurations
HA = "\t\t\t"        # HEADER_ACAPIT
SA = "\t\t"       # SUBHEADER_ACAPIT
TA = "\t"              # TEXT_ACAPIT

JSON_FILE_NAME = "data/events.json"


def main():
    e = Events(JSON_FILE_NAME)
    e.get_events()
    e.get_specific_events()

    print("")
    cm.printBlue(f"{HA}INCOMING EVENTS")
    print("")
    print_events(e.specific_events)

    ACTIONS = ['add event', 'edit event', 'delete event',
               'show incoming events',  'show all events', 'exit']
    selected = 1

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
            e.add_event(name, d, m)
            print("")

        if selected == 2:
            cm.printBlue(f"{HA}EDIT EVENT")
            cm.printCyan(f"{SA}Enter id of event that You want to edit")
            event_id = input("Id: ")
            if len(event_id) != 5:
                cm.printRed(f"{TA}There is no event with such id!")
            else:
                EDIT_ACTIONS = ['name', 'day', 'month']
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
            cm.printGreen(f'{SA}* {e["name"]}\t({e["date"]})\t[{e["id"]}]')
    else:
        cm.printRed(f"{HA}There is no events.")


if __name__ == "__main__":
    main()

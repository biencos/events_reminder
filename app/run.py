import sys

from models.events import Events


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
    print(f"{HA}INCOMING EVENTS")
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
            print(f"{HA}ADD NEW EVENT")
            print(f"{SA}Enter values of new event")
            n, d, m = input("Name: "), input("Day: "), input("Month: ")
            print("")
            e.add_event(n, d, m)
        if selected == 2:
            print(f"{HA}EDIT EVENT")
            print(f"{SA}Enter id of event that You want to edit")
            event_id = input("Id: ")
            if len(event_id) != 5:
                print(f"{TA}There is no event with such id!")
            else:
                EDIT_ACTIONS = ['name', 'day', 'month']
                print_actions(EDIT_ACTIONS, "- to edit")
                print("")
                selected_e = get_selected_option(input(":"), 1, len(ACTIONS))
                selected_attribute = EDIT_ACTIONS[selected_e - 1]
                print(f"{SA}Enter new value of {selected_attribute}")
                value = input(": ")
                print("")
                e.edit_event(event_id, selected_attribute, value)

        if selected == 3:
            print(f"{HA}DELETE EVENT")
            print(f"{SA}Enter id of event that needs to be deleted")
            event_id = input("Id: ")
            print("")
            if len(event_id) == 5:
                e.delete_event(event_id)
            else:
                print(f"{TA}There is no event with such id!")
        if selected == 4:
            print(f"{HA}INCOMING EVENTS")
            print("")
            e.get_specific_events()
            print_events(e.specific_events)
        if selected == 5:
            print(f"{HA}ALL EVENTS")
            print("")
            e.get_events()
            print_events(e.events)

    print(f"{SA}See you next time")


def print_actions(actions, prfx):
    print(f"{HA}WHAT DO YOU WANT TO DO?")
    print("")
    [print(f"{HA}{i+1} {prfx} {actions[i]}") for i in range(len(actions))]


def get_selected_option(inp, inp_limit, inp_limit1):
    try:
        inp = int(inp)
    except:
        print(f"{TA}Option must be a number between {inp_limit} and {inp_limit1}")
        sys.exit(0)

    if inp < inp_limit or inp > inp_limit1:
        print(f"{TA}Option must be a number between {inp_limit} and {inp_limit1}")
        sys.exit(0)
    return inp


def is_valid(inp, inp_limit, inp_limit1):
    try:
        inp = int(inp)
    except:
        print(f"{TA}Option must be a number between {inp_limit} and {inp_limit1}")
        sys.exit(0)

    if inp < inp_limit or inp > inp_limit1:
        print(f"{TA}Option must be a number between {inp_limit} and {inp_limit1}")
        sys.exit(0)
    return inp


def print_events(events):
    if len(events) > 0:
        for e in events:
            print(f'{SA}{e["id"]} - {e["date"]} - {e["name"]}')
    else:
        print(f"{HA}There is no events.")


if __name__ == "__main__":
    main()

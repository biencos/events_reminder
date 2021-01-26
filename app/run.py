import sys
from models.events import Events

JSON_FILE_NAME = "data/events.json"


def main():
    e = Events(JSON_FILE_NAME)
    e.get_events()
    e.get_specific_events()

    print("")
    print("INCOMING EVENTS")
    print_events(e.specific_events)

    ACTIONS = ['add event', 'edit event', 'delete event',
               'show incoming events',  'show all events', 'exit']
    selected = 1

    while 0 < selected < len(ACTIONS):
        print("")
        print_actions(ACTIONS, "-")
        print("")
        selected = get_selected_option(input(":"), 1, len(ACTIONS))

        if selected == 1:
            print("ADD NEW EVENT")
            print("Enter values of new event")
            n, d, m = input("Name: "), input("Day: "), input("Month: ")
            e.add_event(n, d, m)
        if selected == 2:
            print("EDIT EVENT")
            print("Enter id of event that You want to edit (or press 0 to exit)")
            event_id = int(input("Id: "))
            if event_id < 0 or event_id > len(e.events):
                print("There is no event with such id!")
            elif event_id == 0:
                print("")
            else:
                EDIT_ACTIONS = ['name', 'day', 'month']
                print_actions(EDIT_ACTIONS, "- to edit")
                print("")
                selected_e = get_selected_option(input(":"), 1, len(ACTIONS))
                selected_attribute = EDIT_ACTIONS[selected_e - 1]
                print(f"Enter new value of {selected_attribute}")
                value = input(": ")
                e.edit_event(event_id, selected_attribute, value)

        if selected == 3:
            print("DELETE EVENT")
            print("Enter id of event that needs to be deleted")
            event_id = int(input("Id: "))
            e.delete_event(event_id)
        if selected == 4:
            print("INCOMING EVENTS")
            e.get_specific_events()
            print_events(e.specific_events)
        if selected == 5:
            print("ALL EVENTS")
            e.get_events()
            print_events(e.events)

    print('See you next time')


def print_actions(actions, prfx):
    print("WHAT DO YOU WANT TO DO?")
    [print(f"{i+1} {prfx} {actions[i]}") for i in range(len(actions))]


def get_selected_option(inp, inp_limit, inp_limit1):
    try:
        inp = int(inp)
    except:
        print(f"Option must be a number between {inp_limit} and {inp_limit1}")
        sys.exit(0)

    if inp < inp_limit or inp > inp_limit1:
        print(f"Option must be a number between {inp_limit} and {inp_limit1}")
        sys.exit(0)
    return inp


def print_events(events):
    if len(events) > 0:
        for e in events:
            print(f'{e["id"]} - {e["date"]} - {e["name"]}')
    else:
        print("There is no events.")


if __name__ == "__main__":
    main()

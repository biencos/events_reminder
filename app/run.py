import sys
from models.events import Events


def main():
    JSON_FILE_NAME = "data/events.json"
    events = Events(JSON_FILE_NAME)

    print("")
    print("INCOMING EVENTS")
    # TODO - get all events
    # TODO - show incoming events

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
            events.add_event(n, d, m)
        if selected == 2:
            print("EDIT EVENT")
            # TODO - edit event
        if selected == 3:
            print("DELETE EVENT")
            # TODO - delete event
        if selected == 4:
            print("INCOMING EVENTS")
            # TODO - show incoming events
        if selected == 5:
            print("ALL EVENTS")
            # TODO - show all events

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


if __name__ == "__main__":
    main()

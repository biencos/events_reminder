import sys


def main():
    print("")
    print("INCOMING EVENTS")
    # TODO - show incoming events

    ACTIONS = [
        'add event', 'edit event', 'delete event', 'show incoming events',  'show all events', 'exit']
    selected = 0

    while 0 < selected < len(ACTIONS):
        print("")
        # TODO - print actions
        # TODO - get selected option
        # selected = selected option

        if selected == 1:
            print("ADD NEW EVENT")
            # TODO - add event
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


if __name__ == "__main__":
    main()

import sys


def main():
    print("")
    print("INCOMING EVENTS")
    # TODO - show incoming events

    ACTIONS = [
        'add event', 'edit event', 'delete event', 'show incoming events',  'show all events', 'exit']
    selected = 1

    while 0 < selected < len(ACTIONS):
        print("")
        print_actions(ACTIONS, "-")
        print("")
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

        # TODO - delete this lines after adding get selected option
        break

    print('See you next time')


def print_actions(actions, prfx):
    print("WHAT DO YOU WANT TO DO?")
    [print(f"{i+1} {prfx} {actions[i]}") for i in range(len(actions))]


if __name__ == "__main__":
    main()

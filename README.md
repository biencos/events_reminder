# Remi
## _Never forget about upcoming events again_
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Remi is a python console app that reminds You of upcoming annual events (e.g birthdays, anniversaries, etc.).

## Features
- Add new events and don't forget about him ever again
- Modify added events
- Delete unnecessary events
- Load multiple events from text file
- Present events in a convenient, human readable form


## Tech
Remi uses just 2 non built-in python modules:
- [Colorama] - color the text of command line interface
- [Uuid] - generate unique id for event

So everyone with installed python wouldn't have a problem with running and using Remi.

## Installation

Remi requires 2 non built-in python modules: colorama, uuid. If You miss them, then go to project folder and run following command:

```sh
python -m pip install -r requirements.txt
```

If You want to be reminded of upcoming events automatically, You need to go to your startup folder and create a script that runs run.py file inside events_reminder folder. Then every time You run your machine You will get notifications about upcoming events.

### Windows Example
In Windows You will find your startup folder, by pressing [windows] + [R] key, then typing.
```sh
shell:startup
```
In your startup folder create remi.bash file with following content:
```sh
set PATH_TO_APP=<PATH_TO_RUN.PY>  #Replace <PATH_TO_RUN.PY> with your path to run.py file

cd %PATH_TO_APP%
cls
python run.py
pause
```

## License

MIT
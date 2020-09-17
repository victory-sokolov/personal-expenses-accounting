#!/bin/bash

DEFAULT_TABS_TITLE1="Web Service"
DEFAULT_TABS_TITLE2="Recognizer Service"
DEFAULT_TABS_TITLE3="Redis Server"
DEFAULT_TABS_TITLE4="Redis queue"

PROJECT_PATH="${HOME}/Documents/personal-expenses-accounting/app/services"

DEFAULT_TABS_CMD1="cd ${PROJECT_PATH}/server && flask run"
DEFAULT_TABS_CMD2="cd ${PROJECT_PATH}/recogniser && flask run"
DEFAULT_TABS_CMD3="redis-server"
DEFAULT_TABS_CMD4="cd ${PROJECT_PATH}/recogniser && rq worker"

open_default_tabs() {
    gnome-terminal --tab --title "$DEFAULT_TABS_TITLE1" -- bash -ic "$DEFAULT_TABS_CMD1; exec bash;"
    gnome-terminal --tab --title "$DEFAULT_TABS_TITLE2" -- bash -ic "$DEFAULT_TABS_CMD2; exec bash;"
    gnome-terminal --tab --title "$DEFAULT_TABS_TITLE3" -- bash -ic "$DEFAULT_TABS_CMD3; exec bash;"
    gnome-terminal --tab --title "$DEFAULT_TABS_TITLE4" -- bash -ic "$DEFAULT_TABS_CMD4; exec bash;"
}

open_default_tabs


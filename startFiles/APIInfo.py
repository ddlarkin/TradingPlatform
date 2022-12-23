# This file contains the current API key and link, simplifies the update process between files.


def info(value):
    baseURL = "https://api.polygon.io"
    defaultKey = "cEPM8c7z28IogDJl545Y1g4GqWg_Iz0H"
    if value == 'BASE':
        return baseURL
    if value == 'KEY':
        return defaultKey

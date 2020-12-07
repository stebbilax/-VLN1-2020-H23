from enum import Enum

class Enum_Airport(Enum):
    # Airports
    reykjavik = 1
    nuuk = 2
    kulusk = 3
    tingwall = 4
    longyearbyen = 5
    torshavn = 6

class Enum_Title(Enum):
    #Titles 
    office = 1
    airport = 2

class Enum_Country(Enum):
    # Countries
    iceland = 1
    greenland = 2
    shetland = 3
    svalbard = 4
    faroe_islands = 5

def enum_to_regex(enum):
    ''' Converts an enum to a OR regex string '''

    s = '('
    for var in enum:
        s += var.name + '|'

    # Remove trailing OR
    s = s[:-1]

    s += ')'

    return s

def enum_to_instructions(enum):
    ''' Converts an enum to instructions for forms '''

    s = "Must be one of the following: "

    for var in enum:
        s += var.name + ', '

    # Remove trailing whitespace and comma
    s = s[:-2]

    s += '.'

    return s
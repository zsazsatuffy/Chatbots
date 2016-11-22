#!/usr/bin/env python

# Default bot template

import chatServer as c


# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


def setup():
    output("This is the bot template.")
    sleep(1)
    output('It does nothing more than just responding with "Ok".')

    
def response(input):
    print(input)
    output("Ok")

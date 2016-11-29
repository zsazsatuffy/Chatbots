#!/usr/bin/env python

# Default bot template

import chatServer as c
import markovify

with open("MarkovChain/pulpfiction_dialog.txt") as f:
    text = f.read()
text_model = markovify.Text(text)


# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


def setup():
    output("This is the Pulp bot")
    sleep(1)
    output('What?')


def response(input):
    # print(input)
    firstWord = input.split(" ")[0]
    maxcount = 0
    while True:
        rand = text_model.make_sentence()
        maxcount += 1
        if rand and rand.startswith(firstWord):
            output(rand)
            break
        elif maxcount > 500:
            output(rand)
            break
    # output("Ok")

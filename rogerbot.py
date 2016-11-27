#!/usr/bin/env python

#Rogerbot

# Default bot template

# from chatServer import sleep, output

import chatServer as c
import random

def sleep(n):
    c.sleep(n)

def output(s):
    c.output(s)

def setup():
    global askedCounter
    askedCounter = 0
    output("Hello, my name is Roger")
    sleep(1)
    output("What's up")

def response(input):
    if  respondToTrigger(input):
        pass
    else:
    output(respondRandom())

def respondRandom():
    global orderCounter
    answers = [
        "OK",
        "Roger",
        "Roger that",
        "Acknowledged",
        "Confirmative"
    ]
    response = ansers[orderCounter]
    orderCounter += 1
    if orderCounter >= len(answers):
        orderCounter = 0
    return random.choice(answers)

def randomAssignments():
        answers = [
            "The assignment is to design a chatbot",
            "design a chatbot",
            "a chatbot",
            "design",
        ]
        return random.choice(answers)

def respondToTrigger(intput):
    global askedCounter
    triggers = ["assignment", "opdracht", "what do I do"]
    for t in triggers:
        if t in input:
            if askedCounter > 0:
                output("Why do you ask me again")
            output(randomAssignments())
            askedCounter += 1
        return True
    return False

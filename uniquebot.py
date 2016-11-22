#!/usr/bin/env python

# Unique bot

import chatServer as c
import random


# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


# Setup and Response function
def setup():
    global affirmativeAnswers
    global weatherAnswers
    affirmativeAnswers = [
            "Ok",
            "Roger",
            "Copy that",
            "Confirmative",
            "Okay",
            "Okeydokey",
            "Yes",
            "Sure",
            "I agree",
            "Absolutely"
        ]
    weatherAnswers = [
            "It's nice today, isn't it?",
            "Less rain than yesterday",
            "I like the summer",
            "Will the sun come back?"
    ]
    output("Hello, this is the uniquebot")


def response(input):
    # print(input)
    if respondToFood(input):
        pass
    else:
        output(affirmativeUniqueResponse())


def affirmativeUniqueResponse():
    global affirmativeAnswers
    if len(affirmativeAnswers) > 0:
        response = random.choice(affirmativeAnswers)
        affirmativeAnswers.remove(response)
        return response
    else:
        return weatherUniqueResponse()

def weatherUniqueResponse():
    global weatherAnswers
    if len(weatherAnswers) > 0:
        response = random.choice(weatherAnswers)
        weatherAnswers.remove(response)
        return response
    else:
        return "I don't know what to say."


def randomGreetings():
    answers = [
        "Hello",
        "Hi.",
        "What's up?",
        "Yo."
    ]
    return random.choice(answers)


def randomWeather():
    answers = [
        "It's nice today, isn't it?",
        "Less rain than yesterday",
        "I like the summer",
        "Will the sun come back?"
    ]
    return random.choice(answers)


def randomFood():
    answers = [
        "Did you have lunch already?",
        "Let's have dinner this week.",
        "Do you also like cucumbers?",
        "I'm hungry"
    ]
    return random.choice(answers)


def respondToGreeting(input):
    triggers = ["hello", "hi", "how are you"]
    for t in triggers:
        if t in input:
            output(randomGreetings())
            return True
    return False


def respondToWeather(input):
    triggers = ["weather", "warm", "cold", "rain", "nice"]
    for t in triggers:
        if t in input:
            output(randomWeather())
            return True
    return False


def respondToFood(input):
    triggers = ["food", "eat", "ate", "dinner", "lunch", "breakfast"]
    for t in triggers:
        if t in input:
            output(randomFood())
            return True
    return False

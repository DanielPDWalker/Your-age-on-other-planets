"""The Module will open a terminal window for you to work with.
The terminal window will take in your age and a planet and,
return your age on that planet.
"""

import datetime as datetime
import sys
import time


class Planet:
    """Class for the planet objects"""

    def __init__(self, planet_name, days_percent, years_percent):
        self.name = planet_name
        self.percent_day_earth_to_planet = days_percent
        self.percent_years_earth_to_planet = years_percent

    def age_on_planet(self):
        return self.percent_day_earth_to_planet * player.age

    def print_age_on_planet(self):
        return "Your age on {} would be {} days old".format(self.name, age_on_planet())


class User:
    """Class for users details"""

    def __init__(self, age):
        self.age = age
        self.age_in_days = age * 365

    def days_on_earth(self):
        return self.age * 365

    def print_days_on_earth(self):
        return "You are {} earth days old.".format(self.age * 365)


class KeyboardDisable():

    def __init__(self):
        self.on = False
        import msvcrt

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self):
        while self.on:
            msvcrt.getwch()


Active = True
disable_typing = KeyboardDisable()
mars = Planet("Mars", 103, 188)


def type_out(text):
    disable_typing.start()
    text = text + "\n"
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    disable_typing.stop()


def check_input(saved_input):
    if saved_input.lower() == "!yes":
        return True
    if saved_input.lower() == "!no":
        return False


def menu():
    print("")
    print("##################################################")
    print("")
    type_out("Welcome.")
    type_out("Please enter your age in whole years:")
    saved_age = int(input())
    type_out("You have entered {} years old".format(saved_age))
    type_out("If this is correct please enter '!yes'. If incorrect enter '!no'.")
    saved_input = input()
    if not check_input(saved_input):
        menu()
    else:
        player = User(saved_age)
        type_out(player.print_days_on_earth())


while Active:
    menu()

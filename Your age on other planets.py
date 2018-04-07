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

    def print_age_on_planet(self, age):
        return "Your age on {} would be {} days old".format
        (self.name, str(self.percent_day_earth_to_planet * (age * 365)))


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


global age
Active = True
disable_typing = KeyboardDisable()
mars = Planet("Mars", 1.03, 1.88)


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


def check_planet_exists(saved_input):
    if saved_input.lower() == "mars":
        return mars.print_age_on_planet(age)
    else:
        raise ValueError("That planet doesnt exist.")


def print_days_on_earth(age):
        return "You are {} earth days old.".format(age * 365)


def menu():
    global age
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
        age = saved_age
        type_out(print_days_on_earth(age))


def main():
    print("")
    type_out("Please enter a planet you would like to see your age on: (Mars only)")
    saved_input = input()
    if not check_planet_exists(saved_input):
        main()
    else:
        type_out(check_planet_exists(saved_input))


while Active:
    menu()
    main()

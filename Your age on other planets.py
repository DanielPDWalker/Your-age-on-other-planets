"""The Module will open a terminal window for you to work with.
The terminal window will take in your age and then a planet and,
return your age on that planet.
"""

import sys
import time


class Planet:
    """Class for the planet objects."""

    def __init__(self, planet_name, days_percent, years_percent):
        self.name = planet_name
        self.percent_day_earth_to_planet = days_percent
        self.percent_years_earth_to_planet = years_percent

    def print_age_on_planet_in_days(self, age):
        """Returns the formatted string with the users age
        on the selected planet in days.
        """
        return "Your age on {} would be {} days old.".format(self.name,
            str(round(float((age * 365) / self.percent_day_earth_to_planet), 3)))

    def print_age_on_planet_in_years(self, age):
        """Returns the formatted string with the users age
        on the selected planet in years.
        """
        return "Your age on {} would be {} years old.".format(self.name,
            str(round(float(age / self.percent_years_earth_to_planet), 3)))


class KeyboardDisable():
    """Makes an object with which you can disable keyboard input."""

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


# Users age.
global age

# This sets the object to disable the keyboard. Used in type_out().
disable_typing = KeyboardDisable()

# Initialise all the planets.
mercury = Planet("Mercury", 175.9, 0.241)
venus = Planet("Venus", 116.8, 0.615)
mars = Planet("Mars", 1.03, 1.88)
jupiter = Planet("Jupiter", 0.414, 11.9)
saturn = Planet("Saturn", 0.444, 29.4)
uranus = Planet("Uranus", 0.718, 83.7)
neptune = Planet("Neptune", 0.671, 163.7)
pluto = Planet("Pluto", 6.39, 247.9)


def type_out(text):
    """First disables keyboard input then prints out the passed
    text's characters over time in the console/terminal window.
    """
    disable_typing.start()
    text = text + "\n"
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    disable_typing.stop()


def check_input(saved_input):
    """Checks for yes and no awnsers from the user."""
    if saved_input.lower() == "!yes":
        return True
    if saved_input.lower() == "!no":
        return False


def check_planet(saved_input):
    """Checks the users input.lower() against the planet names.
    If a planet is selected it will return the users age in days
    and years on that planet.

    Else this checks if the user wishes to restart or quit.

    If it passes the restart or quit check, it will return that
    the users input is not a planet.
    """
    if saved_input.lower() == "mercury":
        return mercury.print_age_on_planet_in_days(age), mercury.print_age_on_planet_in_years(age)
    elif saved_input.lower() == "venus":
        return venus.print_age_on_planet_in_days(age), venus.print_age_on_planet_in_years(age)
    elif saved_input.lower() == "mars":
        return mars.print_age_on_planet_in_days(age), mars.print_age_on_planet_in_years(age)
    elif saved_input.lower() == "jupiter":
        return jupiter.print_age_on_planet_in_days(age), jupiter.print_age_on_planet_in_years(age)
    elif saved_input.lower() == "saturn":
        return saturn.print_age_on_planet_in_days(age), saturn.print_age_on_planet_in_years(age)
    elif saved_input.lower() == "uranus":
        return uranus.print_age_on_planet_in_days(age), uranus.print_age_on_planet_in_years(age)
    elif saved_input.lower() == "neptune":
        return neptune.print_age_on_planet_in_days(age), neptune.print_age_on_planet_in_years(age)
    elif saved_input.lower() == "pluto":
        return pluto.print_age_on_planet_in_days(age), pluto.print_age_on_planet_in_years(age)
    else:
        if restart_or_quit(saved_input):
            return "{} is not a planet.".format(saved_input), ""


def print_days_on_earth(age):
    """Prints your age in earth days"""
    return "You are {} earth days old.".format(age * 365)


def menu():
    """Runs the menu and set up, asking for users age.

    Makes sure the age passed is an int, and handles any exceptions
    by just restarting.

    This also prints the users age in earth days before calling
    the main() function.
    """
    global age
    print("")
    print("##################################################")
    print("")
    type_out("Welcome.")
    type_out("Please enter your age in whole years:")
    try:
        saved_age = int(input())
        age = saved_age
    except:
        menu()
    type_out("You have entered {} years old".format(age))
    type_out("If this is correct please enter '!yes'. If incorrect enter '!no'.")
    saved_input = input()
    if not check_input(saved_input):
        menu()
    else:
        type_out(print_days_on_earth(age))


def main():
    """Main loop and functionality.

    Will only type the how to restart or quit line once, then loops
    through asking for planets to check user age on.

    check_planet() ended up handling checking for restart or quit.
    """
    the_loop = True
    type_out("If at any time you wish to restart of quit please enter: '!restart' or '!quit'")
    while the_loop:
        print("")
        type_out("Please enter a planet you would like to see your age on:")
        saved_input = input()
        item1, item2 = check_planet(saved_input)
        type_out(item1)
        type_out(item2)


def restart_or_quit(saved_input):
    """Check if the user has input the restart or quit command."""
    if saved_input.lower() == "!restart":
        menu()
    if saved_input.lower() == "!quit":
        exit()
    return True


# Run the actual "program". Looping/flow is handled within the functions.
menu()
main()

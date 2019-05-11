# User      Discord: Bwomp-Womp#2368
#           Git:     GraphicDesignDropout
#           Twitter: @iamtsofu

# Title:    WOP_BeginnerChallenges_01_AgeCalc

import datetime
now = datetime.datetime.now()

userName = input("What's your name? >")

def calculation(name,age):
    until100 = 100 - age
    year100 = int(now.year) + until100
    print("Hi {}, you'll be 100 in {}.".format(name,year100))
    if age > 50 and age < 65:
        print("Wow! Half way there!")
    if age > 65:
        print("Wow, you're experienced!")

def survey():
    valid = False
    while not valid:
        try:
            userAge = int(input("What's your age? >"))
            valid = True
            return userAge
        except:
            print("Error - Are you sure you typed a number?")

calculation(userName, survey())

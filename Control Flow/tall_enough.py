"""
Tall enough to ride

Write a program which asks the user how tall they are
and prints whether or not they're taller than a pre-specified minimum height.

In amusement parks, rollercoasters frequently have minimum height requirements for safety reasons.
Assume for now that the minimum height is 50 of whatever height unit you'd like.

Here's a sample run:

$ python tall_enough.py
How tall are you? 100
You're tall enough to ride!

(For an extra challenge, write code which will repeatedly ask a user how tall they are
and tell them whether or not they're tall enough to ride, until the user doesn't enter any number at all,
in which case the program stops.)
"""

MINIMUM_HEIGHT = 50 # arbitrary units

def main():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, sorry :(")

def tall_enough_extension():
    height = input("How tall are you? ")
    while height != "":
        height = float(height)
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, sorry :(")
        height = input("How tall are you? ")

# tall_enough_extension()

if __name__ == "__main__":
    main()
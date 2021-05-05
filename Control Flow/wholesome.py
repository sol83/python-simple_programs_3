"""
Wholesome machine

Write a program which prompts the user to type an affirmation of your choice until they type it correctly
(We'll use "I am capable of doing anything I put my mind to.").


Here's a sample run of the program:

$ python wholesome.py
Please type the following affirmation: I am capable of doing anything I put my mind to.
Hmmm
That was not the affirmation.
Please type the following affirmation: I am capable of doing anything I put my mind to.
I am capable of doing anything I put my mind to.
That's right! :)

Note that you can call input() with no prompt and it will still wait for a user to type something!
"""

AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)
    while input() != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
    print("That's right! :)")   

if __name__ == "__main__":
    main()
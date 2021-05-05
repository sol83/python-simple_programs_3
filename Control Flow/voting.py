"""
International voting age

Write a program which asks a user for their age
and lets them know if they can or can't vote in the following three fictional countries.

Around the world, different countries have different voting ages.
In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

The voting age in Peturksbouipo is 16
(in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

The voting age in Stanlau is 25
(in real life this is the voting age in the United Arab Emirates)

The voting age in Mayengua is 48
(in real life, as far as we can tell, this isn't the voting age anywhere)

Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

Here's a sample run of the program:

$ python voting.py
How old are you? 20
You can vote in Peturksbouipo where the voting age is 16.
You cannot vote in Stanlau where the voting age is 25.
You cannot vote in Mayengua where the voting age is 48.
"""

PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    age = int(input("How old are you? "))
    if age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    if age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    if age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")

# Simpler but lengthier solution(not recommended):

# def main():
#     age = int(input("How old are you? "))
#     if age < 16:
#         print("You cannot vote in Peturksbouipo where the voting age is 16.")
#         print("You cannot vote in Stanlau where the voting age is 25.")
#         print("You cannot vote in Mayengua where the voting age is 48.")
#     elif age >= 16 and age < 25:
#         print("You can vote in Peturksbouipo where the voting age is 16.")
#         print("You cannot vote in Stanlau where the voting age is 25.")
#         print("You cannot vote in Mayengua where the voting age is 48.")
#     elif age >= 25 and age < 48:
#         print("You can vote in Peturksbouipo where the voting age is 16.")
#         print("You can vote in Stanlau where the voting age is 25.")
#         print("You cannot vote in Mayengua where the voting age is 48.")
#     elif age >= 48:
#         print("You can vote in Peturksbouipo where the voting age is 16.")
#         print("You can vote in Stanlau where the voting age is 25.")
#         print("You can vote in Mayengua where the voting age is 48.")

if __name__ == "__main__":
    main()
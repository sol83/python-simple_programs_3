"""
Sentinel Loops

Write a program that prompts the user for numbers until the user types -1,
then output the total of the numbers. In this case, -1 is called a sentinel value.

Here is an example run of the program:

 Type a number: 10
 Type a number: 20
 Type a number: 30
 Type a number: -1
 total is 60
 """

SENTINEL = -1

def main():
    num = int(input("Type a number: "))
    total = 0
    while num != SENTINEL:
        total += num
        num = int(input("Type a number: "))
    print("total is ", total)

# Another way using the BREAK statement

# SENTINEL = -1

# def main():
#     total = 0
#     while True:
#         num = int(input("Type a number: "))
#         if num == SENTINEL:
#             break
#         total += num
#     print("total is " + str(total))

if __name__ == '__main__':
    main()
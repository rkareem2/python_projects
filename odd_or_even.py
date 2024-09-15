"""
Welcome a user then ask them for a number between 1 and 1000.

When the user gives you the number, you check if it's odd or even and then you print a message letting them know.

Example:

Prompt: What number are you thinking?
Input: 25
Output: That's an odd number! Have another?
"""

# we have to write a code that tells the user if the number is an odd or even number

print("Hello welcome to my app where you know if a number is even or odd")

num = int(input("what number are you thinking? "))
print(f"Input: {num} ")
if num % 2 == 0:
    print(f"That's an even number!")
else:
    print(f"That's an odd number!")


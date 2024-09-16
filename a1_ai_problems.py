# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# arithmetic calculator AI 1

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)

# guessing game AI 2

import random

def guessGame(): 

    guessNum = random.randint(0,10)
    operation = None

    print("Guess a number from 0-10 ")

    while guessNum != operation:
        operation = float(input("Enter guess: "))

        if operation < guessNum:
            print("Too low")
        elif operation > guessNum:
            print("Too high")
        else:
            print("Correct!")

guessGame()

# Mcdonalds serving program AI 3

mcList = ["McChicken", "McFrappe", "McNuggets", "Big Mac"]

print(mcList)

print("What meal do you want to order?")

ask = int(input("0, 1, 2, or 3? "))

print(mcList[ask])


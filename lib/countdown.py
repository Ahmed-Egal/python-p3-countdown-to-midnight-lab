# your code goes here!
import time


def countdown(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        number -= 1
    print("HAPPY NEW YEAR!")
    

def countdown_with_sleep(num):
    while num > 0:
        print(f"{num} SECOND(S)!")
        num -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")


countdown(5)
countdown_with_sleep(5)
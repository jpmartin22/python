import random

number_guessed=input("Enter your guessed digit here: ")

if number_guessed.isdigit():
    number_guessed=int(number_guessed)
    if number_guessed <=0:
        print("Enter the digit greater than 0 next time!")
        quit()
else:
    print("Enter the digit next time!")
    quit()            

random_digit=random.randint(0,number_guessed)
print(random_digit)
if number_guessed == random_digit:
    print("Matched!!!")
else:
    print("Better luck next time:( )")    
print("Welcome to the Quiz")

Playing=input("Do you want to play? ")
if Playing.lower() != "yes":
    quit()

print("Okay ! lets goo :)")
score =0

answer=input("who won 2011 ODI world cup? ")
if answer.lower() == "india":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("who is present indian cricket team captain?  ")
if answer.lower() == "rohit sharma":
    print("correct")
    score+=1
else:
    print("incorrect")

print("you got " + str(score) +" questions correct out of 2 ! ")    
print("you got " + str((score/2)*100) +" Percent! ")   
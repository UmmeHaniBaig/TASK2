print("Welcone to the game")
choice=input("Do you want to play? ")
if choice!="yes":
    quit()

print("Okay lets play")
score=0
answer=input("what does CPU stand for? ")
if answer=="central processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer=input("what does DLD stand for? ")
if answer=="digital logic design":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer=input("what does MU stand for? ")
if answer=="memory unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")

print ("your score is "+str(score))

import random
comp_score=0
user_score=0
tie=0
print("--------welcome to the game-----")
print('''
Winning Rules:
1-if rock and scissor--->rock wins
2-if rock and paper----->paper wins
3-if paper and scissor-->scissor wins''')
print('''options are:
1-rock
2-paper
3-scissor''')
user_choice=int(input("enter any number ranges from 1-3:"))
while user_choice>3 or user_choice<1:
    user_choice=int(input("enter valid number:"))
if user_choice==1:
    choice="You choose rock"
    print(choice)
elif user_choice==2:
     choice="You choose paper"
     print(choice)
     
else:
    choice="You choose scissor"
    print(choice)
print()
print("Now it's computer turn")
computer_choice=random.randint(1,3)
if computer_choice==1:
    choice="Comp choose rock"
    print(choice)
elif computer_choice==2:
     choice="Comp choose paper"
     print(choice)
else:
    choice="Comp choose scissor"
    print(choice)
result=None    
if ((computer_choice=="rock" and user_choice=="paper") or (user_choice=="rock" and computer_choice=="paper")):
    print("paper wins")
    result="paper"
    print(user_score)
elif ((computer_choice=="paper" and user_choice=="Scissor") or (user_choice=="paper"  and computer_choice=="scisor")):
    print("scissor wins")
    result="scissor"
    
elif ((computer_choice=="scissor" and user_choice=="rock")or (user_choice=="scissor"  and computer_choice=="rock")):
    print("rock wins")
    result="rock"
elif user_choice==computer_choice:
    print("it's a tie")
else:
    print("sorry")
    
if result=="tie":
    tie+=1
if result==user_choice:
    user_score+=1
else:
    comp_score+=1

print("scores are:")
print("user score is:",user_score)
print("comp score is:",comp_score)

    
    

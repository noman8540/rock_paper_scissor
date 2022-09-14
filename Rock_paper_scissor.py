import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp,you):
    # if two values are equal, declare a tie!
    if comp==you:
        return None
    
    #check all possibilities when computer chose s 
    elif comp =='r':
        if you=='p':
            return False
        elif you=='s':
            return True

    #Check for all possibilities when computer chose w
    elif comp =='p':
        if you=='s':
            return False
        elif you=='r':
            return True
    # Check for all possibilities when computer chose g
    elif comp=='s':
        if you=='r':
            return False
        elif you=='p':
            return True
print("Comp Turn:Rock(r) Paper(p) or Scissors(s)")
randNo = random.randint(1,3)
if randNo == 1:
    comp ='r'
elif randNo == 2:
    comp ='p'
elif randNo == 3:
    comp ='s'
you = input("Your Turn:Rock(s) Paper(p) or Scissors(s)? ")
a = gameWin(comp,you)

print(f"computer chose {comp}")
print(f"youchose {you}")

if a == None:
    print('the game is tie!')
elif a:
    print('you win')
else:
    print('you lose!')


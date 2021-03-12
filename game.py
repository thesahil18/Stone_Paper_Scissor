import random

def game(comp, user):
    if comp == user:
        return None

    elif comp == 'S':
        if user == 'P':
            return True        
        else:
            return False

    elif comp == 'P':
        if user == 'X':
            return True
        else:
            return False

    elif comp =='X':
        if user == 'S':
            return True
        else:
            return False

user = input("Your choice Stone(S), Paper(P), Scissor(X), Exit(E) : ")
user = user.capitalize()

if user == 'E':
    print(f'Your Choice : {user}\nYou Exited')

elif user == 'S' or user == 'P' or user == 'X':
    randNo = random.randint(1, 3)
    comp = randNo

    if comp == 1:
        comp = 'S'
    elif comp == 2:
        comp = 'P'
    elif comp == 3:
        comp = 'X'

    print(f'Computer choice : {comp}')
    print(f'Your Choice : {user}')

    a = game(comp, user)

    if a == None:
        print("Tie")
    elif a:
        print("You Win")
    else:
        print("You Loose")    

else:
    print("Invalid input")

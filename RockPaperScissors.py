import random

computer = 0
user = 0

comp = random.randint(1,3)

r = 1
s = 2
p = 3

print("Welcome to Rock, Paper, and Scissors! You will go against a computer, first to five wins, wins!")
while computer != 5 and user != 5:
    choice = input("\nPlease enter your choice 'r'ock, 'p'aper, or 's'cissors.")

    comp = random.randint(1,3)
    if comp == 1:
        comp = r
    if comp == 2:
        comp = p
    if comp == 3:
        comp = s

    if choice == "r" and comp == s:
        user += 1
        print("\nYou chose: r \nThe computer chose: s \nYou won! \nScore: \nComputer:", computer,"\nYou:", user,)
    elif choice == "s" and comp == r:
        computer += 1
        print("\nYou chose: s \nThe computer chose: r \nThe computer won! \nScore: \nComputer:", computer, "\nYou:", user,)
    elif choice == "r" and comp == r:
        print("\nYou chose: r \nThe computer chose: r \nNo one wins! \nScore: \nComputer:", computer, "\nYou:", user,)
    elif choice == "s" and comp == s:
        print("\nYou chose: s \nThe computer chose: s \nNo one wins! \nScore: \nComputer:", computer, "\nYou", user,)
    elif choice == "p" and comp == r:
        user += 1
        print("\nYou chose: p \nThe computer chose: r \nYou won! \nScore: \nComputer:", computer, "\nYou:", user, )
    elif choice == "p" and comp == s:
        computer += 1
        print("\nYou chose: p \nThe computer chose: s \nThe computer won! \nScore: \nComputer:", computer, "\nYou:", user,)
    elif choice == "r" and comp == p:
        computer += 1
        print("\nYou chose: r \nThe computer chose: p \nThe computer won! \nScore: \nComputer:", computer, "\nYou:", user,)
    elif choice == "s" and comp == p:
        user += 1
        print("\nYou chose: s \nThe computer chose: p \nYou won! \nScore: \nComputer:", computer, "\nYou:", user,)
    elif choice == "p" and comp == p:
        print("\nYou chose: s \nThe computer chose: s \nNo one wins! \nScore: \nComputer:", computer, "\nYou", user,)
    else:
        print("")

if user == 5:
    print("\nFinal score: \nYou:", user, "\nComputer:", computer, "\nYou won!")
else:
    print("\nFinal score: \nYou:", user, "\nComputer:", computer, "\nThe computer won!")
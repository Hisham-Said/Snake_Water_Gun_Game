#childhood game
import random
def game(c , r):
    if(c == r):
        print("Tie Booyah!")
    elif(((c=="snake" )and (r=="water"))):
        print("Snake Beats Water.")
        print("You Win!")
    elif(((c=="water" and r=="snake"))):
        print("Snake Beats Water.")
        print("Computer Win!")
    elif(((c=="gun") and (r=="snake"))):
        print("Gun Beats Snake.")
        print("You Win!")
    elif(((c=="snake" and r=="gun"))):
         print("Gun Beats Snake.")
         print("Computer Win!")
    elif (((c =="water")and(r == "gun"))):
        print("Water Beats Gun.")
        print("You Win!")
    elif(((c=="gun" and r=="water"))):
        print("Water Beats Gun.")
        print("Computer Win!")

choice = str(input("Enter your choice : "))
print(f"You Choose : {choice}")
choice = choice.lower()
list = ["Snake" , "Water" , "Gun"]
for i in list:
    randoms = random.choice(list)
    randoms = randoms.lower()
    print(f"Computer choose : {randoms}")
    break

if((choice =="snake") or (choice == "gun") or (choice=="water")):
 game(choice ,randoms)
else:
    print("Invalid choice.")

import random

#Name
name = input("Enter your name, adventurer: ")

#Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

#Gender
while True:
    gender = input("(M)ale or (F)emale? ")
    if gender in ("M", "m", "F", "f"):
        break # Exit the loop
    print("Please type M or F")

#Judge
if gender == "M" or gender == "m":
    title = "The Hero"
else:
    title = "The Heroine"
print()
print(f"Your new title is: {title}")
print()

#Stat boxes
hp = 50
attack = 5
gold = 0

#Hero sheet
print(f"{name}, {title}")
print(f"HP: {hp} | Attack: {attack} | Gold: {gold}")
print()

#Lucky Coin
print("Item: Lucky Coin (one reroll, use it wisely)")
print()
input("Press Enter to descend into the tomb...")
print()

#Skeleton boxes
skeleton_hp = 15
skeleton_attack = 3

#room 1: The Gate Hall&Scirpt
continue_text = f"{BLUE}Click enter to continue...{RESET}" #Variable for  contiuning

print(f"{GREEN}ROOM 1: THE GATE HALL{RESET}")
print()
print(f"{GREEN}You step into the Gate Hall. Torchlight flickers off cracked stone pillars, and somewhere far below, something is breathing.{RESET}")
print(f"{YELLOW}The door slams shut behind you. The tomb knows you're here now.{RESET}")
print()
input(continue_text)
print()
print(f"{RED}A skeleton steps out of the shadows, cracks his knuckles, and bows.{RESET}")
print(f'{RED}"Nothing personal," he rasps. "I just really need this job."{RESET}')
print()
input(continue_text)
print()
print(f"{RED}GUARD ON DUTY: Skeleton | HP:{RESET}{skeleton_hp} {RED}| Attack:{RESET}{skeleton_attack}") #SkeletonHud
print()

#(F)ight or (R)un
while True:
    fight_run = input(f"{RED}(F){RESET}ight or {GREEN}(R){RESET}un? ")
    if fight_run in ("F", "f", "R", "r"):
        break # Exit the loop
    print("Please type 'F', 'f', 'R', or 'r'")
    print()

if fight_run in ("F", "f"):
    print()
    print(f"{GREEN}You swing at the Skeleton!{RESET}")
    damage = random.randint(5, 10)
    skeleton_hp = skeleton_hp - damage
    print(f"{GREEN} You hit for {damage}{RESET}" )
elif fight_run in ("R", "r"):
    print()
    print(f"{YELLOW}You try to run...{RESET}")

#Hurt the skeleton
print(f"{RED}The Skeleton staggers! His HP is now {skeleton_hp}{RESET}")

#Skeleton attack
skel_damage = random.randint(1, skeleton_attack)

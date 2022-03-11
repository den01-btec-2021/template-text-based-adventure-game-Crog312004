def main():
  print('Welcome to my game!')
  player_name=input("what is your name? ")
  print("Hi "+ player_name)

  lives=3
  print(f"you have {lives} lives remaining")

  backpack = []
  
  while True:
   direction = input("which direction do you want to go? Please choose north, south, east or west. ")
  
   if direction == "north":
    print("you went north")
    print("you enter the first room")
    puzzle_guess_north = input("What shape has no pointy ends: triangle, square or circle. ")
    if puzzle_guess_north == "circle":
        print("Correct")
        prize = "Spellbook 1"
        print (f"You have acquired {prize}")
        backpack.append(prize)
        
        content_show= input("Do you want to see the contents? ")
        if content_show == "yes":
            for prize in backpack:
                print(f"Your backpack contains {prize}")
        else:
            print("You chose to not open your backpack")
    else:
       print("Incorrect")
       lives -= 1

    

   elif direction == "south":
     print("you went south")
   elif direction == "east":
     print("you went east")
   elif direction == "west":
     print("you went west")
   else:
     print("sorry, not recognised")

   
   if ("Spellbook 1" in backpack) and ("Spellbook 2" in backpack ) and ("Spellbook 3" in backpack) and ("Spellbook 4" in backpack):
     print("Door open! Win game!")

   if lives == 0:
     print("your dead...?")
     print("How can you die this early, your adventure had only just begun...")
     exit()
main()

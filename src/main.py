import time
def main():
  print('Welcome to my game!')
  print("All your answers will need to start with a capital, enjoy!")
  player_name=input("what is your name? ")
  print("Hi "+ player_name)

  lives=3
  print(f"you have {lives} lives remaining")

  backpack = []
  
  while True:
   direction = input("which direction do you want to go? Please choose North, South, East or West. ")
  
   if direction == "North":
       puzzle="What shape has no pointy ends: Triangle, Square or Circle. "
       puzzle_solution= "Circle"
       in_room(puzzle,puzzle_solution)
    

   elif direction == "South":
     print("you went South")
     print("you enter the second room")
     puzzle_guess_south = input("The more of this there is, the less you see. What is it?")
     if puzzle_guess_south == "Darkness":
         print("Correct")
         prize = "Spellbook 1"
         print (f"You have aqquired {prize}")
         backpack.append(prize)

         
   elif direction == "East":
     print("you went East")
   elif direction == "West":
     print("you went West")
   else:
     print("sorry, not recognised")

   
   if ("Spellbook 1" in backpack) and ("Spellbook 2" in backpack ) and ("Spellbook 3" in backpack) and ("Spellbook 4" in backpack):
     print("Door open! Win game!")
     exit()

   if lives == 0:
     print("Your dead...?")
     print("How can you die this early, your adventure had only just begun...")
     exit()

def in_room(puzzle,puzzle_solution):
    print("you went direction")
    time_elapsed = time.time()
    
    print("you enter the first room")
    puzzle_guess_north = input(puzzle)
    if puzzle_guess_north == puzzle_solution:
        print("Correct")
        prize = "Spellbook 1"
        print (f"You have acquired {prize}")
        backpack.append(prize)
        
        content_show= input("Do you want to see the contents? ")
        if content_show == "Yes":
            for prize in backpack:
                print(f"Your backpack contains {prize}")
        else:
            print("You chose to not open your backpack")
    else:
       print("Incorrect")
       lives -= 1
main()

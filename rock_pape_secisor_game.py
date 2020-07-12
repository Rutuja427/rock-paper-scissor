from random import randint
gaming_input = ['r', 'p', 's']
two_user=False
while two_user==False:
     computer = gaming_input[randint(0,2)]
     print("computer :",computer)
     two_user = input("player \t: ").casefold()
     if (computer and two_user) in gaming_input:
     
      if (computer == 'r') and (two_user == 'r'):
          print("Match Draw")

      elif (computer == 'r') and (two_user == 'p'):
          print("player won the game")
      elif (computer == 'r') and (two_user == 's'):
         print("computer won the game")
      elif ( computer== 'p') and (two_user == 'r'):
         print("computer won the game")
      elif (computer == 'p') and (two_user == 'p'):
         print("Match Draw")
      elif (computer == 'p') and (two_user == 's'):
          print("player won the game")
      elif (computer == 's') and (two_user == 'r'):
          print("player won the game")
      elif (computer == 's') and (two_user == 'p'):
          print("computer won the game")
      elif (computer == 's') and (two_user == 's'):
          print("Match Draw")
     else:  
        print("Please provide valid inputs!!!")
     two_user=False
     computer=gaming_input[randint(0,2)]
    
     continue_input = input("Want to try again? (y/n): ").casefold()
     print("\n")
    
     if (continue_input == 'y') or (continue_input == 'yes'):
          continue
     else:
        print("See you again. Bye")
        break
    

     
 
    
 
   
 
    
 
    
 
    
 
   

    
 
    
 
    
 
    
 
 
 
 


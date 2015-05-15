import random
import player
import hashlib
#import :P


#def startgame():
  

def new_player():
  name = input("First, who are you?\n>>")
  print ("Now, please select a class:")
  print ("\t[R]anger")
  print ("\t[W]arrior")
  print ("\t[M]age")
  print ("\t[O]Rouge")
  print ("\t[P]aladin")
  print ("\t[B]arbarian")
  print ("\t[C]leric")
  print ("\t[D]ruid")
  print ("\t[C]leric")
  print ("\t[H]ealer")
  print ("\t[K]Dark mage")
  theclass = input("Please type the letter of the class:\n>>")
  if theclass == "R":
      theplayer = Player(name, 200, 150, 100, 50, 100, 50) #ranger attributes
  elif theclass == "W":
      theplayer = Player(name, 250, 190, 70, 20, 125, 75)
  elif theclass == "M":
      theplayer = Player(name, 200, 225, 250, 200, 100, 75)
  elif theclass == "O":
      theplayer = Player(name, 200, 225, 250, 200, 100, 75)
  
 

def login():
  username = input("Username: ")
  password = input("password: ")
  #if username == player_username:
  #if password == player_password:
    #startgame()
    
def register():
  player_username = input("Enter a username: ")
  player_password = input("Enter a password: ")
  
      
  
startgame = input("If you are a new player type new player \nif you are an existing player type login\n ")

if startgame.lower() == "new player":
    new_player();
if startgame.lower() == "login":
    login(); 
  
  
  


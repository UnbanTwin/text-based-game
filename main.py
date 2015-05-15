import random
import player
import hashlib
#import :P




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
  theclass = input("Please type the letter of the class:\n>>")
  switch theclass:
    case "R":
	theplayer = Player(name, 200, 150, 100, 50, 100, 50) #ranger attributes
    case "W":
    	theplayer = Player(name, 250, 190, 70, 20, 125, 75)
    case "M":
    	theplayer = Player(name, 250, 190, 70, 20, 100, 75)
def login():
  username = input("Username: ")
  password = input("password: ")
def register():
  player_username = input("Enter a username: ")
  player_password = hashlib.()input("Enter a password: ")
  
      
  
startgame = input("If you are a new player type new player \nif you are an existing player type login\n ")

if startgame.lower() == "new player":
    new_player();
if startgame.lower() == "login":
    login(); 
  
  
  


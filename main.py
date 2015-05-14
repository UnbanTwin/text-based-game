import random
import player
#import :)




def new_player():
  print ("First of all, please select a class:")
  print ("\t[R]anger")
  print ("\t[W]arrior")
  print ("\t[M]age")
  print ("\t[O]Rouge")
  print ("\t[P]aladin")
  print ("\t[B]arbarian")
  print ("\t[C]leric")
  print ("\t[D]ruid")
  print ("\t[C]leric")
  theclass = input("Please type the letter of the class")
  switch theclass:
    case "R":
def login():
  username = input("Username: ")
  password = input("password: ")
def register():
  player_username = input("enter a username: ")
  player_password = input("enter a password: ")
  
      
  
startgame = input("If you are a new player type new player \nif you are an existing player type login\n ")

if startgame.lower() == "new player":
    new_player();
if startgame.lower() == "login":
    login(); 
  
  
  


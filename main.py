import random
import player
#import :)




def new_player():
  print ("Welcome to title here")
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
  
startgame = input("If you are a new player type new player \nif you are an existing player type login\n ")

if startgame == "new player":
    new_player();


elif startgame == "login":
    #logstuff
    print("this is where login stuff will happen, yay")
  
else:
    print("unknown command")



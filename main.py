import random
import player
#import hashlib
#import xD
import random

class Player(object):
  def __init__(self, name, race, maxhp, minhp, maxmana, minmana, maxskill, minskill):
    self.hp = random.randint(minhp, maxhp)
    self.mana = random.randint(minman, maxman)
    self.skill = random.randint(minskill, maxskill)
    self.name = name
    self.race = race
    self.gold = 200 + random.randint(50, 200)
    self.inventory = []
    
  def check_dead(self):
    if self.hp < 0:
      print ("You Died...")
      self.inventory = []
      self.gold = 0
      return 0
    else:
      return self.hp

#def startgame():
  #comment
  

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
  print ("\t[H]ealer")
  print ("\t[K]Dark mage")
  theclass = input("Please type the letter of the class:\n>>")
  if theclass == "R":
      theplayer = Player(name, 200, 150, 100, 50, 100, 50) #ranger attributes
  elif theclass == "W":
      theplayer = Player(name, 250, 190, 70, 20, 125, 75)
  elif theclass == "M":
      theplayer = Player(name, 225, 200, 350, 200, 100, 75)
  elif theclass == "O":
      theplayer = Player(name, 325, 300, 10, 0, 150, 100)
  elif theclass == "P":
      theplayer = Player(name, 225, 100, 50, 100, 150, 100)
  elif theclass == "B":
      theplayer = Player(name, 400, 250, 1, 0, 100, 50)
  elif theclass == "C":
      theplayer = Player(name, 200, 190, 50, 100, 200, 190)
  elif theclass == "D":
      theplayer = Player(name, 125, 100, 450, 400, 125, 100)
  elif theclass == "H":
      theplayer = Player(name, 325, 300, 250, 200, 150, 100)
  elif theclass == "K":
      theplayer = Player(name, 125, 100, 500, 450, 150, 100)
  
 

def login():
  username = input("Username: ")
  password = input("password: ")
  #if username == player_username:
  #if password == player_password:
    #startgame()
    
def register():
  player_username = input("Enter a username: ")
  player_password = input("Enter a password: ")
  
      
  
startgame = input("If you are a new player type new \nif you are an existing player type login\n ")

if startgame.lower() == "new":
    new_player();
if startgame.lower() == "login":
    login(); 
  
  
  


import random
import player
#import hashlib
#import :P
import random
import time

gamename = "foobarbaz"

class Player(object):
    def __init__(self, name, maxhp, minhp, maxmana, minmana, maxskill, minskill):
      self.hp = random.randint(minhp, maxhp)
      self.mana = random.randint(minmana, maxmana)
      self.skill = random.randint(minskill, maxskill)
      self.name = name
      #self.race = race
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
    
def prompt(x):
    print(x.name + ":" + str(x.hp) + " HP")


  

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
  if theclass.upper() == "R":
      theplayer = Player(name, 200, 150, 100, 50, 100, 50) #ranger attributes
      aclass = "Ranger"
  elif theclass.upper() == "W":
      theplayer = Player(name, 250, 190, 70, 20, 125, 75)
      aclass = "Warrior"
  elif theclass.upper() == "M":
      theplayer = Player(name, 225, 200, 350, 200, 100, 75)
      aclass = "Mage"
  elif theclass.upper() == "O":
      theplayer = Player(name, 325, 300, 10, 0, 150, 100)
      aclass = "Rouge"
  elif theclass.upper() == "P":
      theplayer = Player(name, 225, 100, 50, 100, 150, 100)
      aclass = "Paladin"
  elif theclass.upper() == "B":
      theplayer = Player(name, 400, 250, 1, 0, 100, 50)
      aclass = "Barbarian"
  elif theclass.upper() == "C":
      theplayer = Player(name, 200, 190, 100, 50, 200, 190)
      aclass = "Cleric"
  elif theclass.upper() == "D":
      theplayer = Player(name, 125, 100, 450, 400, 125, 100)
      aclass = "Druid"
  elif theclass.upper() == "H":
      theplayer = Player(name, 325, 300, 250, 200, 150, 100)
      aclass = "Healer"
  elif theclass.upper() == "K":
      theplayer = Player(name, 125, 100, 500, 450, 150, 100)
      aclass = "Dark Mage"
  else:
      print("Please select a letter of a class")
      new_player()
      return

  def _startgame():
      print("Welcome to " + gamename + " " + name)
      print("To Exit, type exit\nYou can type anywhere you see")
      prompt(theplayer)
      
      return
      
  print("You have selected a " + aclass + " called "+ name + ".")
  sure = input("Are you sure?[Y/N]")
  if sure.upper() == "N" or sure.upper() == "NO":
    new_player()
    return
  print("No going back now!")
  print("Your charicter has " + str(theplayer.hp) + " health, " + str(theplayer.mana) + " mana, and " + str(theplayer.skill) + " skill.")

  file = open("user.txt", "w")
  file.write(name + "\n")
  file.close()
  userfile = open("users/" + name + ".txt", "w")
  userfile.close()
  _startgame()
def login():
  username = input("Username: ")
  if username in open('user.txt').read():
      print ("Existing Profile Loaded")
  else:
      print("You are not known to the world of " + gamename)
      print("Creating new account:")
      new_player()
  return
    
startgame = input("If you are a new player type new \nif you are an existing player type login\n ")



if startgame.lower() == "new":
    new_player()
    
if startgame.lower() == "login":
    login() 
  
def prompt(x):
  print(x.name + ":" + str(x.hp) + " HP")
  


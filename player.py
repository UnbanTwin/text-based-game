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
    

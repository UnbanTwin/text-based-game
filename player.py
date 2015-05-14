import random

class player(object):
  def __init__(self, name, race, maxhp, minhp, maxmana, minmana, maxskill, minskill):
    self.hp = random.randint(minhp, maxhp)
    self.mana = random.randint(minman, maxman)
    self.skill = random.randint(minskill, maxskill)
    self.name = name
    self.race = race

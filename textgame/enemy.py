import items
import random

#Basic enemy class
#not yet implemented
class Enemy(object):

    def attack(self):
        print(f"The {self.name} attacks you!")

class Goblin(Enemy):

    def __init__(self):
        self.weapon = items.Sword()
        self.health = 20
        self.name = goblin

class Ork(Enemy):

    def __init__(self):
        self.weapon = items.Dagger()
        self.health = 30
        self.name = ork

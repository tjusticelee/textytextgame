class Character(object):
    #characters have an empty dictionary to store item they obtain along the way.
     inventory = {}

     def __init__(self):
         self.health = 100
         self.coins = 10

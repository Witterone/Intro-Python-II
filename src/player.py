# Write a class to hold player information, e.g. what room they are in
# currently.

class player:
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = []
    
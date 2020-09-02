from room import Room
from player import player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = player("Bob",'outside')
# Write a loop that:
direction = None
cur_room = None
while direction != "q":
    if cur_room== new_player.location:
        cur_room = cur_room
    else:
        cur_room=room[new_player.location]
    print(f"{new_player.name} is in the {cur_room.name}.")
    
    print(f"{new_player.name} looks...\n {cur_room.description}")

    direction = input("""Enter a direction to travel
                  (n)orth
                  (s)outh
                  (e)ast
                  (w)est
                  (q)uit
                  : """)
    
    
    if direction not in ["n","s","e","w","q"]:
        print("Not a direction or option...\n")
    else:
        if direction=="n":
            cur_room = cur_room.n_to
        elif direction=="s":
            cur_room = cur_room.s_to
        elif direction=="w":
            cur_room = cur_room.w_to
        elif direction=="e":
            cur_room = cur_room.e_to
        else:
            quit()
        
        if cur_room== None:
            print("There's nothing {new_player.name} get to that way...\n")
            
        else:
            print(f"{new_player.name}is moving to the {cur_room.name}\n\n")    
        
            new_player.location = cur_room
        
            
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

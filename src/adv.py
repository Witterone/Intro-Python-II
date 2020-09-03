from room import Room
from player import player
from item import Item
# Declare all the rooms

item = {'rope': Item("rope", """50 feet of strong supple rope used by 
                     climbers, I wonder who forgot this?""",'5'),
                     
        'silver cup': Item("silver cup", """This old cup has seen
                           better days but with a little care it could be 
                           worth something""",'30'),
        'fine shoes': Item("fine shoes", """High quality shoes that very few 
                      afford. Who left these on a cliff, and why?""",'100'),
        'coins': Item("coins","""Old gold coins from a distant land
                      possibly from a treasure hoard.""","15"),
                      
        'dusty note': Item("dusty note", """The note reads (Whoever
                           finds this I hope you will have more luck in the 
                           future. The dragon's greed knows no end and the 
                           king is a coward who only wants to keep the status
                           quo. I doubt even this treasure will be enough to
                           satisfy the beast.) 
                           """,0),
        'bills': Item("bills", """These bills are all past due and 
                      have your name on them, how unlucky.""",-10)
        
        
        }





room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons. 
                     To the south the town is quiet.
                     The sound of distant thunder rumbles,
                   you should get inside. """,item['rope']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. Assorted junk litters the floor.""",
item['silver cup']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no visible way across the chasm.""",
item['fine shoes']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of dust permeates the air.""",item['coins']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['dusty note']),

    'town': Room("Your Town", """You are back in town, everyone is sleeping 
                 dreaming of a miracle to save everyone from povery.""",
                 item['bills']),
    'dragon': Room("The Dragon's Hoard", """You are standing in the great 
                   hall of the Dragon Bezos. He eyes you cautiously sitting 
                   atop a pile of wealth beyond comprehension.""",None)
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].s_to = room['town']
room['town'].n_to = room['outside']
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
player_name = input("Please enter your player's name.")
new_player = player(player_name,room['outside'],[])
# Write a loop that:
direction = None
cur_room = None
print("""\nYour town has been taxed to the brink,
      there are no means to save it, and no one has any money.
      You have been told of an old cave that 
      once held a pirate's treasure north of town.
      No one will venture out of town because of the pack 
      of bandits and tax collecters that wait in the forests.
      You must find a way to save the town!
      """)
input("Press any key to begin")
while direction != "q":
    if cur_room== new_player.location:
        cur_room = cur_room
    else:
        cur_room=new_player.location
    
    
    print(f"{new_player.name} is in the {cur_room.name}.")
    
    print(f"{new_player.name} looks...\n {cur_room.description}")
    if cur_room == room['town']:
        command =input("""do you want to finish the game?
              (y)es
              (n)o""")
        if command =="y":
            
            score = 0
            for i in new_player.inventory:
                score += i.value
            print(f"""{new_player.name} retires from adventuring
                  with a total profit of {score}.""")
            if score==0:
                print("""You returned as you started, with nothing. The
                      town has little hope for survival and you with it.""")
                print("You lose--- Ending(Not Even Trying)")
                input("press any key to finish the game")
                quit()
                direction = "q"
            elif score>0 and score<40:
                print("""You found some items of value but it will do little
                      to stop the eventual decline of the town. You have a 
                      chance at least.\n\n""")
                print("Game Over--- Ending(Just Trying to Make Due")
                input("press any key to finish the game")
                quit()
                direction = "q"
            elif score>=40 and score<=200:
                print("""You Have found treasure indeed. The town will survive
                      but who knows for how long. Your contribution will 
                      surely make you remembered.""")
                print("Game Over--- Ending(Hero of the Day)")
                input("press any key to finish the game")
                quit()
                direction = "q"
            else:
                print("weird ending bro")
                input("press any key to finish the game")
                quit()
                direction = "q"
        else:
            print("You are just stopping in.")
    if cur_room==room['dragon']:
        input("press any key to talk to Bezos")
        print(f"""The dragon Bezos asks {new_player.name} 'Why have you come?
              I am only seeking to add more wealth and I will destroy all who 
              seek to take it. Speak the truth or I will know you are a liar.''
              \n""")
        input("press any key to explain yourself\n")
              
        print(""" You explain the reason for your adventure and the state of the 
              town you are from.\n Bezos answers 'This is a tragedy but none
              of my concern. You should return and think of ways to generate 
              more wealth so I can claim it.'\n""")
        input("press any key to explain the flaw in his plan.\n")
        print("""You explain that unless the 
              people have access to money he will recieve no more from them as
              the bankrupt dead cannot pay for anything. \n The dragon pauses
              and considers what you say.\n...""")
        print("\n...\n\n\n")
        input()
        print("""'I see the problem.
              I will share a small portion of my wealth with your town so they
              may continue to produce in the future. I will call this an 
              investment so I feel better about it. Now GO distribute the 
              wealth so it may return back to me ten fold!'\n\n You return to 
              town with as much treasure as you could carry. The town is saved
              and with this much money they are able to expand and grow into a
              large city. You are elected mayor and lead the city to properity
              with occasional friendly visits from Bezos to check on his 
              'investment'.\n
              """)
        print("Congratulations--- Ending(Hidden Dragon Victory)")
        input("press any key to finish the game")
        direction = "q"
        quit()
        
    
    direction = input("""Enter a command or direction to travel
                  (n)orth
                  (s)outh
                  (e)ast
                  (w)est
                  (q)uit
                  (a)ction
                  : """)
    
    
    if direction not in ["n","s","e","w","q","a"]:
        print("Not a direction or option...\n")
    else:
        if direction=="a":
            action = input("""Enter an action to perform
                           (s)earch
                           (i)nventory
                           (b)ack
                           """)
            if action=="s":
                if cur_room.l_count==0:
                    itm = cur_room.item
                    print(f"{new_player.name} finds a {itm.name}")
                    cmmd = input(f"""do you want {itm.name}?
                                 (y)es
                                 (n)o""")
                    if cmmd=="y":
                        new_player.inventory.append(cur_room.item)
                        print(f"{itm.name} added to inventory.")
                        cur_room.l_count=1
                    else:
                        print("You leave it where it is")
                elif cur_room.item in new_player.inventory:
                    print(f"{new_player.name} can find nothing.\n")
                    
                else:
                    print(f"{new_player.name} can find nothing.")
                    
            elif action=="i":
                print([i.name for i in new_player.inventory])
                answ = input("""Do you want to drop something?
                             (y)es
                             (n)o""")
                if answ =="y":
                    d_item= input("""what do you want to drop?""")
                    new_player.inventory.remove(item[d_item])
                    print(f"{d_item} removed.")
                else:
                    exmn=input("""Do you want to look at something?
                          (y)es
                          (n)o
                          """)
                    if exmn =="y":
                        i_exmn=input("What do you want to look at?")
                        print(i_exmn.description)
                    print(f"Back to {cur_room.name}.")
            elif action=="b" and cur_room.l_count==0:
                print(f"You go back to the {cur_room.name}.")
            else:
                print("That's not a known action")
            cur_room = new_player.location        
            
        elif direction=="n":
            if (cur_room==room['overlook'] and 
            item['rope'] in new_player.inventory):
                cur_room = room['dragon']
            else:    
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
        elif cur_room == new_player.location:
            print("Consider what to do next.")
            
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

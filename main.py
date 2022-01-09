# START IMPORTS
import enemy as e  
import player as p
import items as i
import maps as m
import awardcheck 
import time
# END IMPORTS

#Display victory signs
def victory():
    print("Great warrior! You did an amazing job!")
    time.sleep(1)
    print(" ___      ___ ___  ________  ________  _________  ________     ___     ___   ")
    time.sleep(0.7)
    print("|\  \    /  /|\  \|\   ____\|\   __  \|\___   ___\\   __  \    |\  \   /  /| ")
    time.sleep(0.7)
    print("\ \  \  /  / | \  \ \  \___|\ \  \|\  \|___ \  \_\ \  \|\  \   \ \  \/  / /  ")
    time.sleep(0.7)
    print(" \ \  \/  / / \ \  \ \  \    \ \  \\\\\  \   \ \  \ \ \   _  _\   \ \    / / ")
    time.sleep(0.7)
    print("  \ \    / /   \ \  \ \  \____\ \  \\\\\  \   \ \  \ \ \  \\  \|    \/  /  / ")
    time.sleep(0.7)
    print("   \ \__/ /     \ \__\ \_______\ \_______\   \ \__\ \ \__\\ __\ __/  /  /    ")
    time.sleep(0.7)
    print("    \|__|/       \|__|\|_______|\|_______|    \|__|  \|__|\|__|\___/  /      ")
    time.sleep(0.7)
    print("                                                               \|___|/     \n")
    
    
# START INTRO/ PLAYER INSTANTTION    
print("HEY THIS IS A PLACEHOLDER WELCOME MESSAGE!")
print('''
1. Knight
2. Wizard
''')

p.character_create()

print()
print(p.player)

print()
print("""[this is placeholder text]
You find yourself in a dark room.
Enter 'help' to find out what other commands you can use.\n""")
# END INTRO/ PLAYER INSTANTTION

# Start other pre-gameloop code
commands = {'help':p.player.help,
            'quit':p.player.quit,
            'stats':p.player.stats,
            'inv':p.inventory}

movement_commands = {'look':m.look,
                     'left':m.move_left,
                     'l':m.move_left,
                     'right':m.move_right,
                     'r':m.move_right,
                     'up':m.move_up,
                     'u':m.move_up,
                     'down':m.move_down,
                     'd':m.move_down}

## 'look' does not need to be here because it is called individually in the game loop
# End pre-gameloop code

# GAME SET
m.parse_world()
start_position = m.find_start()
p.player.create_position(start_position[0],start_position[1])
print(p.player.position())

error_command=0
# GAME RUNTIME
while p.player.game_playing and p.player.isalive():

    current_tile = m.world_map[p.player.x][p.player.y]
    if m.tile_check(current_tile) == False or p.player.game_playing == False or p.player.isalive() == False:
        break
            
    player_input = input('\n>> ')
    
    if player_input.lower() in movement_commands.keys():
        movement_commands[player_input.lower()](p.player)
        error_command=0
    elif player_input.lower() in commands.keys():
        commands[player_input.lower()]()
        error_command=0
    else:
        if error_command > 10:
            print("Introducing to the quitters' club.")
            time.sleep(1)
            p.player.quit()
        elif error_command > 8:
            print("Are you wanting to quit?")
        elif error_command > 5:
            print("I don't think that help can save you.")
        elif error_command > 2:
            print("You should try the command 'help'")
        else:
            print("Invalid command")
        error_command +=1

time.sleep(2)

# GIVE RESPONSE based on player stats
if p.player.game_playing == False:
    print("\nGotta agree with you. I think the game is quite boring, too.")
    time.sleep(1)
    print("You quitted the game.")
else:
    if p.player.isalive() == True:
        awardcheck.award_check()
        victory()
    else:
        print('''
 _                      
| |                _    
| |      ___   ___| |_  
| |     / _ \ /___)  _) 
| |____| |_| |___ | |__ 
|_______)___/(___/ \___)
                        ''')
        time.sleep(1)
        print("Maybe try harder next time.")
        
time.sleep(1)
print("The GAME END")
# END ALL

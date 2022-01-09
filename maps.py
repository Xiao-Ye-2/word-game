from random import randint
import time
import items as i
import enemy as e
import player as p
import actions

#TWO variables that helps with the awardcheck module
boss_encounter = 0
key_usage = 0


#The general map layout
world_map_layout = [
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', 'MT','IT','MT', 'ET', 'ET', 'MT', '  '],
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', 'MT','  ','  ', 'MT', '  ', 'MT', '  '],
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', 'IT', 'MT', 'MT', 'MT','MT','  ', '  ', '  ', '  ', 'IT','  ','MT', 'ET', '  ', 'MT', '  '],
['  ', '  ', '  ', '  ', 'ET','MT','MT', 'ET', 'MT', '  ', '  ','  ','  ', 'MT', '  ', '  ', '  ','MT','  ', '  ', '  ', '  ', '  ','  ','MT', '  ', '  ', 'ET', '  '],
['  ', '  ', '  ', '  ', 'MT','  ','  ', '  ', 'MT', '  ', '  ','  ','  ', 'MT', '  ', '  ', '  ','ET','  ', '  ', '  ', '  ', '  ','  ','IT', 'MT', '  ', 'MT', '  '],
['  ', 'ST', 'MT', 'MT', 'IT','  ','  ', '  ', 'PT', 'MT', 'PT','BT','MT', 'ET', '  ', '  ', '  ','PT','MT', 'IT', '  ', '  ', '  ','  ','  ', 'MT', '  ', 'IT', '  '],
['  ', '  ', '  ', '  ', 'MT','  ','  ', '  ', 'MT', '  ', '  ','  ','  ', '  ', '  ', 'MT', 'ET','MT','  ', 'MT', '  ', '  ', '  ','  ','MT', 'IT', '  ', 'MT', '  '],
['  ', '  ', '  ', '  ', 'MT','SI','MT', 'MT', 'MT', '  ', '  ','  ','  ', '  ', '  ', 'SI', '  ','  ','MT', 'IT', '  ', '  ', 'MT','PT','MT', '  ', '  ', 'MT', '  '],
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', 'MT', 'MT','MT','MT', 'BT', 'MT', 'PT', 'MT','  ','MT', 'SI', '  ', 'ET', '  '],
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', 'MT', '  ', 'MT', '  '],
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','IT', 'MT', '  ', 'MT', '  ','  ','  ', '  '],
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','MT', '  ', '  ', 'MT', '  ','  ','FT', '  '],
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','MT', 'IT', 'MT', 'IT', 'MT','MT','BT', '  '],
['  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ', '  ', '  ', '  ','  ','  ', '  ']]

  
#first plot: x=6,y=8
#second plot: x=6,y=10


#Different map tile class, including descrition
class MapTile():
    def __init__(self, x, y, desc):
        self.x = x
        self.y = y
        self.desc = desc
    def __str__(self):
        return f"You are located at X = {self.y}, Y = {self.x} ({self.desc})."
    def intro_text(self):
      raise NotImplementedError()
    def modity_player(self, player):
      raise NotImplementedError()
    
class EmptyTile(MapTile):
    def __init__(self, x, y, desc="Empty tile"):
        super().__init__(x,y, desc)
        
class PlotTile(MapTile):
    def __init__(self, x, y, desc="Plot tile", plot="None"):
        super().__init__(x,y, desc)
        self.plot = plot
        
class EnemyTile(MapTile):
    def __init__(self, x, y, desc="Enemy tile", has_enemy=True):
        super().__init__(x,y, desc)
        self.has_enemy = has_enemy

class BossTile(MapTile):
    def __init__(self, x, y, desc="Boss tile", has_boss=True):
        super().__init__(x,y, desc)
        self.has_boss = has_boss
        
class ItemTile(MapTile):
    def __init__(self, x, y, desc="Item tile", has_item=True):
        super().__init__(x,y, desc)
        self.has_item = has_item

class StartTile(MapTile):
    def __init__(self, x, y, desc="Start tile"):
        super().__init__(x,y, desc)

class FinishTile(MapTile):
    def __init__(self, x, y, desc="End tile"):
        super().__init__(x,y, desc)

class ForbiddenTile(MapTile):
    def __init__(self,x,y, desc="Forbidden tile"):
        super().__init__(x,y,desc)
        
class SpecialItem(MapTile):
    def __init__(self,x,y,desc="Special Item tile",specialitem =True):
        super().__init__(x,y,desc)
        self.specialitem = specialitem



#An explaination that showing what the letters on the layout means
tile_type_dict = {"ST": StartTile,
                  "ET": EnemyTile,
                  "BT": BossTile,
                  "IT": ItemTile,
                  "MT": EmptyTile,
                  "PT": PlotTile,
                  "FT": FinishTile,
                  "SI": SpecialItem,
                  "  ": ForbiddenTile}

#An empty list to hold all the created tile objects (will be create in the parse_world function)
world_map = [[],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             []]


#This function turns map layout into a two-dimentional list with tile objects
def parse_world():
    for x in range(len(world_map_layout)):
        for y in range(len(world_map_layout[x])):
            if(world_map_layout[x][y] in tile_type_dict.keys()):
                tile_type = tile_type_dict[world_map_layout[x][y]]
                world_map[x].append(tile_type(x,y))


#The function sets player's initial coordinate                
def find_start():
  for x in range(len(world_map)):
        for y in range(len(world_map[x])):
            if world_map[x][y].desc == 'Start tile':
                return [x,y]


#The function that check where the player can go  
def look(player):
    movable_directions = {'left':'l','right':'r','up':'u','down':'d'}
    
    if world_map[player.x][player.y-1].desc == 'Forbidden tile':
        movable_directions.pop('left')
    if world_map[player.x][player.y+1].desc == 'Forbidden tile':
        movable_directions.pop('right') 
    if world_map[player.x-1][player.y].desc == 'Forbidden tile':
        movable_directions.pop('up') 
    if world_map[player.x+1][player.y].desc == 'Forbidden tile':
        movable_directions.pop('down') 
        
    print(world_map[player.x][player.y])
    print("You can move in the following directions:")
    for direction in movable_directions.keys():
        print(direction)  



def move_left(player):
    if world_map[player.x][player.y-1].desc == 'Forbidden tile':
        print('You cannot move in this direction!')
    else:
        player.y -= 1
        look(player)
    
def move_right(player):
    if world_map[player.x][player.y+1].desc == 'Forbidden tile':
        print('You cannot move in this direction!')
    else:
        player.y += 1
        look(player)
    
def move_up(player):
    if world_map[player.x-1][player.y].desc == 'Forbidden tile':
        print('You cannot move in this direction!')
    else:
        player.x -= 1
        look(player)
    
def move_down(player):
    if world_map[player.x+1][player.y].desc == 'Forbidden tile':
        print('You cannot move in this direction!')
    else:
        player.x += 1
        look(player)



#Check the player's current tile and response based on tile type
def tile_check(tile):
    #When the tile is an 'Enemy tile' and has_enemy
    if tile.desc == 'Enemy tile' and tile.has_enemy == True:
        time.sleep(0.5)
        tep_enemy=e.enemy_level1()
        print(f"\nYou have encoutered a wild {tep_enemy.name} - get ready to fight!")
        print(f"The {tep_enemy.name} is surprised. You attack first.")
        actions.combat(p.player, tep_enemy)
        tile.has_enemy = False
        if p.player.isalive() == False:
            return False

    #When the tile is an 'Item tile' and has_item
    if tile.desc == "Item tile" and tile.has_item == True:
        time.sleep(1)
        print("\nYou find a treasure box on the floor.\nDo you want to open it?\n")
        time.sleep(1)
        choice = input('You only have one time to decide.\nType "y" or "yes" to open. (Anything else to exit)\n>> ')
        #the player choose whether to open the box
        if choice.lower() == "y" or choice.lower() == "yes":
            time.sleep(1)
            chances=randint(0,3)
            #There is 1 in 3 change that the player needs to fight an enemy
            if chances != 0:
                print("You have successfully open the box.\n")
                time.sleep(1)
                if p.player.class_type == "Wizard":
                    i.wizard_tier1()
                else:
                    i.knight_tier1()
            else:
                tep_enemy=e.enemy_level1()
                print(f"A(n) {tep_enemy.name} has jumped out of the box\n")
                time.sleep(1)
                print(f"{tep_enemy.name} is also surprised - get ready to fight!")
                time.sleep(1)
                actions.combat(p.player, tep_enemy)
        tile.has_item = False

    #When the tile is a 'Boss tile' and has_boss
    if tile.desc == "Boss tile" and tile.has_boss == True:
        global boss_encounter,key_usage,boss
        print("\nYou have encountered a boss.\n")
        time.sleep(1.5)
        choice = input('Are you ready?\nType "y" or "yes" to start. (Anything else to exit)\n>> ')
        if choice.lower() == "y" or choice.lower() == "yes":
            boss_encounter += 1
            #The fight with the first boos
            if boss_encounter == 1:
                boss = e.Boss1()
                key = i.key1()
                for a in range(len(i.slots)):
                    if i.slots[a].name == key.name:
                        print("Do you want to use your key to avoid the battle?")
                        time.sleep(1)
                        choice=input('Type "y" or "yes" to avoid. (Anything else to exit)\n>> ')
                        if choice.lower() == "y" or choice.lower() == "yes":
                            p.use_items(key)
                            key_usage += 1
                            print("\nYou made the boss disappear.")
                            tile.has_boss = False
                            return
            #The fight with the second boss
            elif boss_encounter == 2:
                boss = e.Boss2()
                key = i.key2()
                for a in range(len(i.slots)):
                    if i.slots[a].name == key.name:
                        print("Do you want to use your key to avoid the battle?")
                        time.sleep(1)
                        choice=input('Type "y" or "yes" to avoid. (Anything else to exit)\n>> ')
                        if choice.lower() == "y" or choice.lower() == "yes":
                            p.use_items(key)
                            key_usage += 1
                            print("\nYou made the boss disappear.")
                            tile.has_boss = False
                            return
            #The fight with the third boss
            elif boss_encounter == 3:
                boss = e.Boss3()
                key = i.key3()
                for a in range(len(i.slots)):
                    if i.slots[a].name == key.name:
                        print("Do you want to use your key to avoid the battle?")
                        time.sleep(1)
                        choice=input('Type "y" or "yes" to avoid. (Anything else to exit)\n>> ')
                        if choice.lower() == "y" or choice.lower() == "yes":
                            p.use_items(key)
                            key_usage += 1
                            print("\nYou made the boss disappear.")
                            tile.has_boss = False
                            return
            print(f"The battle has begun. You are facing the {boss.name}")
            time.sleep(2)
            actions.combat(p.player, boss)
            tile.has_boss = False
            time.sleep(1)
            if p.player.isalive():
                print("\nYou also receive a small potion to heal yourself.\n")
                drop=i.SmallPotion()
                i.receive_item(drop)
        else:
            #If the player don't want to fight right now, they will be teleported one step back
            #The tile "has_boss" attribute will still be Ture
            print("You have been teleported one step back")
            p.player.y -=1
            return

    #The "Special Item tile" that offers keys to avoid bosses
    if tile.desc == "Special Item tile" and tile.specialitem == True:
        print("\nYou have found a special item\n")
        time.sleep(1.5)
        if tile.x == 8 and tile.y == 5:
            drop = i.key1()
            i.receive_item(drop)
        elif tile.x == 8 and tile.y == 15:
            drop = i.key2()
            i.receive_item(drop)
        elif tile.x == 9 and tile.y == 25:
            drop = i.key3()
            i.receive_item(drop)
        tile.specialitem = False

    #The "End tile" that will finish the entire game
    if tile.desc == "End tile":
        time.sleep(1.5)
        print("\n\nYou are at the End Tile. Do you want to exit?")
        choice = input('Type "y" or "yes" to exit. (Anything else to stay)\n>> ')
        if choice.lower() == "y" or choice.lower() == "yes":
            time.sleep(1)
            return False

    return True
    

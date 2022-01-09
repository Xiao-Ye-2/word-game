import items as i
import time

#Player class, having max_hp, real_hp, base_hp, base_dmg, real_dmg
#PLAYER.help()-shows the commands, P.position-shows the postion
#setup_hp(), setup_dmg(), quit(), stats(), isalive()function
class PLAYER():  

    class_type = None
    game_playing = True

    def __init__(self, base_hp, base_dmg):
        self.max_hp = base_hp
        self.real_hp = base_hp
        self.base_hp = base_hp
        self.base_dmg = base_dmg
        self.real_dmg = base_dmg

    def __str__(self):
        return f"""
------------------------------
{self.name}: the {self.class_type}
Hitpoints: {self.real_hp}/{self.base_hp}
Damage: +{self.base_dmg}
------------------------------"""

    def name(self, name):
        self.name = name
    
    def create_position(self, x, y):
        self.x = x
        self.y = y
    
    def position(self):
        return f"Position: X = {self.y}, Y = {self.x}" 
                
    def help(self):
        print("""Commands you can use:
'help' - it's this
'quit' - exits the game
'stats' - check player's health & damage
'inv' - check player's inventory
'look' - see available path around you
'left' or 'l' - moves you to the left
'right' or 'r' - moves you to the right
'up' or 'u' - moves you upwards
'down' or 'd' - moves you downwards""")

    def quit(self):
        choice = input('Are you sure to quit?\nType "y" or "yes" to quit the game. (Anything else to exit)\n>> ')
        if choice.lower() == "y" or choice.lower() == "yes":
            self.game_playing = False

    def stats(self):
        self.setup_hp()
        self.setup_dmg()
        print(f"""
----------------------
Hp: {self.real_hp}/{self.max_hp}
Damage: {self.real_dmg}
----------------------""")

    def setup_hp(self):
        percentage_health = float(self.real_hp / self.max_hp)
        self.max_hp = self.base_hp + player_weapon.hp + player_apparel.hp
        self.real_hp = int((percentage_health * self.max_hp)//1)
        if self.real_hp < 2:
            self.real_hp = 2
    
    def setup_dmg(self):
        self.real_dmg = self.base_dmg + player_weapon.dmg + player_apparel.dmg
        
    def isalive(self):
        return self.real_hp > 0


#Knight subclass, base_hp=105,base_dmg=15
class Knight(PLAYER):

    class_type = "Knight"

    def __init__(self, base_hp = 105, base_dmg = 15):
        super().__init__(base_hp, base_dmg)


#Wizard subclass, base_hp=85,base_dmg=20
class Wizard(PLAYER):
    class_type = "Wizard"

    def __init__(self, base_hp = 85, base_dmg = 20):
        super().__init__(base_hp, base_dmg)


#Three blank (white board) equips
def base_weapon():
    return i.Weapons(name="weapon",dmg=0)
def base_apparel():
    return i.Apparel(name="apparel",hp=0)
def base_ring():
    return i.Ring(name="ring",effect="")

#Setting up blank equips
player_weapon = base_weapon()
player_apparel = base_apparel()
player_ring = base_ring()


#Function organizing the inventory
def sort_inventory():
    
    global inv_weapons, inv_apparel, inv_others
    inv_weapons = []
    inv_apparel = []
    inv_others = []
    
    for x in range(len(i.slots)):
        if i.slots[x].item_type == "Weapons":
            inv_weapons.append(i.slots[x])
        elif i.slots[x].item_type == "Apparel":
            inv_apparel.append(i.slots[x])
        else:
            inv_others.append(i.slots[x])
            
    for x in range(len(inv_weapons)-1):
        for y in range(len(inv_weapons)-1-x):
            if inv_weapons[y].dmg<inv_weapons[y+1].dmg:
                inv_weapons[y],inv_weapons[y+1] = inv_weapons[y+1], inv_weapons[y]
                
    for x in range(len(inv_apparel)-1):
        for y in range(len(inv_apparel)-1-x):
            if inv_apparel[y].hp<inv_apparel[y+1].hp:
                inv_apparel[y],inv_apparel[y+1] = inv_apparel[y+1], inv_apparel[y]
    i.slots=inv_weapons+inv_apparel+inv_others


#Function that use/equip items based on item_type   
def use_items(x):
    
    if x.item_type == "Ring":
        global player_ring
        for a in range(len(i.slots)):
            if player_ring == i.slots[a]:
                i.slots[a].name = i.slots[a].name.rstrip("(equipped)")
        player_ring = x
        
    elif x.item_type == "Potion" or x.item_type == "Key":
        if x.name == "Small Potion":
            player.real_hp = player.real_hp + 0.25*player.max_hp
        elif x.name == "Large Potion":
            player.real_hp = player.real_hp + 0.25*player.max_hp
        player.real_hp = player.real_hp//1
        if player.real_hp > player.max_hp:
            print("\nYou are at full health")
            player.real_hp = player.max_hp
        for a in range(len(i.slots)):
            if i.slots[a].name == x.name:
                i.slots.pop(a)
                break
                
    elif x.item_type == "Weapons":
        global player_weapon
        for a in range(len(i.slots)):
            if player_weapon == i.slots[a]:
                i.slots[a].name = i.slots[a].name.rstrip("(equipped)")
        player_weapon = x
        player.setup_hp()
        player.setup_dmg() 
        
    elif x.item_type == "Apparel":
        global player_apparel
        for a in range(len(i.slots)):
            if player_apparel == i.slots[a]:
                i.slots[a].name = i.slots[a].name.rstrip("(equipped)")
        player_apparel = x
        player.setup_hp()
        player.setup_dmg()


#Inventory display    
def inventory():
    
    print("----------------\nINVENTORY")
    #no items in the inventory
    if len(i.slots) == 0:
        print("\nThe inventory is empty.\n----------------")
    else:
        sort_inventory()
        count = 0
        #Displaying items in orders of weapons, apparel, others
        print("\nWeapons(high dmg to low):")
        for a in range(len(inv_weapons)):
            print("  ",a+1,"->",i.slots[a].name)
            count += 1
        print("\nApparel(high hp to low):")
        for a in range(count,count+len(inv_apparel)):
            print("  ",a+1,"->",i.slots[a].name)
            count += 1
        print("\nOthers:")
        for a in range(count,count+len(inv_others)):
            print("  ",a+1,"->",i.slots[a].name)
            count += 1
        print("----------------")
        try:
            #The num_input is not in the inventory
            num_input = int(input("\n\nEnter the number of the item:(Anything else to exit) "))
            if num_input not in range(1,count+1):
                print("\nNumber of item does not exist.\n\n")
                time.sleep(1)
                inventory()
            else:
                try:
                    #Three choices of items (read,equip,return back to inventory)
                    user_choice = input('\nEnter "r" to read info, "e" to equip/unequip, "b" to go back (Anything else to exit): ')
                    #Read item info
                    if user_choice.lower() == "r":
                        item_check = True
                        while item_check == True:
                            try:
                                if num_input in range(1,len(i.slots)+1):
                                    print("\n\nName:",i.slots[num_input-1].name)
                                    print("Decription:",i.slots[num_input-1].desc)
                                    print(i.slots[num_input-1])
                                    item_check = False
                            except:
                                item_check = False
                                return
                    #Item equipping
                    if user_choice.lower() == "e":
                        try:
                            if i.slots[num_input-1].item_type == "Key":
                                print("\nYou can only use a key when facing the bosses.")
                                return
                            if i.slots[num_input-1].name[-10:] == '(equipped)':
                                i.slots[num_input-1].name = i.slots[num_input-1].name.rstrip("(equipped)")    
                                if i.slots[num_input-1].item_type == 'Weapons':
                                    use_items(base_weapon())
                                if i.slots[num_input-1].item_type == 'Apparel':
                                    use_items(base_apparel())
                                if i.slots[num_input-1].item_type == 'Ring':
                                    use_items(base_ring())
                                print('Item unequipped')
                                    
                            elif num_input in range(1,len(i.slots)+1):
                                if i.slots[num_input-1].item_type == "Potion":
                                    print("\nYou drink a bottle of potion and gain some health")
                                    use_items(i.slots[num_input-1])
                                else:
                                    use_items(i.slots[num_input-1])
                                    if i.slots[num_input-1].name[-1] == ' ':
                                        i.slots[num_input-1].name += '(equipped)'
                                    else:
                                        i.slots[num_input-1].name += ' (equipped)'
                                    print("Item equipped")  
                        except:
                            return
                    #Return back to inventory
                    if user_choice.lower() == "b":
                        time.sleep(1)
                        print("")
                        inventory()
                except:
                    return
        except:
            return
          

#Player generate (1-Knight, 2-Wizard)
def character_create():
    class_choice = None
    while class_choice not in [1,2]:
        try:
            class_choice = int(input("Enter a number to choose your class: "))
        except:
            print("Enter again please.")
            continue
    global player
    if class_choice == 1:
        player = Knight()
    elif class_choice == 2:
        player = Wizard()
    player.name(input("\nEnter a name for your character: "))

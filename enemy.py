from random import randrange,randint

class Enemy:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def isalive(self):
        return self.hp > 0 

class Kobold(Enemy):
    def __init__(self):
        super().__init__("Kobold", 30, 6)

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 35, 8)

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 45, 13)

class Grue(Enemy):
    def __init__(self):
        super().__init__("Grue", 50, 15)

class Boss1(Enemy):
    def __init__(self):
        super().__init__("Swamp Thing", 100, 12)

class Boss2(Enemy):
    def __init__(self):
        super().__init__("Headless Horseman", 70, 18)

class Boss3(Enemy):
    def __init__(self):
        super().__init__("Wolfman", 60, 24)
        
#Random all four normal enemies
def enemy_generate():
    global e_1,e_2,e_3,e_4
    e_1=Kobold()
    e_2=Goblin()
    e_3=Orc()
    e_4=Grue()

# return one out of four enemies, ratio of 1:11:7:1
def enemy_level1():
    enemy_generate()
    enemy_list1 = [e_2 for i in range(11)]
    enemy_list2 = [e_3 for i in range(7)]
    enemy_list = enemy_list1 + enemy_list2 + [e_1] + [e_4]
    enemy_1 = enemy_list[randint(0,19)]
    return enemy_1
    
    
    
    

from random import randrange,randint

#Items that player has
slots=[]

#The one super class
class ITEM:
    def __init__ (self,desc,worth="Unknown value"):
        self.desc=desc
        self.worth=worth

#The subclass of ITEM, superclass of keys
class Key(ITEM):
    item_type="Key"
    def __init__(self,name,desc):
        self.name=name
        super().__init__(desc)
    def __str__(self):
        return f"One of the three special items"

#Three different keys that can be used to avoid bosses   
class key1(Key):
    def __init__(self):
        super().__init__(name="The first key",desc="Use to avoid the first boss.")
class key2(Key):
    def __init__(self):
        super().__init__(name="The second key",desc="Use to avoid the second boss.")
class key3(Key):
    def __init__(self):
        super().__init__(name="The third key",desc="Use to avoid the third boss.")



#The subclass of ITEM, superclass of potions        
class Potion(ITEM):
    item_type="Potion"
    def __init__(self,name,effect,desc):
        self.name=name
        self.effect=effect
        super().__init__(desc)

#Two different potions, SmallPotion heals 25%, LargePotion heals 50%
class SmallPotion(Potion):
    def __init__(self):
        super().__init__(name="Small Potion",effect="s_p",desc="Healing potion")
    def __str__(self):
        return f"This item heal 25% of your health"
class LargePotion(Potion):
    def __init__(self):
        super().__init__(name="Large Potion",effect="l_p",desc="Healing potion")
    def __str__(self):
        return f"This item heal 50% of your health"



#The subclass of ITEM, superclass of all equippable items
class Equips(ITEM):
    def __init__(self,name,dmg=0, hp=0, desc="Something you could use."):
        self.name=name
        self.dmg=dmg
        self.hp=hp
        super().__init__(desc)




#The subclass of Equips, superclass of all armors     
class Apparel(Equips):
    item_type="Apparel"
    def __init__(self,name,hp,dmg=0,desc="This is something you could wear.\nOr you could choose being naked"):
        super().__init__(name,dmg,hp,desc)
    def __str__(self):
        return f"This item can increase {self.hp} hp for you"

#Four different kinds of Knight armors (from weak to strong)
class LeatherArmor(Apparel):
    def __init__(self):
        super().__init__(name="Leather Armor",hp=randrange(13,20),desc="This is a armor made of leather. Something to wear")
class ChainArmor(Apparel):
    def __init__(self):
        super().__init__(name="Chain Armor",hp=randrange(23,30),desc="This is a armor made of chains. Something to wear")
class IronArmor(Apparel):
    def __init__(self):
        super().__init__(name="Iron Armor",hp=randrange(33,40),desc="This is a armor made of iron ingots. Something to wear")
class DiamondArmor(Apparel):
    def __init__(self):
        super().__init__(name="Diamond Armor",hp=randrange(55,80),desc="An armor carved out of diamond. Something to wear")

#Four different kinds of Wizard armors (from weak to strong)
class FlaxCape(Apparel):
    def __init__(self):
        super().__init__(name="Flax Cape",hp=randrange(11,16),desc="Just a cape made of normal flax")
class SilkCape(Apparel):
    def __init__(self):
        super().__init__(name="Silk Cape",hp=randrange(17,25),desc="Silk??? Does it protect?")
class AncientCape(Apparel):
    def __init__(self):
        super().__init__(name="Ancient Cape",hp=randrange(29,33),desc="Found it in the basement. I hope it would work.")
class MagicCape(Apparel):
    def __init__(self):
        super().__init__(name="Magic Cape",hp=35,dmg=10,desc="The cape enhanced by the great wizard. +30hp +10dmg")




#The subclass of Equips, superclass of all weapons     
class Weapons(Equips):
    item_type="Weapons"
    def __init__(self,name,dmg,desc="Something you can use to attack",hp=0):
        super().__init__(name,dmg,hp,desc)
    def __str__(self):
        return f"This item can increase {self.dmg} dmg for you"

#Five different kinds of Knight weapons (from weak to strong)
class Rock(Weapons):
    def __init__(self):
        super().__init__(name="A peddle",dmg=randrange(2,4),desc="A peddle you can hit people")
class Dagger(Weapons):
    def __init__(self):
        super().__init__(name="Dagger",dmg=randrange(3,7),desc="A knife you spread butter with")
class Sword(Weapons):
    def __init__(self):
        super().__init__(name="Sword",dmg=randrange(5,9),desc="Ancient knight's saber")
class Club(Weapons):
    def __init__(self):
        super().__init__(name="Wooden Club",dmg=randrange(6,11),desc="Rotten Club")
class Axe(Weapons):
    def __init__(self):
        super().__init__(desc="",name="Axe",dmg=randrange(6,13))
        if self.dmg>8:
            self.desc="An enhanced axe"
        else:
            self.desc="A little weak axe"      

#Five different kinds of Wizard weapons (from weak to strong)
class TornadoSpell(Weapons):
    def __init__(self):
        super().__init__(name="Tornado Spell",dmg=randrange(2,5),desc="Just a wind Breeze")
class FireSpell(Weapons):
    def __init__(self):
        super().__init__(name="Fire Ball",dmg=randrange(4,7),desc="You have learnt to throw fire balls")
class PoisionSpell(Weapons):
    def __init__(self):
        super().__init__(name="Poision Spell",dmg=randrange(6,9),desc="A little snake bite")
class EarthquakeSpell(Weapons):
    def __init__(self):
        super().__init__(name="Earthquake Spell",dmg=randrange(6,13),desc="Weak and Powerful, 2 in 1 combo")
class LightningSpell(Weapons):
    def __init__(self):
        super().__init__(name="Lighting Ball",dmg=randrange(11,16),desc="The king of lighting")




#The subclass of ITEM, superclass of all ring
class Ring(Equips):
    item_type="Ring"
    def __init__(self,name,effect,desc="A ring"):
        super().__init__(name,effect,desc)
    def __str__(self):
        return f"An amazing ring"

#Three types of rings that have different effects (Currently do not do anything)
class RedRing(Ring):
    def __init__(self):
        super().__init__(name="Red Ring",effect="r",desc="A ring that enhances your weapon")
class GreenRing(Ring):
    def __init__(self):
        super().__init__(name="Green Ring",effect="g",desc="A ring that improves your health")
class BlueRing(Ring):
    def __init__(self):
        super().__init__(name="Blue Ring",effect="b",desc="Ring of evasion")



#Special Weapon, Fork, extreme high dmg       
class Fork(Weapons):
    def __init__(self):
        super().__init__(name="Golden Fork",dmg=1000,desc="You beat the game, go at them")



#function that generate all possible Knight drops
def create_drop_knight():
    global w_1,w_2,w_3,w_4,w_5,w_6,a_1,a_2,a_3,a_4,r_1,r_2,r_3,p_1,p_2
    w_1=Rock()
    w_2=Dagger()
    w_3=Sword()
    w_4=Club()
    w_5=Axe()
    w_6=Fork()
    a_1=LeatherArmor()
    a_2=ChainArmor()
    a_3=IronArmor()
    a_4=DiamondArmor()
    r_1=RedRing()
    r_2=GreenRing()
    r_3=BlueRing()
    p_1=SmallPotion()
    p_2=LargePotion()

#function that generate all possible Wizard drop
def create_drop_wizard():
    global w_1,w_2,w_3,w_4,w_5,w_6,a_1,a_2,a_3,a_4,r_1,r_2,r_3,p_1,p_2
    w_1=TornadoSpell()
    w_2=FireSpell()
    w_3=PoisionSpell()
    w_4=EarthquakeSpell()
    w_5=LightningSpell()
    w_6=Fork()
    a_1=FlaxCape()
    a_2=SilkCape()
    a_3=AncientCape()
    a_4=MagicCape()
    r_1=RedRing()
    r_2=GreenRing()
    r_3=BlueRing()
    p_1=SmallPotion()
    p_2=LargePotion()



#Function used when giving player one specific item
def receive_item(drop):
    print("Name:",drop.name)
    print("Decription:",drop.desc)
    print(drop)
    print("This item has been place into your inventory")
    slots.append(drop)




#Four drop tier boxes
def knight_tier1():
    create_drop_knight()
    k_drop1=[a_1 for i in range(350)]
    k_drop2=[a_2 for i in range(150)]
    k_drop3=[w_1 for i in range(300)]
    k_drop4=[w_2 for i in range(150)]
    k_drop5=[w_3 for i in range(40)]
    k_drop6=[p_1 for i in range(6)]
    k_drop7=[p_2 for i in range(3)]
    k_drop=k_drop1+k_drop2+k_drop3+k_drop4+k_drop5+k_drop6+k_drop7+[w_6]
    tep_drop=k_drop[randint(0,999)]
    receive_item(tep_drop)

def knight_tier2():
    create_drop_knight()
    k_drop1=[a_1 for i in range(50)]
    k_drop2=[a_2 for i in range(150)]
    k_drop4=[w_2 for i in range(150)]
    k_drop5=[w_3 for i in range(40)]
    k_drop6=[p_1 for i in range(6)]
    k_drop7=[p_2 for i in range(3)]
    k_drop=k_drop1+k_drop2+k_drop4+k_drop5+k_drop6+k_drop7+[w_6]
    tep_drop=k_drop[randint(0,399)]
    receive_item(tep_drop)

def wizard_tier1():
    create_drop_wizard()
    w_drop1=[a_1 for i in range(350)]
    w_drop2=[a_2 for i in range(150)]
    w_drop3=[w_1 for i in range(300)]
    w_drop4=[w_2 for i in range(150)]
    w_drop5=[w_3 for i in range(40)]
    w_drop6=[p_1 for i in range(6)]
    w_drop7=[p_2 for i in range(3)]
    w_drop=w_drop1+w_drop2+w_drop3+w_drop4+w_drop5+w_drop6+w_drop7+[w_6]
    tep_drop=w_drop[randint(0,999)]
    receive_item(tep_drop)

def wizard_tier2():
    create_drop_wizard()
    w_drop1=[a_1 for i in range(50)]
    w_drop2=[a_2 for i in range(150)]
    w_drop4=[w_2 for i in range(150)]
    w_drop5=[w_3 for i in range(40)]
    w_drop6=[p_1 for i in range(6)]
    w_drop7=[p_2 for i in range(3)]
    w_drop=w_drop1+w_drop2+w_drop4+w_drop5+w_drop6+w_drop7+[w_6]
    tep_drop=w_drop[randint(0,399)]
    receive_item(tep_drop)



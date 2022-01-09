import maps as m
import player as p
import items as i

#This is text formating
def award_print(x):
    tep=len(x)
    print("----",end='')
    for i in range(tep):
        print("-",end='')
    print("----")
    print("||  " + x + "  ||")
    print("----",end='')
    for i in range(tep):
        print("-",end='')
    print("----\n")

def award_check():
    Fork_own = False
    keys_owned = 0
    key1 = i.key1()
    key2 = i.key2()
    key3 = i.key3()
    item = i.Fork()
    #checking keys/Fork in player's inventory
    for a in range(len(i.slots)):
        if i.slots[a].name == key1.name or i.slots[a].name == key2.name or i.slots[a].name == key3.name:
            keys_owned += 1
        if i.slots[a].name == item.name:
            Fork_own = True
    if Fork_own == True:
        award_print("Super Luck (Having Golden Fork)")
#Awards given based on owning keys
    if keys_owned == 1:
        award_print("The Forgetful (Left one key in inventory)")
    elif keys_owned == 2:
        award_print("The Brave One (Have two keys in inventory)")
    elif keys_owned == 3:
        award_print("Master (Have keys but never used)")
#Awards given based on used keys      
    if m.key_usage == 3:
        award_print("Bronze Warrior (Using all keys)")
    elif m.key_usage == 2:
        award_print("Silver Warrior (Using keys two times)")
    elif m.key_usage == 1:
        award_print("Golden Warrior (Using keys one time)")
    elif m.key_usage == 0:
        award_print("Platinum Warrior (Never used the key)")

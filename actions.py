from random import randrange,randint
import time
import enemy as e
import player as p
import items as i

#Define three bosses)
boss1 = e.Boss1()
boss2 = e.Boss2()
boss3 = e.Boss3()

#Player damage range        
def player_dmg(player):
    
    dmg_min=int((player.real_dmg * 0.8)//1)
    dmg_max=int((player.real_dmg * 1.15)//1)
    return randint(dmg_min,dmg_max)

#Enemy damage range  
def enemy_dmg(enemy):
    
    dmg_min=int((enemy.dmg * 0.8)//1)
    dmg_max=int((enemy.dmg * 1.2)//1)
    return randint(dmg_min,dmg_max)

#Combat function (given player and enemy to start a combat)
#Drops are taken into count in this function
def combat(player,enemy):
    
    print(f'''{enemy.name}:
Enemy Hp: {enemy.hp}
Enemy dmg: {enemy.dmg}''')
    
    while player.isalive():

        attacks = ['atk'] #more attacking methods can be added
        p_attack = input('\nEnter an attack ("atk" is the only option): ')
        while p_attack not in attacks:
            p_attack = input('Error! Try "atk": ')
            
        if randrange(0,8) == 0: #Enemy have 1 in 8 chance to defend
            print(f"\nThe {enemy.name} defended itself, taking no damage.")
        else:
            p_dmg = player_dmg(player)
            print(f"\nGood {p_attack}!. You caused {p_dmg} damage")
            enemy.hp -= p_dmg
        
        if enemy.isalive() == True:
            print(f"The {enemy.name} has {enemy.hp} hp left")
        else:
            print(f"\nWhat a wonderful battle! \nYou have defeated {enemy.name}.\n")
            time.sleep(1.5)
            if p.player.class_type == "Wizard":
                if enemy == boss1 or enemy == boss2 or enemy == boss3:
                    i.wizard_tier2() #boss drop
                else:
                    i.wizard_tier1() #normal drop
            else:
                if enemy == boss1 or enemy == boss2 or enemy == boss3:
                    i.knight_tier2() #boss drop
                else:
                    i.knight_tier1() #normal drop
            break

        defences = ["jump","duck", "parry", "block"]
        p_defence = input(f'\nThe {enemy.name} attacks! Enter a defence ("jump","duck", "parry", or "block"): ')
        while p_defence not in defences:
            p_defence = input('Error! Try "jump","duck", "parry", or "block": ')
    
        if p_defence == defences[randrange(0,4)]: #1 in 4 chance for player to defend
            print(f"\nPerfect {p_defence}!. The {enemy.name} did not hit you.")
        else:
            e_dmg = enemy_dmg(enemy)
            print(f"\nThe {enemy.name} hit you, causing {e_dmg} damage.")
            player.real_hp -= e_dmg

        if player.isalive() == False:
            time.sleep(1.5)
            print("\nGame OVERRRR. TOO BAD SO SAD. Maybe? Try again?")
        else:
            print(f"\nYour hp stats are {player.real_hp} / {player.max_hp}")
            time.sleep(1.5)

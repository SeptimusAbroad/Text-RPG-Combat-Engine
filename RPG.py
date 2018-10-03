from random import randint

playername = input("What is thy name, traveller? ")
player = playername

#The first of the weapon classes
class Sword:

    def __init__(self, dam_mod):
        self.dam_mod = dam_mod

    def __repr__(self):
        return f"Sword({self.dam_mod})"

    def __str__(self):
        if self.dam_mod == 1:
            return "A very sharp sword with a keen edge!"
        elif self.dam_mod == 2:
            return "A very sharp sword with a keen edge and a magic glimmer!"
        elif self.dam_mod == 3:
            return "This is a magical and deadly blade."
        elif self.dam_mod == 4:
            return "Behold! The magical blade of the dreaming god! It goes, 'SCHING SCHING!'when you swing it."
        elif self.dam_mod == 5:
            return "Good for Jabberwocks and evil wizards. It has 'snicker-snack' written on the side in runes."
        elif self.dam_mod == 6:
            return "Basically a lightsaber of magic energy. It'll mess fools up. Right in the face. Like, for real."
        return "A very sharp sword!"

    def attack(self):
        return randint(1, 6) + self.dam_mod

#The first of the monster classes
class Ork:

    def __init__(self, name, HP, AC, skill=0, weapon=Sword(0)):
        self.name = name
        self.HP = HP
        self.AC = AC
        self.skill = skill
        self.weapon = weapon

    def __repr__(self):
        return f"Ork({self.name}, {self.HP}, {self.AC})"

    def __str__(self):
        return f"You see a gnarly looking Ork. If he could speak your language, you think he'd call himself '{self.name}'"

#The first of the player classes
class Hero:

    def __init__(self, HP, AC, name=playername, skill=1, weapon=None):
        self.HP = HP
        self.AC = AC
        self.name = name
        self.skill = skill
        self.weapon = weapon

#Assign player and monster for combat debugging
player = Hero(10, 12, weapon=Sword(6))
ork1 = Ork("Ork1", 10, 10, weapon=Sword(0))


#Combat function
def attack(target):
    #Win, lose or withdraw messages
    win = f"{target.name} was slain by {player.name}! Huzzah for wanton murder!"
    loss = f"{player.name} has been slain by {target.name}. You die unsung and left to the crows."
    decide_against_combat = "You decide against slaughter. Pansy."
    answer = None

    #initiative roll
    player_init_roll = randint(1, 20) + player.skill
    print(f"{player.name} rolls {player_init_roll} for initiative!")
    target_init_roll = randint(1, 20) + target.skill
    print(f"{target.name} rolls {target_init_roll} for initiative!")
    fighter1 = None
    fighter2 = None
    if player_init_roll > target_init_roll or player_init_roll == target_init_roll:
        fighter1 = player
        fighter2 = target
        print(f"{player.name} goes first this round!")
    elif player_init_roll < target_init_roll:
        fighter1 = target
        fighter2 = player
        print(f"{target.name} goes first this round!")

    #If player wins initiative, they can decide to withdraw if close to death
    if fighter1 == target:
        answer = "y"
    elif fighter1 == player:
        answer = input(f"Attack {target.name}?\n")
    #Withdraw condition
    if answer == "n":
        return print(decide_against_combat)

    #Combat proper
    elif answer == "y":
        if target.HP > 0 and player.HP > 0:
            #fighter1 misses and fighter2 hits check for victory restart loop
            fighter1_to_hit = fighter1.skill
            fighter1_attack_roll = fighter1_to_hit + randint(1,20)
            print(f"{fighter1.name} rolls {fighter1_attack_roll} to hit!")
            if fighter1_attack_roll < fighter2.AC:
                print(f"{fighter1.name} misses!")
                fighter2_to_hit = fighter2.skill
                fighter2_attack_roll = fighter2_to_hit + randint(1, 20)
                print(f"{fighter2.name} rolls {fighter2_attack_roll} to hit!")
                if fighter2_attack_roll >= fighter1.AC:
                    print(f"{fighter2.name} attacks {fighter1.name} with {fighter2.weapon}")
                    damage = fighter2.weapon.attack()
                    print(f"{fighter2.name} does {damage} damage to {fighter1.name}!")
                    fighter1.HP = fighter1.HP - damage
                    print(f"{fighter1.name} has {fighter1.HP} hit points!")
                    if target.HP <= 0:
                        return print(win)
                    elif player.HP <= 0:
                        return print(loss)
                    else:
                        attack(target)

                #fighter1 and fighter2 miss and loop restarts
                elif fighter2_attack_roll < fighter1.AC:
                    print(f"{fighter2.name} misses!")
                    attack(target)


            #fighter1 hits, check for victory, move onto fighter two attack
            elif fighter1_attack_roll >= fighter2.AC:
                print(f"{fighter1.name} attacks {fighter2.name} with {fighter1.weapon}")
                damage = fighter1.weapon.attack()
                print(f"{fighter1.name} does {damage} damage to {fighter2.name}!")
                fighter2.HP = fighter2.HP - damage
                print(f"{fighter2.name} has {fighter2.HP} hit points!")
                if target.HP <= 0:
                    return print(win)
                elif player.HP <= 0:
                    return print(loss)

                #fighter2 attack and miss then restart loop
                fighter2_to_hit = fighter2.skill
                fighter2_attack_roll = fighter2_to_hit + randint(1, 20)
                print(f"{fighter2.name} rolls {fighter2_attack_roll} to hit!")
                if fighter2_attack_roll <= fighter1.AC:
                        print(f"{fighter2.name} misses!")
                        attack(target)

                #fighter2 hits check for victory and restart loop
                elif fighter2_attack_roll >= fighter1.AC:
                    print(f"{fighter2.name} attacks {fighter1.name} with {fighter2.weapon}")
                    damage = fighter2.weapon.attack()
                    print(f"{fighter2.name} does {damage} damage to {fighter1.name}!")
                    fighter1.HP = fighter1.HP - damage
                    print(f"{fighter1.name} has {fighter1.HP} hit points!")
                    if target.HP <= 0:
                        return print(win)
                    elif player.HP <= 0:
                        return print(loss)
                    else:
                        attack(target)


attack(ork1)
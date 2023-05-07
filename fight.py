from config import *


HEROES_ACTIONS_BUFFS = {
    'Basic': None,
    'Basic Slash' : False,
    'Knife Cut' : False,
    'Wand Swing' : False,
    'Fire Ball' : False,

    'Secondary': None,
    'Jump Slash' : {'Damage': +0.2, 'Armor': -0.1},
    'Arrow Shot' : {'Ammo': -1},
    'Heal' : {'Heal': +0.2},
    'Weakening Spell' : {'Enemy Strength': -0.2},
    
    'Special': None,
    'Spinning Attack' : {'Cooldown': +1},
    'Piercing Arrow' : {'Damage': +0.2, 'Ammo': -1, 'Cooldown': +1},
    'Revive' : {'Cooldown': +2, 'Heal': +0.4},
    'Growing Roots' : {'Enemy Armor': -0.2},

    'Defense' : {'Armor': +0.3}
}

INVENTORY = {
    'Money': 0,
    'Heal Potions': 0,
    'Warrior Upgrade': False,
    'Archer Upgrade': False,
    'Healer Upgrade': False,
    'Mage Upgrade': False
}

SAVE = False

class Character():
    def __init__(self, id, camp, char_name, health, speed, damage, armor, ammo=None,x=0, y=0, scale=1):
        super().__init__

        self.is_alive = True
        self.id = id
        self.char_name = char_name
        self.camp = camp
        self.cooldown = 0

        self.frame_index = 0 # Frame for animation
        self.action_frame = 0 # Frame for animation

        self.Health = health
        self.MaxHealth = health

        self.Speed = speed
        self.BaseSpeed = speed

        self.Damage = damage
        self.BaseDamage = damage

        self.Armor = armor # armor = resistance ==> 'health -= damage * armor' (scale from 0 to 1)
        self.BaseArmor = armor

        self.Ammo = ammo # For the archer
        self.MaxAmmo = ammo


class Fight():
    def __init__(self):
    # Reset or not if no saves
        if SAVE == True:
            self.load_vars()
        else:
            self.reset_vars()
    
    def main(self, wave):
    # Basic variables
        self.win_team = None
        self.wave_ended = False
        self.fight_ended = False

    # Si chasseur en vie, refill des 5 flèches en début de manche
        for hero in player_group:
            if (hero == Chasseur) and (hero.is_alive):
                hero.Ammo = hero.MaxAmmo

        self.win_team = self.fight_syst(wave)
        if self.fight_ended:
        # Si combat fini, alors mettre fin au combat / à automatiser + adapter à pygame /!\
            self.fight_end(self.win_team)

    def load_vars(self):
    # Load variables on a json file
        pass

    def reset_vars(self):
    # Reset variables on a json file
        pass

    def ui(self,wave,turn,atk): # / adapt to pygame /!\
        self.is_alive(wave, False)

        print(f"""
    Wave n°{wave+1}
Turn : {turn}""")
        print(f"The attacker is {atk.char_name} {'ID:' + str(atk.id) if atk in monster_group[wave] else ''}               <<<<<")
    # Si l'attaquant est un héros, alors Affichage des cibles possibles
        if atk.camp == 'hero':
            print("""
 –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
|        Action         |                         Description                   |
 –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
|   0. Print stats      | Affiche la vie de tous les personnages                |
|   8. Instant Kill     | Tue instantanément un ennemi                          |
|   9. Revive/Heal      | Réanime et Soigne complétement tout les alliés        |""")
            
            if atk == Guerrier:
                print(""" –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
|   1. Basic Slash      | Basic Attack                                          |
|   2. Jump Slash       | + 20%. of damages  / Armor -10%                       |
|   3. Spining Attack   | Ignore Enemy Armor / Cooldown of 1 turn               |
|   4. Defend           | Increase armor     / Armor +30%. for one turn         |
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯""")
            elif atk == Chasseur:
                print(""" –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
|   1. Knife Cut        | Basic Attack                                          |
|   2. Arrow Shot       | Ignore Enemy Armor / Maximum: 5 arrows per wave       |
|   3. Piercing Arrow   | +20%. of damages   / Cooldown of 1 turn               |
|   4. Defend           | Increase armor     / Armor +30%. for one turn         |
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯""")
                # working
            elif atk == Guerisseur:
                print(""" –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
|   1. Wand Swing       | Basic Attack                                          |
|   2. Heal             | Heal an Ally   / +20%. of Ally Max Health             |
|   3. Revive           | Revive an Ally / +40%. Max Health + Cooldown 2 turns  |
|   4. Defend           | Increase armor / Armor +30%. for one turn             |
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯""")
            elif atk == Mage:
                print(""" –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
|   1. Fire Ball        | Basic Attack     (Chance to burn enemies ?)           |
|   2. Weakening Spell  | Weak the Enemy / Enemy Strength -20%. for one turn    |
|   3. Growing Roots    | Weak an Enemy  / Enemy Armor -20%. for one wave       |
|   4. Defend           | Increase armor / Armor +30%. for one turn             |
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯""")

            print("\n\tPossibles targets :")
            for i,monster in enumerate(monster_group[wave]):
                if monster.is_alive:
                    print(f'{i+1}. {monster.char_name} (ID:{monster.id})')
                else:
                    print(f'{i+1}. {monster.char_name} (ID:{monster.id}) DEAD')

# Fight system management
    def fight_syst(self,wave):
        turn = 0
        index = -1

        if not self.fight_ended:
            self.wave_ended = False
            print("–––––––––––––––––––––––––––––––––––––")
            print("\nStart of the wave number",str(wave+1))
            print("Alive Allies are :",", ".join([str(x.char_name) for x in (player_group) if (x.is_alive == True)]))
            print("\nEnemies are :",", ".join([str(y.char_name) + ' ID:' + str(y.id) for y in monster_group[wave]]))
            print("–––––––––––––––––––––––––––––––––––––")

        while not self.wave_ended:
        # Manage des incrémentations de tours et d'indexations
            turn += 1
            index += 1
            atk_list = self.get_turn(wave) # get_turn() donne l'ordre d'attaque des personnages
            
        # Manage index of turn list
            self.check = False
            while not self.check:
                if index >= len(atk_list):
                    index = 0
                    self.check = False
                elif not atk_list[index].is_alive:
                    index +=1
                    self.check = False
                elif atk_list[index].is_alive and index <= len(atk_list):
                    self.check = True
            
                
        # Global vars
            target = None
            ally = None
            action = None
            security = True

        # Print reccursive ui for the player / adapt to pygame /!\
            if DEBUG: print('\nIndex =',index)

            self.ui(wave,turn,atk_list[index]) #+ is_alive func.

            if (atk_list[index] != None) and (atk_list[index] in player_group):
                while security:
                    action = input("\n>>> Choose your move :\n ")
                    try :
                        action = int(action)
                    except ValueError:
                        print('\n>>> Invalid action, please try again.')
                    else:
                        if action in [2,3]:
                            if atk_list[index] == Guerrier:
                                if action == 2:
                                    target = input("Wanna attack which ennemy ?\n ")
                                elif action == 3:
                                    if atk_list[index].cooldown == 0:
                                        target = input("Wanna attack which ennemy ?\n ")
                                    else:
                                        target= None
                                        print(f'This attack is on cooldown for {atk_list[index].cooldown} turns.')

                            elif atk_list[index] == Chasseur:
                                if atk_list[index].Ammo > 0:
                                    if action == 2:
                                        target = input("Wanna attack which ennemy ?\n ")
                                    elif action == 3:
                                        if atk_list[index].cooldown == 0:
                                            target = input("Wanna attack which ennemy ?\n ")
                                        else:
                                            target= None
                                            print(f'This attack is on cooldown for {atk_list[index].cooldown} turns.')
                                else:
                                    target= None
                                    print('You have no more arrows for this wave.')

                            elif atk_list[index] == Guerisseur:
                                print("Allies Healable :")
                                for j,x in enumerate(player_group):
                                    if (x.is_alive and (x.Health < x.MaxHealth)):
                                        print(f"{j}. {x.char_name} ({x.Health} => {int(x.Health + (x.MaxHealth * 0.2)) if int(x.Health + (x.MaxHealth * 0.2)) <= x.MaxHealth else f'{x.MaxHealth}'})")
                                print("Allies Resurrectable :")
                                for j,x in enumerate(player_group):
                                    if not x.is_alive:
                                        print(f"{j}. {x.char_name} ({int(x.MaxHealth * 0.4)})")
                                if action == 2:
                                    ally = int(input("Wanna heal which ally ?\n "))
                                    try:
                                        ally = int(ally)
                                        if player_group[ally].is_alive:
                                            pass
                                    except ValueError:
                                        print('\n>>> Invalid target, please try again.')
                                    except IndexError:
                                        ally = None
                                        target = None

                                    if not ally in range(0,len(player_group)) and player_group[ally].is_alive:
                                        target = None
                                        print('Target must be an alive ally.')
                                elif action == 3:
                                    if atk_list[index].cooldown == 0:
                                            ally = int(input("Wanna revive wich ally ?\n "))
                                            try:
                                                if player_group[ally].is_alive:
                                                    pass
                                            except IndexError:
                                                ally = None
                                                target = None

                                            if not ally in range(0,len(player_group)) and not player_group[ally].is_alive:
                                                target = None
                                                print('Target must be a dead ally.')
                                    else:
                                        target= None
                                        print(f'This attack is on cooldown for {atk_list[index].cooldown} turns.')

                            elif atk_list[index] == Mage:
                                target = input("Wanna attack which ennemy ?\n ")
        
                        elif action in [1,8]:
                            target = input("Wanna attack which ennemy ?\n ")
                        elif action == 4:
                            print("You'll block some of the next damage you'll receive next attack (this turn only)")
                            target = 0
                        elif action == 0:
                            target = 0
                            print("\nHeroes :")
                            for x in player_group:
                                print(f'{x.char_name}| ID:{x.id}| Vie:{x.Health} ({(x.Health/x.MaxHealth)*100}%) | Armor: {x.Armor*100}%')
                            print("Monsters :")
                            for y in monster_group[wave]:
                                print(f'{y.char_name}| ID:{y.id}| Vie:{y.Health} ({(y.Health/y.MaxHealth)*100}%) | Armor: {y.Armor*100}%')
                        elif action == 9:
                            target = 0
                            for x in player_group:
                                x.Health = x.MaxHealth
                                x.is_alive = True
                            print('All heroes have been healed / revived.')
                        else: action = None; target = None

                        try:
                            target = int(target)
                        except ValueError:
                            print('\n>>> Invalid target, please try again.')
                        except TypeError:
                            pass
                        else: 
                            if (action not in [0,9]) and not (target in range(0, len(Waves[wave]) + 1)):
                                print('\n>>> Target isn\'t valid! Choose another target.')
                            
                            if ((target == 0) and not (action in [0,4,9]) and ally == None):
                                target = None
                                print('\n>>> Target can\'t be yourself!')
                    
                    if (action in [1,2,3,4,8]) and ((target in range(0, len(Waves[wave]) + 1)) or ally != None):
                        security = False

                    if not security and ally == None:
                        self.is_alive(wave,True)
                        if target == 0: pass
                        elif not Waves[wave][target - 1].is_alive:
                            target = None
                            security = True
                            print('\n>>> Target\'s already dead! Choose another target.')

                    # ---- End of while loop ----

                if ally == None:
                    i = target -1 # Index target -1 pour faciliter dans la suite du programme
                    target = Waves[wave][i]

                # Check if the target is a monster or the hero itself (defense action)
                    if i != -1:
                        print('The target is :',target.char_name, 'ID:' + str(target.id) if target.camp == 'monster' else '')
                        print(f'{atk_list[index].char_name} has attacked')
                    elif i == -1:
                        print(f'{atk_list[index].char_name} will protect itself')
                
                else:
                    ally = player_group[ally]

        # Si c'est au tour du monstre d'attaquer, alors :
            elif atk_list[index] in Waves[wave]:
            # init monster action and target with ui() function
                target,action = self.ai()
                print(f'{atk_list[index].char_name} has attacked')
                print(f'Target of the {atk_list[index].char_name} is', target.char_name)

        # Manage the fight between attacker and target
            if ally == None:
                self.manage_fight(atk_list[index],target,action)
            else:
                self.manage_fight(atk_list[index],ally,action)

        # ---- Check for any dead team ----
            self.is_alive(wave, False)

            Pdeads = Mdeads = 0
            for monster in monster_group[wave]:
            # check si morts des monstres ==> victoire des héros
                if not monster.is_alive:
                    Mdeads += 1
                if Mdeads == len(monster_group[wave]):
                    win_team = 'heroes'
                    self.wave_ended = True
                    self.fight_ended = True
                    break

            for member in player_group:
            # check si morts des héros ==> victoire des monstres
                if not member.is_alive:
                    Pdeads += 1
                if Pdeads == len(player_group):
                    win_team = 'monsters'
                    self.wave_ended = True
                    self.fight_ended = True
                    break
        # ---- End of the while wave loop ----
        return win_team
    # ---- Going back to the for Game loop (last lines of the pgrgm) ----

    def is_alive(self,wave,out=False):
        for character in player_group:
            if character.Health <= 0:
                character.Health = 0
                character.is_alive = False
            if DEBUG and out: print(f'check alive hero {character.char_name}: {character.is_alive}')
        for character in Waves[wave]:
            if character.Health <= 0:
                character.Health = 0
                character.is_alive = False
            if DEBUG and out: print(f'check alive monster {character.char_name}{character.id}: {character.is_alive}')

    def fight_end(self,win_team):
        print('\n-\nVague terminée\n-')
        if win_team == 'monsters':
            print('Game lost')
            self.end_game()
        else:
            print('Victory')
        print(f'The {win_team} has won.')
        time.sleep(2)
        
# AI of the monsters
    def ai(self):
    # Range of random actions of the monster
        action = random.randint(1,1)
    # Range of the random target of the monsters
        target = random.choice([x for x in player_group if x.is_alive == True])
        return target, action

# System for turn by turn gameplay
    def get_turn(self,wave):
        self.is_alive(wave, False)
        turns_list = []
        speeds_list = []

        for member in player_group:
            speeds_list.append(member.Speed)
        for monster in monster_group[wave]:
            speeds_list.append(monster.Speed)
        speeds_list.sort()
        i = 0
        IDs = []
        for turn in speeds_list:
            j = k = 0
            j += 1
            for monster in monster_group[wave]:
                if (monster.Speed == turn) and (j <= len(monster_group[wave])) and (monster.id not in IDs):
                    i += 1
                    turns_list.insert(i,monster)
                    IDs.append(monster.id)
            k += 1
            for member in player_group:
                if member.Speed == turn and (k <= len(player_group)):
                    i += 1
                    turns_list.insert(i,member)
        if DEBUG:
            print(speeds_list)
            for i,x in enumerate(turns_list):
                print(f'{i+1}. {x.char_name} ID:{x.id}')
        
        time.sleep(1)
        return turns_list

    def manage_fight(self,attacker,target,action):
    # reset to MaxArmor, cooldown -= 1, Armor + ... ==> Reduce or Resistance/ Armor
        if attacker in player_group:
            attacker.Armor = attacker.BaseArmor
            attacker.Damage = attacker.BaseDamage
        #attacker.Speed = attacker.BaseSpeed
        ignore_armor = False

        attacker.cooldown -=1
        if attacker.cooldown < 0:
            attacker.cooldown = 0

    # Test for special attacks of every Heroes
        if action in [2,3]:
            if attacker == Guerrier:
                if action == 2:
                    attacker.Damage += 0.2 * attacker.BaseDamage
                    attacker.Armor += round(0.1 * attacker.BaseArmor,2)
                elif action == 3:
                    attacker.cooldown += 1
                    ignore_armor = True
                
                if ignore_armor:
                    damage = int(attacker.Damage)
                else:
                    damage = int(attacker.Damage * target.Armor)
                target.Health -= damage

                print(f"{attacker.char_name} used {'Jump Slash' if action == 2 else 'Spining Attack'}.")
                print(f"{attacker.char_name} has hit {target.char_name}, dealing {damage} damages.")
    
            elif attacker == Chasseur:
                if action == 2:
                    ignore_armor = True
                    attacker.Ammo -= 1
                elif action == 3:
                    attacker.Damage += 0.2 * attacker.BaseDamage
                    attacker.cooldown += 1
                    ignore_armor = True
                    attacker.Ammo -= 1
                
                if ignore_armor:
                    damage = int(attacker.Damage)
                else:
                    damage = int(attacker.Damage * target.Armor)
                target.Health -= damage

                print(f"{attacker.char_name} used {'Arrow Shot' if action == 2 else 'Piercing Arrow'} ({attacker.Ammo} Arrows Remaining).")
                print(f"{attacker.char_name} has hit {target.char_name}, dealing {damage} damages.")
    # working
            elif attacker == Guerisseur:
                if action == 2:
                    ally = target
                    heal = int(ally.Health + (ally.MaxHealth * 0.2))
                    ally.Health = heal
                    if ally.Health > ally.MaxHealth:
                        ally.Health = ally.MaxHealth
                elif action == 3:
                    ally = target
                    heal = int(ally.MaxHealth * 0.4)
                    ally.is_alive = True
                    ally.Health = heal

                print(f"{attacker.char_name} used {'Heal' if action == 2 else 'Revive'}.")
                print(f"{attacker.char_name} {f'is healing {ally.char_name} by {heal} HP' if action == 2 else f'is reviving {ally.char_name} from the deads'}.")
                
            elif attacker == Mage:
                if action == 2:
                    target.Damage = int(target.Damage * 0.8)
                elif action == 3:
                    target.Armor *= 1.2
                    target.Armor = round(target.Armor,2)
            
                print(f"{attacker.char_name} used {'Weakening Spell' if action == 2 else 'Growing Roots'}.")
                print(f"{attacker.char_name} {f'has weakened {target.char_name}' if action == 2 else f'has reduced {target.char_name} Armor by {str(20)}%.'}.")

            elif attacker.camp == 'monster':
            # Création d'attaques spéciales pour les monstres
                pass

        elif action == 1:
            damage = int(attacker.Damage * target.Armor)
        # print à rallonge
            print(f"{attacker.char_name} used {'Basic Slash' if (attacker == Guerrier) else 'Knife Cut' if (attacker == Chasseur) else 'Stick Swing' if (attacker == Guerisseur) else 'Fire Ball' if (attacker == Mage) else 'Basic Attack'}.")
            target.Health -= damage
            print(f'{attacker.char_name} has hit {target.char_name}, dealing {damage} damages.')

        elif action == 4:
            print(f'{attacker.char_name} will block some of the damage recieved during this turn.')
            attacker.Armor *= 1.3
            attacker.Armor = round(attacker.Armor,2)
            print(f'{attacker.char_name} Armor is now for this turn at {int(attacker.Armor * 100)}%.')

        elif action == 8:
            print(f'Insta killed {target.char_name}')
            target.Health -= target.Health
        
        if target.Health < 0:
            target.Health = 0
        if action != 4 and ((attacker not in [Mage,Guerisseur]) and (action not in [2,3])):
            print(target.char_name,('ID:' + str(target.id)+' ' if target.camp == 'monster' else '') + 'has now',target.Health,'HP !')
        
# -

    def end_game(self):
    # Écran End Game (pygame)
        pass

    def screen_print(self,x,y):
    # Automatisation Affichages messages à l'écran (pygame)
        pass

    def update(self):
    # Pygame update function or whatever
        pass

def stats(team):
    print("–––––––––––––––––––––––––––––––––––––")
    for member in team:
        print('\n',member.char_name,':')
        for stat in vars(member):
            if str(stat) in chararcter_stats:
                print('-',stat,'=',member.__getattribute__(stat))

chararcter_stats = ['Health','Damage','Armor','Ammo','Speed']
monster_group = []
player_group = []

for char_name in PLAYER_CHARACTERS: # health, attack Speed, damage, armor + max ammo
    if char_name == 'warrior':
        Guerrier = Character(0,"hero","Guerrier",20,1,14,0.4)
        player_group.append(Guerrier)
    elif char_name == 'elve':
        Chasseur = Character(0,"hero","Chasseur",18,3,12,0.8,5)
        player_group.append(Chasseur)
    elif char_name == 'healer':
        Guerisseur = Character(0,"hero","Guerisseur",16,5,8,1.1)
        player_group.append(Guerisseur)
    else:
        Mage = Character(0,"hero","Mage",16,4,14,0.9)
        player_group.append(Mage)

Enemies = ['Ogre', 'Dragon']
Waves = [[Enemies[0]],
         [Enemies[0],Enemies[0]],
         [Enemies[0],Enemies[0],Enemies[0]],
         [Enemies[1]]]

for wave in Waves:
    i = 0
    row = []
    for char_name in wave:
        if char_name == 'Dragon':
            Dragon = Character(i,'monster',char_name,60,6,40,0.1)
            row.append(Dragon)
        else:
            i +=1 # id des monstres ==> différencier tel ou tel monstre
            Ogre = Character(i,'monster',char_name,20,2,8,0.6)
            row.append(Ogre)
    monster_group.append(row)
    i = Waves.index(wave)
    if DEBUG: print(f"""
Index : {i}
    >""",', '.join([(str(x.char_name) + ' ID:' + str(x.id)) for x in monster_group[i]]))

Waves = monster_group
Players = player_group
Enemies = [Ogre, Dragon]


FightSyst = Fight()

"""
stats(player_group); stats(Enemies)
for wave_number in range(0,len(Waves)):
    Game.main(wave_number)
"""


""" liste des attaques: / Cooldown = can't play for x turn(s)
Guerrier (Humain):
|   1. Basic Slash      | Basic Attack                                          |
|   2. Jump Slash       | + 20%. of damages  / Armor -10%                       |
|   3. Spin Attack      | Ignore Enemy Armor / Cooldown of 1 turn               |
|   4. Defend           | Increase armor     / Armor +30%. for one turn         |

Chasseur (Elfe) :
|   1. Knife Cut        | Basic Attack                                          |
|   2. Arrow Shot       | Ignore Enemy Armor / Maximum: 5 arrows per wave       |
|   3. Piercing Arrow   | +20%. of damages   / Cooldown of 1 turn               |
|   4. Defend           | Increase armor     / Armor +30%. for one turn         |

Guerisseur (??) :
|   1. Wand Swing       | Basic Attack                                          |
|   2. Heal             | Heal an Ally   / +20%. of Ally Max Health             |
|   3. Revive           | Revive an Ally / Backslash (40%.) + Cooldown 2 turns  |
|   4. Defend           | Increase armor / Armor +30%. for one turn             |

Mage (Arcaniste) :
|   1. Fire Ball        | Basic Attack     (Chance to burn enemies ?)           |
|   2. Weakening Spell  | Weak the Enemy / Enemy Strength -20%. for one turn    |
|   3. Growing Roots    | Weak an Enemy  / Enemy Armor -20%. for one wave       |
|   4. Defend           | Increase armor / Armor +30%. for one turn             |
"""



""" list of stats
Ogre:
HEALTH = 20
SPEED = 2
DAMAGE = 8
ARMOR = 0.6

Dragon:
HEALTH = 60
SPEED = 6
DAMAGE = 40
ARMOR = 0.1

Guerrier:
HEALTH = 20
SPEED = 1
DAMAGE = 14
ARMOR = 0.4

Chasseur:
HEALTH = 18
SPEED = 3
DAMAGE = 12
ARMOR = 0.8
AMMO = 5

Guerisseur:
HEALTH = 16
SPEED = 5
DAMAGE = 8
ARMOR = 1.1

Mage:
HEALTH = 16
SPEED = 4
DAMAGE = 14
ARMOR = 0.9
"""
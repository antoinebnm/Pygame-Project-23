from config import *

SAVE = False

class Chararcter():
    def __init__(self, id, camp, char_name, health, speed, damage, armor, ammo=None,x=0, y=0, scale=1):
        super().__init__

        self.is_alive = True
        self.id = id
        self.char_name = char_name
        self.speed = speed
        self.camp = camp

        self.frame_index = 0 # Frame for animation
        self.action_frame = 0 # Frame for animation

        self.Health = health
        self.MaxHealth = health
        self.Speed = speed
        self.MaxSpeed = speed
        self.Damage = damage
        self.Armor = armor # armor = resistance ==> 'health -= damage * armor' (scale from 0 to 1)

        if ammo != None:
            self.Ammo = ammo # For the elven
            self.MaxAmmo = ammo


class Fight():
    def __init__(self, wave):
    # Basic variables
        self.win_team = None
        self.fight_ended = False
        self.wave_ended = False
    # Reset or not if no saves
        if SAVE == True:
            self.load_vars()
        else:
            self.reset_vars()
        
        if player_group == []:
            self.end_game()
        else:
            self.win_team = self.fight_syst(wave)
            if self.fight_ended:
            # Si combat fini, alors mettre fin au combat / à automatiser + adapter à pygame /!\
                self.fight_end(self.win_team)

    def load_vars(self):
        pass

    def reset_vars(self):
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
 _____________________________________________________
|        Action         |         Description         |
 –––––––––––––––––––––––––––––––––––––––––––––––––––––
|   1. Primary Attack   | Basic Attack                |
|   2. Secondary Attack | Ignore target's Armor       |
|   3. Special attack   | Define for each hero        |
|   4. Defend           | Increase armor for 1 turn   |
 –––––––––––––––––––––––––––––––––––––––––––––––––––––
| 0: Print stats        | 9: Revive/Heal all heroes   |
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
            Possibles targets :""")
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
        # Manage des incrémentations de tours et d'indexations #
            turn += 1                                          #
            index += 1                                         #
            atk_list = self.get_turn(wave)                     #
            if index >= len(atk_list):                         #
                index = 0                                      #

            target = None
            action = None
            security = True

# Print reccursive ui for the player / adapt to pygame /!\
            if DEBUG: print('Index =',index)

            self.ui(wave,turn,atk_list[index]) #+ is_alive func.

            if (atk_list[index] != None) and (atk_list[index] in player_group):
                while security:
                    action = input("\n>>> Choose your move :\n ")
                    try :
                        action = int(action)
                    except ValueError:
                        print('\n>>> Invalid action, please try again.')
                    else:
                        if action in [1,2,3]:
                            target = input("Wanna attack which ennemy ?\n ")
                        elif action == 4:
                            print("You'll block some of the next damage you'll receive next attack (this turn only)")
                            target = 0
                        elif action == 0:
                            target = 0
                            print("\nHeroes :")
                            for x in player_group:
                                print(f'{x.char_name}| ID:{x.id}| Vie:{x.Health} ({(x.Health/x.MaxHealth)*100}%)')
                            print("Monsters :")
                            for y in monster_group[wave]:
                                print(f'{y.char_name}| ID:{y.id}| Vie:{y.Health} ({(y.Health/y.MaxHealth)*100}%)')
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
                        else: 
                            if (action not in [0,9]) and not (target in range(0, len(Waves[wave]) + 1)):
                                print('\n>>> Target isn\'t valid! Choose another target.')
                            
                            if (target == 0) and not (action in [0,4,9]):
                                target = None
                                print('\n>>> Target can\'t be yourself!')
                    
                    if (action in [1,2,3,4]) and (target in range(0, len(Waves[wave]) + 1)):
                        security = False

                    if not security:
                        self.is_alive(wave,True)
                        if target == 0: pass
                        elif not Waves[wave][target - 1].is_alive:
                            target = None
                            security = True
                            print('\n>>> Target\'s already dead! Choose another target.')

                    # ---- End of while loop ----
                
                i = target -1 # Index target -1 pour faciliter dans la suite du programme
                target = Waves[wave][i]
            # Check if the target is a monster or the hero itself (defense action)
                if i != -1:
                    print('The target is :',target.char_name, 'ID:' + str(target.id) if target.camp == 'monster' else '')
                    print(f'{atk_list[index].char_name} has attacked')
                elif i == -1:
                    print(f'{atk_list[index].char_name} will protect itself')
            
        # Si c'est au tour du monstre d'attaquer, alors :
            elif atk_list[index] in Waves[wave]:
            # init monster action and target with ui() function
                target,action = self.ai()
                print(f'{atk_list[index].char_name} has attacked')
                print(f'Target of the {atk_list[index].char_name} is :', target.char_name)

        # Manage the fight between attacker and target
            self.manage_fight(atk_list[index],target,action)
        
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
        print('Vague terminée\n-\n-')
        if win_team == 'monsters':
            print('Game lost')
        else:
            print('Victory')
        print(f'The {win_team} has won.')
        time.sleep(2)

    def ai(self):                   # AI of the monsters
        action = random.randint(1,2)            # Range of random attacks of the monster
        target = random.choice([x for x in player_group if x.is_alive == True])        # Range of the random target of the monsters
        return target, action

# System for turn by turn gameplay
    def get_turn(self,wave):
        self.is_alive(wave, False)
        turns_list = []
        speeds_list = []

        for member in player_group:
            if member.is_alive:
                speeds_list.append(member.Speed)
            if DEBUG: print(member.char_name,member.Speed)
        for monster in monster_group[wave]:
            if monster.is_alive:
                speeds_list.append(monster.Speed)
            if DEBUG: print(monster.char_name,monster.Speed)
        speeds_list.sort()
        i = 0
        IDs = []
        for turn in speeds_list:
            j = k = 0
            j += 1
            for monster in monster_group[wave]:
                if (monster.Speed == turn) and (j <= len(monster_group[wave])) and (monster.id not in IDs) and (monster.is_alive == True):
                    i += 1
                    turns_list.insert(i,monster)
                    IDs.append(monster.id)
            k += 1
            for member in player_group:
                if member.Speed == turn and (k <= len(player_group)) and (member.is_alive == True):
                    i += 1
                    turns_list.insert(i,member)
        if DEBUG:
            print(speeds_list)
            for i,x in enumerate(turns_list):
                print(f'{i+1}. {x.char_name} ID:{x.id}')
        
        time.sleep(1)
        return turns_list

    def manage_fight(self,attacker,target,action):
        if action == 1:
            print(f'{attacker.char_name} used Primary Attack.')
            damage = attacker.Damage * target.Armor
            target.Health -= damage # vie -= dégats * armure
            print(f'{attacker.char_name} hit {target.char_name}, dealing {damage} damages.')
        elif action == 2:
            print(f'{attacker.char_name} used Secondary Attack.')
            damage = attacker.Damage
            target.Health -= damage # vie -= dégats
            print(f'{attacker.char_name} hit {target.char_name}, dealing {damage} damages.')
        elif action == 3:
            print(f'{attacker.char_name} used Special Attack.')
            damage = attacker.Damage # Create special_attack() function
            target.Health -= damage # vie -= dégats
            print(f'{attacker.char_name} hit {target.char_name}, dealing {damage} damages.')
        elif action == 4:
            print(f'{attacker.char_name} will block some of the damage recieved during this turn.')
            block = attacker.Health * attacker.Armor
            print(f'{attacker.char_name}, will prevent {block} damages.')
        if target.Health < 0:
            target.Health = 0
        if action != 4:
            print(target.char_name,('ID:' + str(target.id)+' ' if target.camp == 'monster' else '') + 'has now',target.Health,'HP !')
# -

    def end_game(self):
        pass

    def screen_print(self,x,y):
        pass

    def update(self):
        pass

def stats(team):
    print("–––––––––––––––––––––––––––––––––––––")
    for i,member in enumerate(team):
        print('\n',member.char_name,':')
        for j,stat in enumerate(vars(member)):
            if str(stat) in chararcter_stats:
                print(stat,member.__getattribute__(stat))
    print("–––––––––––––––––––––––––––––––––––––")

chararcter_stats = ['Health','Damage','Armor','Ammo','Speed']
monster_group = []
player_group = []

for char_name in PLAYER_CHARACTERS: # health, attack Speed, damage, armor + max ammo
    if char_name == 'warrior':
        Guerrier = Chararcter(0,"hero","Guerrier",20,1,14,0.4)
        player_group.append(Guerrier)
    elif char_name == 'elve':
        Elfe = Chararcter(0,"hero","Elfe",18,3,12,0.8,5)
        player_group.append(Elfe)
    elif char_name == 'healer':
        Guerrisseur = Chararcter(0,"hero","Guerrisseur",16,5,8,1.1)
        player_group.append(Guerrisseur)
    else:
        Mage = Chararcter(0,"hero","Mage",16,4,14,0.9)
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
            Dragon = Chararcter(i,'monster',char_name,60,6,40,0.1)
            row.append(Dragon)
        else:
            i +=1 # id des monstres ==> différencier tel ou tel monstre
            Ogre = Chararcter(i,'monster',char_name,20,2,8,0.6)
            row.append(Ogre)
    monster_group.append(row)
    i = Waves.index(wave)
    if DEBUG: print(f"""
Index : {i}
    >""",', '.join([(str(x.char_name) + ' ID:' + str(x.id)) for x in monster_group[i]]))

Waves = monster_group
Players = player_group
Enemies = [Ogre, Dragon]

stats(player_group); stats(Enemies)

""""""
for wave_number in range(len(Waves)):
    game = Fight((wave_number))

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

Guerrisseur:
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
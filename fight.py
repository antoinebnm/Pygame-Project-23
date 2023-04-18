from config import *

SAVE = False

class Chararcter():
    def __init__(self, camp, char_name, health, speed, damage, armor, ammo=None, x=0, y=0, scale=1):
        super().__init__

        self.is_alive = True
        self.char_name = char_name
        self.speed = speed
        self.camp = camp

        self.health = health
        self.max_health = health
        self.damage = damage # troll = 8
        # armor = resistance ==> 'health -= damage * armor' (scale from 0 to 1)
        self.armor = armor # troll = 0.3
        if ammo != None:
            self.ammo = ammo # For the elven
            self.max_ammo = ammo

        self.frame_index = 0 # Frame for animation
        self.action_frame = 0 # Frame for animation

        self.Health = health
        self.MaxHealth = health
        self.Speed = speed
        self.MaxSpeed = speed
        self.Damage = damage
        self.Armor = armor
        self.Ammo = ammo
        


class Fight():
    def __init__(self, team, wave):
    # Basic variables
        self.team = team
        self.wave_ended = False
    # Reset or not if no saves
        if SAVE == True:
            self.load_vars()
        else:
            self.reset_vars()
        
        if team == []:
            self.end_game()
        else:
            self.fight_syst(wave)

    def load_vars(self):
        pass

    def reset_vars(self):
        pass

    def ui(self,wave,turn,atk): # / adapt to pygame
        print(f"""
        Wave n°{wave+1}
        Turn : {turn}
__________________________________
︳1. Primary Attack               ︳
︳2. Secondary Attack             ︳
︳3. Special attack               ︳
︳4. Defend                       ︳
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
The attacker is {atk.char_name}
""")
    # Si l'attaquant est un héros, alors Affichage des cibles possibles
        if atk.camp == 'hero':
            print("Possibles targets :")
            for i in range(len(Waves[wave])):
                print(str(i+1)+'. '+", ".join([str(x.char_name) for i,x in enumerate(Waves[wave])]))

# Fight system management
    def fight_syst(self,wave):
        turn = 0
        index = -1
        if not self.wave_ended:
            print("–––––––––––––––––––––––––––––––––––––")
            print("\nStart of the wave number",str(wave+1))
            print("Allies are :",", ".join([str(x.char_name) for x in (self.team)]))
            print("\nEnemies are :",", ".join([str(y.char_name) for y in Waves[wave]]))
            print("–––––––––––––––––––––––––––––––––––––")
        else:
        # Si vague finie, alors mettre fin au combat / à automatiser + adapter à pygame
            self.fight_end()

    # Sinon lancer le combat
        while not self.wave_ended:
        # Manage des incrémentations de tours et d'indexations #
            turn += 1                                          #
            index += 1                                         #
            atk_list = self.get_turn(wave)                     #
            if index == len(atk_list):                         #
                index = 0                                      #

            target = None
            action = None

# Print reccursive ui for the player / adapt to pygame
            print('Index =',index)
            self.ui(wave,turn,atk_list[index])

            if (atk_list[index] != None) and (atk_list[index] in self.team):
                while (action not in [1,2,3,4]) and ((target not in Waves[wave]) or target != 0):
                    action = int(input("Choose your move : "))
                    if action == 1:
                        target = int(input("Wanna attack which ennemy ? "))
                    elif action == 2:
                        target = int(input("Wanna attack which ennemy ? "))
                    elif action == 3:
                        target = int(input("Wanna attack which ennemy ? "))
                    elif action == 4:
                        print("You'll block some of the next damage you'll receive next attack (this turn only)")
                        target = 0
                    else: action = None; target = None

                target -=1 # Index target -1 pour faciliter dans la suite du programme
                if target != -1:
                    print('The target is :',Waves[wave][target].char_name)
                    target = Waves[wave][target]
                print('Hero has attacked')
    # Si c'est au tour du monstre d'attaquer, alors :
            elif atk_list[index] in Waves[wave]:
                target,action = self.ai()       # défini l'action et la cible du monstre avec
                print('Monster has attacked')   # la fonction self.ui()
                print(f'Target of the {atk_list[index].char_name} is :', target.char_name)
            self.manage_fight(atk_list[index],target,action)
            
            win_team = self.is_alive(wave)
            if win_team != None:
                self.wave_ended = True
                self.fight_end(win_team)
            else: pass

    def is_alive(self,wave):
        win_team = None
        x = y = 0
        for member in self.team:
            if member.Health <= 0:
                member.is_alive = False
                x += 1
        for monster in Waves[wave]:
            if monster.Health <= 0:
                monster.is_alive = False
                y += 1
        if x == len(self.team):
            win_team = 'monsters'
        elif y == len(Waves[wave]):
            win_team = 'heroes'
        return win_team 

    def fight_end(self,win_team):
        print('Vague terminée\n-\n-')
        if win_team == 'monsters':
            print('Game lost')
        else:
            print('Victory')
        print(f'The {win_team} has won.')

    def ai(self):
        action = random.randint(1,2)
        target = random.choice(self.team)
        return target, action

# System for turn by turn gameplay
    def get_turn(self,wave):
        turns_list = []
        speeds_list = []

        for member in player_group:
            speeds_list.append(member.Speed)
            #print(member.char_name,member.Speed)
        for monster in Waves[wave]:
            speeds_list.append(monster.Speed)
            #print(monster.char_name,monster.Speed)
        speeds_list.sort()
        
        for i,turn in enumerate(speeds_list):
            for monster in Waves[wave]:
                if monster.Speed == turn:
                    turns_list.insert(i,monster)
            for member in player_group:
                if member.Speed == turn:
                    turns_list.insert(i,member)
        
        print(speeds_list, ', '.join([str(x.char_name) for x in turns_list]))
        return turns_list

    def manage_fight(self,attacker,target,action):
        if action == 1:
            print(f'{attacker.char_name} used Primary Attack.')
            damage = attacker.Damage * target.Armor
            target.Health -= damage # vie -= dégats * armure
            print(f'{attacker.char_name} hit {target.char_name}, dealing {damage} damages.')
        if action == 2:
            print(f'{attacker.char_name} used Secondary Attack.')
            damage = attacker.Damage
            target.Health -= damage # vie -= dégats
            print(f'{attacker.char_name} hit {target.char_name}, dealing {damage} damages.')
        if action == 3:
            print(f'{attacker.char_name} used Special Attack.')
            damage = attacker.Damage # Create special_attack() function
            target.Health -= damage # vie -= dégats
            print(f'{attacker.char_name} hit {target.char_name}, dealing {damage} damages.')
        if action == 4:
            print(f'{attacker.char_name} will block some of the damage recieved during this turn.')
            block = attacker.Health * attacker.Armor
            print(f'{attacker.char_name}, will prevent {block} damages.')
        if target.Health < 0:
            target.Health = 0
        print(f'{target.char_name} has now {target.Health} HP !')
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
        Guerrier = Chararcter("hero",char_name,20,1,14,0.4)
        player_group.append(Guerrier)
    elif char_name == 'elve':
        Elfe = Chararcter("hero",char_name,18,3,12,0.8,5)
        player_group.append(Elfe)
    elif char_name == 'healer':
        Healer = Chararcter("hero",char_name,16,5,8,1.1)
        player_group.append(Healer)
    else:
        Mage = Chararcter("hero",char_name,16,4,14,0.9)
        player_group.append(Mage)

Enemies = ['Ogre', 'Dragon']
for char_name in Enemies:
    if char_name == 'Dragon':
        Dragon = Chararcter('monster',char_name,60,6,40,0.1)
        monster_group.append(Dragon)
    else:
        Ogre = Chararcter('monster',char_name,20,2,12,0.6)
        monster_group.append(Ogre)

Enemies = [Ogre, Dragon]
Waves = [[Enemies[0]],
         [Enemies[0],Enemies[0]],
         [Enemies[0],Enemies[0],Enemies[0]],
         [Enemies[1]]]

#stats(player_group); stats(monster_group)

""""""
for wave_number in range(1):#len(Waves)):
    game = Fight(player_group,(wave_number))

""" list of stats
Ogre:
HEALTH = 20
SPEED = 2
DAMAGE = 12
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
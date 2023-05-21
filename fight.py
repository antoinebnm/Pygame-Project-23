from config import *
from button import *

################################################################
#                                                              #
#               Character Class / Statistics init              #
#                                                              #
################################################################

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

        self.Armor = armor # Armure = coeficient multiplicateur ==> ~0 --> très résistant / ~1 --> peu résistant
        self.BaseArmor = armor

        self.Ammo = ammo # For the archer
        self.MaxAmmo = ammo


################################################################
#                                                              #
#                Main Class : Fight System Core                #
#                                                              #
################################################################

class Fight():
    def __init__(self):
        self.gameover = False
        self.fighting = False
        self.ThreadLaunched = False

        self.EVENT = ''
    # Reset or not if no saves
        if SAVE == True:
            self.load_vars()
        else:
            self.reset_vars()
    
    ###################################################################
    #                                                                 #
    #            Main Fight Loop --> Calls the other functions        #
    #                                                                 #
    ###################################################################
    def main(self, wave):
        self.wave_num = wave
        if wave in range(len(Waves)):
            # Basic variables
            self.win_team = None
            self.wave_ended = False
            self.fighting = True

            # Si chasseur en vie, refill des 5 flèches en début de manche
            for hero in player_group:
                if (hero == Chasseur):
                    hero.Ammo = hero.MaxAmmo
                hero.cooldown = 0

            self.win_team = self.fight_syst(wave)
            if not self.fighting:
            # Si combat fini, alors mettre fin au combat / à automatiser + adapter à pygame /!\
                self.fight_end(self.win_team)


###################################################################
#                                                                 #
#                             SAVE SYSTEM                         #
#                                                                 #
###################################################################

    def load_vars(self):
    # Load variables on a json file
        pass

    def reset_vars(self):
    # Reset variables on a json file
        pass

    def end_game(self):
    # Écran End Game (pygame)
        window.fill(pygame.color.Color(0,0,0,60),window.get_rect())

        self.gameover = True
        self.fighting = False

    # Affichage buggé, mise en commentaire
        """if not (self.wave_num > len(Waves)):
            window.blit(pygame.transform.scale(end_frame,window.get_size()),(0,0))"""
# -


###################################################################
#                                                                 #
#                       TO DELETE / USELESS                       #
#                                                                 #
###################################################################
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
# -



###################################################################
#                                                                 #
#                    Fighting system management                   #
#                                                                 #
###################################################################
    def fight_syst(self,wave):
        global action, target, ally, turn, atk_list, index, wave_num
        wave_num = wave

        turn = 0
        index = -1
        self.fighting = True

        if self.fighting:
            self.wave_ended = False
            print("–––––––––––––––––––––––––––––––––––––")
            print("\nStart of the wave number",str(wave+1))
            text_write(40, 40, ("Start of the wave number" + str(wave+1)),placement='console')
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
            
                
        # Global variables
            target = None
            ally = None
            action = None
            security = True

        # Print reccursive ui for the player / adapt to pygame /!\
            if DEBUG: print('\nIndex =',index)

            self.ui(wave,turn,atk_list[index]) #+ is_alive func.

            if (atk_list[index] != None) and (atk_list[index] in player_group):
                while security:
                    while action == None:
                        self.EVENT = 'action'
                    try :
                        action = int(action)
                    except ValueError:
                        text_write(40, 40,'>>> Invalid action, please try again.',placement='console')
                    except TypeError:
                        pass
                    else:
                        if action in [2,3]:
                            if (atk_list[index] == Guerrier) or ((atk_list[index] == Chasseur) and atk_list[index].Ammo > 0):
                                if action == 2:
                                    while target == None:
                                        text_write(40, 40,'Wanna attack which ennemy ?',placement='console')
                                        self.EVENT = 'target'
                                elif action == 3:
                                    if atk_list[index].cooldown == 0:
                                        while target == None:
                                            text_write(40, 40,"Wanna attack which ennemy ?",placement='console')
                                            self.EVENT = 'target'
                                    else:
                                        target= None
                                        action = None
                                        self.EVENT = 'cooldown'
                                        text_write(40, 40,(f'This attack is on cooldown for {atk_list[index].cooldown} turns.'))
                                        pass

                            elif atk_list[index] == Chasseur and atk_list[index].Ammo <=0:
                                target= None
                                self.EVENT = 'no arrows'
                                text_write(40, 40,'You have no more arrows for this wave.',placement='console')

                            elif atk_list[index] == Guerisseur:
                                # Shell Printing
                                """print("Allies Healable :")
                                for j,x in enumerate(player_group):
                                    if (x.is_alive and (x.Health < x.MaxHealth)):
                                        print(f"{j}. {x.char_name} ({x.Health} => {int(x.Health + (x.MaxHealth * 0.2)) if int(x.Health + (x.MaxHealth * 0.2)) <= x.MaxHealth else f'{x.MaxHealth}'})")
                                print("Allies Resurrectable :")
                                for j,x in enumerate(player_group):
                                    if not x.is_alive:
                                        print(f"{j}. {x.char_name} ({int(x.MaxHealth * 0.4)})")"""
                                if action == 2:
                                    a = 0
                                    for x in player_group:
                                        if (x.Health < x.MaxHealth):
                                            a += 1
                                        
                                    if a == 0:
                                        text_write(40, 40,"No ally is healable.",placement='console')
                                    else:
                                        self.EVENT = 'heal'
                                        while ally == None and self.EVENT == 'heal':
                                            text_write(40, 40,"Wanna heal which ally ?",placement='console')
                                            self.EVENT = 'heal'
                                        try:
                                            ally = int(ally)
                                            player_group[ally].is_alive
                                        except ValueError:
                                            ally = None
                                            target = None
                                            text_write(40, 40,'>>> Invalid target, please try again.',placement='console')
                                        except IndexError:
                                            ally = None
                                            target = None
                                        except TypeError:
                                            pass
                                        else:
                                            if not ally in range(0,len(player_group)) and player_group[ally].is_alive:
                                                target = None
                                                text_write(40, 40,'Target must be an alive ally.',placement='console')
                                elif action == 3:
                                    a = 0
                                    for x in player_group:
                                        if not x.is_alive:
                                            a += 1
                                        
                                    if a == 0:
                                        text_write(40, 40,"No ally is revivable.",placement='console')
                                    else:
                                        if atk_list[index].cooldown == 0:
                                            self.EVENT = 'revive'
                                            while ally == None and self.EVENT == 'revive':
                                                text_write(40, 40,"Wanna revive wich ally ?",placement='console')
                                                self.EVENT = 'revive'
                                            try:
                                                player_group[ally].is_alive
                                            except IndexError:
                                                ally = None
                                                target = None
                                            else:
                                                if not ally in range(0,len(player_group)) and not player_group[ally].is_alive:
                                                    target = None
                                                    self.EVENT = 'dead ally'
                                                    text_write(40, 40,'Target must be a dead ally.',placement='console')
                                        else:
                                            target= None
                                            self.EVENT = 'cooldown'
                                            text_write(40, 40,f'This attack is on cooldown for {atk_list[index].cooldown} turns.',placement='console')

                            elif atk_list[index] == Mage:
                                while target == None:
                                    text_write(40, 40,"Wanna attack which ennemy ?",placement='console')
                                    self.EVENT = 'target'
        
                        elif action in [1,8]:
                            while target == None:
                                text_write(40, 40,"Wanna attack which ennemy ?",placement='console')
                                self.EVENT = 'target'
                        elif action == 4:
                            self.EVENT = 'defense'
                            text_write(40, 40,"You'll block some of the next damage",placement='console')
                            text_write(40,60,"you'll receive next attack (this turn only)",placement='console')
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
                            print('All heroes have been healed / revived.',placement='console')
                        else: 
                            text_write(40, 40,'>>> Invalid action, please try again.',placement='console')
                            action = None; target = None

                        try:
                            self.EVENT = ''
                            target = int(target)
                        except:
                            text_write(40, 40,'>>> Invalid target, please try again.',placement='console')
                        else:
                            if (action not in [0,9]) and not (target in range(0, len(Waves[wave]) + 1)):
                                text_write(40, 40,'>>> Target isn\'t valid! Choose another target.',placement='console')
                            
                            if ((target == 0) and not (action in [0,4,9]) and ally == None):
                                target = None
                                text_write(40, 40,'>>> Target can\'t be yourself!',placement='console')
                    
                    if (action in [1,2,3,4,8]) and ((target in range(0, len(Waves[wave]) + 1)) or ally != None):
                        security = False

                    if not security and ally == None:
                        self.is_alive(wave,True)
                        if target == 0: pass
                        elif not Waves[wave][target - 1].is_alive:
                            target = None
                            security = True
                            text_write(40, 40,'>>> Target\'s already dead! Choose another target.',placement='console')

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
                target,action = self.ai(wave)
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
                    self.fighting = False
                    break

            for member in player_group:
            # check si morts des héros ==> victoire des monstres
                if not member.is_alive:
                    Pdeads += 1
                if Pdeads == len(player_group):
                    win_team = 'monsters'
                    self.wave_ended = True
                    self.fighting = False
                    break
        # ---- End of the while wave loop ----
        return win_team
    # ---- Going back to the for Game loop (last lines of the pgrgm) ----


###################################################################
#                                                                 #
#                "Character IS ALIVE?" Function                   #
#                                                                 #
###################################################################
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


# End Screen / Victory & Game Over
    def fight_end(self,win_team):
        self.fighting = False
        self.ThreadLaunched = False
        self.wave_num += 1
        #print('\n-\nVague terminée\n-')
        if win_team == 'monsters':
            print('Game lost')
            self.end_game()
        else:
            print('Victory')
            if self.wave_num >= len(Waves):
                self.end_game()
        #print(f'The {win_team} has won.')

# AI of the monsters
    def ai(self,wave):
    # Range of random actions of the monster
        self.is_alive(wave)
        action = random.randint(1,1)
    # Range of the random target of the monsters
        try:
            target = random.choice([x for x in player_group if x.is_alive == True])
        except: 
            target = None
            self.fight_end('monsters')
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
                    oldhealth = ally.Health
                    ally.Health = heal
                    if ally.Health > ally.MaxHealth:
                        ally.Health = ally.MaxHealth
                elif action == 3:
                    ally = target
                    heal = int(ally.MaxHealth * 0.4)
                    ally.is_alive = True
                    oldhealth = ally.Health
                    ally.Health = heal

                print(f"{attacker.char_name} used {'Heal' if action == 2 else 'Revive'}.")
                print(f"{attacker.char_name} {f'is healing {ally.char_name} by {heal - oldhealth} HP' if action == 2 else f'is reviving {ally.char_name} from the deads'}.")
                
            elif attacker == Mage:
                if action == 2:
                    target.Damage = int(target.Damage * 0.8)
                elif action == 3:
                    target.Armor = round(target.Armor * 1.2,2)
            
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
            attacker.Armor = round(attacker.Armor * 0.7 ,2)
            print(f'{attacker.char_name} Armor is now for this turn at {int(attacker.Armor * 100)}%.')
    
    # Admin command
        elif action == 8:
            print(f'Insta killed {target.char_name}')
            target.Health -= target.Health
        
        if target.Health < 0:
            target.Health = 0
        if action != 4 and ((attacker not in [Mage,Guerisseur]) and (action not in [2,3])):
            print(target.char_name,('ID:' + str(target.id)+' ' if target.camp == 'monster' else '') + 'has now',target.Health,'HP !')
        
# -

################################################################
#                                                              #
#       Easy accessed Functions / Screen text printing         #
#                                                              #
################################################################

def text_write(x, y, text='default text', center="topleft" , placement='ui', color=COLOR_WHITE, scale=1):
    scale = float(scale)
    text = font.render(text, False, color).convert_alpha()
    text = pygame.transform.scale_by(text,scale)
    text_rect = text.get_rect()
    if placement == 'ui':
        y += SCREEN_HEIGHT # adjust to bottom of screen / ui
    elif placement == 'console':
        x += console.left
    exec(f'text_rect.{center} = (({x}),({y}))')
    window.blit(text, text_rect)
    return text_rect

def ui_update():
    global action, target, ally, turn, atk_list, index
    global EVENT, mouse_coord

    mouse_coord = pygame.mouse.get_pos()
    EVENT = FightSyst.EVENT

    window.fill(COLOR_UI,ui_rect)
    window.blit(pygame.transform.scale(lineV_img,(lineV_img.get_width(),window.get_height())),(console.topleft))
    window.blit(pygame.transform.scale(lineH_img,(console.w,lineH_img.get_height())),(console.bottomleft))
    if clock.get_time()> 23:
        window.fill(COLOR_UI,console)

# UI indicator
    char_text = []
    for i,char in enumerate(player_group):
        char_text.append(text_write(40, int((ui_rect.height//12))+ (i* 40),str(char.char_name)))

        if char_text[i].collidepoint(mouse_coord):
            window.blit(frame, (220,450))
            for x,stat in enumerate(stats_icons):
                if (stat != ammo_icon) or (char == Chasseur):
                    window.blit(stat, (240, int(screen.bottom + 16 + (x*32))))
                    text_write(280, int((ui_rect.height//16) * 1), f'{char.Health} / {char.MaxHealth}')
                    text_write(280, int((ui_rect.height//16) * 3), f'{char.Damage}')
                    text_write(280, int((ui_rect.height//16) * 5), f'{char.Armor}')
                    if char == Chasseur:
                        text_write(280, int((ui_rect.height//16) * 7), f'{char.Ammo}')
    try:
        EVENT = str(EVENT).lower()
    except:
        pass
    else:
        if EVENT == 'action':
            text_write(660, int((ui_rect.height//15)), 'Choose your move :')
        elif EVENT == 'target':
            text_write(660, int((ui_rect.height//15)), 'Choose your target :')
        
        player_interact()

        
def player_interact():
    global action, target, ally, turn, atk_list, index, wave_num
    global EVENT, mouse_coord

    try:
        EVENT = str(EVENT).lower()
    except:
        pass
    else:
        if EVENT == 'action':
            for i,act in enumerate(actions_buttons):
                security = i
                attacks = []

                try:
                    atk_list[index]
                except: pass
                else:
                    if atk_list[index].camp == 'hero':
                        if act.check():
                            action = i+1
                            EVENT = 'target'
                            time.sleep(0.2)
            
                        try:
                            ind = player_group.index(atk_list[index])
                        except:
                            pass

                        for j,atk in enumerate(HEROES_ACTIONS_BUFFS.keys()):
                            if (j % 5) == (ind+1) or (atk) == 'Defense':
                                attacks.append(atk)

                for atk in attacks:
                    if security == i:
                        text_write(act.rect.centerx,(act.rect.centery - int(SCREEN_HEIGHT + 16)),attacks[i],center="center",color=COLOR_BLACK)
                        security = None
        
        elif EVENT == 'target':
            for i,targetable in enumerate(Waves[wave_num]):
                i += 1
                k = text_write(600,int((ui_rect.height//15) * ((i)*4)),(f'{i}: ' + targetable.char_name + (' DEAD' if not targetable.is_alive else '')),color=COLOR_WHITE)
                if Button(k.left,k.top,pygame.rect.Rect(k.left,k.top,k.w,k.h)).check():
                    target = Waves[wave_num].index(targetable) + 1
                    EVENT = ''
                    time.sleep(0.2)

    # Healer Actions
        elif EVENT == 'heal':
            for i,targetable in enumerate(player_group):
                """return_text = text_write(500,int((ui_rect.height//15)),('- Retour -'),color=COLOR_WHITE)
                if Button(return_text.left,return_text.top,pygame.rect.Rect(return_text.left,return_text.top,return_text.w,return_text.h)).check():
                    ally = None
                    action = None
                    EVENT = 'action'"""

                if targetable.is_alive and (targetable.Health < targetable.MaxHealth):
                    i += 1
                    k = text_write(600,int((ui_rect.height//15) * ((i)*4)),(f'{i}: ' + targetable.char_name + f' : {targetable.Health}->{int(targetable.Health + (targetable.MaxHealth * 0.2))}'),color=COLOR_WHITE)
                    if Button(k.left,k.top,pygame.rect.Rect(k.left,k.top,k.w,k.h)).check():
                        ally = player_group.index(targetable)
                        EVENT = ''
                        time.sleep(0.2)

        elif EVENT == 'revive':
            for i,targetable in enumerate(player_group):
                """return_text = text_write(500,int((ui_rect.height//15)),('- Retour -'),color=COLOR_WHITE)
                if Button(return_text.left,return_text.top,pygame.rect.Rect(return_text.left,return_text.top,return_text.w,return_text.h)).check():
                    ally = None
                    action = None
                    EVENT = 'action'"""

                if not targetable.is_alive:
                    i += 1
                    k = text_write(600,int((ui_rect.height//15) * ((i)*4)),(f'{i}: ' + targetable.char_name + f'est mort(e). : {targetable.Health} -> {int(targetable.MaxHealth * 0.4)}'),color=COLOR_WHITE)
                    if Button(k.left,k.top,pygame.rect.Rect(k.left,k.top,k.w,k.h)).check():
                        ally = player_group.index(targetable)
                        EVENT = ''
                        time.sleep(0.2)


# Shell Printing of Teams Statistics (Heros + Enemies)
def stats(team):
    print("–––––––––––––––––––––––––––––––––––––")
    for member in team:
        print('\n',member.char_name,':')
        for stat in vars(member):
            if str(stat) in chararcter_stats:
                print('-',stat,'=',member.__getattribute__(stat))



################################################################
#                                                              #
#       Global Variables and images for Fight Core System      #
#                                                              #
################################################################
# IMPORTS

ui_rect = pygame.rect.Rect(screen.left, screen.bottom, window.get_width(), LOWER_MARGIN)
frame = pygame.image.load(img_path + 'frame.png').convert_alpha()
lineV_img = pygame.image.load(img_path + 'lineV.png').convert_alpha()
lineH_img = pygame.image.load(img_path + 'lineH.png').convert_alpha()
action_frame = pygame.image.load(img_path + 'actions_frame.png').convert_alpha()
end_frame = pygame.image.load(img_path + 'end_game.webp').convert_alpha()

# Buttons
act1 = Button(660,int((ui_rect.height//8) * 16), action_frame, 0.5)
act2 = Button(924,int((ui_rect.height//8) * 16), action_frame, 0.5)
act3 = Button(660,int((ui_rect.height//8) * 19), action_frame, 0.5)
act4 = Button(924,int((ui_rect.height//8) * 19), action_frame, 0.5)
actions_buttons = [act1,act2,act3,act4]

# Stats images
health_icon = pygame.image.load((img_path + 'health' + '_icon.png')).convert_alpha()
damage_icon = pygame.image.load((img_path + 'damage' + '_icon.png')).convert_alpha()
armor_icon = pygame.image.load((img_path + 'armor' + '_icon.png')).convert_alpha()
ammo_icon = pygame.image.load((img_path + 'ammo' + '_icon.png')).convert_alpha()
stats_icons = []
stats_icons.append([ a for i, a in locals().items() if str(i).endswith('_icon')])
stats_icons = stats_icons[0]

chararcter_stats = ['Health','Damage','Armor','Ammo','Speed']
monster_group = []
player_group = []



################################################################
#                                                              #
#      Storage of Monster Waves and Heroes in Global List      #
#                                                              #
################################################################

# Armure = coeficient multiplicateur ==> ~0 --> très résistant / ~1 --> peu résistant

for key, value in PLAYER_CHARACTERS.items():
    # Guerrier, Chasseur, Guerisseur, Mage
    # Stats : [Health, Attack turn, Damage, Armor, Ammo]
    if key == 'Guerrier':
        Guerrier = Character(0, "hero", key, value[0], value[1], value[2], value[3], value[4])
        player_group.append(Guerrier)
    elif key == 'Chasseur':
        Chasseur = Character(0, "hero", key, value[0], value[1], value[2], value[3], value[4])
        player_group.append(Chasseur)
    elif key == 'Guerisseur':
        Guerisseur = Character(0, "hero", key, value[0], value[1], value[2], value[3], value[4])
        player_group.append(Guerisseur)
    else:
        Mage = Character(0, "hero", key, value[0], value[1], value[2], value[3], value[4])
        player_group.append(Mage)
    
Enemies = ['Ogre', 'Dragon']
Waves = [[Enemies[0]],
         [Enemies[0],Enemies[0]],
         [Enemies[0],Enemies[0],Enemies[0]],
         [Enemies[1]]]

for monster_wave in Waves:
    i = 0
    row = []
    for char_name in monster_wave:
        if char_name == 'Dragon':
            Dragon = Character(i,'monster',char_name,60,6,40,0.1)
            row.append(Dragon)
        else:
            i +=1 # id des monstres ==> différencier tel ou tel monstre
            Ogre = Character(i,'monster',char_name,20,2,8,0.6)
            row.append(Ogre)
    monster_group.append(row)
    i = Waves.index(monster_wave)
    if DEBUG: print(f"""
Index : {i}
    >""",', '.join([(str(x.char_name) + ' ID:' + str(x.id)) for x in monster_group[i]]))

Waves = monster_group
Players = player_group
Enemies = [Ogre, Dragon]

# -


if DEBUG: stats(player_group); stats(Enemies)

FightSyst = Fight()

"""
for wave_number in range(0,len(Waves)):
    #text_write(400,((-1) * SCREEN_HEIGHT + 60), ('Wave n°' + str(wave_number)),2.4)
    FightSyst.main(wave_number)
"""


################################################################
#                                                              #
#                    Statistics Explaination                   #
#                                                              #
################################################################

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
|   1. Fire Ball        | Basic Attack                                          |
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
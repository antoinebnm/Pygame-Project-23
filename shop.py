#Shop.py

#Définition des couleurs
#noir, rouge, vert, jaune, bleu, violet, cyan, blanc
#[30m, [31m,  [32m, [33m,  [34m, [35m,   [36m, [37m   Code ANSI pour le texte
#[90m, [91m,  [92m, [93m,  [94m, [95m,   [96m, [97m   Code ANSI plus clair pour le texte
#[40m, [41m,  [42m, [43m,  [44m, [45m,   [46m, [47m   Code ANSI pour le fond
class color:
    n = '\033[0m' #gris, couleur normale
    r = '\033[91m' # rouge
    g = '\033[92m' # vert
    y = '\033[93m' # jaune
    b = '\033[94m' # bleu

#Pour savoir si on peux acheter l'item ou non: vert on peut, rouge on ne peut pas
def is_buyable(price, gold):
    r = ''
    if price <= gold:
        r += color.g + str(price) + color.n
    else:
        r += color.r + str(price) + color.n
    return r

#pour afficher l'item en couleur
def colorise(txt, col):
    return col + str(txt) + color.n

#Pour acheter l'item
def buy_item(nb_gold):

    #4 items, 1 par character, nb_gold partagé
    items = {"sword" : 100, "quiver" : 150, "spell book" : 200, "heal stick": 300}

    #boucle qui tourne tant que le user ne choisit pas de quitter la boutique
    secu = True
    while secu:
        
        #affichage des items et de leur valeur avec l'argent total
        ls=[]
        i=1
        print("\n")
        for keys, val in items.items():
            print(i, colorise(keys, color.b), ":", is_buyable(val, nb_gold), "gold")
            i+=1
            ls.append(keys)
        print("\n0 Sortir de la boutique")
        print("\nvous avez", colorise(nb_gold, color.y), "gold")
        print("Voici votre inventaire :", inventory)
        choice = input("Quel est le numéro de l'item que vous souhaitez acheter : ")
        
        #Eviter les problemes d'index et de valeur
        try :
            choice = int(choice)
            if 1 <= choice <= len(ls):
                choix = ls[choice - 1]
            elif choice == 0:
                secu = False
            else:
                raise IndexError
            
        #Pour les malins qui ne mettent pas un nombre
        except ValueError:
            print("Entrer un nombre")

        #Pour les malins qui mettent un nombre aberrant
        except IndexError:
            print("Entrer un nombre entre 0 et", len(items), "\n")
        else:

            #Si le prix de l'objet est abordable, il est acheté et stocké dans la liste inventory
            choix = ls[choice-1]
            if items[choix] <= nb_gold:
                nb_gold -= items[choix]
                print("Vous avez acheté", colorise(choix, color.b), "pour", colorise(items[choix], color.g), "gold")
                print("Il vous reste", colorise(nb_gold, color.y), "gold")
                inventory.append(choix)
                del items[choix]
            
            #Si le choix == 0, on sort de la boucle
            elif choice == 0:
                secu = False

            #Si le prix de l'objet n'est pas abordable, il n'est pas acheté
            elif items[choix] > nb_gold:
                print("Vous n'avez pas assez de gold pour", colorise(choix, color.b)+ ".", "Il vous manque", colorise((items[choix]-nb_gold), color.y), "gold")
                print("Il vous reste", colorise(nb_gold, color.y), "gold")
                print("Faites un autre choix")

    print("\nInventaire :", inventory, "\n")
            
#A rajouter dans le code principale
"""
if "sword" in inventory:
    Guerrier.ATK += 5
if "quiver" in inventory:
    Archer.nb_fleche += 3
if "spell book" in inventory:
    Mage.ATK += 4
if "heal stick" in inventory:
    Guerrisseur.ATK += 3
"""
inventory = []
buy_item(250)
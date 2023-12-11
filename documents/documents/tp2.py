# Maxine Dussault et Mateo Coda-Forno
# 8 décembre 2023

# Ce programme implémente le jeu de cartes "Addiction Solitaire". 
# Ce jeu est une version de solitaire qui utilise un jeu de 52 cartes standard.
# L'objectif du jeu est de disposer toutes les cartes en séquences ascendantes 
# de même couleur, en commençant par les "2". Il ya des options tels que 
# brasser, ou recommencer une partie qui sont proposer a l'utilisateur.

cartes = [
        "2C.svg", "2D.svg", "2H.svg", "2S.svg", 
        "3C.svg", "3D.svg", "3H.svg", "3S.svg", 
        "4C.svg", "4D.svg", "4H.svg", "4S.svg", 
        "5C.svg", "5D.svg", "5H.svg", "5S.svg", 
        "6C.svg", "6D.svg", "6H.svg", "6S.svg", 
        "7C.svg", "7D.svg", "7H.svg", "7S.svg", 
        "8C.svg", "8D.svg", "8H.svg", "8S.svg", 
        "9C.svg", "9D.svg", "9H.svg", "9S.svg", 
        "10C.svg", "10D.svg", "10H.svg", "10S.svg", 
        "JC.svg", "JD.svg", "JH.svg", "JS.svg", 
        "QC.svg", "QD.svg", "QH.svg", "QS.svg", 
        "KC.svg", "KD.svg", "KH.svg", "KS.svg", 
        "absent.svg", "absent.svg", "absent.svg", "absent.svg"
        ]

nb_de_cartes=len(cartes)

nb_de_brasse=3 # Nombre de brassé permis à l'utilisateur initialement
 
num_cartes_deux=[0,1,2,3] # Les numéros de cartes qui représente un deux

premiere_colonne=[0,13,26,39] # Positions à la première colonne
derniere_colonne=[12,25,38,51] # Positions à la dernière colonne

nb_cartes_par_rangee=13
nb_rangee=4

# La fonction melanger prend en paramètre un tableau de 
# chaîne de caractères représentant les noms des cartes.
# Elle mélange le contenu de ce tableau en échangeant chaque 
# carte avec un carte du tableau choisit aléatoirement, en commençant
# par la dernière et en progressant vers le début du tableau. 
# La fonction retourne le tableau de cartes mélangés et un tableau
# de nombres entiers représentant les index des cartes de ce dernier tableau.
def melanger(paquet): 
    global nouveau_paquet, index_paquet
    nouveau_paquet = paquet.copy()
    index_paquet=list(range(nb_de_cartes))
    for i in range(51, 0, -1):

        index_aleatoire = math.floor(random()*nb_de_cartes)
        
        # Échanger les cartes dans le paquet
        carte_temporaire = nouveau_paquet[i]
        nouveau_paquet[i] = nouveau_paquet[index_aleatoire]
        nouveau_paquet[index_aleatoire] = carte_temporaire

        # Échanger les index de ces cartes dans le paquet
        index_temporaire=index_paquet[i]
        index_paquet[i]= index_paquet[index_aleatoire] 
        index_paquet[index_aleatoire]=index_temporaire 
    return nouveau_paquet,index_paquet

def test_melanger():
    paquet = [
        "2C.svg", "2D.svg", "2H.svg", "2S.svg", 
        "3C.svg", "3D.svg", "3H.svg", "3S.svg", 
        "4C.svg", "4D.svg", "4H.svg", "4S.svg", 
        "5C.svg", "5D.svg", "5H.svg", "5S.svg", 
        "6C.svg", "6D.svg", "6H.svg", "6S.svg", 
        "7C.svg", "7D.svg", "7H.svg", "7S.svg", 
        "8C.svg", "8D.svg", "8H.svg", "8S.svg", 
        "9C.svg", "9D.svg", "9H.svg", "9S.svg", 
        "10C.svg", "10D.svg", "10H.svg", "10S.svg", 
        "JC.svg", "JD.svg", "JH.svg", "JS.svg", 
        "QC.svg", "QD.svg", "QH.svg", "QS.svg", 
        "KC.svg", "KD.svg", "KH.svg", "KS.svg", 
        "absent.svg", "absent.svg", "absent.svg", "absent.svg"
        ]
    nouveau_paquet, positions = melanger(paquet)
    assert(paquet!=nouveau_paquet)

# La fonction options prend en paramètre un tableau d'entiers représentant
# les numéros des cartes mélangées et un tableau de chaîne de caractères
# représentant les noms des cartes mélangées. Elle retourne un tableau
# de nombres entiers représentant les positions des cartes déplaçables.
def options(num_cartes,paquet_melange):
    global position_trous, num_cartes_avant_trous, num_cartes_deplacables,\
        position_carte_deplacable, position_carte_avant_trous

    # Indentifier les positions des trous 
    position_trous=[]
    index=0
    for carte in paquet_melange:
        if carte=="absent.svg":
            position_trous.append(index)
        index+=1

    # Identifier les positions des cartes positionnées avant les trous 
    position_carte_avant_trous=list(map(lambda position_trou: position_trou-1,\
                                         position_trous))
    position_carte_avant_trous = list(filter(lambda position: position>=0, \
                                             position_carte_avant_trous)) 
    for position in derniere_colonne:
        while position in position_carte_avant_trous:
            position_carte_avant_trous.remove(position)
    

    # Identifier les cartes positionnées avant les trous
    num_cartes_avant_trous=[]
    for position in position_carte_avant_trous:
        carte=num_cartes[position]
        num_cartes_avant_trous.append(carte)

    # Identifier les cartes déplaçables
    num_cartes_deplacables=[]
    for carte_avant in num_cartes_avant_trous:
        for carte in num_cartes:
            # Vérifier s'il y a une séquence croissante de même couleur:
            if carte%4==carte_avant%4 and carte//4==(carte_avant//4)+1 and\
                  carte<48:
                num_cartes_deplacables.append(carte)                      
    for position in position_trous:
        # S'il y a un trou dans la première colonne
        if position in premiere_colonne: 
            # Ajouter tous les carte de valeur "2":
            for carte in num_cartes_deux:num_cartes_deplacables.append(carte) 
          
    # Identifier les positions des cartes déplaçables 
    position_carte_deplacable=[]
    for position_carte in range(nb_de_cartes):
        carte=num_cartes[position_carte]
        if carte in num_cartes_deplacables:
            position_carte_deplacable.append(position_carte)

    return position_carte_deplacable

def test_options():
    # Cas basique:
    assert options([26, 2, 15, 12, 36, 24, 18, 3, 34, 30, 23, 9, 8, 10, 37, 20,
                    43, 1, 4, 31, 40, 11, 14, 46, 39, 25, 0, 5, 41, 47, 6, 28, 
                    32, 7, 22,48, 13, 17, 29, 19, 50, 27, 38, 35, 21, 33, 51, 
                    45, 49, 42, 16, 44],\
                    ['8H.svg', '2H.svg', '5S.svg', '5C.svg', 'JC.svg', 
                     '8C.svg', '6H.svg','2S.svg', '10H.svg', '9H.svg', 
                     '7S.svg', '4D.svg', '4C.svg', '4H.svg', 'JD.svg', 
                    '7C.svg', 'QS.svg', '2D.svg', '3C.svg', '9S.svg', 
                     'QC.svg', '4S.svg', '5H.svg', 'KH.svg', 'JS.svg', 
                     '8D.svg', '2C.svg', '3D.svg', 'QD.svg', 'KS.svg', 
                     '3H.svg', '9C.svg', '10C.svg', '3S.svg', '7H.svg', 
                     'absent.svg', '5D.svg', '6D.svg', '9D.svg', '6S.svg', 
                     'absent.svg','8S.svg', 'JH.svg', '10S.svg', '7D.svg', 
                     '10D.svg', 'absent.svg', 'KD.svg', 'absent.svg', 'QH.svg',
                     '6C.svg', 'KC.svg'] ) == [0, 10, 14]
    # Cas ou il faut pouvoir déplacer des 2 dans la première colonne:
    assert options([2, 6, 49, 47, 20, 13, 44, 29, 3, 9, 46, 16, 36, 38, 4, 33, 
                    40, 42, 25, 7, 21, 51, 45, 22, 18, 10, 28, 14, 17, 11, 43, 
                    8, 27, 1, 26, 50, 19, 39, 34, 48, 30, 23, 15, 5, 32, 35, 
                    31, 37, 0, 12, 24, 41], \
                    ['2H.svg', '3H.svg', 'absent.svg', 'KS.svg', '7C.svg', 
                     '5D.svg', 'KC.svg', '9D.svg', '2S.svg', '4D.svg', 
                     'KH.svg', '6C.svg', 'JC.svg','JH.svg', '3C.svg', 
                     '10D.svg', 'QC.svg', 'QH.svg', '8D.svg', '3S.svg', 
                     '7D.svg', 'absent.svg', 'KD.svg', '7H.svg', '6H.svg', 
                     '4H.svg','9C.svg', '5H.svg', '6D.svg', '4S.svg', 'QS.svg',
                     '4C.svg', '8S.svg', '2D.svg', '8H.svg', 'absent.svg', 
                     '6S.svg', 'JS.svg', '10H.svg','absent.svg', '9H.svg', 
                     '7S.svg', '5S.svg', '3D.svg', '10C.svg', '10S.svg', 
                     '9S.svg', 'JD.svg', '2C.svg', '5C.svg', '8C.svg', 
                     'QD.svg']) == [0, 8, 18, 25, 33, 40, 48]
    
    # Cas ou on ne peut plus bouger de cartes:
    assert options([2, 6, 10, 14, 18, 24, 44, 51, 49, 48, 41, 45, 36, 38, 4, 8,
                    40, 42, 46, 50, 21, 25, 29, 33, 37, 22, 28, 32, 17, 11, 43,
                    47, 27, 1, 26, 30, 19, 39, 34, 3, 7, 23, 15, 5, 9, 13, 31, 
                    35, 0, 12, 16, 20],\
                     ['2H.svg', '3H.svg', '4H.svg', '5H.svg', '6H.svg', 
                      '8C.svg', 'KC.svg', 'absent.svg', 'absent.svg', 
                      'absent.svg', 'QD.svg', 'KD.svg', 'JC.svg','JH.svg', 
                      '3C.svg', '4C.svg', 'QC.svg', 'QH.svg', 'KH.svg', 
                      'absent.svg', '7D.svg', '8D.svg', '9D.svg', '10D.svg', 
                      'JD.svg', '7H.svg', '9C.svg', '10C.svg', '6D.svg',
                      '4S.svg', 'QS.svg', 'KS.svg', '8S.svg', '2D.svg', 
                      '8H.svg', '9H.svg', '6S.svg', 'JS.svg', '10H.svg', 
                      '2S.svg', '3S.svg', '7S.svg', '5S.svg', '3D.svg', 
                      '4D.svg', '5D.svg','9S.svg', '10S.svg', '2C.svg', 
                      '5C.svg', '6C.svg', '7C.svg']) == []
    
# La procédure cartes_vartes prend en paramètres un tableau de nombres
# entiers représentants les positions des cartes qu'il faut mettre en vert.
# Elle met un fond vert à chaque carte dans le tableau. 
def cartes_vertes(positions_cartes):
    for carte in positions_cartes:
        numero_case="#case"+str(carte)
        case=document.querySelector(numero_case)
        case.setAttribute("style", "background-color: lime")

# Intervertir prend en paramètre deux nombres entiers représentant la 
# position de la carte et la position du trou qu'on doit intervertir.
# Elle interverti c'est deux cartes et puis met à jour le tableau
# de nom de cartes et le tableau de ses index associés.
def intervertir(position_carte,position_trou):
    # Échanger la position de la carte avec celle du trou:
    nouveau_paquet[position_trou] = nouveau_paquet[position_carte]
    nouveau_paquet[position_carte] = 'absent.svg'

    # Échanger l'index de la carte avec celle du trou:
    temporaire = index_paquet[position_trou]
    index_paquet[position_trou] = index_paquet[position_carte]
    index_paquet[position_carte] = temporaire

# La fonction gagner vérifie si l'utilisateur a placé toutes les cartes
# en séquence ascendante, de même couleur, en commençant par un 2. Si c'est 
# le cas, elle retourne True, sinon elle retourne False.
def gagner():
    # Création d'un tableau de tableaux contenant chaque rangée de cartes:
    rangees = []
    for premiere_carte in range(0, nb_de_cartes, nb_cartes_par_rangee):
        derniere_carte=premiere_carte+nb_cartes_par_rangee
        rangee=index_paquet[premiere_carte:derniere_carte]
        rangees.append(rangee)

    for rangee in rangees:
        index = 0 
        # Vérifier si la première carte est un 2
        if rangee[index] in num_cartes_deux: 
            for carte in rangee:
                if index==0: index+=1 # Ignorer le 2
                else:
                    # Vérifier s'il y a une séquence croissante de même couleur
                    carte_avant=rangee[index-1]
                    if carte%4==carte_avant%4 and carte//4==(carte_avant//4)+1\
                        and carte<48:
                        index+=1
                    # S'il n'y as pas séquence croissante de même couleur
                    else: return False 
        else: return False # Si la première carte n'est pas un 2
    return True # L'utilisateur a gagné

# La procédure mise_a_jour prend en paramètre un nombre entier représentant la 
# carte cliquée par l'utilisateur. Elle vérifie si la carte cliquée peut être 
# déplacée et échange sa position avec celle du trou associé si c'est le cas. 
# De plus, elle met à jour le jeu, détermine la situation actuelle (gagner, 
# perdre ou besoin de brasser),et met à jour l'affichage HTML en conséquence.
def mise_a_jour(position_cliquee):
    # Déterminer l'index de la carte cliquée selon sa position dans le paquet 
    # mélangé:
    index_carte_clique = index_paquet[position_cliquee]
    # Vérifier si la carte cliqué peut etre déplacée:
    if position_cliquee in position_carte_deplacable:
        for carte in num_cartes_avant_trous:
            if index_carte_clique//4 == (carte//4)+1 and \
                  index_carte_clique%4==carte%4: 
                # Determiner quel est l'index du trou associé a la carte:
                index_carte=num_cartes_avant_trous.index(carte)
                index_trou_associe=position_carte_avant_trous[index_carte]+1
                # Intervertir la carte avec le trou et mettre a jour les
                # paquets de cartes et d'indexs:      
                intervertir(position_cliquee,index_trou_associe)

        # Si l'utilisateur a cliqué sur un 2:
        if index_carte_clique in num_cartes_deux: 
            for trou in position_trous:
                # Identifier dans quel case de la premiere colonne est le trou
                if trou in premiere_colonne: 
                    intervertir(position_cliquee,trou)
            
        # Mise a jour du jeux selon l'action éffectué par l'utilisateur:

        position_cartes_deplacables=options(index_paquet,nouveau_paquet)

        situation = gagner() # Vérifier s'il a gagné 
        if situation: 
            situation = 1 # Le joueur a gagné
        elif num_cartes_deplacables == [] and nb_de_brasse == 0:
            situation = 2 # Le joueur a perdu
        elif num_cartes_deplacables == [] and nb_de_brasse != 0:
            situation = 3 # Le joueur doit brasser

        # Mise à jour de l'affichage:
        affichage(nouveau_paquet,situation) 
        cartes_vertes(position_cartes_deplacables) 
    # S'il y a rien à mettre à jour:
    else:
        pass 

# La procédure brasser est appelée lorsque l'utilisateur appuie sur le bouton 
# lui permettant de brasser les cartes. Cette procédure va mélanger tous les 
# cartes du paquets, sauf celles déjà bien placées et puis les afficher. 
def brasser():
    global nouveau_paquet, index_paquet, nb_de_brasse

    nb_de_brasse-=1 

    paquet_initiale=nouveau_paquet.copy()
    num_cartes_initiale=index_paquet.copy()

    positions_carte_ne_pas_melanger=[]
    num_cartes_a_ne_pas_melanger=[]

    # Parcourir chaque rangée:
    for rangee in range(nb_rangee):

        index_premiere_carte=rangee*nb_cartes_par_rangee
        premiere_carte=num_cartes_initiale[index_premiere_carte]

        # Si la premiere carte de la rangée est un deux
        if premiere_carte in num_cartes_deux: 
            positions_carte_ne_pas_melanger.append(index_premiere_carte)
            num_cartes_a_ne_pas_melanger.append(premiere_carte)

            compteur=1 # Initialisation du compteur

            # Parcourir les autres cartes de la rangée:
            while compteur<nb_cartes_par_rangee:
                index_carte_actuelle=index_premiere_carte+compteur
                carte_actuelle=num_cartes_initiale[index_carte_actuelle]
                carte_avant=num_cartes_initiale[index_carte_actuelle-1]

                # Vérifier s'il y a une séquence croissante de même couleur:
                if carte_avant%4==carte_actuelle%4==premiere_carte%4 \
                    and carte_avant//4==(carte_actuelle//4)-1:
                    positions_carte_ne_pas_melanger.append\
                        (index_carte_actuelle)
                    num_cartes_a_ne_pas_melanger.append(carte_actuelle)
                else:
                    break
                compteur+=1

    # Trouver les noms de cartes à ne pas mélanger:
    nom_carte_a_ne_pas_melanger=[]
    for position in positions_carte_ne_pas_melanger:
        nom_carte=paquet_initiale[position]
        nom_carte_a_ne_pas_melanger.append(nom_carte)

    # Mélanger le paquet sans prendre en compte les cartes à ne pas mélanger:
    paquet_melanger,index_cartes_melanger=melanger(cartes)

    # Combiner le paquet initiale et le paquet mélangé en laissant les cartes 
    # à ne pas mélanger à leur position initale:
    if num_cartes_a_ne_pas_melanger!=[]:
        paquet_combine=paquet_initiale.copy()
        num_cartes_combines=num_cartes_initiale.copy() 

        # Initialisation des index pour chaque paquet:
        index_paquet_combine=0
        index_paquet_melanger=0

        while index_paquet_melanger<nb_de_cartes and index_paquet_combine<nb_de_cartes:
            for carte in paquet_combine:
                if carte in nom_carte_a_ne_pas_melanger:
                    pass
                else:
                    # Trouver la prochaine carte mélangée qui ne doit pas 
                    # rester à sa position initiale:
                    while paquet_melanger[index_paquet_melanger] in \
                        nom_carte_a_ne_pas_melanger:
                        index_paquet_melanger+=1
                    else:
                        # Échanger les cartes dans le paquet combiné:
                        paquet_combine[index_paquet_combine]=\
                            paquet_melanger[index_paquet_melanger]
                        num_cartes_combines[index_paquet_combine]=\
                            index_cartes_melanger[index_paquet_melanger]
                        index_paquet_melanger+=1
                index_paquet_combine+=1

        # Mise à jour du paquet et de ses index associés:        
        nouveau_paquet=paquet_combine
        index_paquet=num_cartes_combines

    # S'il n'avait pas de cartes à ne pas mélanger:
    else: 
        nouveau_paquet=paquet_melanger
        index_paquet=index_cartes_melanger

    # Mise à jour de l'affichage:    
    affichage(nouveau_paquet,False)
    position_cartes_deplacables=options(index_paquet,nouveau_paquet)
    cartes_vertes(position_cartes_deplacables)

# La procédure recommencer() permet de réinitialiser tout les 
# variables nécessaires afin de que l'utilisateur puisse recommencer
# une nouvelle partie.
def recommencer():
    global nb_de_brasse, nouveau_paquet
    nb_de_brasse=3 # Réinitialisation du nombres de brasser permise
    nouveau_paquet=cartes # Réinitialisation de l'ordre des cartes
    init() 

# La procédure affichage prend en paramètre un tableau de chaînes de caractères
# représentant les noms des cartes mélangés et un nombre entier ou un booléen.
# Si le nombre entier est égale à 1, l'utilisateur a gagné, si le nombre entier
# est égale à 2, l'utilisateur a perdu et puis si le nombre entier est égale à 
# 3, l'utilisateur doit brasser. De plus, si le paramètre est égale ou booléen 
# False, c'est qu'on est dans aucunes de ces situations. Cette procédure permet
# l'affichage des cartes mélangés et des boutons dans le contenu HTML.
def affichage(nouvelle_liste_cartes,situation):
    global nb_de_brasse

    # Initialisation du contenu HTML 
    contenu_html = (
        "<style>"
        "  #jeu table { float:none; }"
        "  #jeu table td { border:0;padding:1px 2px;height:auto; width:auto; }"
        "  #jeu table td img { height:140px; }"
        "</style>" 
        "<div id='jeu'>"
        "  <table>"
    )

    # Construction du tableau de cartes mélangés:
    num_case = 0
    for _ in range(nb_rangee):
        contenu_html += "<tr>"
        for _ in range(nb_cartes_par_rangee):
            contenu_html += "<td id='case" + str(num_case) + \
                "' onclick='mise_a_jour(" + str(num_case) + ")'><img src=\
                    'cards/" + nouvelle_liste_cartes[num_case] + "'></td>"
            num_case += 1
        contenu_html += "</tr>" 
    contenu_html += "<table>" 

    # Affichage de messages et boutons en fonction de la situation:
    if not situation:
        # Affichage du bouton permettant de brasser s'il est encore possible 
        # de brasser:
        if nb_de_brasse>0:    
            contenu_html+="Vous pouvez encore <button onclick='brasser()'>\
                Brasser les cartes</button> "+str(nb_de_brasse)+" fois"
        else: 
            contenu_html+="Vous ne pouvez plus brasser les cartes"      
    elif situation == 1: # S'il a gagné
        contenu_html += "Vous avez réussi!  Bravo!"
    elif situation == 2: # S'il a perdu
        contenu_html+= "Vous n'avez pas réussi à placer toutes les \
            cartes... Essayez à nouveau!"
    elif situation == 3: #S'il est obligé de brasser
        contenu_html+="<button onclick='brasser()'>\
            Vous devez brasser.</button>"
    contenu_html += "</table>"
    # Bouton permettant de recommencer la partie
    contenu_html+="<button onclick='recommencer()'>Nouvelle partie</button>"

    racine = document.querySelector("#cb-body")
    racine.innerHTML = contenu_html

def init():
    # Tests unitaires:
    test_melanger()
    test_options()
    
    cartes_melangees,index_cartes_melangees = melanger(cartes)

    affichage(cartes_melangees,False)

    position_cartes_deplacables=\
        options(index_cartes_melangees,cartes_melangees)
    
    cartes_vertes(position_cartes_deplacables)

    

    

    
    
    




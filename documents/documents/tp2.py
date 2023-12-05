# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.
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
nb_de_brasse=3
def melanger(paquet): 
    global nouveau_paquet, index_paquet
    nouveau_paquet = paquet.copy()
    index_paquet=list(range(52))
    for i in range(51, 0, -1):
        index_aleatoire = randint(0, 51)
        
        # Échanger les cartes dans le paquet
        carte_temporaire = nouveau_paquet[i]
        nouveau_paquet[i] = nouveau_paquet[index_aleatoire]
        nouveau_paquet[index_aleatoire] = carte_temporaire

        # Échanger les index de ces cartes dans le paquet
        index_temporaire=index_paquet[i]
        index_paquet[i]= index_paquet[index_aleatoire] 
        index_paquet[index_aleatoire]=index_temporaire 
        
    return nouveau_paquet,index_paquet

def cartes_vertes(index_cartes):
    for carte in index_cartes:
        numero_case="#case"+str(carte)
        case=document.querySelector(numero_case)
        case.setAttribute("style", "background-color: lime")

def options(cartes,paquet_melange):
    global index_trous, cartes_avant_trous, cartes_deplacables , position_carte_deplacable, index_carte_avant_trous
    premiere_colonne=[0,13,26,39]
    derniere_colonne=[12,25,38,51]
    # Indentifier les trous 
    index_trous=[]
    index=0
    for carte in paquet_melange:
        if carte=="absent.svg":
            index_trous.append(index)
        index+=1

    # Identifier les index des cartes positionnées avant les trous 
    index_carte_avant_trous=list(map(lambda index_trou: index_trou-1, index_trous))
    index_carte_avant_trous = list(filter(lambda index: index>=0, index_carte_avant_trous)) 
    for index in derniere_colonne:
        while index in index_carte_avant_trous:
            index_carte_avant_trous.remove(index)
    

    # Identifier les cartes positionnées avant les trous
    cartes_avant_trous= []
    for i in index_carte_avant_trous:
        carte=cartes[i]
        cartes_avant_trous.append(carte)

    # Identifier les cartes déplaçables
 
    cartes_deplacables=[]
    for carte_avant in cartes_avant_trous:
        for carte in cartes:
            if carte%4==carte_avant%4 and carte//4==(carte_avant//4)+1 and carte<48:
                cartes_deplacables.append(carte)                      
    for i in index_trous:
        if i in premiere_colonne: # S'il y a un trou dans la première colonne
            for carte in range(4): cartes_deplacables.append(carte) # Ajouter tous les carte de valeur "2"
          

    # Identifier les positions des cartes déplaçables 
    position_carte_deplacable=[]
    for index_carte in range(52):
        carte=cartes[index_carte]
        if carte in cartes_deplacables:
            position_carte_deplacable.append(index_carte)


    return position_carte_deplacable

def intervertir(position,index_trou):
    nouveau_paquet[index_trou] = nouveau_paquet[position]
    nouveau_paquet[position] = 'absent.svg'

    temporaire = index_paquet[index_trou]
    index_paquet[index_trou] = index_paquet[position]
    index_paquet[position] = temporaire


def mise_a_jour(position):
   
    # On determine l'index de la carte clique selon sa position dans le paquet mélangé:
    index_carte_clique = index_paquet[position]
    #On vérifie si la carte cliqué peut etre déplacer:
    if position in position_carte_deplacable:
        for carte in cartes_avant_trous:
            if index_carte_clique//4 == (carte//4)+1 and index_carte_clique%4==carte%4: 
                # On determine quel est l'index du trou associe a la carte:
                index_carte = cartes_avant_trous.index(carte)
                index_trou_associe = index_carte_avant_trous[index_carte] + 1
                # On interverti la carte avec le trou  # et met a jour les paquets de cartes et d'indexs:      
                intervertir(position,index_trou_associe)

        if index_carte_clique in [0,1,2,3]: # C'est un deux
            for trou in index_trous:
                if trou in [0,13,26,39]: # On identifie dans quel ligne de la premiere colonne est le(s) trou.
                    intervertir(position,trou)
            
        # Mise a jour du jeux selon l'action éffectué par l'utilisateur:
        affichage(nouveau_paquet)
        position_cartes_deplacables=options(index_paquet,nouveau_paquet)
        cartes_vertes(position_cartes_deplacables)
    else:
        pass

def brasser():
    global nouveau_paquet, index_paquet, nb_de_brasse
    nb_de_brasse-=1
    paquet=nouveau_paquet.copy()
    num_cartes=index_paquet.copy()
    positions_carte_a_ne_pas_melanger=[]
    num_cartes_a_ne_pas_melanger=[]
    nb_rangee=4
    for rangee in range(nb_rangee):
        index_premiere_carte=rangee*13
        premiere_carte=num_cartes[index_premiere_carte]
        if premiere_carte in [0,1,2,3]: # Si la premiere carte de la rangée est un deux
            positions_carte_a_ne_pas_melanger.append(index_premiere_carte)
            num_cartes_a_ne_pas_melanger.append(premiere_carte)
            compteur=1 # Initialisation du compteur
            while compteur<13:
                index_carte_actuelle=index_premiere_carte+compteur
                carte_actuelle=num_cartes[index_carte_actuelle]
                carte_avant=num_cartes[index_carte_actuelle-1]
                if carte_avant%4==carte_actuelle%4==num_cartes[index_premiere_carte]%4 and carte_avant//4==(carte_actuelle//4)-1:
                    positions_carte_a_ne_pas_melanger.append(index_carte_actuelle)
                    num_cartes_a_ne_pas_melanger.append(carte_actuelle)
                else:
                    break
                compteur+=1

    nom_carte_a_ne_pas_melanger=[]
    for position in positions_carte_a_ne_pas_melanger:
        nom_carte=paquet[position]
        nom_carte_a_ne_pas_melanger.append(nom_carte)

    nom_cartes_melanger,index_cartes_melanger=melanger(cartes)
    if num_cartes_a_ne_pas_melanger!=[]:
        i=0
        n=0
        while i<52 and n<52:
            for carte in paquet:
                if carte in nom_carte_a_ne_pas_melanger:
                    pass
                else:
                    while nom_cartes_melanger[n] in nom_carte_a_ne_pas_melanger:
                        n+=1
                    else:
                        paquet[i]=nom_cartes_melanger[n]
                        num_cartes[i]=index_cartes_melanger[n]
                        n+=1
                i+=1
    else:
        paquet=nom_cartes_melanger
        num_cartes=index_cartes_melanger
    nouveau_paquet=paquet
    index_paquet=num_cartes
    affichage(nouveau_paquet)
    position_cartes_deplacables=options(index_paquet,nouveau_paquet)
    # Cartes vertes:
    cartes_vertes(position_cartes_deplacables)

def recommencer():
    global nb_de_brasse, nouveau_paquet
    nb_de_brasse=3
    nouveau_paquet=cartes
    init()


def affichage(nouvelle_liste_cartes):
    global nb_de_brasse
    contenu_html = (
        "<style>"
        "  #jeu table { float:none; }"
        "  #jeu table td { border:0; padding:1px 2px; height:auto; width:auto; }"
        "  #jeu table td img { height:140px; }"
        "</style>" 
        "<div id='jeu'>"
        "  <table>"
    )

    index = 0
    for i in range(4):
        contenu_html += "<tr>"
        for j in range(13):
            contenu_html += "<td id='case" + str(index) + "' onclick='mise_a_jour(" + str(index) + ")'><img src='cards/" + nouvelle_liste_cartes[index] + "'></td>"
            index += 1
        contenu_html += "</tr>" 
    contenu_html += "<table>"    
    while nb_de_brasse>0:    
        contenu_html += "Vous pouvez encore <button onclick='brasser()'>Brasser les cartes</button> "+str(nb_de_brasse)+" fois"
        break 
    else: 
        contenu_html+="Vous ne pouvez plus brasser les cartes"
    contenu_html += "</table>"
    contenu_html+="<button onclick='recommencer()'>Nouvelle partie</button>"


    racine = document.querySelector("#cb-body")
    racine.innerHTML = contenu_html

def init():

    cartes_melangees,index_cartes_melangees = melanger(cartes)

    affichage(cartes_melangees)

    position_cartes_deplacables=options(index_cartes_melangees,cartes_melangees)
    
    # Cartes vertes:
    cartes_vertes(position_cartes_deplacables)
    
    




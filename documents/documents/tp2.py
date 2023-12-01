# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

def melanger(paquet): 
    nouveau_paquet = paquet.copy()
    index_melanges=list(range(52))
    for i in range(51, 0, -1):
        index_aleatoire = randint(0, 51)
        carte_temporaire = nouveau_paquet[i]
        index_temporaire=index_melanges[i]
        nouveau_paquet[i] = nouveau_paquet[index_aleatoire]
        nouveau_paquet[index_aleatoire] = carte_temporaire
        index_melanges[i]= index_melanges[index_aleatoire] 
        index_melanges[index_aleatoire]=index_temporaire 
    return nouveau_paquet,index_melanges

def options(cartes,paquet_melange):
    index_trous=[]
    index=0
    for carte in paquet_melange:
        if carte=="empty.svg":
            index_trous.append(index)
        index+=1
    index_carte_avant_trous=list(map(lambda index_trou: index_trou-1, index_trous))
    index_carte_avant_trous = list(filter(lambda index: index>=0, index_carte_avant_trous))
    cartes_avant_trous= []
    for i in index_carte_avant_trous:
        if cartes[i]<48:
            cartes_avant_trous.append(cartes[i])
    cartes_deplacables=[]
    for carte_avant in cartes_avant_trous:
        for carte in cartes:
            if carte%4==carte_avant%4 and carte//4==(carte_avant//4)+1 and carte<48:
                cartes_deplacables.append(carte)
    for i_trou in index_trous:
        if i_trou==0 or i_trou==13 or i_trou==26 or i_trou==39:
            for x in range(4): cartes_deplacables.append(x)
    index_carte_deplacable=[]
    for carte in cartes_deplacables:
        for i in range(51):
            if carte==cartes[i]:
                index_carte_deplacable.append(i)
    return index_carte_deplacable



 
def init():
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
        "empty.svg", "empty.svg", "empty.svg", "empty.svg"
        ]
  

    cartes_melangees,index_cartes_melangees = melanger(cartes)

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
            contenu_html += "<td id='case" + str(index) + "'><img src='cards/" + cartes_melangees[index] + "'></td>"
            index += 1
        contenu_html += "</tr>"


    racine = document.querySelector("#cb-body")
    racine.innerHTML = contenu_html

    cartes_jouables=options(index_cartes_melangees,cartes_melangees)
    for carte in cartes_jouables:
        numero_case="#case"+str(carte)
        case=document.querySelector(numero_case)
        case.setAttribute("style", "background-color: lime")



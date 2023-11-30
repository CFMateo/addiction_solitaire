# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

def melanger(paquet):
    nouveau_paquet = paquet.copy()
    for i in range(51, 0, -1):
        index_aleatoire = randint(0, 51)
        temporaire = nouveau_paquet[i]

        nouveau_paquet[i] = nouveau_paquet[index_aleatoire]
        nouveau_paquet[index_aleatoire] = temporaire
    return nouveau_paquet

def lala():
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

    cartes_melangees = melanger(cartes)
    

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


    case0 = document.querySelector("#case0")
    case0.setAttribute("style", "background-color: lime")

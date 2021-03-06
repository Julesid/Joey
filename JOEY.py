from tkinter import *



# Quand on appuie sur une touche, on l'ajoute à la liste
def enfoncee(evt) :
    T = evt.keysym.upper() # En majuscule pour confondre 'a' et 'A'
    if  T not in Touches :
        Touches.append(T)

# Quand on relache la touche, on la retire
def relachee(evt) :
    T = evt.keysym.upper()
    if T in Touches :
        Touches.remove(T)

# Boucle principale :
def animation() :
    global XS, YS
    NomFichier = 'sourisFICHIERD0'
    Xavant, Yavant = XS, YS
    if "UP" in Touches :
        # On regarde si on se situe sur une échelle :
        if Decors[YS//40][XS//40] == 'H' :
            YS = YS - 8
            NomFichier = 'sourisFICHIERM0'
    if "DOWN" in Touches :
        # On regarde si on a une échelle sous les pieds ( La souris mesure
        # 40 pixels de haut, on regarde donc à YS + 19 + 8
        if Decors[(YS+27)//40][XS//40] == 'H' :
            YS = YS + 8
            NomFichier = 'sourisFICHIERM0'
    if "LEFT" in Touches :
        # On regarde ce qu'il y a au pied gauche de la souris : La souris fait
        # 30 pixels de large et 40 pixels de haut, on regarde donc la case qui
        # se situe à (XS - 15 - 8 , YS + 19)
        if Decors[(YS+19)//40][(XS-23)//40] in (' ','P','H') :
            XS = XS - 8
            NomFichier = 'sourisFICHIERG0'
    if "RIGHT" in Touches :
        # Idem à droite
        if Decors[(YS+19)//40][(XS+23)//40] in (' ','P','H') :
            XS = XS + 8
            NomFichier = 'sourisFICHIERD0'
    # On regarde si on tombe :
    if Decors[(YS+20)//40][(XS)//40] in (' ','P') :
        YS = YS + 8
        NomFichier = 'sourisFICHIERT0'
    #on modifie les coordonnées  et l'image de la souris
    Fond.itemconfigure(souris, image=eval(NomFichier))
    Fond.coords(souris, XS, YS)

    # on relance la fonction animation après 4ms ce qui permet de continuer les animations
    #même si aucune  touche n'est enfoncée!!
    fenetre.after(40,animation)




def lisDecors(fichier):
    """
    Fonction qui lis le contenu du fichier fichier et la place dans
    la liste 2D Decors
    """
    filin = open(fichier,'r')
    R = [list(line.replace('\n','')) for line in filin]
    filin.close()
    return R

def dessine():
    """
    Fonction qui dessine le plateau de jeu avec les données de la liste Decors
    """
    global XS, YS, XC, YC
    ligne, colonne = 0, 0
    while ligne < 17 :
      if Decors[ligne][colonne] == 'X' :
        Fond.create_image(colonne*40, ligne*40, image=X, anchor=NW)
      if Decors[ligne][colonne] == 'T' :
        Fond.create_image(colonne*40, ligne*40, image=T, anchor=NW)
      if Decors[ligne][colonne] == 'H' :
        Fond.create_image(colonne*40, ligne*40, image=H, anchor=NW)
      if Decors[ligne][colonne]=='P' :
        Fond.create_image(colonne*40, ligne*40, image=P, anchor=NW)
      if Decors[ligne][colonne] == 'S' :    # Si on a une souris dans le décors
        XS, YS = colonne*40+20, ligne*40+20 # On initialise les coordonnées
        Decors[ligne][colonne] = ' '        # On l'efface du décors
      if Decors[ligne][colonne] == 'C' :
        XC, YC = colonne*40+20, ligne*40+20
        Decors[ligne][colonne] = ' '
      colonne=colonne+1
      if colonne == 25 :
        colonne = 0
        ligne = ligne + 1


fenetre=Tk()
fenetre.resizable(width=False, height=False)

fenetre.title("Joe & Joey")
fenetre.geometry("1200x680")

# Chargement des fichiers :
T=PhotoImage(file="images/FondS.gif")
H=PhotoImage(file="images/FondH.gif")
X=PhotoImage(file="images/FondX.gif")
P=PhotoImage(file="images/pancake.gif")

# Dessin de l'interface
Fond=Canvas(fenetre,width=1200,height=680,bg="#C0C0FF")
Fond.place(x=0,y=0)
Fond.create_rectangle(1000,0,1200,680,fill="grey",width=5,outline="white")
Fond.create_image(1100,225,image=P)
Txt=Fond.create_text(1100,275,text="0 cupcake sur 5",font=("comic sans ms","15"),fill="#5736A6")

# Informations sur la souris :
sourisFICHIERG0=PhotoImage(file="images/sourisG0.gif") #fichier de la souris gauche position 0
sourisFICHIERD0=PhotoImage(file="images/sourisD0.gif") #fichier de la souris droite position 0
sourisFICHIERG1=PhotoImage(file="images/sourisG1.gif") #fichier de la souris gauche position 1
sourisFICHIERD1=PhotoImage(file="images/sourisD1.gif") #fichier de la souris droite position 1
sourisFICHIERM0=PhotoImage(file="images/sourisM0.gif") #fichier de la souris monte position 1
sourisFICHIERM1=PhotoImage(file="images/sourisM1.gif") #fichier de la souris monte position 1
sourisFICHIERT0=PhotoImage(file="images/sourisT0.gif") #fichier du souris qui tombe
sourisFICHIERT1=PhotoImage(file="images/sourisT1.gif") #fichier du souris qui tombe
XS, YS = 0, 0   # Position


# Informations sur le chat :
chatFICHIERG0=PhotoImage(file="images/chatG0.gif") #fichier du chat gauche position 0
chatFICHIERD0=PhotoImage(file="images/chatD0.gif") #fichier du chat droite position 0
chatFICHIERG1=PhotoImage(file="images/chatG1.gif") #fichier du chat gauche position 1
chatFICHIERD1=PhotoImage(file="images/chatD1.gif") #fichier du chat droite position 1
chatFICHIERM0=PhotoImage(file="images/chatM0.gif") #fichier du chat monte position 1
chatFICHIERM1=PhotoImage(file="images/chatM1.gif") #fichier du chat monte position 1
chatFICHIERT0=PhotoImage(file="images/chatT0.gif") #fichier du chat qui tombe
chatFICHIERT1=PhotoImage(file="images/chatT1.gif") #fichier du chat qui tombe
XC, YC = 0, 0   # Position


# On lis le décors. On garde les informations du décors dans une liste pour
# pouvoir tester si on tombe, si on peut monter, ....
Decors = lisDecors('niveaux/niv1.txt')
dessine()

souris=Fond.create_image(XS, YS, image=sourisFICHIERG0)
chat=Fond.create_image(XC, YC, image=chatFICHIERG0)


# Surveillance des touches
Touches = []
fenetre.bind_all("<KeyPress>",enfoncee)
fenetre.bind_all("<KeyRelease>",relachee)

animation()

fenetre.mainloop()

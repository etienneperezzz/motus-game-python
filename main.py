from tkinter import *
from tkinter.messagebox import *
import motus

# COULEUR
BLEU = "#0000FF"
BLEUPALE = "#C0DFEF"
# DIMENSION
w = 800  # width for the Tk root
h = 650  # height for the Tk root

global compteur
compteur = 0


def creationFenetre():
    global jeuMotus
    jeuMotus = Tk()
    jeuMotus.title("Accueil Motus")
    ws = jeuMotus.winfo_screenwidth()  # width of the screen
    hs = jeuMotus.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    jeuMotus.configure(bg=BLEUPALE)
    jeuMotus.geometry("%dx%d+%d+%d" % (w, h, x, y))
    jeuMotus.maxsize(1500, 800)
    jeuMotus.minsize(300, 400)
    creationWidgetPageAccueil(jeuMotus)
    jeuMotus.mainloop()


def creationWidgetPageAccueil(jeuMotus):
    # Texte
    txtRegle = Label(jeuMotus, font=(None, 12),
                     text="But du jeu du Motus : Retrouver un mot de 4 à 7 lettres en un minimum de coups !")
    txtRegle.pack(pady=20)
    # txtRegle.grid(row=8, column=5, columnspan=2, pady=10, padx=20, sticky=E + W)

    # Spinbox
    global spinChoixLettre, choix
    choix = ["Mot en 4 lettres", "Mot en 5 lettres", "Mot en 6 lettres", "Mot en 7 lettres"]
    spinChoixLettre = Spinbox(jeuMotus, values=choix, command=choixMot, width=30, justify=CENTER)
    spinChoixLettre.pack(pady=10)

    # Boutons
    btnCommencer = Button(jeuMotus, font=(None, 12), text="Commencer", command=lambda: commencerJeu())
    btnCommencer.pack()
    # spinChoixLettre.grid(row=10, column=5, columnspan=2, pady=10, padx=20, sticky=E + W)


def commencerJeu():
    global jeuMotus, jeuCommence
    jeuCommence = Toplevel(jeuMotus)
    jeuMotus.withdraw()
    jeuCommence.title("Jeu Motus")
    '''ws = jeuCommence.winfo_screenwidth()  # width of the screen
    hs = jeuCommence.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)'''
    jeuCommence.configure(bg=BLEUPALE)
    jeuCommence.maxsize(1500, 800)
    jeuCommence.minsize(300, 400)
    creationWidgetPageJeu(jeuCommence, choixMot())
    jeuCommence.mainloop()


def je_clique(event):
    global compteur
    compteur += 1
    print(compteur)


def verifMot(entreeMot, motAleatoire):
    print(motAleatoire)
    global motEntree, compteur
    motEntree = entreeMot.get().upper()
    if len(motEntree) != len(motAleatoire):
        showwarning("formatNonConforme", f"Entrez un mot de {len(motAleatoire)} lettres.")
    else:
        for i in range(7):
            for j in range(len(motAleatoire)):
                if (motEntree == motAleatoire):
                    a = Label(jeuCommence, text=motEntree[j], bg="green", width=len(motAleatoire) + 4, height=2,
                              font=(None, 20),
                              foreground='#FFF')
                    a.grid(row=compteur - 1, column=j, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=1, pady=1)

                else:
                    if (motAleatoire[j] == motEntree[j]):
                        c = Label(jeuCommence, text=motEntree[j], bg="green", width=len(motAleatoire) + 4, height=2,
                                  font=(None, 20),
                                  foreground='#FFF')
                        c.grid(row=compteur - 1, column=j, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=1,
                               pady=1)
                        g = Label(jeuCommence, text=motEntree[j], bg="green", width=len(motAleatoire) + 4, height=2,
                                  font=(None, 20),
                                  foreground='#FFF')
                        g.grid(row=compteur, column=j, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=1,
                               pady=1)
                    elif (motEntree[j] in motAleatoire and motEntree[j] != motAleatoire[j]):
                        b = Label(jeuCommence, text=motEntree[j], bg="orange", width=len(motAleatoire) + 4,
                                  height=2,
                                  font=(None, 20),
                                  foreground='#FFF')
                        b.grid(row=compteur - 1, column=j, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=1,
                               pady=1)
                    elif (motEntree[j] not in motAleatoire):
                        d = Label(jeuCommence, text=motEntree[j], bg="red", width=len(motAleatoire) + 4, height=2,
                                  font=(None, 20),
                                  foreground='#FFF')
                        d.grid(row=compteur - 1, column=j, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=1,
                               pady=1)
        entreeMot.delete(0, len(entreeMot.get()))



def creationWidgetPageJeu(jeuCommence, motAleatoire):
    global e, btnValider, entreeMot
    for i in range(7):
        for j in range(len(motAleatoire)):
            if (j == 0 and len(motAleatoire) < 6):
                f = Label(jeuCommence, text=motAleatoire[j], bg="blue", width=len(motAleatoire) + 4, height=2,
                          font=(None, 20),
                          foreground='#FFF')
                f.grid(row=i, column=j, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=2, pady=1)
            elif ((len(motAleatoire) >= 6) and (j == 0)):
                h = Label(jeuCommence, text=motAleatoire[j], bg="blue", width=len(motAleatoire) + 4, height=2,
                          font=(None, 20),
                          foreground='#FFF')
                h.grid(row=i, column=j, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=2, pady=1)
                l = Label(jeuCommence, text=motAleatoire[j + 3], bg="blue", width=len(motAleatoire) + 4, height=2,
                          font=(None, 20),
                          foreground='#FFF')
                l.grid(row=i, column=j + 3, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=2, pady=1)
            else:
                e = Label(jeuCommence, text=".", bg="blue", width=len(motAleatoire) + 4, height=2, font=(None, 20),
                          foreground='#FFF')
                e.grid(row=i, column=j, columnspan=1, sticky=E + W, ipadx=15, ipady=10, padx=2, pady=1)

    # ENTREE UTILISATEUR
    entreeMot = Entry(jeuCommence, font=(None, 20), width=len(motAleatoire) * (len(motAleatoire) + 4))
    entreeMot.grid(row=9, column=0, columnspan=len(motAleatoire) - 1, pady=10, padx=10)

    # BOUTON VALIDER
    btnValider = Button(jeuCommence, font=(None, 20), text="Valider", command=lambda: verifMot(entreeMot, motAleatoire))
    btnValider.grid(row=9, column=len(motAleatoire) - 1, pady=1, padx=2)
    btnValider.bind("<Button-1>", je_clique)
    # BOUTON RETOUR MENU
    btnRetourMenu = Button(jeuCommence, font=(None, 20), text="Menu", command=lambda: showAccueil())
    btnRetourMenu.grid(row=10, column=len(motAleatoire) - 1, pady=1, padx=2)


def showAccueil():
    global compteur
    jeuMotus.deiconify()
    jeuCommence.destroy()
    compteur = 0


def victoire():
    showinfo("victoire", f"Bravo vous avez trouvé le mot en {compteur} essais!")


def choixMot():
    global motAleatoire
    motAleatoire = ""
    nbreLettre = spinChoixLettre.get()
    if nbreLettre == choix[0]:
        motAleatoire = motus.choisirMot4Lettres()
    elif nbreLettre == choix[1]:
        motAleatoire = motus.choisirMot5Lettres()
    elif nbreLettre == choix[2]:
        motAleatoire = motus.choisirMot6Lettres()
    elif nbreLettre == choix[3]:
        motAleatoire = motus.choisirMot7Lettres()
    return motAleatoire


if __name__ == "__main__":
    creationFenetre()

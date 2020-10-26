from tkinter import filedialog
from tkinter import *
import os

root = Tk()
root.title("ZipLogGui")
root.geometry("580x300")


class Principale:
    """Classe principale de l'interface graphipe"""

    def __init__(self, master, entree, sortie, taille, doctype, config):
        """

        :param master:  root tkinter
        :param entree:  dossier source
        :param sortie:  dossier cible
        :param taille:  seuil de sélection des fichiers à traiter
        :param doctype: extension des fichiers à traiter
        :param config:  oui/non mode autonome sans GUI
        """
        # Déclaration des variables
        self.maframe = Frame(master)
        self.maframe.grid()
        self.entree = entree
        self.entree2 = self.entree
        self.sortie = sortie
        self.sortie2 = self.sortie
        self.taille = taille
        self.doctype = doctype
        self.var = StringVar()
        self.var.set(config)
        self.config = config
        self.entree2 = ""
        self.valeur = ""
        self.param = ""
        self.liste_valeur = ["CONFIGURATION ACTUELLE : ", self.entree, self.sortie, self.taille,
                             self.doctype, self.config]
        self.liste_param = ["", "Source: ", "Cible: ", "Taille en Mo: ", "Extension: ", "Exécution automatique: "]
        self.colorfg = "white"
        self.colorbg = "grey"
        self.tour = 0
        self.valide = "oui"
        self.c1 = True  # Condition 1
        self.c2 = True  # Condition 2
        self.c3 = True  # Condition 3

        # Constuction de l'interface
        self.label_source = Label(master, text="Dossier source :")
        self.label_source.grid(row=0, column=0, sticky="w")
        self.entry_in = Entry(master, width=60)
        self.entry_in.grid(row=0, column=1,)
        self.entry_in.insert(0, self.entree)
        self.btsrcdir = Button(master, text="Parcourir", command=self.opendir_in)
        self.btsrcdir.grid(row=0, column=2)
        self.label_cible = Label(master, text="Dossier cible :")
        self.label_cible.grid(row=1, column=0, sticky="w")
        self.entry_out = Entry(master, width=60)
        self.entry_out.grid(row=1, column=1)
        self.entry_out.insert(0, self.sortie)
        self.btcibdir = Button(master, text="Parcourir", height=1, command=self.opendir_out)
        self.btcibdir.grid(row=1, column=2)
        self.label_seuil = Label(master, text="Taille en Mo :")
        self.label_seuil.grid(row=3, column=0, sticky="w")
        self.entry_seuil = Entry(master, width=4)
        self.entry_seuil.grid(row=3, column=1, sticky="w")
        self.entry_seuil.insert(0, self.taille)
        self.label_doctype = Label(master, text="Extension des fichiers :")
        self.label_doctype.grid(row=4, column=0, sticky="w")
        self.entry_doctype = Entry(master, width=4)
        self.entry_doctype.grid(row=4, column=1, sticky="w")
        self.entry_doctype.insert(0, self.doctype)
        self.label_sauv = Label(master, text="Exécution automatique :")
        self.label_sauv.grid(row=5, column=0, sticky="w")
        self.sauv_config = Checkbutton(master, variable=self.var, offvalue="non", onvalue="oui")
        self.sauv_config.grid(row=5, column=1, sticky="w")
        self.bouton_valide = Button(master, text="Appliquer", bd=4, activebackground="green",
                                    bg="white", command=self.get_entry_in)
        self.bouton_valide.grid(row=5, column=2, sticky="e")
        self.bouton_maj = Button(master, text="modifier", bd=4, activebackground="green",
                                 bg="white", command=self.mise_a_jour)

        self.bouton_annule = Button(master, text="Annuler", bd=4, activebackground="red",
                                    command=self.annuler)
        self.bouton_annule.grid(row=5, column=1, sticky="e")
        self.bouton_applique = Button(master, text="Exécuter", bd=4, activebackground="green",
                                      bg="white", command=lambda: self.maframe.quit())
        self.label_result_param = Label(master, text=self.param)
        self.label_titre_result = Label(master, text="")
        self.text_result_valeur = Text(root, height=1, width=45, bg='grey', fg=self.colorfg)
        self.state = DISABLED
        root.protocol("WM_DELETE_WINDOW", self.annuler)  # Interrompt l'exécution si fenetre fermée avec X

    def annuler(self):
        self.maframe.quit()
        self.valide = "non"

    def opendir_in(self):
        """
        :return: la variable entree(dossier source) est retournée par filedialog.askdirectory
        """
        self.entree2 = filedialog.askdirectory()
        self.entree = self.entry_in.delete(0, END)
        self.entree = self.entry_in.insert(0, self.entree2)

    def opendir_out(self):
        """

        :return: la variable sortie(dossier cible) est retournée par filedialog.askdirectory
        """
        self.sortie2 = filedialog.askdirectory()
        self.sortie = self.entry_out.delete(0, END)
        self.sortie = self.entry_out.insert(0, self.sortie2)

    def get_entry_in(self):
        """

        :return: retourne les varibales des widgets de saisie
        """

        self.entree = self.entry_in.get()
        self.sortie = self.entry_out.get()
        self.taille = self.entry_seuil.get()
        self.doctype = self.entry_doctype.get()
        self.config = self.var.get()
        self.maj_liste()
        self.affiche_resutlat()
        self.tour += 1
        self.state = NORMAL

    def maj_liste(self):
        """

        :return: Une liste contenant les valeurs de : entree, sortie, taille, doctype et config
        """
        self.param = [self.entree, self.sortie, self.taille, self.doctype, self.config]
        self.liste_valeur[1] = self.entree
        self.liste_valeur[2] = self.sortie
        self.liste_valeur[3] = self.taille
        self.liste_valeur[4] = self.doctype
        self.liste_valeur[5] = self.config
        if self.tour > 0:
            self.liste_valeur[0] = "CONFIGURATION VALIDE"  # Change le titre de l'affichage après une validation

    def validation(self):
        """
        Execute un test des entrées et change l'affichage en conséquences
        :return: valeurs boolennes de validation des conditions des entrées
        """
        if not self.taille.isdigit() or int(self.taille) < 1:  # vérifie que la taille est un entier > 0
            self.liste_valeur[0] = "ERREUR DANS LA CONFIGURATION"
            self.colorfg = "white"
            self.colorbg = "#630505"
            self.liste_valeur[3] = "==> ENTREZ UN ENTIER > 0 <=="
            self.bouton_applique.config(bg="#0d6305", state="disabled", fg="white")
            self.c1 = False

        if not os.path.exists(self.entree):  # vérifie que le dossier source existe
            self.liste_valeur[0] = "ERREUR DANS LA CONFIGURATION"
            self.colorfg = "white"
            self.colorbg = "#630505"
            self.liste_valeur[1] = "==> DOSSIER INVALIDE OU INEXISTANT <=="
            self.bouton_applique.config(bg="#0d6305", state="disabled", fg="white")
            self.c2 = False

        if not os.path.exists(self.sortie):  # vérifie que le dossier cible existe
            self.liste_valeur[0] = "ERREUR DANS LA CONFIGURATION"
            self.colorfg = "white"
            self.colorbg = "#630505"
            self.liste_valeur[2] = "==> DOSSIER INVALIDE OU INEXISTANT <=="
            self.bouton_applique.config(bg="#0d6305", state="disabled", fg="white")
            self.c3 = False

        if self.liste_valeur[5] == "oui":
            self.colorfg = "white"
            self.liste_valeur[5] = " OUI = MODE AUTONOME"
            self.colorbg = "#42a7f5"
            self.bouton_applique.config(bg="#0d6305", state="normal", fg="white")
            if not self.c1 or not self.c2 or not self.c3:  # vérifie que les 3 conditions précédentes sont vraies
                print("au moins un parametre est invalie")
                self.colorfg = "white"
                self.colorbg = "#630505"
                self.bouton_applique.config(bg="#0d6305", state="disabled", fg="white")
            else:
                self.bouton_applique.config(bg="#0d6305", state="normal", fg="white")

    def affiche_resutlat(self):
        """

        :return: Affiche le résultat de la configuration
        """
        self.validation()
        i = 8
        y = 8
        for self.valeur in self.liste_valeur:
            self.text_result_valeur = Text(root, height=1, width=45, bg=self.colorbg, fg=self.colorfg)
            self.text_result_valeur.insert(INSERT, self.valeur)
            self.text_result_valeur.configure(state=DISABLED)
            self.text_result_valeur.grid(row=i, column=1, sticky="w")
            self.text_result_valeur.config(bg=self.colorbg)
            i += 1

        for self.param in self.liste_param:
            self.label_result_param = Label(root, text=self.param)
            self.label_result_param.grid_remove()
            self.label_result_param.grid(row=y, column=0, sticky="w")
            y += 1

        self.bouton_valide.destroy()
        self.bouton_maj.grid(row=5, column=2, sticky="e")
        self.bouton_applique.grid(row=15, column=2, sticky="e")
        self.label_titre_result.grid(row=7, columnspan=3)

    def mise_a_jour(self):
        """

        :return:    self.entree, self.sortie, self.taille, self.doctype, self.config par une méthode get
        """

        self.entree = self.entry_in.get()
        self.entry_in.delete(0, END)
        self.entry_in.insert(0, self.entree)

        self.sortie = self.entry_out.get()
        self.entry_out.delete(0, END)
        self.entry_out.insert(0, self.sortie)

        self.taille = self.entry_seuil.get()
        self.entry_seuil.delete(0, END)
        self.entry_seuil.insert(0, self.taille)

        self.doctype = self.entry_doctype.get()
        self.entry_doctype.delete(0, END)
        self.entry_doctype.insert(0, self.doctype)

        self.config = self.var.get()

        self.maj_liste()
        self.colorfg = "white"
        self.colorbg = "grey"
        self.bouton_applique.config(bg="#0d6305", state="normal", fg="white")
        self.c1 = True
        self.c2 = True
        self.c3 = True

        self.affiche_resutlat()

from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("ZipLogGui")
root.geometry("580x300")

# t = Principale(root, "l'entréé", "la sortie", 10, "log", "oui")


class Principale:
    def __init__(self, master, entree, sortie, taille, doctype, config):
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
        self.entree2 = "testentree2"
        self.valeur = "------------------------"
        self.param = ""
        self.liste_valeur = ["CONFIGURATION ACTUELLE : ", self.entree, self.sortie, self.taille
            , self.doctype, self.config]
        self.liste_param = ["", "Dossier Source: ", "Dossier Cible: ", "Taille en Mo: ", "Extension: "
            , "Sauvegarde Config: "]
        self.color = "white"

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
        self.label_sauv = Label(master, text="Sauver la configuration :")
        self.label_sauv.grid(row=5, column=0, sticky="w")
        self.sauv_config = Checkbutton(master, variable=self.var, offvalue="non", onvalue="oui")
        self.sauv_config.grid(row=5, column=1, sticky="w")
        self.bouton_valide = Button(master, text="Valider", bd=4, activebackground="green"
                                    , bg="white", command=self.get_entry_in)
        self.bouton_valide.grid(row=5, column=2, sticky="e")
        self.bouton_maj = Button(master, text="modifier", bd=4, activebackground="green"
                                    , bg="white", command=self.mise_a_jour)

        self.bouton_annule = Button(master, text="Annuler", bd=4, activebackground="red"
                                    , command=lambda: self.maframe.quit())
        self.bouton_annule.grid(row=5, column=1, sticky="e")
        self.bouton_applique = Button(master, text="Appliquer", bd=4, activebackground="green"
                                    , command=lambda: self.maframe.quit())
        self.label_result_valeur = Label(master, text=self.valeur)
        self.label_result_param = Label(master, text=self.param)
        self.label_titre_result = Label(master, text="")
        self.state = DISABLED

    def opendir_in(self):
        self.entree2 = filedialog.askdirectory()
        self.entree = self.entry_in.delete(0, END)
        self.entree = self.entry_in.insert(0, self.entree2)

    def opendir_out(self):
        self.sortie2 = filedialog.askdirectory()
        self.sortie = self.entry_out.delete(0, END)
        self.sortie = self.entry_out.insert(0, self.sortie2)

    def get_entry_in(self):

        self.entree = self.entry_in.get()
        self.sortie = self.entry_out.get()
        self.taille = self.entry_seuil.get()
        self.doctype = self.entry_doctype.get()
        self.config = self.var.get()
        self.maj_liste()
        self.affiche_resutlat()
        self.state = NORMAL
        # self.maframe.quit()

    def maj_liste(self):
        self.liste_valeur[1] = self.entree
        self.liste_valeur[2] = self.sortie
        self.liste_valeur[3] = self.taille
        self.liste_valeur[4] = self.doctype
        self.liste_valeur[5] = self.config

    def affiche_resutlat(self):
        i = 8
        y = 8

        for self.valeur in self.liste_valeur:

            self.label_result_valeur = Text(root, height=1, width=45, bg='grey', fg=self.color)
            self.label_result_valeur.insert(INSERT, self.valeur)
            self.label_result_valeur.configure(state=DISABLED)
            self.label_result_valeur.grid(row=i, column=1, sticky="w")
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

    def etat_entrees(self):
        pass

    def mise_a_jour(self):

        self.state = NORMAL

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

        self.affiche_resutlat()

# t = Principale(root, "l'entréé", "la sortie", 10, "log", "non")

# root.mainloop()
# root.destroy()


# print("entree= " + t.entree, "sortie= " + t.sortie, "taille= "+str(t.taille), "Extension= "
#       + t.doctype, "config= "+t.config)

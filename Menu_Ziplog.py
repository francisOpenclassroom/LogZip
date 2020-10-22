import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sys
import os



class Application(tk.Tk):
    def __init__(self,entree,sortie,seuil,doctype):
        tk.Tk.__init__(self)


        self.entree = entree
        self.entree2 = "entree2"
        self.sortie = sortie
        self.sortie2 = "Sortie2"
        self.seuil = seuil
        self.doctype = doctype
        self.checked =""
        self.creer_widgets()




    def config_hs(self):
        print("Fichier de configuration invalide",self.entree)





    def opendir_in(self):
        self.entree2 = filedialog.askdirectory()
        self.entry_in.delete(0,256)
        self.entree = self.entry_in.insert(0, self.entree2)

    def opendir_out(self):
        self.sortie2 = filedialog.askdirectory()
        self.entry_out.delete(0,256)
        self.sortie = self.entry_out.insert(0, self.sortie2)

    def get_entry_in(self):

        self.entree = self.entry_in.get()
        self.sortie = self.entry_out.get()
        self.seuil = self.entry_seuil.get()
        self.doctype = self.entry_doctype.get()
        self.checked = self.var.get()
        if self.checked == 0:
            self.checked ="non"
        else:
            self.checked="oui"
        self.var.get()

        # if self.entree == "" or self.sortie == "" or self.seuil == "" or self.doctype == "" :
        #
        #     self.config_hs()
        # print("configuration invalide")
        self.quit()



    def creer_widgets(self):
        self.entry_in = tk.Entry(self,width=60)
        self.entry_in.grid(row=0, column=1)
        self.entry_in.insert(0,self.entree)

        self.entry_out = tk.Entry(self,width =60)
        self.entry_out.grid(row=1, column=1)
        self.entry_out.insert(0, self.sortie)
        self.bouton = tk.Button(self, text="Appliquer", bd=4, activebackground="green", command=self.get_entry_in)
        self.bouton.grid(row=6, column=2, sticky="e")
        self.btsrcdir = tk.Button(self, text="...", command=self.opendir_in)
        self.btsrcdir.grid(row=0, column=2)
        self.btcibdir = tk.Button(self, text="...", command=self.opendir_out)
        self.btcibdir.grid(row=1, column=2)
        self.label_source = tk.Label(self, text="Dossier source :")
        self.label_source.grid(row=0, column=0, sticky="w")
        self.label_cible = tk.Label(self, text="Dossier cible :")
        self.label_cible.grid(row=1, column=0, sticky="w")
        self.label_seuil = tk.Label(self, text="Taille en Mo :")
        self.label_seuil.grid(row=3, column=0, sticky="w")
        self.entry_seuil = tk.Entry(self, width=4)
        self.entry_seuil.grid(row=3, column=1, sticky="w")
        self.entry_seuil.insert(0,self.seuil)
        self.label_doctype = tk.Label(self, text="Extension des fichiers :")
        self.label_doctype.grid(row=4, column=0, sticky="w")
        self.entry_doctype = tk.Entry(self, width=4)
        self.entry_doctype.insert(0,self.doctype)
        self.entry_doctype.grid(row=4, column=1, sticky="w")
        self.var = tk.IntVar()
        self.label_sauv = tk.Label(self, text="Sauver la configuration :")
        self.label_sauv.grid(row=5, column=0, sticky="w")
        self.checked = self.var.get()
        print(self.checked)
        texte = "mode auto, il sera nécessaire d'éditer le fichier conf.ini"
        self.sauv_config = tk.Checkbutton(self, variable=self.var,text=texte)
        self.sauv_config.grid(row=5, column=1, sticky="w")


class File_exists:

    def __init__(self,entree,sortie,taille,doctype):

        self.entree = entree
        self.sortie = sortie
        self.taille = taille
        self.doctype = doctype
        self.local = (os.getcwd())

        self.config_exists(self.entree,sortie,taille,doctype)

    def config_exists(self,entre,sortie,taille,doctype):
        root = tk.Tk()
        root.withdraw()
        result = messagebox.askquestion("Fichier de configuration existant",

                                        "Souhaitez vous valider et utiliser le fichier de configuration actuel ?\n"
                                        "\n"
                                        "Source: {}\n"
                                        "Destination: {}\n"
                                        "Taille des fichiers: {} Mo\n"
                                        "Extension des fichiers: {}".format(entre,sortie,taille,doctype)


                                        , icon='warning')
        if result == 'yes':
            print("oui")
        else:
            print("On quitte")
            quit()


# if __name__ == "__main__":
    # app = Application()
    #
    # app.title("ZipLog")
    # app.mainloop()




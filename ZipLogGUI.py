from Menu_Ziplog import *
import os
from tkinter import messagebox
import tkinter as tk
import zipfile
import sys


class LectureConfig:

    def __init__(self,fichier_conf):
        self.path_in = "Vide"
        self.path_out = "Vide"
        self.config = "Vide"
        self.doctype = "Vide"
        self.taille = "Vide"
        self.fichier_conf = fichier_conf
        self.lecture_fichier()

    def lecture_fichier(self):
        dic={}

        with open(self.fichier_conf, "r") as conf:

            for line in conf:

                key, valeur = line.strip().split("=")
                dic[key] = valeur
                dic.update(dic)
        print()

        self.path_in = str((dic["path_in"]))
        self.path_out = str((dic["path_out"]))
        self.doctype = str((dic["doctype"]))
        self.config = str((dic["config"]))
        self.taille = str((dic["taille"]))


class CreationFichierConf:
    def __init__(self):
        contenu = "path_in="+app.entree+"\npath_out="+app.sortie+"\ndoctype="+app.doctype+"\ntaille="+app.seuil+"\nconfig="+app.checked
        print(contenu)
        conf = open(fichier_conf,"w")
        conf.write(contenu)
        conf.close()


class Traitement:
    def __init__(self,path_in,path_out,doctype,taille):
        self.path_in = path_in
        self.path_out = path_out
        self.doctype = doctype
        self.taille = taille
        # print(self.path_in, self.path_out, self.doctype, self.taille)
        self.zipit()

    def zipit(self):
        nbre=0

        for (path,root,files) in os.walk(self.path_in):
            for file in files:
                pass
                print(file)










local = (os.getcwd())
fichier_conf = str(local + "/conf.ini").replace("\\", "/")


if not os.path.exists(fichier_conf):
    app = Application("","","","")
    app.title("ZipLog")
    app.mainloop()
    CreationFichierConf()
    print("traitement")
    Traitement(app.entree,app.sortie,app.doctype,app.seuil)


else:
    # LectureConfig(fichier_conf)
    lecture = LectureConfig(fichier_conf)
    # print("lecture path_in ="+lecture.path_in)
    if lecture.config == "non":
        File_exists(lecture.path_in,lecture.path_out,lecture.taille,lecture.doctype)
        app = Application(lecture.path_in,lecture.path_out,lecture.taille,lecture.doctype)
        # print(lecture.path_in,lecture.path_out,lecture.taille,lecture.doctype)
        app.title("ZipLog")
        # print("app="+app.entree,app.sortie,app.doctype,app.seuil,app.checked)
        app.mainloop()
        print("app=" + app.entree, app.sortie, app.doctype, app.seuil, app.checked)
        CreationFichierConf()
        Traitement(app.entree,app.sortie,app.doctype,app.seuil)
    else:
        Traitement(lecture.path_in,lecture.path_out,lecture.taille,lecture.doctype)

# print(app.entree,app.checked)
# app=Application()
# app.title("ZipLog")
# app.mainloop()






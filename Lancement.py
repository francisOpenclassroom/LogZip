from ZipLogInterface import *
import os
import zipfile


local = (os.getcwd())
fichier_conf = str(local + "/conf.ini").replace("\\", "/")


class CreationFichierConf:
    def __init__(self, entree, sortie, taille, doctype, config):
        self.entree = entree
        self.sortie = sortie
        self.taille = taille
        self.doctype = doctype
        self.config = config
        contenu = "path_in="+self.entree+"\npath_out="+self.sortie+"\ndoctype="+self.doctype+"\ntaille="\
                  + self.taille+"\nconfig=" + self.config
        conf = open(fichier_conf, "w")
        conf.write(contenu)
        conf.close()


class LectureConfig:

    def __init__(self, fichier_conf):
        self.path_in = "Vide"
        self.path_out = "Vide"
        self.config = "Vide"
        self.doctype = "Vide"
        self.taille = "Vide"
        self.fichier_conf = fichier_conf
        self.lecture_fichier()

    def lecture_fichier(self):
        dic = {}

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


class Traitement:
    def __init__(self, path_in, path_out, doctype, taille):
        self.path_in = path_in
        self.path_out = path_out
        self.doctype = doctype
        self.taille = taille
        self.zipit()

    def zipit(self):

        nbre = 0
        self.taille = int(self.taille) * 1000000
        for (path, dossiers, files) in os.walk(self.path_in):

            for file in files:
                if len(dossiers) > 0:
                    long_ext = -abs(len(self.doctype))
                    if self.doctype in file[long_ext:]:
                        seuil= float(os.stat(path+"/"+file).st_size/1000000)
                        seuil = "{:.2f}".format(seuil)
                        print(path+"/"+file+" "+str(seuil)+" Mo")
                        print()

                        if os.stat(path+"/"+file).st_size > int(self.taille):
                            print("éligible :" + file)
                            fichier_in = (path+"/"+file)
                            fichier_out = (file[:long_ext] + "zip")
                            chemin_out = self.path_out + "/" + fichier_out
                            print(chemin_out)
                            with zipfile.ZipFile(chemin_out,"w", compression=zipfile.ZIP_STORED, compresslevel=9) as Zip:
                                Zip.write(fichier_in)
                            nbre += 1




        print(str(nbre) + " Fichiers trouvés")




if not os.path.exists(fichier_conf):
    p = Principale(root, "", "", "", "", "non")
    root.mainloop()
    CreationFichierConf(p.entree, p.sortie, p.taille, p.doctype, p.config)
    Traitement(p.entree, p.sortie, p.doctype, p.taille)
else:

    lec = LectureConfig(fichier_conf)
    if lec.config == "non":
        p = Principale(root, lec.path_in, lec.path_out, lec.taille, lec.doctype, lec.config)
        root.mainloop()
        CreationFichierConf(p.entree, p.sortie, p.taille, p.doctype, p.config)
        Traitement(p.entree, p.sortie, p.doctype, p.taille)
    else:
        print("Config = oui")

# p = Principale(root, "l'entréé", "la sortie", 10, "log", "non")
# print(p.entree,p.sortie,p.taille,p.doctype,p.config)
# root.mainloop()
#
# print(p.entree,p.sortie,p.taille,p.doctype,p.config)

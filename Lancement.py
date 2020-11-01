from ZipLogInterface import *
import os
import zipfile
import sys
import datetime
import shutil

# déclaration des variables
local = (os.getcwd())
fichier_conf = str(local + "/conf.ini").replace("\\", "/")
ts = str(datetime.datetime.now())
ts = "_" + ts[0:10] + "_" + ts[11:13] + ts[14:16] + ts[17:19]


class CreationFichierConf:
    """
    Classe de création et d'écriture du fichier de configuration

    """
    def __init__(self, entree, sortie, taille, doctype, config):
        """
        :param entree: Dossier d'entrée des fichiers à compresser
        :param sortie: Dossier de sortie des fichiers compressés
        :param taille: Valeur en Mo du seuil de sélection des fichiers à compresser
        :param doctype: l'extension des fichiers à compresser
        :param config: oui/non - si oui l'execution s'effectue sans GUI
        """
        self.fichier_conf = str(local + "/conf.ini").replace("\\", "/")
        self.entree = entree
        self.sortie = sortie
        self.taille = taille
        self.doctype = doctype
        self.config = config
        contenu = "path_in="+self.entree+"\npath_out="+self.sortie+"\ndoctype="+self.doctype+"\ntaille="\
                  + self.taille+"\nconfig=" + self.config
        conf = open(self.fichier_conf, "w")
        conf.write(contenu)
        conf.close()


class LectureConfig:
    """
        Classe de lecture du fichier de configuration conf.ini et mise en variable des infomations
        de configuration.
    """

    def __init__(self):
        """

        """
        self.fichier_conf = str(local + "/conf.ini").replace("\\", "/")
        self.path_in = "Vide"
        self.path_out = "Vide"
        self.config = "Vide"
        self.doctype = "Vide"
        self.taille = "Vide"
        self.lecture_fichier()

    def lecture_fichier(self):
        """
        :return:    retourne les variables :
        path_in :   Dossier source
        path_out :  Dossier cible
        doctype :   Extension des fichiers à traiter
        config :    Enregistrer la configuration pour mode sans GUI
        taille :    taille à partir de laquelle les fichiers sont traités en Mo
        """
        dic = {}

        with open(self.fichier_conf, "r") as conf:

            for line in conf:

                key, valeur = line.strip().split("=")
                dic[key] = valeur
                dic.update(dic)

        self.path_in = str((dic["path_in"]))
        self.path_out = str((dic["path_out"]))
        self.doctype = str((dic["doctype"]))
        self.config = str((dic["config"]))
        self.taille = str((dic["taille"]))


class FichierLog:
    def __init__(self, path_in, file_in, file_out, nbre, pourcent):

        self.pourcent = pourcent
        self.file_in = file_in
        self.file_out = file_out
        self.path_in = path_in
        self.ladate = ts[1:11]
        self.fic_journal = open(self.path_in + "/_Ziplog.log", "a")
        self.nbre = nbre
        self.bas_de_page = ""

    def entete(self):

        self.fic_journal.write("\n")
        self.fic_journal.write(self.ladate + self.nbre + " Fichier(s) traité(s)\n")
        self.fic_journal.write("-------------------\n")

    def loggin_fl(self):
        self.file_in = self.file_in
        self.file_out = self.file_out

        self.fic_journal.write("{} --> {} ({}%)\n".format(self.file_in, self.file_out, self.pourcent))
        self.fic_journal.write("")
        self.fic_journal.close()

    def nbre(self):
        self.fic_journal.write("\n")
        self.bas_de_page = ("{} : {} Fichiers traités\n".format(self.ladate, self.nbre, self.pourcent))
        print(len(self.bas_de_page))
        if int(self.nbre) > 1:
            self.fic_journal.write("{} : {} Fichiers traités\n".format(self.ladate, self.nbre, self.pourcent))
        else:
            self.fic_journal.write("{} : {} Fichier traité\n".format(self.ladate, self.nbre, self.pourcent))
        self.fic_journal.write("-" * len(self.bas_de_page) + "\n")


class RotationFic:
    def __init__(self, retention):
        self.nom_de_fichier = ""
        self.nouveau_nom_in = ""
        self.nouveau_nom_out = ""
        self.indice = 1
        self.retention = retention
        self.list_fic = []
        self.path = ""

    def presence_fichier(self, nom_de_fichier, path):
        self.nom_de_fichier = nom_de_fichier
        self.path = path

        dic = {"0": self.nom_de_fichier + ".zip"}
        for x in range(1, self.retention):
            dic["{0}".format(x)] = self.nom_de_fichier + "_{}.zip".format(x)
        print(dic)
        for key, valeur in dic.items():

            if os.path.exists(self.path + "/" + valeur):  # permet de vérifier l'existence des fichiers
                self.list_fic.append(valeur)
        print(len(self.list_fic))

        if len(self.list_fic) == 0:
            print("première version")
            self.nom_de_fichier = self.nom_de_fichier + ".zip"
            print("lefichier sera sauvegardé sous: " + self.path + "/" + self.nom_de_fichier)

        if 0 < len(self.list_fic) < self.retention:
            self.indice = str(len(self.list_fic))
            print("lefichier sera sauvegardé sous: " + self.nom_de_fichier + "_" + str(self.indice) + ".zip")
            self.nom_de_fichier = self.nom_de_fichier + "_" + str(self.indice) + ".zip"

        if len(self.list_fic) == self.retention:
            print("la boucle est bouclée")
            nom = dic.get(str(self.retention - 1))
            print("le fichier: " + self.path + "/" + nom + " est supprimé ")
            os.remove(self.path + "/" + nom)

            for n in range(self.retention, 1, -1):
                name_in = dic.get(str(n - 2))
                name_out = dic.get(str(n - 1))
                print("{} ---> {}".format(name_in, name_out))
                shutil.move(self.path + "/" + name_in, self.path + "/" + name_out)
            print("ecriture de " + dic.get(str(0)))
            print(nom_de_fichier + ".zip")
            self.nom_de_fichier = self.nom_de_fichier + ".zip"


class Traitement:
    """
    Classe de traitement des fichiers selon les paramètres de configuration
    """
    def __init__(self, path_in, path_out, doctype, taille):
        """
        Mise en variable des valeurs
        :param path_in:     Dossier source
        :param path_out:    Dossier cible
        :param doctype:     extension des fichiers
        :param taille:      seuil en Mo des fichiers à traiter
        """
        self.path_in = path_in
        self.path_out = path_out
        self.doctype = doctype
        self.taille = taille
        self.zipit()

    def zipit(self):
        """
        :return: compression des fichiers avec le module Zipfile
        """

        nbre = 0
        self.taille = int(self.taille) * 1000000
        for (path, dossiers, files) in os.walk(self.path_in):
            # e = FichierLog(path, "", "", "")
            # FichierLog.entete(e)

            for file in files:
                if len(dossiers) > 0:
                    long_ext = -abs(len(self.doctype))
                    if self.doctype in file[long_ext:]:
                        taille_in = float(os.stat(path + "/" + file).st_size/1000000)
                        taille_in = "{:.2f}".format(taille_in)
                        file_in = (file+" "+str(taille_in)+" Mo")

                        if os.stat(path+"/"+file).st_size > int(self.taille):
                            fichier_in = (path+"/"+file)
                            fichier_out = (file[:(long_ext - 1)])

                            chemin_out = self.path_out + "/" + fichier_out
                            print(chemin_out)
                            r = RotationFic(10)
                            RotationFic.presence_fichier(r, fichier_out, self.path_out)
                            print("r.nom de fichier = " + r.nom_de_fichier)
                            chemin_out = self.path_out + "/" + r.nom_de_fichier
                            with zipfile.ZipFile(chemin_out, "w",
                                                 compression=zipfile.ZIP_DEFLATED, compresslevel=9) as Zip:
                                Zip.write(fichier_in)
                            nbre += 1
                            taille_out = float(os.stat(chemin_out).st_size / 1000000)
                            taille_out = "{:.2f}".format(taille_out)
                            file_out = fichier_out + " " + str(taille_out) + " Mo"
                            pourcentage = 100 - float(taille_out) / float(taille_in) * 100
                            pourcentage = "{:.2f}".format(pourcentage)
                            log = FichierLog(path, file_in, file_out, nbre, pourcentage)
                            FichierLog.loggin_fl(log)
        print(self.path_in)
        e = FichierLog(self.path_in, "", "", str(nbre), "")
        FichierLog.nbre(e)
        print(str(nbre) + " Fichiers trouvés")


if len(sys.argv) > 1:
    if sys.argv[1] == "-reset":
        print("Configuration initialisée")
        while True:
            try:
                os.remove(fichier_conf)
                quit()
            except FileNotFoundError:
                quit()

# test de l'existence des fichiers pour déterminer quel module doit être exécuté
if not os.path.exists(fichier_conf):
    p = Principale(root, "", "", "", "", "non")
    root.mainloop()
    if p.valide == "oui":
        CreationFichierConf(p.entree, p.sortie, p.taille, p.doctype, p.config)
        Traitement(p.entree, p.sortie, p.doctype, p.taille)
    else:
        print("Annulation par l'utilisateur")
else:

    lec = LectureConfig()
    if lec.config == "non":
        p = Principale(root, lec.path_in, lec.path_out, lec.taille, lec.doctype, lec.config)
        root.mainloop()
        if p.valide == "oui":
            CreationFichierConf(p.entree, p.sortie, p.taille, p.doctype, p.config)
            Traitement(p.entree, p.sortie, p.doctype, p.taille)
        else:
            print("Annulation par l'utilisateur")
    else:
        print("Traitement automatique")
        p = Principale(root, lec.path_in, lec.path_out, lec.taille, lec.doctype, lec.config)
        Traitement(p.entree, p.sortie, p.doctype, p.taille)

from ZipLogInterface import *
import os
import zipfile
import sys
import datetime
import shutil

# déclaration des variables du code principal
local = (os.getcwd())
fichier_conf = str(local + "/conf.ini").replace("\\", "/")
ts = str(datetime.datetime.now())
ts = "_" + ts[0:10] + "_" + ts[11:13] + ts[14:16] + ts[17:19]


class CreationFichierConf:
    """
    Classe de création et d'écriture du fichier de configuration

    """
    def __init__(self, entree, sortie, taille, doctype, config, rotation):
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
        self.rotation = rotation
        contenu = "path_in="+self.entree+"\npath_out="+self.sortie+"\ndoctype="+self.doctype+"\ntaille="\
                  + self.taille+"\nconfig=" + self.config + "\nrotation=" + self.rotation
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
        Déclaration des variables et lancement de la procédure de lecture du fichier conf.ini
        """
        self.fichier_conf = str(local + "/conf.ini").replace("\\", "/")
        self.path_in = "Vide"
        self.path_out = "Vide"
        self.config = "Vide"
        self.doctype = "Vide"
        self.taille = "Vide"
        self.rotation = "Vide"
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
        # Les variables sont ajoutées à un dictionnaire
        self.path_in = str((dic["path_in"]))
        self.path_out = str((dic["path_out"]))
        self.doctype = str((dic["doctype"]))
        self.config = str((dic["config"]))
        self.taille = str((dic["taille"]))
        self.rotation = str((dic["rotation"]))


class FichierLog:
    """
    Classe de création du fichier de log. Un fichier _Ziplog.log est généré
    dans le dossier source et contient l'activité de l'archivage
    """
    def __init__(self, path_in, file_in, file_out, nbre, pourcent):
        """

        :param path_in:     Dossier source
        :param file_in:     Fichier source
        :param file_out:    Fichier cible
        :param nbre:        Nombre de fichiers traités
        :param pourcent:    Pourcentage de compression
        """

        self.pourcent = pourcent
        self.file_in = file_in
        self.file_out = file_out
        self.path_in = path_in
        self.ladate = ts[1:11]
        self.fic_journal = open(self.path_in + "/_Ziplog.log", "a")
        self.nbre = nbre
        self.bas_de_page = ""

    def entete(self):
        """
        :return: Affiche un résumé ainsi que la date
        """
        self.fic_journal.write("\n")
        self.fic_journal.write(self.ladate + self.nbre + " Fichier(s) traité(s)\n")
        self.fic_journal.write("-------------------\n")

    def loggin_fl(self):
        """
        :return: Ecriture des inforamtions dans le fichier de log
        """
        self.file_in = self.file_in
        self.file_out = self.file_out

        self.fic_journal.write("{} --> {} ({}%)\n".format(self.file_in, self.file_out, self.pourcent))
        self.fic_journal.write("")
        self.fic_journal.close()

    def nbre(self):
        """
        :return: Mise en forme du nombre de fichiers traités pour le fichier journal
        """
        self.fic_journal.write("\n")
        self.bas_de_page = ("{} : {} Fichiers traités\n".format(self.ladate, self.nbre, self.pourcent))
        if int(self.nbre) > 1:
            self.fic_journal.write("{} : {} Fichiers traités\n".format(self.ladate, self.nbre, self.pourcent))
        else:
            self.fic_journal.write("{} : {} Fichier traité\n".format(self.ladate, self.nbre, self.pourcent))
        self.fic_journal.write("-" * len(self.bas_de_page) + "\n")


class RotationFic:
    """
    Classe de rotation des fichiers log, un nombre de fichiers
    correspondant à la valeur est sauvegardé plus le dernier fichier traité
    """
    def __init__(self, retention):
        """
        :param retention: nombre de fichiers à conserver dans la rotation
        """
        self.nom_de_fichier = ""
        self.nouveau_nom_in = ""
        self.nouveau_nom_out = ""
        self.retention = retention
        self.list_fic = []
        self.path = ""

    def presence_fichier(self, nom_de_fichier, path):
        """

        :param nom_de_fichier: nom du fichier à traiter
        :param path: chemin du fichier à traiter
        :return: conditons permttant d'effectuer la rotation des versions
        les fichiers sont copiés vers l'indice supérieur
        en commençant par la fin - 1 pour éviter l'écrasement.
        """
        self.nom_de_fichier = nom_de_fichier
        self.path = path

        dic = {"0": self.nom_de_fichier + ".zip"}
        for x in range(1, self.retention):
            dic["{0}".format(x)] = self.nom_de_fichier + "_{}.zip".format(x)
        for key, valeur in dic.items():

            if os.path.exists(self.path + "/" + valeur):  # permet de vérifier l'existence des fichiers
                self.list_fic.append(valeur)

        if len(self.list_fic) == 0:
            self.nom_de_fichier = self.nom_de_fichier + ".zip"

        if 0 < len(self.list_fic):
            for y in range(len(self.list_fic), 0, -1):
                fic_in = (self.path + "/" + self.list_fic[y-1])
                fic_out = (self.path + "/" + self.nom_de_fichier + "_" + str(y) + ".zip")
                shutil.move(fic_in, fic_out)
            self.nom_de_fichier = self.nom_de_fichier + ".zip"


class Traitement:
    """
    Classe de traitement des fichiers selon les paramètres de configuration
    """
    def __init__(self, path_in, path_out, doctype, taille, rotation):
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
        self.rotation = rotation
        self.zipit()

    def zipit(self):
        """
        :return: compression des fichiers avec le module Zipfile
        """

        nbre = 0
        self.taille = int(self.taille) * 1000000
        for (path, dossiers, files) in os.walk(self.path_in):

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

                            r = RotationFic(int(self.rotation))
                            RotationFic.presence_fichier(r, fichier_out, self.path_out)
                            chemin_out = self.path_out + "/" + r.nom_de_fichier
                            with zipfile.ZipFile(chemin_out, "w",
                                                 compression=zipfile.ZIP_DEFLATED, compresslevel=9) as Zip:
                                Zip.write(fichier_in)
                            nbre += 1
                            taille_out = float(os.stat(chemin_out).st_size / 1000000)
                            taille_out = "{:.2f}".format(taille_out)
                            file_out = fichier_out + ".zip " + str(taille_out) + " Mo"
                            pourcentage = 100 - float(taille_out) / float(taille_in) * 100
                            pourcentage = "{:.2f}".format(pourcentage)
                            log = FichierLog(path, file_in, file_out, nbre, pourcentage)
                            FichierLog.loggin_fl(log)
                            os.remove(fichier_in)
        e = FichierLog(self.path_in, "", "", str(nbre), "")
        FichierLog.nbre(e)


# reinitialisation si le programme est lancé avec l'option -reset -> Suppression du fichier conf.ini
if len(sys.argv) > 1:
    if sys.argv[1] == "-reset":
        print("Configuration initialisée")
        while True:
            try:
                os.remove(fichier_conf)
                quit()
            except FileNotFoundError:
                quit()

# test de l'existence du fichier conf.ini pour déterminer quel module doit être exécuté

# Si le fichier conf.ini est absent
if not os.path.exists(fichier_conf):
    p = Principale(root, "", "", "", "", "non", 2)
    root.mainloop()
    if p.valide == "oui":  # La variable valide permet de détecter une annulation par l'utilisateur

        CreationFichierConf(p.entree, p.sortie, p.taille, p.doctype, p.config, p.rotation)
        Traitement(p.entree, p.sortie, p.doctype, p.taille, p.rotation)
    else:
        print("Annulation par l'utilisateur")
else:

    lec = LectureConfig()
    if lec.config == "non":  # Si le paramètre config du fichier conf.ini est non l'interface graphique est exécutée
        p = Principale(root, lec.path_in, lec.path_out, lec.taille, lec.doctype, lec.config, lec.rotation)
        root.mainloop()
        if p.valide == "oui":  # Détection de l'annulation par l'utilisateur
            CreationFichierConf(p.entree, p.sortie, p.taille, p.doctype, p.config, p.rotation)
            Traitement(p.entree, p.sortie, p.doctype, p.taille, p.rotation)
        else:
            print("Annulation par l'utilisateur")
    else:  # La variable config du fichier conf.ini est sur oui, l'exécution est silencieuse
        p = Principale(root, lec.path_in, lec.path_out, lec.taille, lec.doctype, lec.config, lec.rotation)
        Traitement(p.entree, p.sortie, p.doctype, p.taille, p.rotation)

import os
import zipfile
import sys

# variables
local = (os.getcwd())
dic = {}

#  détection de l'os pour la syntaxe des chemins de fichiers
print(sys.platform)


""" LogZip """

# Fonction de gestion du fichier config.ini

def config_file():

    """ Fonction de gestion du fichier config.ini
        Le fichier config.ini contient les informations
        de configurations :
        (Ne pas mettre d'espace ou de guillemets autour des valeurs)

        path_in=e:\Logs                 -> le chemin des fichiers sources
        path_out=e:\Logs\Logs_archives  -> le chemin du dossier cible
        doctype=.log                    -> l'extension des fichiers à traiter
        config=oui                      -> si "oui" le programme a déjà été lancé et est configuré
                                        -> si "non" il s'agit d'une première exécution
        taille=1                        -> la taille minimale des fichiers à traiter en Mo

         """
    fic_conf = open(fichier_conf, "rt")
    contenu = fic_conf.read()
    contenu = contenu.replace("non", "oui")
    fic_conf.close()
    fic_conf = open(fichier_conf, "wt")
    fic_conf.write(contenu)
    fic_conf.close()

def CreationConfig():

    fic_conf = open(fichier_conf, "rt")
    contenu = fic_conf.read()
    contenu = contenu.replace("non", "oui")
    fic_conf.close()
    fic_conf = open(fichier_conf, "wt")
    fic_conf.write(contenu)
    fic_conf.close()


fichier_conf = local + "/config.ini"

if not os.path.isfile(fichier_conf):
    print("le fichier de configuration est absent ou invalide")
    print("Exécution du module de configuration")
    quit()



# Paramêtrage des répertoires de travail avec un fichier config.ini




with open(fichier_conf,"r") as conf:

    for line in conf:
        key,valeur = line.strip().split("=")
        dic[key] = valeur
        dic.update(dic)
print()

path_in = str((dic["path_in"]).replace("\\","/"))
path_out = str((dic["path_out"]).replace("\\","/"))

doctype = dic["doctype"]
config = dic["config"]
taille = dic["taille"]


if not os.path.exists(path_in):
    print("le répertoire source n'existe pas ")
    quit()

format_dos = path_out.replace("/","\\")

if os.path.exists(path_out) and config == "oui":
    print("utilisation du dossier d'archives : {} ".format(format_dos))

elif os.path.exists(path_out) and config == "non":

    est_sur = True
    while est_sur:
                sur = input("Le dossier {} existe déjà, \nêtes vous sur de vouloir utiliser ce dossier ? ".format(format_dos))
                sur = sur.lower()
                if sur == "n":
                    print("programme arreté par l'utilisateur")
                    quit()
                elif sur == "o":
                    est_sur = False
                    if config == "non":
                        config_file()
                else:
                    print("Quitter : n , accepter : o")


elif not os.path.exists(path_out):
    est_sur = True
    while est_sur:
        creation_dossier = input("le dossier {} n'existe pas, souhaitez vous le créer ? ".format(path_out))
        creation_dossier = creation_dossier.lower()
        if creation_dossier == "n":
            print("Programme arrêté par l'utilisateur")
            quit()
        elif creation_dossier == "o":
            est_sur = False
            print("creation du dossier : {}".format(format_dos))
            os.mkdir(format_dos)
            if config == "non":
                config_file()
        else:
            print("Quitter : n , accepter : o")





taille = int(taille)*1000000
nbre = 0
for (path, root, files) in os.walk(path_in):

    for file in files:
        if files:

            if doctype in file:

                fichier_in =(path_in + "/" + file)
                file_out = (file[:-3] + "zip")
                chemin_out = path_out + "/" + file_out
                if os.stat(fichier_in).st_size > int(taille):
                    print(fichier_in.replace("/","\\") +  " --> " + chemin_out.replace("/","\\"))
                    size_in = os.stat(fichier_in).st_size
                    nbre += 1
                    with zipfile.ZipFile(chemin_out,"w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as Zip:
                        Zip.write(fichier_in)
                    os.remove(fichier_in)
if nbre <= 1:
    print(nbre, " Fichier traité")
else:
    print(nbre, " Fichiers traités")
# help(config_file)














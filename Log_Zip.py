import os
import zipfile
local = (os.getcwd())
dic = {}


""" LogZip """

def config_file():
    fic_conf = open(fichier_conf, "rt")
    contenu = fic_conf.read()
    contenu = contenu.replace("non", "oui")
    fic_conf.close()
    fic_conf = open(fichier_conf, "wt")
    fic_conf.write(contenu)
    fic_conf.close()

# Paramêtrage des répertoires de travail avec un fichier config.ini
print()


fichier_conf = local + "/config.ini"


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



if  os.path.exists(path_out):
    direxists="oui"
else:
    direxists="non"

# print(direxists)


if direxists == "oui" and config == "oui":
    print("utilisation du dossier d'archives : {} ".format(path_out).replace("/","\\"))

elif direxists == "oui" and config == "non":

    est_sur = True
    while est_sur:
                sur = input("Le dossier {} existe déjà, \nêtes vous sur de vouloir utiliser ce dossier ? ".format(path_out).replace("/","\\"))
                sur = sur.lower()
                if sur == "n":
                    print("on quitte")
                    quit()
                elif sur == "o":
                    est_sur = False
                    if config == "non":
                        config_file()
                else:
                    print("Quitter : n , accepter : o")


elif direxists == "non":
    est_sur = True
    while est_sur:
        creation_dossier = input("le dossier {} n'existe pas, souhaitez vous le créer ? ".format(path_out))
        creation_dossier = creation_dossier.lower()
        if creation_dossier == "n":
            print("Programme arrêté par l'utilisateur")
            quit()
        elif creation_dossier == "o":
            est_sur = False
            print("creation du dossier : {}".format(path_out).replace("/","\\"))
            os.mkdir(path_out.replace("/","\\"))
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
                    size_out = os.stat(chemin_out).st_size
                    os.remove(fichier_in)

print(nbre, " Fichier(s) traités")














import os
import zipfile
local = (os.getcwd())
dic = {}


""" LogZip """

# Paramêtrage des répertoires de travail avec un fichier config.ini
print()
print("Utilisation du fichier " + local + "\config.ini")

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
print(config)

if  os.path.exists(path_out):
    direxists="oui"
else:
    direxists="non"

# print(direxists)


if direxists == "oui" and config == "oui":
    print("utilisation du dossier d'archives : ".format(path_out))

elif direxists == "oui" and config == "non":

    est_sur = True
    while est_sur:
                sur = input("Le dossier {} existe déjà, \nêtes vous sur de vouloir utiliser ce dossier ? ".format(path_out))
                sur = sur.lower()
                if sur == "n":
                    print("on quite")
                    quit()
                elif sur == "o":
                    est_sur = False
                else:
                    print(chr(27)+'[2j')
                    print("Quitter : n , accepter : o")




elif direxists == "non":
    creation_dossier = input("le dossier {} n'existe pas, souhaitez vous le créer ? ".format(path_out))
    print("creation du dossier d'achives : {}".format(path_out))




for (path, root, files) in os.walk(path_in):
    nbre = 0
    for file in files:
        if files:

            if doctype in file:
                nbre += 1
                fichier_in =(path_in + "/" + file)
                file_out = (file[:-3] + "zip")
                chemin_out = path_out + "/" + file_out
                print(fichier_in.replace("/","\\") +  " --> " + chemin_out.replace("/","\\"))
                with zipfile.ZipFile(chemin_out,"w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as Zip:
                    Zip.write(fichier_in)
#                 os.remove(chemin_in)
















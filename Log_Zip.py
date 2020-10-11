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
direxists = dic["direxists"]

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
















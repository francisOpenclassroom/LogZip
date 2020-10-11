import os
import zipfile
local = (os.getcwd())
dic = {}


""" LogZip """

# Paramêtrage des répertoires de travail avec un fichier config.ini
print()
print("Utilisation du fichier " + local + "\config.ini")
fichier_conf = local + "\config.ini"
with open(fichier_conf,"r") as conf:

    for line in conf:
        key,valeur = line.strip().split("=")
        dic[key] = valeur
        dic.update(dic)
print()
# print("Les fichiers .log présents dans le dossier {} seront archivés dans le dossier {}".format(dic["path_in"], dic["path_out"]))

path_in = str((dic["path_in"]).replace("\\","/"))

# print("le chemin est : " + path_in)

for (path, root, files) in os.walk(path_in):
    # print(files)
    nbre = 0
    for file in files:
        if files:

            if ".log" in file:
                nbre += 1
                # print("le fichier {} sera traité ".format(file))
                fichier_in =(path_in + "/" + file)
                # print(fichier_in)
                file_out = (file[:-3] + "zip")
                # print(file_out)
                chemin_out = path + "/Logs_archives/" + file_out
                print(fichier_in +  " --> " + chemin_out)
                with zipfile.ZipFile(chemin_out,"w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as Zip:
                    Zip.write(fichier_in)
#                 os.remove(chemin_in)
















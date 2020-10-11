import os
import zipfile

local = (os.getcwd())
dic = {}

print()
print("Utilisation du fichier " + local + "\config.ini")
fichier_conf = local + "\config.ini"
with open(fichier_conf,"r") as conf:

    for line in conf:
        key,valeur = line.strip().split("=")
        dic[key] = valeur
        dic.update(dic)
print()
print("Les fichiers .log présents dans le dossier {} seront archivés dans le dossier {}".format(dic["path_in"], dic["path_out"]))

chemin = str((dic["path_in"]))
print("le chemin est : " + chemin)
for (path, root, files) in os.walk("e:\Logs"):
    print(files)

    for file in files:
        if files:

            if ".log" in file:
                print(file)
#                 chemin_in =(path + "/" + file)
#                 file_out = (file[:-3] + "zip")
#                 chemin_out = path + "/Logs_archives/" + file_out
#                 print(chemin_in +  " --> " + chemin_out)
#                 with zipfile.ZipFile(chemin_out,"w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as Zip:
#                     Zip.write(chemin_in)
#                 print(chemin_in)
#                 os.remove(chemin_in)
















# LogZip

## Table des matières

1. [Description]
2. [Technos]
3. [Installation]
4. [Utilisation]

# Description :

Ce script Python a pour fonction d'automatiser la gestion des fichiers journeaux de type log, txt, xml ou de toutes autres extensions qui parfois encombrent des espaces de stockage. L'interface graphique permet le paramètrage du type et de la taille des fichiers éligibles à la compression. Une fonction permet d'automatiser la tâche sans interaction permettant ainsi la planification de la tâche.

![image](https://user-images.githubusercontent.com/72203692/97585174-213b0800-19f9-11eb-993f-27671360789e.png)

# Technos

Les technologies utilisées pour développer ce script sont : Python 3.8.5 et Pycharm IDE 2020.2
L'interface graphique est construite avec le module Tkinter.

Lien vers Python : https://www.python.org/

Lien vers Pycharam : https://www.jetbrains.com/fr-fr/pycharm/

Lien vers tkinter : https://docs.python.org/fr/3/library/tk.html

# Installation

Une version de Python 3 est nécessaire pour exécuter ce script, copier les fichiers lancement.py et ZipLogInterface.py dans un dossier. Les fichiers sont téléchargeables à l'adresse : https://github.com/francisOpenclassroom/LogZip.git


# Utilisation

pour lancer le progranmme :

`python lancement.py`

La première exécution du script affiche l'interface graphique de configuration :

- Le Dossier source est l'emplacement où se trouvent les fichiers à compresser.

- Le Dossier cible est l'empcement ou seront stockés les fichiers compressés

- La taille en Mo est le seuil à partir duquel les fichiers seront compressés dans le dossier cible et supprimés du dossier source

- L'extension est l'extension des fichiers (.log, .txt..., sans le '.' à traiter 

- L'exécution automatique permet de ne plus afficher l'interface graphique au prochain lancement permettant ainsi d'exécuter le programmme à partir d'un tâche planifiée.

- Pour réinitialiser la configuration, et afficher le menu à nouveau, la syntaxe est la suivante :

`python lancement.py -reset`

- Un fichier _ZipLog.log est créé dans le dossier source, il contient la journalisation de l'activité du programme.

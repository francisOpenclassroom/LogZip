# LogZip

## Table des matières

 1. [Description](#Description-)
 2. [Technos](#Technos)
 3. [Installation](#Installation)
 4. [Utilisation](#Utilisation)
 5. [Fonctionnalités](#Fonctionalités)
 6. [Auteur](#Auteur)
 7. [Licence](#Licence)

# Description :

Ce script Python a pour fonction d'automatiser la gestion des fichiers journeaux de type log, txt, xml ou de toutes autres extensions qui parfois encombrent des espaces de stockage. L'interface graphique permet le paramètrage du type et de la taille des fichiers éligibles à la compression. Une fonction permet d'automatiser la tâche sans interaction permettant ainsi la planification de la tâche.

![image](https://user-images.githubusercontent.com/72203692/97974642-2d8fde00-1dc8-11eb-8ac7-7f40bff0e30b.png)

# Technos

Les technologies utilisées pour développer ce script sont : Python 3.8.5 et Pycharm IDE 2020.2
L'interface graphique est construite avec le module Tkinter.

Lien vers Python : https://www.python.org/

Lien vers Pycharam : https://www.jetbrains.com/fr-fr/pycharm/

Lien vers tkinter : https://docs.python.org/fr/3/library/tk.html

# Installation

Une version de Python 3 est nécessaire pour exécuter ce script, copier les fichiers lancement.py et ZipLogInterface.py dans un dossier. Les fichiers sont téléchargeables à l'adresse : https://github.com/francisOpenclassroom/LogZip.git

Ce script a été développé avec la version 3.8.5 et devrait fonctionner avec toutes les versions 3.x de Python.

Créez un dossier portant le nom de votre choix, déposer les fichiers dans ce dossier :

* Aide_V1.html :   
_Le fichier d'aide en ligne_
* conf.ini :            
_un exemple de fichier de configuration (optionnel)_
* Lancement.py :        
_Le programme principal_
* principale.png :      
_L'image de l'interface principale pour le fichier d'aide_
* Z.ico :        
_Le fichier image de l'icone de l'interface graphique_
* ZiplogInterface.py :  
_Le code du module graphique Tkinter_


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

# Fonctionnalités 

L'interface principale permet de configurer les options d'entrée, sortie, la taille, l'extension ainsi que la possibilité d'une exécution silencieuse :

![image](https://user-images.githubusercontent.com/72203692/97609270-ac28fc00-1a13-11eb-8fff-297ef39a11e7.png)

Le bouton Modifier permet d'appliquer la configuration, si des erreurs sont détectées, un message contextuel permet de repérer la donnée entrée erronée et l'éxecution du programme n'est pas possible tant que les erreurs ne sont pas corrigées, le bouton exécuter reste inactif :

![image](https://user-images.githubusercontent.com/72203692/97610031-a849a980-1a14-11eb-8a56-0fb55ac6bd3b.png)

En mode silencieux, la fenêtre du résumé de la configuration change de couleur et passe au bleu :

![image](https://user-images.githubusercontent.com/72203692/97610420-21490100-1a15-11eb-88cc-3d72861e54b2.png)

# Auteur

Francis ROUILLON 

francis.rouillon.openclassrooms@gmail.com


# Licence

Ce projet est distribué sous licence MIT 

MIT License

Copyright (c) [2020] [Francis ROUILLON]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

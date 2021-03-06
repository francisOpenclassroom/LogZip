# LogZip

## Table des matières

 1. [Description](#Description)
 2. [Technos](#Technos)
 3. [Installation](#Installation)
 4. [Utilisation](#Utilisation)
 5. [Fonctionnalités](#Fonctionnalités)
 6. [Auteur](#Auteur)
 7. [Licence](#Licence)

# Description

Ce script Python a pour fonction d'automatiser la gestion des fichiers journaux de type log, txt... ou de toutes autres extensions qui parfois encombrent des espaces de stockage. L'interface graphique permet le paramètrage du type et de la taille des fichiers éligibles à la compression. Une fonction permet d'automatiser la tâche sans interaction permettant ainsi la planification de la tâche.

![image](https://user-images.githubusercontent.com/72203692/98028438-66eb3c80-1e0e-11eb-949a-ebbd3a83a91d.png)

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
* <strong>Lancement.py</strong> :        
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

- Le Dossier source est l'emplacement où se trouvent les fichiers à compresser, le script supporte des chemins UNC sous windows.

- Le Dossier cible est l'emplacement où seront stockés les fichiers compressés, le script supporte des chemins UNC sous windows.

- La taille en Mo est le seuil à partir duquel les fichiers seront compressés dans le dossier cible et supprimés du dossier source.

- L'extension est l'extension des fichiers (.log, .txt..., sans le '.') à traiter. 

- L'exécution automatique permet de ne plus afficher l'interface graphique au prochain lancement permettant ainsi d'exécuter le programmme à partir d'une tâche planifiée.

_Pour réinitialiser la configuration, et afficher le menu à nouveau, la syntaxe est la suivante :_

`python lancement.py -reset`

- Rotations est le nombre de versions de fichiers archivés à conserver, au minimum la version courante et une version archivée sont sauvegardés (valeur : 1).

_<strong>Un fichier ZipLog.log est créé dans le dossier source, il contient la journalisation de l'activité du programme.</strong>_

L'utilisateur exécutant le programme doit bénéficier de droits d'écriture dans le dossier source et le dossier cible.

# Fonctionnalités 

L'interface principale permet de configurer les options d'entrée, sortie, la taille, l'extension, le nombre de fichiers archivés ainsi que la possibilité d'une exécution silencieuse :

![image](https://user-images.githubusercontent.com/72203692/98030488-5be5db80-1e11-11eb-9da5-c2c048d7d42c.png)

Le bouton Modifier permet d'appliquer la configuration, si des erreurs sont détectées, un message contextuel permet de repérer la donnée entrée erronée et l'éxecution du programme n'est pas possible tant que les erreurs ne sont pas corrigées (bouton Exécuter inactif).

Une aide en ligne est disponible en cliquant sur le bouton ?.

Des contrôles sont effectués sur l'existence des dossiers source
et cible, la présence d'une extension et les valeurs numériques du champ taille et nombre de rotations :

![image](https://user-images.githubusercontent.com/72203692/98030864-f2b29800-1e11-11eb-8b18-08127af09646.png)

En mode silencieux, la fenêtre du résumé de la configuration change de couleur et passe au bleu :

![image](https://user-images.githubusercontent.com/72203692/98031603-027eac00-1e13-11eb-9b9c-a22fa4b2262c.png)

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

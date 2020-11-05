# Logique


# Sommaire :

 1. [Algorithme principal](#algorithme-principal-)
 2. [Algorithme du module graphique](#algorithme-du-module-graphique-)
 3. [Algorithme du code primaire](#algorithme-du-code-primaire-)
 4. [Algorithme de traitement](#algorithme-de-traitement-)

# Algorithme principal :

Le script est structuré de la manière suivante :

Un script principal Lancement.py et un module graphique ZipLogInterface.py

Le script principal prend en charge les traitements, le module graphique prend en charge le GUI et la validation des données saisies.

La persitence de la configuration est assurée par la création ou la modification d'un fichier de configuration conf.ini.

Exemple de contenu du fichier conf.ini :

`path_in=E:/Logs`       
`path_out=E:/Logs/Logs_archives`  
`doctype=log`        
`taille=1`     
`config=non`     
`rotation=1`     

Lors de l'exécution est effectué en premier un test d'existence de ce fichier :

Si le fichier conf.ini n'existe pas dans le répertoire courant on exécute la classe Principale du module graphique ZipLogInterface.py avec des parmêtres fixes par défaut.
On entre alors dans une boucle tkinter, une variable self.valide permet de détecter un click sur le bouton annuler et sert alors de condition lors de la sortie de la boucle graphique à l'exécution de la creation du fichier de configuration par la classe CreationFichierConf et le traitement des fichiers par la classe Traitement.

Si la variable self.valide retournée est "oui" la création et le traitement sont effectués, si "non" est retourné l'exécution du programme est interrompue.  

Si le fichier conf.ini est présent, les données de ce fichier sont lues par la classe LectureConfig et intégrées dans un dictionnaire Python, si la directive config du fichier est oui la classe Principale est exécutée sans boucle graphique et ensuite la classe Traitement.
Si la directive config est non, la classe Principale est exécutée dans une boucle graphique et suit le même schéma d'exécution que lorsque le fichier conf.ini est absent, le fichier conf.ini est alors recréé avec les nouvelles informations de sortie.


![image](https://user-images.githubusercontent.com/72203692/98155179-1dfebb00-1ed6-11eb-96ab-c6a4773c36cf.png)

# Algorithme du module graphique :

![image](https://user-images.githubusercontent.com/72203692/98028438-66eb3c80-1e0e-11eb-949a-ebbd3a83a91d.png)

Le module graphique ZipLogInterface.py prend en charge la saisie et la validation des données entrées par l'utilisateur. Le constructeur de la classe Principale met en place l'intégralité des éléments graphiques Tkinter, les zones de saisie, les boutons générant les actions ainsi que les éléments de texte.
Les boutons Parcourir exécutent une fonction opendir_in() et opendir_out() respectivement qui s'appuie sur la méthode filedialog.askdirectory de Tkinter faisant appel à un explorateur de fichier du système d'exploitation qui se substitue alors à la zone de saisie manuelle du dossier source et cible assurée par des widgets Entry.

Le bouton Annuler exécute la fonction annuler() qui se charge de sortir de la boucle graphique et de modifier la variable self.valide à "non".



![image](https://user-images.githubusercontent.com/72203692/98159861-95841880-1edd-11eb-805e-d7ae3c623b09.png)

# Algorithme du code primaire :

![image](https://user-images.githubusercontent.com/72203692/98163100-9c615a00-1ee2-11eb-9503-bedb454197a2.png)

# Algorithme de traitement :

![image](https://user-images.githubusercontent.com/72203692/98169476-96707680-1eec-11eb-8431-86fa638aa76d.png)


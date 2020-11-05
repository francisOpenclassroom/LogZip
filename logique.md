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
Lignes 264 à 272 du script Lancement.py



![image](https://user-images.githubusercontent.com/72203692/98155179-1dfebb00-1ed6-11eb-96ab-c6a4773c36cf.png)

# Algorithme du module graphique :

![image](https://user-images.githubusercontent.com/72203692/98159861-95841880-1edd-11eb-805e-d7ae3c623b09.png)

# Algorithme du code primaire :

![image](https://user-images.githubusercontent.com/72203692/98163100-9c615a00-1ee2-11eb-9503-bedb454197a2.png)

# Algorithme de traitement :

![image](https://user-images.githubusercontent.com/72203692/98169476-96707680-1eec-11eb-8431-86fa638aa76d.png)


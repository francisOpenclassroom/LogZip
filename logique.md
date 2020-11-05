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

La  saisie de la taille des fichiers, l’extension et le nombre de rotations est assurée par des widgets de type Entry. Le choix d’exécution automatique par un widget Checkbutton.  
Les boutons sont des widgets de type Button.  
Le bouton Appliquer exécute la fonction get_entry(), cette fonction se charge de récupérer les valeurs entrées dans les champs de saisie de type Entry, de la méthode filedialog.askdirectory ainsi que Checkbutton par des méthodes get(). Cette même fonction get_entry() appelle dans un premier temps une autre fonction maj_list().   

La fonction maj_list() utilise une liste Python liste_valeur pour stocker les éléments saisis par l’utilisateur afin de permettre un échange entre les autres fonctions utilisées pour les modifier et les contextualiser.

La fonction affiche_resultat() est ensuite exécutée. A l’intérieur de cette dernière, une fonction de validation de la saisie validation() est exécutée dans un premier temps et gère les conditions suivantes :

Existence du dossier source et du dossier cible
Existence de la saisie d’une extension 
Les nombres saisis dans la taille et le nombre de rotations doivent être des entiers supérieurs à 0
Les conditions retournent une valeur booléenne et modifient le contenu de la liste liste_valeur pour contextualiser les messages d’erreur.

De plus, tant que toutes les conditions ne sont pas remplies (valeur booléennes False) le bouton Exécuter est rendu inactif par une modification de l’état du widget Button à  disabled ainsi que la modification de la couleur du panneau de résumé.

Les données de cette liste sont alors affichées par la fonction affiche_resultat() à l’aide d’une boucle, le bouton Appliquer est détruit et remplacé par un bouton modifier, le bouton Exécuter est quant à lui actif ou inactif selon l’état des conditions ce qui garantit une exécution du traitement uniquement lorsque toutes les données sont valides.

Le bouton modifier prend alors en charge la mise à jour des données via la fonction mise_a_jour() qui lit et insère les nouvelles valeurs des variables. Cette fonction boucle alors avec la fonction affiche_resultat() jusqu’à l’utilisation d’un autre bouton (Annuler ou Exécuter).

Le bouton exécuter sort de la boucle graphique et retourne dans le code principal les variables du dossier source et cible, de l’extension et de la taille des fichiers, du nombre de rotations ainsi que oui ou non de la directive config.




![image](https://user-images.githubusercontent.com/72203692/98159861-95841880-1edd-11eb-805e-d7ae3c623b09.png)

# Algorithme du code primaire :

![image](https://user-images.githubusercontent.com/72203692/98163100-9c615a00-1ee2-11eb-9503-bedb454197a2.png)

# Algorithme de traitement :

![image](https://user-images.githubusercontent.com/72203692/98169476-96707680-1eec-11eb-8431-86fa638aa76d.png)


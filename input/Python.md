---
title: Python
subtitle: programmer en Python
author: Damien Belvèze
date: 08-02-2021
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: [Py]
tags: [Programmation]
---
[documentation officielle](https://docs.python.org/3/)

Pour les conférences sur Python voir [[Cocopy]]
Une partie du contenu ci-dessous provient de la formation donnée par Cédric Gémy à l'URFIST de Rennes les 26 et 27 novembre 2024

# Origines et principales caractéristiques de Python

Langage informatique multiplateforme mis au point par Guido van Rossum, à partir de 1989. Baptisé ainsi en hommage aux Monty Pythons. ([[@azoulaiPythonRoman2024]], p60)

Python a essayé de réduire les éléments syntaxiques au maximum pour que le code soit le plus lisible possible à un oeil humain. 
langage moderne fortement structuré contrairement à des langages plus anciens comme [[C(langage)]]
dispose d'une documentation intégrée.

en tant que langage multiplateforme, Python fonctionne avec un interpréteur. Installer Python c'est installer l'interpréteur Python. (pour les langages [[compilation|compilés]] comme C, on produit un exécutable (.exe) qui ne va fonctionner que sur un ordi sous Windows. La compilation représente un gain en rapidité qui n'est plus tellement nécessaire aujourd'hui, sauf pour le traitement d'images 3D avec [[blender]] par exemple).

# fonctions usuelles

une **fonction** marche sur n'importe quelle classe
*print()* est une fonction
une **méthode** ne fonctionne que sur une classe en particulier 
*lower()* est une fonction qui ne marche que sur la classe "string"

pour avoir l'ensemble des méthodes qui fonctionnent sur une classe donnée : 

```python
dir(str)
```
## typage fort de Python

Python, contrairement à C est un langage où le typage est fort. Chaque variable doit disposer d'un type à un moment donné et ne peut pas être interprétée de manière indifférenciée par rapport à son type. 

Par exemple, la fonction chr (conversion de l'ASCII en caractères) ne peut s'exercer que sur des entiers (puisque les caractères ASCII sont des entiers), donc si on récupère dans un fichier une chaîne de caractères comme 65, il faut d'abord la convertir en entier pour ensuite retrouver avec la fonction chr le caractère correspondant : 

```python
chr(str(65))
# si 65 est une chaîne de caractères et pas un entier, alors il faut d'abord convertir 65 en entier pour obtenir le résultat (A)
```
On ne peut pas concaténer ou additionner des variables qui relèvent de types différents. 

Par exemple on peut additionner 40 et 2 si 40 et 2 sont des entiers, mais on ne peut pas concaténer 1001 nuits si 1001 est un entier et nuits est une chaîne de caractère. Dans ce cas, il faudra d'abord convertir 1001 en chaîne de caractères (string)

```python
nombre = 1001
texte = nuits
print(str(1001) +''+texte)
```
[[@lafourcade15EnigmesLudiques2022]], p67

A tout moment, on peut vérifier le type d'une variable avec la commande type(variable)
Le typage de Python est dynamique : le type des variables n'est pas seulement vérifié lors de la compilation du code (contrairement à C) mais chaque fois que la variable est lue, ce qui rend les erreurs de typage plus facile à détecter.

## concaténer

```python
nom_langage = "Python"
sentiment = "J'aime"
print(sentiment +' '+nom_langage)
```
voir [[échapper]]

concaténer des objets différents, nécessité de convertir les entiers en chaînes de caractère : 

```python
nom_langage = "Python"
sentiment = "J'aime"
annee = 2025
annee_str = str(annee)
print('en ' + annee_str+',' + sentiment +' '+nom_langage)
```
(fonction string)

autre possibilité : 

```python
nom_langage = "Python"
sentiment = "J'aime"
annee = 2025
annee_str = str(annee)
print('en ' + str(annee)+',' + sentiment +' '+nom_langage)
```
ça va bien si on n'a pas besoin de réutiliser annee en format numérique par la suite.

pour repasser l'objet de la variable annee en entier : 

```python
int(annee)
```

flottant (float) = nombre décimal

```python
i = 2025
f = float(i)
print(f)
```

```python
import statistics
note1 = float(input("note1 : "))
note2 = float(input("note2 : "))
note3 = float(input("note3 : "))
data = [note1, note2, note3]
moyenne = statistics.mean(data)
print(moyenne)
```
## convertir de l'ASCII en caractères

chr()
donne le caractère d'un nombre [[ASCII]] : 
chr(97) donne *a* [[@lafourcade15EnigmesLudiques2022]]

```python
resultat=""
fichier = open('enigme1.txt','r')
for ligne in fichier :
	for mot in ligne.split():
		resultat = resultat + chr(int(mot))
print(resultat)	
```
Utiliser avec le <a href="enigme1.txt" download>fichier de l'énigme</a> 

## séparateur

faire une ligne de séparateur : 

```python
print('-'*10)
```


## commenter

Les guillemets pour du texte long
```python
"""
created by Damien Belvèze on Tue Nov 26
email : damien.belveze@univ-rennes.fr
licence : GPL
"""
```
le croisillon (#) pour commenter dans le code ligne après ligne. 

```python
nom_langage = "Python"
sentiment = "J'aime"
# annee = 2025
annee = input("quelle année sommes-nous ?") #choix de l'espace  
annee_str = str(annee)
print('en ' + str(annee)+',' + sentiment +' '+nom_langage)
```

# charger des modules

soit import (ensemble du module)
soit import d'une fonction provenant d'un module : 

*from* module *import* fonction

Ne pas oublier de relier la fonction à son contexte, c'est à dire au module dont il est extrait : 

```python
import math
print(math.pi)
```

Si on n'a besoin que d'une fonction il n'est pas nécessaire d'importer tout le module. 

pour avoir des infos sur une fonction, taper dans le shell

``help(module.fonction) ``

par exemple pour la fonction randint dans le module random : 

```python
help(random.randint)
# permet d'avoir des informations sur la façon dont on doit utiliser la fonction randint du module random
```
## environnements virtuels

voir [[environnement virtuel#virtual env pour Python]]
pour créer et activer un environnement virtuel

# types composés de variables

une variable peut-être un tuple, une liste, un dictionnaire et parfois une chaîne.

un tuple n'est pas modifiable ; si je veux ajouter ou retrancher quelque chose, ce n'est pas possible. 
un tuple sert à créer en début de programme des informations qui vont rester intangibles. Un tuple peut servir à faire un menu d'options, dans la mesure où ces options ne vont jamais changer. 
Faire une liste des chefs-lieux de canton d'un département consiste en langage de programmation à faire un tuple car leur nombre est fini et intangible (dans une certaine mesure, celle du programme).

les parenthèses sont une représentation simplifiée du type tuple. 
Les listes utilisent des crochets

pour savoir si t est un tuple ou une liste : 

```python
type(t)
```

Une liste peut en revanche être modifiée. 

pour créer une liste vide : 

```python
listeVide = list()
```
Possibilité de décomposer une variable en sous-ensembles

```python
legumes = ('poireaux', 'tomates') # il s'agit d'un tuple
fruits = {'pomme':'apple', 'banane':'banana'} # il s'agit d'un dictionnaire 
# pomme est une clé
```

```python
legumes[0]
# invoque le premier item de la liste legumes (actuellement 'poireaux')
# le premier item d'une liste est le 0, car ça permet de compter une dizaine de 0 à 9
fruits['pomme']
# invoque l'instance de pomme (actuellement 'apple')

```

possibilité de prendre le dernier item d'une longue liste : 

```python
legumes(-1) 
# prend le premier élément en partant de la fin, c'est à dire le dernier (-2 = avant-dernier)
```

```python
liste[0:2] # prend la liste de 0 à 2 (2 est exclu)
```

 - tuple : ( )
- liste : \[ ]
- dictionnaire : { }

dans tous les cas, le séparateur est une virgule (,)

pour créer un dictionnaire, utiliser la commande dict

```python
recette = {'farine':200, 'pommes':3, 'sucre':150, 'beurre':100}

recette['sucre']
```
```python
recette['legumes'][0] # prend le premier élément de la liste légumes
```

## append

```python
recette.append('cannelle')
# ajoute un objet à la fin de la liste (on ne peut pas utiliser append pour un dictionnaire)
```
contraire d'append : remove 
```python
recette.remove('sucre')
# ajoute un objet à la fin de la liste (on ne peut pas utiliser append pour un dictionnaire)
```

ajouter à un dictionnaire : 
```python
recette['pruneaux']=6
# si la clé existe déjà, sa valeur est remplacée par 6, si la clé n'existe pas, elle s'ajoute au dictionnaire
```
pour enlever une valeur dans un dictionnaire, on peut utiliser la fonction *pop* ou *remove*

*pop* enlève à partir de la position dans une liste, *remove* enlève à partir de la valeur dans une liste ou un dictionnaire

```python
fruits.remove('pomme') # enlève 'pomme' à la liste
recettes.remove('pruneaux') # enlève 'prunaux' au dictionnaire 
```

```python
recettes = {'d':fruits}
append.fruits(citrons)
```

on va pouvoir parcourir les listes, leur appliquer des traitements en utilisant de l'itération (boucles et itérations : boucles *for* et boucles *while*)
# boucles et itération

## random

```python
from random import randint

groupe = randint(2,10)

print(f"le prix pour le groupe sera {groupe*5}")
```



à partir de Python 3.6, possibilité d'utiliser une f-string

```python
print(f"{nom}.{prenom}@univ-rennes{universite}.fr")
```
autre avantage de la f-string : pas nécessaire de faire de la conversion de types dans les variables. la f-string ne prend en compte que des chaînes de caractères, donc les variables qui ont pour objet des entiers sont automatiquement rendus comme des chaînes de caractères.

possibilité de faire des calculs dans l'accolade

```python

for l in legumes:
#ne pas oublier de mettre les deux points à la fin de la ligne for (cf. bloc d'instruction)
	print(l) # ne pas oublier l'indentation pour indiquer que print est une action de for (il peut y en avoir plusieurs)
```

```python

for l in legumes:
#ne pas oublier de mettre les deux points à la fin de la ligne for (cf. bloc d'instruction)
	print(str(float(l) # ne pas oublier l'indentation pour indiquer que print est une action de for (il peut y en avoir plusieurs)
```

pour les dictionnaires : choisir de traiter les clés, les valeurs ou les deux
```python
for r in recette.keys():
	print(r)
	# afficher les clés
```

```python
for r in recette.keys():
	print(recette[r])
	# afficher les valeurs des clés
```

équivalent : 

for r in recette.values():
print(r)

```python
for r in recette.keys():
	print(f"cle = {r}, valeur = {recette[r]}")
	# afficher les clés et leurs valeurs
```

```python
for k, v in recette.items():
	print(f"cle ={k}, valeur = {v}")
# affiche les clés et leurs valeurs	
```

## range

```python
range(0,10)
for r in range(10):
	print(r)
# O inclus, 10 exclu
```

## len

*len* permet d'avoir la longueur d'une liste


# afficher des instructions


le module input() va permettre d'afficher une instruction et d'attendre que l'utilisateur frappe une touche

```python
input("frappez une touche de votre clavier pour afficher l'ensemble des notes de votre coffre")
```

```python
nom_langage = input("quel langage tu aimes?")
```

## combinaisons des fonctions précédentes

```python
"""
créer un outil d'assistance à la conjugaison pour le présent de l'indicatif des verbes du premier groupe
-er [chanter, aimer // aller]
demander à l'utilisateur le verbe dont il souhaite la conjugaison
"""
verbe = input("quel verbe : chanter|aimer")
liste = {
"je":"e",
"tu":"es",
"il/elle/iel" : "e",
"nous" : "ons",
"ils/elles" : "ent"
}
radical = verbe.removesuffix("er")
for k,v in liste.items():
	print(f"{k} {radical}{v}")

```

```python
pronom = ['je','tu','il','nous','vous','ils']
term = ['e','es','e','ons','ez','ent']
radical = verbe.removesuffix("er")
for p in range(0,6)
	print(f"{pronom[p]} {radical}{term[p]}")
# p n'est que la position des éléments.
```

# conditions

le signe = est un signe qui permet l'**affectation** par exemple d'une valeur à une variable : 
```python
x = 3
```
le signe == est un test de condition
```python
if x == 3 :
	print(x)
```
chaque condition doit être suivie du signe : et d'une indentation à la ligne suivante.


```python
verbe = input("quel verbe")
pronom = ['je','tu','il','nous','vous','ils']
term = ['e','es','e','ons','ez','ent']
radical = verbe.removesuffix("er")
if verbe.endswith("er") == True :
	for p in range(0,6) :
		print(f"{pronom[p]} {radical}{term[p]}")
elif verbe.endswith("ir") and not verbe.endswith("oir"):
	print("c'est un verbe du deuxième groupe")
else :
	print("ceci n'est pas un verbe du premier groupe")
```




```python

input(age ="votre âge")
if age < 18:
	print("vous êtes mineur")
elif 18 < age < 30:
	print("vous n'êtes pas encore trentenaire")
else: 
	print("vous avez plus de trente ans")
```
Veiller aux indentations entre if, elif et else et aux doubles points après ces mots
([[@azoulaiPythonRoman2024]], p119)

## While

*for* sans fin avec un *if* implicite. 
risque de ne jamais sortir de la boucle et de saturer la mémoire de l'ordinateur.  

ne pas oublier les : et l'indentation après while comme pour for et if
```python
i=0
while (i < 10):
	print(i)
	i=i+1
```
imprime 123456789 puis s'arrête

équivalent avec *for*

```python
for i in range(10):
	print(i)
```
voir [[@lafourcade15EnigmesLudiques2022]]

```Python
verbe = input("quel verbe tu veux conjuguer")
while not verbe.endswith("er") :
	verbe = input("quel verbe tu veux conjuguer")
print("continue")
```

deviner le nombre secret 

```python
nombre = input("donne un nombre")
while not int(nombre) == 23 :
if int(nombre) < 23 :
	nombre = input("c'est un nombre plus élevé, réessaie")
else :
	nombre = input("c'est un nombre moins élevé, réessaie")
	print("gagné")
```

générer des numéros de carte bleue virtuels : 

```python
from random import randint
def creer_cb() #définit la fonction qui crée la carte bleue
	cb = str() # définir les numéros de la carte comme une chaîne de caractère pour y ajouter des espaces (qui ne sont pas des entiers)
	for i in range(0,4): # Deux bloucles enchevêtrées
		for i2 in range(0,4):
			n = randint(0,9)
			cb = cb+str(n)
		cb += " " # pour ajouter un espace à cb à la fin de chaque groupe
  return cb.rstrip #retourne le résultat de la fonction et y retranche le dernier caractère (l'espace surnuméraire)
a = creer_cb()
b = creer_cb()
print(a) # affichage du premier numéro de CB
print(b) # affichage du second numéro de CB
```

créer un programme qui compte le nombre de voyelles dans une chaîne donnée par l'utilisateur

```python
voyelles = ['a','e','i','o','u','y']
compteur = int()
a = input("veuillez saisir un texte : \")
for i in range(0,len(a)):
	if a[i] in voyelles:
		compteur += 1
print(compteur)
```


```python
i = 1
while i<6
print(i)
i += 1
```
imprime 1,2, 3, 4, 5
(imprime i qui augmente d'une unité, tant que i est inférieur à 6 puis s'arrête) ([[@azoulaiPythonRoman2024]], p121)

```python
nom = input("quel est votre nom ?").lower()

prenom = input("quel est votre prénom ?").lower()

while True:
	try: 
		universite = int(input('quelle est votre université : taper 1 pour Rennes 1, 2 pour Rennes 2'))
		break
	except:
		print("option non valide!")

print(prenom +'.'+nom+'@univ-rennes'+ str(universite) + '.fr')

```


# sélectionner un fichier avec une interface graphique

## tkinter

interface graphique présente par défaut dans Python

````shell
pip install tk
````

````python
import Tkinter
from tkinter.filedialog import askdirectory
path = askdirectory()
````
(source : https://youtu.be/YTOUBGHEgZg)

## easygui

easygui est un [[package]] Python qui permet de proposer à l'utilisateur de faire un choix dans une interface graphique. 

Installation : 

````shell
pip install python
````

écrire un menu pour un choix oui / non
``
```python
import easygui
easygui.ynbox('voulez-vous continuer', 'Titre', ('oui', 'non'))
```

Le titre s'affiche en haut du pop-up

faire sélectionner un fichier dans un répertoire

````python
import os
path = "[C://Users//dbelveze//Desktop//gfg](C://Users//dbelveze//Desktop)"
dir_list = os.listdir(path)
`````


faire choisir un fichier de cette liste

````python
import easygui
msg = "sélectionnner le fichier"
title = "sélection du fichier"
choices = [dir_list]
choice = choicebox(msg, title, choices)
`````

# afficher la liste de tous les fichiers selon leur format
````python
import os
# traverse whole directory
for root, dirs, files in os.walk(r'D:'):
    # select file name
    for file in files:
        # check the extension of files
        if file.endswith('.md'):
            # print whole path of files
            print(os.path.join(root, dirs, file))
         else:
input("il n'y a pas de note dans ce coffre dans le bon format")

``````

cherche et affiche tous les documents en markdown dans le disque D: (recherche récursive dans tous les dossiers)

Autre possibilité, utiliser glob

````shell
pip install glob2
`````

````python
list_notes = glob.glob(os.path.join(path, '*.md'), recursive=True)
`````
cherche dans le répertoire Path et les dossiers sous-jacents tous les fichiers qui sont en markdown (md)

## vérifier qu'un fichier au moins d'une certaine extension se trouve dans un dossier

````python
import os
import tkinter
from tkinter.filedialog import askdirectory
path = askdirectory()
if not any(File.endswith('.md') for File in os.listdir(path)):
	print("pas de note trouvée")
else:
    input("sélectionner un fichier")
`````

Si le fichier avec la bonne extension n'est pas présent, demander à l'utilisateur de charger ailleurs un fichier avec la bonne extension : 



# chercher un document sur Internet et le télécharger 

Cela se fait avec le module wget de Python
Pour installer le module : 

````shell
import wget
url = "https://www.zotero.org/styles/nature"
wget.download(url, "C://Users//dbelveze//Desktop")
`````

# créer un dossier avec Python

On va utiliser OS comme toute commande de Python qui met en jeu le système d'exploitation

````python
import os
os.mkdir('biblio')
`````
crée un dossier biblio
```

# ouvrir, écrire, modifier, fermer un fichier

Ouvre un fichier et le lit tout d'un coup
"r" = read ([[@SchultzPythonpourSHS2021]], p81)
> ouvre un fichier avec la fonction *open* en donnant le chemin du fichier et le mode lecture "r" puis stocke le lien vers le fichier ouvert dans la variable **fichier** 


``````python
fichier=open("data1.txt", "r")
contenu=fichier.read()
``````

``````python
fichier.close()
print(contenu[0:40])
``````

ferme le fichier, imprime les premières lignes (de la première ligne à la ligne 40)

# modifier des caractères dans un fichier

``````python
# ouvre et lit le fichier titre.md
with open('titre.md', 'r') as file :
  filedata = file.read()

# remplace dans ce fichier le e par un a
filedata = filedata.replace('e', 'a')

# écrit un fichier avec le texte modifié dont le nom est file.txt
with open('file.txt', 'w') as file:
  file.write(filedata)
``````

# remplacer une chaîne de caractères par une autre dans plusieurs fichiers d'un même dossier

```python
import os

import fileinput

def replace_string_in_files(directory, old_string, new_string):

    # List all Markdown files in the specified directory

    markdown_files = [f for f in os.listdir(directory) if f.endswith('.md')]

  

    # Iterate through each Markdown file and replace the string

    for file_name in markdown_files:

        file_path = os.path.join(directory, file_name)

  

        # Use fileinput for in-place editing

        with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:

            for line in file:

                # Replace the old string with the new string

                print(line.replace(old_string, new_string), end='')

  

    print(f'String "{old_string}" replaced with "{new_string}" in all Markdown files.')

  

# Replace "auteurs" with "author" in all Markdown files in the current directory

replace_string_in_files('.', 'auteurs', 'author')
```

# insérer une chaîne de caractères en début et en fin de fichier


```python
import os

def append_to_files(directory, file_extension, text_to_append):
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                original_content = file.read()

            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(text_to_append + original_content + text_to_append + '\n')

# Specify the directory containing your files, the file extension, and the text to append
directory_path = 'D:/Home/dbelveze/Desktop/biblio/references'
file_extension = '.md'
text_to_append = '---'

append_to_files(directory_path, file_extension, text_to_append)

```
Dans l'exemple ci-dessus, il s'agissait d'ajouter "---" au début de chaque fichier de référence en markdown contenu dans le dossier references (contenu dans le dossier biblio où se script se trouvait) suivi (au début) ou précédé (à la fin) d'un retour à la ligne ('\\n')

L'ajout de **encoding='utf-8'** a été nécessaire pour régler une erreur du à la présence de caractères spéciaux dans les fichiers en question.  

commande pour exécuter le code :

```bash
python ./code.py
```


# spliter des chemins (path)

Les fichiers sélectionnés viennent souvent avec leur path (chemin)
Par exemple : 
D:/users/dbelveze/dossier/texte.txt
Afin de ne conserver que texte.txt

déterminer un chemin et utiliser la fonction basename




```python


````python
import os.path
path = "D:/users/dbelveze/dossier/texte.txt"
file = os.path.basename(path)
`````
Pour séparer le nom de fichier de l'extension, utiliser la fonction split()

````python
notefull = notepath.split('.')
notename = notefull[0]
noteext = notefull[1]
``````
notename est le nom de fichier sans l'extension. Pour rappel l'élément en première position d'une liste dans Python occupe toujours la place 0.

# supprimer des lignes qui contiennent une suite de caractères

Programme utilisé et testé dans le cadre de la [[faire une revue de littérature avec Zotero|revue de littérature avec Zotero]]

Contexte : les exports en RIS des bases de données comme Cochrane ou WOS contiennent des descripteurs qui sont indésirables (KW) lors de l'import des fichiers dans [[Zotero]]. Pour plus de clarté, aucun marqueur ne doit être hérité au cours de l'import. 
Il s'agit donc d'effacer ces descripteurs qui se présentent comme suit dans les fichiers d'import : 

KW   - descripteurs

Le script suivant permet de générer un fichier (output.txt) qui copie toutes les lignes du fichier d'import (input.txt) à l'exception de celles qui contiennent la chaîne de caractères "KW   -" (prendre en compte le tirer de telle sorte de ne pas éléminer de faux positifs, par exemple dans les noms d'auteur)

``````python
with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
    for line in inp:
        if 'KW  -' not in line:
            out.write(line)
``````


# créer un environnement virtuel pour Python


# créer un installateur pour Windows à partir d'un script pour Python

cela se fait avec avec le module pyinstaller ([source](https://www.geeksforgeeks.org/convert-python-script-to-exe-file/))
Installer Pyinstaller
taper ensuite la commande suivante : 

ouvrir une fenêtre powershell (flêche haut- clic droit) dans la fenêtre où apparaît le script python. 
Dans powershell, 

````shell
pyinstaller --onefile -w script.py
`````

La localisation du fichier .exe se trouve en bas du résultat. 

# créer une liste csv d'utilisateurs avec mots de passe

cette liste est créée en vue d'un import dans RAGaRenn

```python
import pandas as pd
import random
import string

email_list = "angelique.riffault@univ-poitiers.fr, aurelie.hilt@univ-poitiers.fr, alice.henocq@univ-tours.fr, alexia.neupont@univ-poitiers.fr, thomas.pierron@univ-poitiers.fr, marine.lamiaud-bregeon@univ-lr.fr, lea.maubon@univ-poitiers.fr, helene.hubert@univ-poitiers.fr, stephanie.tisserand@univ-lr.fr, anne.azanza@univ-tours.fr , christele.herve@univ-tours.fr, patrick.de.martel@univ-poitiers.fr, magali.meiffren@univ-tours.fr, pascal.pinoteau@univ-tours.fr, emmanuel.collier@campus-condorcet.fr, celine.fondaneche@unilim.fr, carine.lavigne@univ-lr.fr, audrey.werquin@univ-orleans.fr"
# Convert the string into list of emails
emails = [email.strip() for email in email_list.split(',')]

# Create DataFrame from the list and add 'Name' column with extracted names
df = pd.DataFrame(emails, columns=['Email'])
df['Name'] = df['Email'].apply(lambda x: " ".join(x.split('@')[0].split('.')).title())

# Function to generate a random password of 10 characters
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Add 'role' and 'password' columns with empty values and random passwords respectively
df['Role'] = 'User'
df['Password'] = df.apply(lambda _: generate_password(), axis=1)

# Reorder the DataFrame columns as specified
df = df[['Name', 'Email', 'Password', 'Role']]

# Save the DataFrame to a CSV file
df.to_csv('user_data.csv', index=False)
```


---
title: Linux commandes de base
subtitle:
author: Damien Belvèze
date: 11-04-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: [linux, programmation]
---

![](images/linux_basic_commands.jpg)

# gérer les dossiers et les fichiers

## Lister les fichiers

lister les fichiers d'un répertoire

`ls`

(équivalent du GetChildItem ou gci pour [[shell|powershell]])

lister tous les fichiers textes dans un répertoire

`ls *.txt`

lister les fichiers (également cachés)

`ls -a`

lister les dossiers en même temps que les fichiers

`ls -p`

afficher les dossier et les fichiers avec les droits sur ces fichiers

`ls -al`

## naviguer dans les fichiers et les dossiers

A noter : les slashs ne sont pas les mêmes dans un terminal Windows (MS-DOS ou powershell par exemple) ou un terminal Linux ou Git-Bash : 
Accéder au répertoire sous Linux : 

``cd`` permet d'aller sous tel ou tel répertoire (équivalent Powershell : ``Set-Location`` ou ``sl``)

`cd /users/ianmilligan1/mallet-2.0.7`

et sous Windows :

`cd c:\mallet-2.0.7\`

(le chemin change aussi /users/nomdelutilisateur/répertoire sous Linux, c:\\répertoire sous Windows

Se positionner sur un dossier:

``cd dossier``

ouvrir un dossier

`cd`seul permet de revenir à la racine

revenir au dossier parent : 

``cd ..``

remonter l'arborescence de deux niveaux : 

``cd ../..`` / trois niveaux : ``cd ../../..``

remonter à la racine : 

``cd /.``

~ est un raccourci pour désigner le dossier de l'utilisateur

``cd ~/etc/config`` est l'équivalent de ``cd /home/nomutilisateur/config``

Afficher le dossier où l'on se trouve

``pwd``

pwd = publication working directory : l'espace de travail

pour revenir au Home avec CD : 

`cd --`

donne le chemin absolu du dossier dans lequel on se trouve. 


voir [[architecture des fichiers Linux]]


### chercher des fichiers

````bash
$ find . -name "log.txt"
````
cherche dans le répertoire courant le fichier dont le nom est log.txt

````bash
$ find /home/linuxopsys -iname "log.txt"
````
Même chose que précédemment mais sans tenir compte de la casse (éviter de ne pas trouver un fichier du même nom à cause d'une majuscule)
````bash
$ find /home/linuxopsys/ -name "*.sh"
````
cherche dans le répertoire courant les fichiers qui ont pour extension *sh*

Chercher des fichiers ayant plusieurs extensions dans plusieurs dossiers : 

![](images/find_files_directories.jpg)

 -  type f : cherche uniquement des fichiers, pas des dossiers (voir plus haut) 
 -  \( and \)\` : nécessaire pour que le -type f soit appliqué à tous les arguments
 -   -o : opérateur booléen OR 
 -   -iname : comme -name, mais insensible à la casse
 
### chercher des fichiers qui comportent une chaîne de caractères (avec grep)



````bash
find / -type f -exec grep -il "linux" {} \;
````
cherche des fichiers qui comportent le mot *linux*

#### arguments de grep

- -i = pas sensible à la [[casse]]
- -r = récursif
- -l = liste seulement les fichiers qui comportent la suite de caractères indiquée
```
grep -irl linux
```

ou

```
grep -i -r -l linux
```
 
## Créer un fichier

``touch fichier.txt``

*touch* sans argument crée un fichier. Avec -c ou -h il permet de changer le [[timestamp]] d'un fichier

pour connaître des détails sur un fichier (timestamp et droits), faire la commande suivante : 

```bash
ls -lt <chemin ou nom du fichier>
```
permet de savoir quand le fichier a été accédé la dernière fois.
On peut aussi créer un fichier en écrivant une ligne : 

``echo "voici mon texte" >> fichier.txt`` 

crée un fichier intitulé fichier.txt dans lequel on trouve la ligne *voici mon texte*

## Créer un dossier

### créer un dossier

`mkdir nomdudossier`

possibilité de créer plusieurs dossiers en même temps de même niveau 

`mkdir nomdudossier1 nomdudossier2 nomdudossier3`

ou une arborescence de dossiers

`mkdir -p nomdudossier1/nomdudossier2/nomdudossier3`

### chercher un dossier

````bash
$ find /home/linuxopsys/ -name "linux" -type d
````
cherche dans le répertoire courant le dossier qui a pour nom Linux

chercher les dossiers vides : 

````bash
$ find /home/linuxopsys -type d -empty
````

chercher les dossiers cachés : 
````bash
$ find /home/linuxopsys/ -type f -name ".*"
````

Les dossiers cachés se présentent toujours avec un point à l'initiale (.dossier)



## Copier et déplacer des fichiers

`cp nomdufichier nomdudossier/`

copier des dossiers 

utiliser l'argument -r (recursive) pour indiquer qu'on veut copier le dossier mais aussi tous les éléments qu'il contient.

`cp -r nomdudossiersource/ nomdudossierdestination/`

déplacer des fichiers

`mv nomdufichier nomdudossier/`

déplacer des dossiers

`mv -r nomdudossiersource/ nomdudossierdestination/`

attention, on ne peut pas changer des dossiers & fichiers depuis le répertoire actuel : 

génère une erreur du type : impossible de déplacer '.' vers '/opt/mattermost/.': Périphérique ou ressource occupé

You're trying to move the current working directory **while you're inside it** — which Linux does not allow, because it would involve deleting or moving a directory that is "in use."

faire un cd pour aller au dossier parent, modifier le chemin en conséquence du dossier à déplacer et refaire la commande, pour envoyer vers opt, il faut être sudoer.
## renommer des fichiers ou des dossiers

`mv anciennomdudossier/ nouveaunomdudossier/`

La commande move est utilisée à la place de rename : si le nouveaunomdudossier n'existe pas, alors l'anciennomdudossier sera remplacé par le nouveaunomdudossier
## Supprimer des fichiers ou des dossiers

### commande remove (rm)

la commande `rm`permet de supprimer des fichiers ou des dossiers. Pour supprimer à la fois un dossier et son contenu, utiliser `rm -r dossier`

équivalent Powershell de ``Remove-Item`` également utilisable sous sa forme abrégée ``rm``

`rm -f`: suppression de fichiers protégés en écriture : à manier avec précaution

**attention la suppression avec rm est définitive**: pas de corbeille ou de possible restauration.

### supprimer des fichiers volumineux

````bash
$ find /home/linuxopsys/ -type f -size +45000k -exec ls -l {} \; | awk '{ print $9 }' | xargs rm -i >/dev/null
````
efface dans le répertoire Linuxopsys les fichiers dont la taille excède 45000 ko


### supprimer des fichiers vides
````bash
$ find /home/linuxopsys/ -empty -delete
````
efface dans le répertoire Linuxopsys les fichiers vides

## retrouver un fichier

`locate document`

renvoie tous les fichiers qui ont document dans leur nom avec le chemin pour les localiser

(par exemple /etc/usr/bob/document.txt)

Pour mettre l'index de ces fichiers et avoir des résultats à jour : `updatedb`

Commande *find* permet de chercher tous les documents correspondants à certaines caractéristiques : 

`find . -name "twi*" -d`

permet d'afficher à partir du dossier courant (.)la liste des dossiers (-d) dont le nom (-name) commence par les trois lettres twi (twi*)

`find . -name "photo*" -exec cp {} {}.bak \;`

trouve et copie (avec une extension .bak) tous les fichiers dont les noms débutent par "photo"

afficher la liste des fichiers qui ont une taille supérieure à 10mio (mebibytes) (1024*1024 octets)

`find . -size +10M`

-size : argument qui spécifie de chercher par taille
+ = plus de (on peut utiliser - ou =)
M: unité (en l'occurrence Mio) pour des octets (bytes), on utilise c



## Afficher le contenu d'un fichier

`cat fichier`

affiche le contenu d'un fichier, idéal pour un fichier court. 
cat est l'abréviation de concatenate, donc peut servir à concaténer deux fichiers. 

`cat fichier1 fichier2`

concatène les fichiers 1 et 2

`cat fichier1 fichier2 > fichier 3`

concatène le fichier 1 et 2 dans un nouveau fichier 3

afficher la version de Linux installée sur l'ordinateur : 

```shell
cat /etc/os-release
```
(https://mastodon.social/@nixCraft/115045071992936992)

Pour afficher des textes longs et ainsi naviguer dedans, utiliser la commande **less**

Pour poursuivre sur l'écran d'affichage : 

parcourir le fichier à l'aide des flèches Haut/Bas, mais aussi faire de plus grand sauts avec les flèches Page Up/Page Down ;

quitter l'interface avec la touche q;

g permet de se rendre au début du fichier ;

G permet de se rendre en fin de fichier ;

écrire / suivi d'un mot permet de rechercher le mot dans le document.


par exemple, l'action `less /var/log/syslog`affiche la liste des dernières connexions au serveur. 

Pour ne retenir que 10 lignes depuis le début du fichier, utiliser la commande `head -n 10 /var/log/syslog`; à l'inverse, pour retenir les 10 dernières lignes du fichier, utiliser la commande `tail -n 10 /var/log/syslog`


## utiliser la commande *sed* pour modifier du texte

voir [tutos en ligne](https://www.malekal.com/commande-sed-utilisation-et-exemples/)



## Utiliser l'éditeur de texte nano

`nano nomdufichier`

modifier le fichier, enregistrer avec Ctrl+O et Entrée
Quitter avec Ctrl+X


## manipuler des fichiers

### trouver des expressions avec grep : 

`grep "^anti-*" /usr/share/dict/french`

affiche tous les mots commençant par anti- du dictionnaire français présent dans share.

`grep -r "noir"`(avec le -r de la récursivité déjà vu plus haut) : affiche tous les dossiers dont le nom comporte le mot noir et dans ces dossiers tous les fichiers dont le nom et le contenu comportent le mot "noir"

## compter le nombre de mots, lignes, caractères d'un fichier

`wc document.txt`

si on a le résultat suivant : 

6 56 340 document.txt

cela signifie que notre document comporte 6 lignes, 56 mots et 340 caractères

`sort document.txt`

trie les lignes du document.txt par ordre alphabétique (ordre par défaut)

récupérer la liste de tous les mots français qui comporte le w

`grep "w" /usr/share/dict/french > ~/Documents/mots_w.txt`

envoie tous les mots du dictionnaire français qui comportent un w dans un fichier texte présent dans les documents

` wc ~/Documents/mots_w.txt`

affiche le nombre de lignes et de mots (équivalent ici) de ce fichier. 594 mots comportent la lettre w


# chaîner des commandes

on procède avec le [[pipe]] (|)



# mettre à jour des paquets

lister les paquets pouvant être mis à jour

`apt list --upgradable`

mettre à jour la liste des paquets

`sudo apt update`

mettre à jour les paquets pouvant être mis à jour

`sudo apt upgrade`


# installer des packages

Les [[package|packages]] pour Linux arrivent assez souvent sous la forme d'archives (tar.gz)
Pour extraire les dossiers d'une archive : 

````shell
tar -xvf nomdufichier.tar.gz
````

même chose pour les packages en tar.bz2 : 

````shell
tar -xvf nomdufichier.tar.bz2
````

Si l'application se présente directement sous l'apparence d'un paquet [[Debian]] (.deb)

````shell
deb -i nomdufichier.deb
````

installation d'un [[driver|pilote]] pour une imprimante
```bash
cd chemin/vers/le/fichier/pilote-5.40-1-deb.tar.gz

tar -xzf pilote-5.40-1-deb.tar.gz  
cd pilote-5.40-1-deb/

./install.sh
```
(mail Pierre d'Actux)

# interrompre un process

```shell
top #affiche la liste des process en cours, interrompre avec Ctrl+C quand on a noté le process
kill -9 <PID process> # interrompt le process (utiliser son PID) -9 à utiliser si le programme est bloqué
```

# Charger des applications qui ne fonctionnent que sous Windows sur un ordi Linux

voir [[Wine]]




# mémo Linux

par [[Julia Evans]]

![[linux_Julia_Evans.pdf]]


# Bibliographie

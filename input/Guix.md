---
title: Guix
subtitle: 
id: 20240725_Guix
author: Damien Belvèze
date: 2024-07-25
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - guix
tags:
  - donnees_recherche
  - programmation
---
Guix (issu du langage Guile et du [[gestionnaire de paquets]] [[Nix]]) est un gestionnaire de paquets qui permet de sauvegarder des environnements pour assurer la reproductibilité du code quelque soit les caractéristiques de la machine hôte sur lequel on exécute le code. 

- pour [[Nix]] avec [[R (logiciel)|R]], voir [[Rix]] ou bien 
- pour [[Guix]] avec [[R]], voir [[R avec Guix]] (Attention : R est disponible sur Guix mais pas Rstudio)

Guix est écrit dans le langage de programmation [[scheme]], un langage dérivé de [[Lisp]], l'un des plus vieux [[langages informatiques]] qui existent. 

Présentation de Simon Tournier https://www.youtube.com/watch?v=E4mo1B6y5_k

[distribution RDE basée sur Guix system](https://trop.in/rde/)

# installation


https://gricad-doc.univ-grenoble-alpes.fr/hpc/softenv/guix/

voir aussi l'installation de system crafters : 
https://systemcrafters.net/craft-your-system-with-guix/installing-the-package-manager/




1. en téléchargeant Guix depuis GNU
Exécuter ces commandes en root pour que ça fonctionne (https://guix.gnu.org/manual/fr/html_node/Installation-binaire.html)

```
cd /tmp
wget https://git.savannah.gnu.org/cgit/guix.git/plain/etc/guix-install.sh
chmod +x guix-install.sh
./guix-install.sh
```

A faire ensuite : dans ~/.profile, ajouter : 

```text
# set path for guix in shell 
GUIX_PROFILE="$HOME/.guix-profile" ; \
source "$GUIX_PROFILE/etc/profile"
```

A l'endroit suivant
/var/guix/profiles/per-user/
créer un dossier au nom de l'utilisateur, puis donner à l'utilisateur la propriété sur ce dossier
```shell
cd /var/guix/profiles/per-user/
mkdir dbelveze
sudo chown dbelveze dbelveze
```
(sur 'chown' voir [[Gestion des utilisateurs sous Linux#changer les droits des utilisateurs et des groupes]])

2. Charger Guix avec apt
```
sudo apt install guix
```

source : https://une-tasse-de.cafe/blog/guix/#installer-guix

# Commencer avec guix

obtenir des packages guix et des mises à jour de sécurité

```shell
guix pull
guix package -u
```
$\newline$

# éditer un graph

```shell
guix graph --max-depth=6 python | dot -Tpng > graph-python.png
```
Cette commande illustre la liste des dépendances jusqu'au niveau 6 de [[Python]] 3.9

requiert le chargement préalable de Graphviz
```shell
sudo apt install graphviz
```




# bibliographie
$\newline$







---
title: Rix
subtitle: Présentation de Bruno Rodrigues de l'Université du Luxembourg (café Recherche Reproductible)
id: 20250613_Rix
author: Damien Belvèze
date: 2025-06-13
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - code_source
  - nixOS
  - R_logiciel
---
[Lien vers la présentation du Webinaire](https://www.recherche-reproductible.fr/webinaires/2025/06/13/Nix-Rix.html)

Présentateur : Bruno Rodriguez, économiste de formation, travaille aujourd'hui à l'Université du Luxembourg (est luxembourgeois)

Le "puzzle de la reproductibilité du logiciel écrit avec R" est constitué de 4 pièces 
1. [[Renv]] (=environnement virtuel)
2. [[Docker]] (=conteneurisation)
3. [[Git|git]] (=contrôle de versio)
4. targets (optionnel) (=chaînage des opérations)


Targets permet de dépasser le stade des projets qui sont juste une succession de scripts que vous devez exécuter à la main, Targets est une librairie pour [[R (logiciel)|R]] un peu équivalente à [[Makefile|make]]

Rix permet de remplacer Renv, Docker et targets

Rix (écrit par Bruno Rodrigues) : gestion des paquets R, mais permet aussi d'écrire votre projet de telle sorte qu'il soit construit par Nix

Renv est un équivalent de Groundhog : Ces packages ne gèrent que les dépendances logicielles du script et pas la version de R utilisée pour le développer.

Avec le temps, votre système d'exploitation va évoluer et les dépendances système nécessaires pour charger ces packages ne vont plus être recompilées automatiquement.

Docker permet d'aller plus loin en gérant les dépendances système avec une version d'Ubuntu et de R-base.

Ce qui est reproductible c'est d'exécuter les conteneurs ; l'exécution d'un même conteneur (docker run) donnera toujours les mêmes résultats. Mais Docker en soi n'est pas reproductible.  Construire à partir du même code un conteneur ne donnera pas les mêmes images après un intervalle de temps.
La création d'une image docker n'est pas reproductible
Ce problème va être résolu avec Rix.
Rix est codé à partir de Nix.

Nix est fourni soit comme système d'exploitation en soi soit comme gestionnaire de paquets (c'est dans cette deuxième version qu'on va en parler ici)

Qu'est-ce qu'unpaquet ? tout logiciel (pas seulement un paquet R), voir [[dépendances]].
Qu'est-ce qu'un gestionnaire de paquets ?
L' app store sur iphone est un gestionnaire de paquets comme l'Android play store, comme Pip pour Python, un magasin de librairies destiné à un certain logiciel ou système d'exploitation.

les packages R et autres dépendances doivent être gérés explicitement.

le package R sf, par exemple utilise les dépendances systèmes gdal, proj et geos ; il faut gérer cela : pas seulement les dépendances mais aussi les dépendances de dépendances. 

Qu'est-ce qui faudrait faire pour qu'un gestionnaire de paquets soit reproductible ? La réponse est simple, mais la mise en pratique est complexe : il faudrait pouvoir installer avec R toutes les dépendances de R ainsi que les dépendances de dépendances, bref tout **l'arbre généalogique des dépendances**. 

Nix installe les logiciels et tout l'arbre généalogique. 
Nix va pouvoir remplacer à la fois Docker et Renv

Rix est une librairie R qui génère le fichier de configuration de Nix pour vous. 

Nix permet (contrairement à Docker) de faire des images reproductibles. 

Si on veut utiliser Rstudio, on doit l'installer via [[Nix]] (pas obligatoire pour l'IDE Positron)
Sous Windows il faut installer Nix à travers le [[WSL]] 

Les fichiers Renv.lock peuvent servir de points de départ. La fonction renv2nix() du package R convertit un fichier renv.lock en default.nix

Attention Renv peut fixer une version trop ancienne de R (prévoir d'ajouter override_r_ver = numéro de version)
Essayer de voir quelle version de R était disponible au moment où les paquets ont été utilisés 
possibilité d'ajouter un IDE (Rstudio, Radian ou VS Code, possibilité d'inclure Python, LaTeX ou Github. Restent encore des bugs pour les paquets en Julia)

génération du fichier default.nix

build avec rix::nix_build()
accéder à l'environnement de développement avec nix-shell

On peut installer des versions spécifiques de paquets 
on prend les paquets du CRAN on les patche pour qu'ils fonctionnent sur Nix, 99% des paquets du CRAN et de Bioconductor fonctionnent dans Nix. 
Si on tombe sur un paquet n'est pas comptable créer une issue dans le repo de Bruno Rodrigues

Possibilité d'inclure le fichier default.nix dans le Dockerfile pour reconstituer l'environnement créé avec nix.

Introduire Renv dans Rix : 

voir vidéo enregistrée par [Bruno Rodriguez](https://www.youtube.com/watch?v=6GbMyAceCDU)

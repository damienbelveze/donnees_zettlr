---
title: programmation lettrée
subtitle: 
id: 202212131519_programmation lettrée
author: Damien Belvèze
date: 13-12-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - literate programming
  - executable paper
tags:
  - programmation
---

# Bref historique

>Instead of imagining that our main task is to instruct a **computer** what to do, let us concentrate rather on explaining to **human beings** what we want the computer to do.

(Donald Knuth, 1984) [Source](https://towardsdatascience.com/literate-programming-reproducible-research-and-clean-code-docstrings-accf1a9f6661)

voir https://cours-376c29.gricad-pages.univ-grenoble-alpes.fr/#/notebook-literate-programming-1

distinguer **literate computing** et **literate programming** : 
- literate programming : j'écris du code et je le commente ligne après ligne
- literate computing : j'écris un texte et j'insère du code exécutable qui permet de générer les graphiques ou des expressions mathématiques : 

> A literate computing environment is one that allows users not only to execute commands but also to store in a literate document format the results of these commands along with figures and free-form text that can include formatted mathematical expressions. In practice it can be seen as a blend of a command-line environment such as the Unix shell with a word processor, since the resulting documents can be read like text, but contain blocks of code that were executed by the underlying computational system

(source : [[@dombrowskiIntroductionJupyterNotebooks2019]])


Premier essai en Sciences : en 2001, on peut encapsuler du code dans LaTeX. 
En 2016, [[R (logiciel)#Rmarkdown]], plus simple à apprendre prend le pas sur LaTeX dans le domaine de la bioinformatique. 
En 2022, naît [[Quarto]], qui poursuit le travail de R mais en l'ouvrant à davantage de [[langages informatiques|langages de programmation]] : Python, Observable javascript

# Principe de la programmation lettrée

La programmation lettrée alterne des "[[chuncks]]" de code avec du langage lisible par un humain (voir par exemple [[R (logiciel)|R]] et Rstudio)
Après [[compilation]] le document comporte à la fois le code, et le résultat du code sur les données sous la forme de graphique ou de tableaux commentés par des lignes de texte.

# reproductibilité

Ce qui assure la [[reproductibilité]] des expériences, c'est que le résultat obtenu (par exemple le graphique) est associé dans le document partagé au code exécuté, contrairement à ce qu'on observe sur Word où le graphique a été collé sans lien avec le logiciel qui a permis de le concevoir à partir des données.
Par ailleurs si le calcul doit être reconduit avec de nouvelles données, très peu de changements sont à opérer pour réitérer l'étude : il suffit d'ajouter ces données, d'exécuter le code et la publication tiendra compte des dernières données. C'est un gain de temps considérable. (plus à ce sujet  : [[@ziemannFivePillarsComputational2023]])





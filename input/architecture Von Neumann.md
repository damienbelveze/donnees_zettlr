---
title: 
subtitle:
author: Damien Belvèze
date: 15-03-2023
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---
Mis au point par John Von Neumann, né en 1903 en Hongrie, membre du [[Projet Manhattan]] au début des années 40.

Le principe de l'ordinateur est de regrouper les informations et les instructions pour traiter ces informations dans une mémoire et de séparer cette mémoire de l'unité de [[calcul informatique]].

architecture de la plupart des utilisateurs : 

- l'unité de calcul ou unité arithmétique et logique (ALU) : réalise les calculs
- unité de contrôle : ordonnance les calculs, pilote l'ALU
- mémoire : stocke instructions et résultats des calculs. dans les ordinateurs modernes on distingue la mémoire vive et le disque dur
- périphériques (entrée + sortie) qui permettent de relier ces calcults au monde extérieur. Parmi ces périphériques on compte habituellement un clavier (entrée) et un écran (sortie)

L'ALU et l'unité de contrôle constituent le processeur ([[CPU]]). Aujourd'hui, les processeurs ont souvent plusieurs ALU (processeur double-coeur = dispose de deux ALU)
[[@aschwandenScienceIsntBroken2015]]
L'architecture de Von Neumann a été mise en oeuvre en 1951 avec l'EDVAC qui succédait au premier ordinateur l'[[ENIAC]](source : [[@cardonCultureNumerique2019]], p21).

> Il conçoit notamment une séparation nette entre l'unité de commande, celle qui organise le flot séquencé des instructions, le programme codé, et l'unité arithmétique, celle qui exécute ces instructions (les calculs), soit plusieurs niveaux de mémoire ainsi que des organes d'entrée, de transfert et de sortie. C'est indirectement grâce à lui que le nombre de transistors (les interrupteurs de courant) d'un microprocesseur augmentera de manière faramineuse. 

(source : [[@azoulaiPythonRoman2024]], p100)

La séparation entre les cellules de calcul et celles qui comportent de la mémoire est énergivore. Pour réduire les émissions de gaz à effets de serre engendrés par les ordinateurs, il apparaît nécessaire aujourd'hui de remettre en cause cette séparation. 

> le principal responsable de l’inefficacité des processeurs actuels est l’architecture von Neumann, universellement adoptée. Plus précisément, la séparation physique des composants utilisés pour effectuer des calculs et stocker des données. En raison de cette séparation, les processeurs doivent récupérer des données de la mémoire pour effectuer des calculs, ce qui implique le déplacement de charges électriques, la charge et la décharge de condensateurs et la transmission de courants le long de lignes, qui dissipent toutes de l’énergie.

(source : [[@EtapeImportanteDans2023]])

Le molybdène, en tant que matériau semi-conducteur comporte la promesse de préserver l'informatique de cette déperdition d'énergie en concentrant à la fois la mémorisation des données et la puissance de calcul. 








# Bibliographie

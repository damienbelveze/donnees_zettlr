---
title: OStrails
subtitle: 
id: 20240917_OStrails
author: Damien Belvèze
date: 2024-09-17
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - OS trails
tags:
  - FAIRisation
  - données_recherche
---
(Maud Medves, INRIA Grenoble)

Projet [[EOSC]] : améliorer la manière dont on planifie, dont on suit et dont on évalue la production scientifique

1. Planning research = [[Plan de gestion des données|Plan de gestion de données]]
2. tracking research = knowleedge graph ([[Recherche data gouv]] considéré comme entités, affiliations des auteurs également considéré comme entités)
3. assessing research = [[FAIR]]ness

transformer des PDF en plans machine-actionable (JSON)
Intégrer les outils d'évaluation FAIR ([Fair checker](https://fair-checker.france-bioinformatique.fr/), [Fuji](https://www.fairsfair.eu/f-uji-automated-fair-data-assessment-tool), [Foops](https://foops.linkeddata.es/about.html)) dans les plans de gestion de données. Améliorer au fur et à mesure le degré de [[fAIR]]itude. 

24 pilotes (communautés qui vont tester ce qui sort d'OStrails, 19 pilotes nationaux + 5 pilotes thématiques les scientific clusters d'EOSC)

Comment le logiciel peut-il être intégré dans le PGD avec quel repository pour les rendre interopérables avec la plateforme Software Heritage. On pense d'abord à [[Software Heritage]]
[[HAL]] est aussi un candidat potentiel. . Est-ce que les PGD ne pourraient pas être publiés de manière automatique dans un repository type HAL. 

Qu'est-ce que c'est qu'un logiciel FAIR, comment on évalue le FAIR ? 

Problème de l'adaptation de FAIR au logiciel. FAIR est un principe généraliste qui devrait s'appliquer à tous les objets scientifiques mais une partie de la communauté considère que FAIR n'est pas adapté au logiciel. Certains scientifiques considèrent même que FAIR n'est pas adapté à tous les types de données. 

sur l'adaptation de FAIR au logiciel :[[@chuehongFAIRPrinciplesResearch2022]]
Il n'existe pas de version d'enregistrement du logiciel comme il existe une version d'enregistrement de la publication ou du jeu de données [[@lyonRobertoDiCosmo12]] : 

> This mutable \[of software\] nature makes it a quite singular object in the research landscape, requiring more a record of versions than the version of record which is central for publications.

Interface PGL sur Dmp-Opidor ?
C'est prévu pour les évolutions prochaines. 

L'interface d'OStrails, ça pourrait être opidor. 
Difficulté à faire remonter de la métadonnée de Software Heritage, mais via HAL c'est possible (fournir le HAL-ID)
argument en faveur d'archiver dans SFH et de décrire le logiciel dans HAL

Qu'est-ce qui se passe si à la base du repo [[Git|git]] il y a un [[codemeta]] correctement renseigné ? 
Faire en sorte qu'OStrails reconnaisse le contenu de ce fichier. La priorité c'est d'assurer l'interopérabilité avec HAL et Software Heritage. 

Les pilotes ne démarrent pas avant la fin du printemps 2025






$\newline$
# bibliographie
$\newline$







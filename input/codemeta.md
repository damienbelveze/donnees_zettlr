---
title: codemeta
subtitle: 
id: 20231220_codemeta
author: Damien Belvèze
date: 2023-12-20
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - codemeta.json
tags:
  - programmation
  - reproductibilité
  - archives
  - code_source
---
fichier normalisé facilitant l'archivage du Code et détaillant : 
- les auteurs
- les licences
- la date
- la version du code archivée
- l'identification unique
- le financeur
- le répertoire de versement
- l'URL vers la gestion des bugs
- l'environnement ([[système d'exploitation]], version du [[compilation|compilateur]], langages utilisés, la référence de la publication associée)

Le codemeta est aujourd'hui plutôt en JSON mais cela n'exclut pas d'autres langages possibles interprétables par la machine en même temps que lisibles par l'humain : 

> Various file formats to encode this meta-data are surmisable. Among others there are: ini (Initialization File), xml (Extensible Markup Language), yaml ([[YAML]] Ain’t Markup Language) and json (Javascript Object Notation), which is suggested in [46, 26]. Basic requirements for such a file are a plain text encoding and a human readable formatting. Additionally, a simple syntax26 as well as the availability of parsing facilities should be considered. Due to its renownedness and easy readability for human and machine, the authors suggest to use the ini file format, as the more elaborate grammars xml, yaml and json require sophisticated parsers.

(source: [[@fehrBestPracticesReplicability2016]]) 

si on veut lier une publication à un logiciel, on peut aussi fournir dans le codemeta dans l'attribut "reference publication" le nom de la publication, le lien apparaîtra cliquable dans Software Heritage. 
(voir [[National Tripartite Event EOSC-FRANCE#Archiving, referencing and describing software with HAL and Software Heritage]]) voir [[EOSC]]

pour générer un fichier codemeta voir https://codemeta.github.io/codemeta-generator/

pour un fichier mentionnant uniquement date, auteurs, licence, voir [[fichier CFF]]




$\newline$
# bibliographie
$\newline$







---
title: formation URFIST à OpenRefine
subtitle: 
id: 20250405_formation URFIST à OpenRefine
author: Damien Belvèze
date: 2025-04-30
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - données_recherche
---
extension [[ROR]] pour OpenRefine : https://gist.github.com/rndblnch/2b496948204c5453c45a74c2518ec463


version 3.9.0 pas stable (disponible dans [[snap]]), télécharger plutôt version 3.9.3 depuis le site (télécharger l'archive, dézipper)

possibilité de télécharger l'archive
Windows : cliquer sur le ficher refine.bat
Linux : cliquer sur le fichier ./refine

s'inscrit dans le [[web sémantique]]

"things not strings"
La BNF comprend les gens comme des entités, mais les noms de lieux encore comme des chaînes de caractères : plusieurs expressions de Rennes
voir liste des lieux de naissance : 
https://tinyurl.com/Rennes-BNF

graphes d'entités, triplets, éléments, propriétés, sommes, noeuds ou arêtes, bref [[ontologie|ontologies]]

un arbre généalogique est avant tout un graphe. 
arbre des Rougon-Macquard : graphe pas assez sémantisé (informations redondantes dans les noeuds, pas de propriétés, les propriétés sont dans les noeuds eux-mêmes)

[[URI]]
[[RDF]], RDFs 

OpenRefine permet de traiter des données longues que les tableurs ne peuvent pas traiter mais avec une [[interface graphique]] pour que ce soit plus accessible que le traitement des données avec [[R (logiciel)|R(logiciel)]] ou la bibliothèque Panda de [[Python]]
développé à la base par Google (Google Refine), récupération par une communauté de bénévoles qui a récupéré le code et l'a libéré  en 2012 sous le nom d'OpenRefine. 
Utilisé par l'[[ISCJ]] pour traiter les données issues en 2016 des [[Panama papers]]
Possibilité de développer des extensions

# Fonctionnalités d'OpenRefine

Nettoyer des données (désordonnées, incohérentes, mal formatées)

- transformer et formater
- Lier et enrichir avec [[Wikidata|wikidata]], VIAF ou [[IdRef]]
- Réconcilier
- Exploration

Possibilité d'installer OpenRefine sur un serveur pour permettre à des collaborateurs de travailler en même temps sur le même document sans avoir à télécharger le logiciel

La version 3.9.3 intègre [[Java]] (pour pallier le caractère payant des derniers environnements Java développés par Oracle)

import/export de JSON, XML, [[CSV]], [[TSV]]

ouvre l'adresse locale sur le port 3333 (127.0.0.1:3333), fonctionne avec tous les navigateurs

possibilité d'ouvrir un fichier de données à partir de son URL, possibilité d'ouvrir trois fichiers d'un coup. 
Possibilité d'ouvrir une base de donnée en ligne MySQLlight, PostGrest, MariaDB...

ouvrir et importer un fichier (on peut l'ouvrir sans l'importer) ; dans un projet OpenRefine on peut aussi importer un fichier avec l'historique des modifications (format OpenRefine)

subtilité : lignes et entrées , il peut être possible de grouper plusieurs lignes qui deviennent des entrées (par exemple auteurs ayant produit plusieurs publications)
OpenRefine n'affiche que 10 lignes sur 347

\^Le : [[expression régulière]] pour dire que la ligne doit commencer par Le (ne pas oublier de cocher "expression régulière" dans les filtres)

Si on exporte le travail sous la forme d'archive open refine on conserve les filtres et les facettes utilisées dans le document exporté
Toutes les opérations réalisées (sauf le choix des filtres et des facettes) sont enregistrées automatiquement.
Possibilité d'annulation les opérations précédentes
Possibilité d'extraire en format [[JSON]] les opérations de manière distincte des données. Possibilité de ne pas extraire toutes les opérations mais de sélectionner celles qui sont intéressantes 

Possibilité d'inclure des lignes Python dans les facettes
Par exemple vérifier que le premier caractère de la ligne est une capitale : 

```python
line[0]
#affiche le premier caractère de la ligne 
```

[[GREL]] (General Refine Language) : langage propre à OpenRefine ; ces fonctions ressemblent un peu aux fonctions [[Excel]] mais sont beaucoup plus nombreuses.

```grel

value.split(" ")[0]
# coupe la chaîne de caractères au niveau de l'espace et ne conserve que le premier membre, celui avant le premier espace
```

Rassembler les espaces consécutifs, supprimer les espaces de début et de fin sont des tâches triviales à faire sur un jeu de données.

Possibilité d'inverser le nom et le prénom
Lorsqu'on utilise une opération avec l'interface graphique, il nous fournit le code GREL correspondant

Grouper et éditer (dans éditer des cellules) : merger des versions plus proches
-> fusionner la version et regrouper

## Réconcilier des données

La barre verte dans l'entête indique une colonne dans laquelle les données ont été réconciliées

Réconcilier la colonne avec [[Wikidata]] (en fr, en en, avec Wikimedia Commons)

[Reconciliation servce test bench](https://reconciliation-api.github.io/testbench/#/) sur Github

GeoNames disponible mais pas pour la France, donc il faut procéder autrement. 
Certaines ontologies suggèrent des entités proches (c'est le cas de Wikidata), d'autres non. 

Afficher les facettes de réconciliation dans le menu 'réconcilier'
Visuellement il affiche les images de Wikidata mais celles-ci ne sont pas inscrites dans le fichier

###   Ajouter des données à partir des colonnes réconciliées

Prendre une colonne verte (données réconciliées)

menu : éditer la colonne > ajouter une colonne en fonction de cette colonne
ajouter des colonnes à partir de la colonne creator : ajoute l'élément date de naissance de Wikidata à partir du nom du peintre présent dans la colonne creator

La BNF n'a pas de endpoint SPARQL
Les URI sont aussi des URL on peut donc les parser (extraire du contenu d'une URL)
\> éditer la colonne > ajouter une colonne en moissonnant/parsant des URL
Possibilité d'utiliser cette fonction avec [[OpenAlex]]

La réconciliation concerne les services qui comme Wikidata sont paramétrés pour ce type de service, l'alignement relève du bricolage en parsant des URL, récupérant du JSON










$\newline$
# bibliographie
$\newline$







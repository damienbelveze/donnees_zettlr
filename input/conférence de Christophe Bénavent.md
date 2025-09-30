---
title: conférence de Christophe Bénavent
subtitle:
id: 20231113_conférence de Christophe Bénavent
author: Damien Belvèze
date: 2023-11-13
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---
# Conférence de Christophe Bénavent

https://github.com/BenaventC

site réalisé avec [[Quarto]] depuis Github : https://github.com/BenaventC/blog


"Il est impensable aujourd'hui de commencer une thèse sans connaître le logiciel [[R (logiciel)|R]]"
"Utiliser [[Microsoft Word]] aujourd'hui pour une thèse, c'est du travail d'amateur"


Lien avec le [[traitement automatique du langage naturel|TAL]]

utilisation des API ou [[scraper|scraping]] 
<!-- Question de la sécurité du scraping pour la bibliothèque -->
Scraping de theses.fr

Les revues de littérature systématique ne devraient pas nous intéresser en économie : 
- qualitatif # [[reproductible]]
- en médecine, la preuve scientifique peut être administrée suite à une revue de littérature 

En médecine , on est plutôt sur le registre des revues narratives : on cherche à raconter une histoire avec ces données biblio. 
(cf. PMP authorship analysis)

Présentation de quelques packages R pour du TAL

[[tidyverse]] : suite de packages pour R comporte ggplot 
udpipe : annotation syntaxique : quelle est la grammaire du texte : où sont les noms communs, où sont les adjectifs, les déterminants, les adverbes ; il va falloir annoter chacune des phrases et annoter les "part of speech". Universal Part of Speech (UPOS) : toutes les langues ont la même structure.

<!-- est-ce que l'éditeur demande le fichier Rmarkdown pour juger de la reproductibilité des données-->

<!-- programmation lettrée, fiabilité -->

Journal of Business Research : revue prédatrice ([[Editeurs prédateurs en open access]])
Une revue normale publie 500 numéros par an. 

Pour trente étudiants il y a un chercheur. Explosion de la production [[publish or perish]], Eclipse du savoir. 

Pour prendre en main et faire des analyses [[NLP]], il faut une semaine entière. 

[[package]] rscopus : accéder à Scopus depuis l'API (clé API).

<!-- scopus clé accès quand on est client de science direct mais pas de scopus -->
ajouter la fonction de rscopus abstract_retrieval  

nécessité de boucler un code pour récupérer d'autres sets de 40 références pour accéder à 27 000 références. 

projection des Tsne des mots-clé   nuages de mots


$\newline$
# bibliographie
$\newline$







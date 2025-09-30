---
title: traitement automatique du langage
subtitle: 
id: 20231113_traitement automatique du langage
author: Damien Belvèze
date: 2023-11-13
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - TAL
  - NLP
  - Natural Language Processing
  - TALN
tags:
  - analyse_corpus
  - données_recherche
  - IA
---
voir [[grands modèles de langage|intelligence artificielle]]
corpus de rap : pas de ponctuation, 7000 mots, peu d'inventivité grammaticales (au contraire) mais une invention lexicale très importante, grand nombre d'hapax

# histoire du TALN

Zipf : première approche du TAL en 1930
théorie distributionnelle du langage : le sens des mots n'est pas dans le dictionnaire, mais il est dans leur co-occurrence (cf. chatgpt)

1963 : Benzecri publie l'analyse factorielle des correspondances multiples

2003 : Bley : module Latent Dirichlet Allocation model

2013 : embeddings "plongement" : on va transformer un mot en un vecteur dans un espace de grande dimension. 

2018 : transformeurs = modèles d'embeddings. Modèle commun en France : BERT (CamemBERT et flauBERT)

Je suis Christophe : quelle probabilité avec laquelle après Je il y ait suis. 

On ne travaille plus avec des mots avec des tokens : 
1 mot normalement = 2 tokens, un pour "normal", 1 pour marquer un adverbe
1 port d'ordinateur = 1 token, 1 port de pêche = 1 autre token. voir [[tokenisation]].

ChatGPT (GPT4) n'est rien d'autre qu'un transformeur particulièrement abouti. espace à 12 couches, 3000 dimensions, 180 milliards de paramètres. 

Modèles ([[LLM]]) ouverts, plus petits que ChatGPT : LLaMa 
on peut entraîner ce LLM avec des corpus particuliers pour des tâches particulières : boom économique de ce type d'entraînement. 

ex. construire un détecteur de figures de style dans un corpus de données (translittérations d'émissions vidéo)

Ce qui est difficile c'est la manipulation des données, pas la construction du modèle. 

# intelligence générative vs intelligence transformative

possibilité d'entraîner un LLM pour transformer du texte et non pour en générer (voir [[@bjarnasonFeelingItch2023]])

> My problem is that the generative model features I’d _want_ as both a developer and a user – truly parametric adjustment of style and structure instead of the abysmal and counter-productive prompt-and-pray nonsense currently on offer – just don’t exist and nobody seems to be developing them. Everything is all about generating bullshit and replacing existing work with something worse.



$\newline$
# bibliographie
$\newline$







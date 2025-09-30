---
title: documentation technique
subtitle: 
id: 20230626_documentation technique
author: Damien Belvèze
date: 2023-06-26
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - Documentation technique
  - Technical documentation
tags:
  - documentation
---

# comment écrire de la documentation à destination de professionnels en informatique

(source : https://twitter.com/ImraneSubstack/status/1672954868477067265)

>Comment écrire une bonne doc dans une équipe IT ? Tout le monde sait qu'il faut écrire de la doc pour partager les connaissances Par contre difficile de savoir comment les écrire. Je te partage mon template que j'utilise depuis des années
>1) But du document Ce document décrit/explique/donne/montre ... "En une phrase on doit comprendre si la suite va nous aider ou pas"
>2) Pré requis "Avant d'aller plus loin, il donne les informations/accès/compétences que tu dois avoir pour pouvoir utiliser le document"
>3) Sauvegarde Qu'est-ce que je dois faire pour sauvegarder l'état initial AVANT toute modification ? C'est souvent utile quand on touche à des serveurs, des bases de données
>4) Rollback Quelle est la procédure exacte à suivre pour remettre le système à son état initial ? Ça doit fonctionner, quelle que soit l'étape à laquelle on est dans nos manipulations.
>5) Sans la présence du 3 et 4, je n'entreprends aucune action. C'est primordial quand on touche à la production de revenir à minima à l'état initial, même si c'est un état "cassé". Mais au moins on n’empire pas les choses.
>6) S'il n’y a vraiment rien à faire en 3 et 4, ça doit être écrit pourquoi ce n'est pas nécessaire. (mais c'est assez rare, même pour l'exemple bateau de la création d'une boite mail)
>7) Enfin seulement, les instructions C'est le corps de la doc Généralement un mod opératoire à suivre avec plusieurs étapes C'est la partie la plus importante. Ici, quelques bonnes pratiques : • Trop de détails tue la doc
>8) À qui s'adresse cette doc ? Des gens qui ont mon niveau ? Des gens totalement débutants ? En fonction je mets le bon niveau de détails • Un tableau plutôt qu'une liste Chaque ligne = une instruction Colonne 1 = ce qu'il faut faire Colonne 2 = le screenshot pertinent associé
>9) Les cas d'erreurs Que faire en cas d'erreurs ? Quelles erreurs ont déjà été rencontrées ? Qu'est-ce qui pourrait se passer ? Et comment contourner ça ? Que faire si une nouvelle erreur apparait ? Est-ce que ce sont des erreurs qui nécessitent le rollback ?
>10) Si l’on doit attendre qu’une action se termine, quel est l'intervalle dans lequel on patiente ? À quel moment on se dit que ce n’est pas bon ? À quelle vitesse telle ou telle action doit se passer normalement ? Si ce n’est pas le cas, que faire ?
>11) vec ça, tu as écrit une doc que tu aurais aimé avoir en cas de pépin. Tu vas me dire : c'est long !!! En fait, c'est très rapide à écrire si tu connais le niveau de détail à mettre.
>12) Dans les équipes de Tech où j'ai travaillé, : "écrire : se connecter en ssh sur le serveur" suffisait. Ils savent c'est quoi SSH, il savent identifier le serveur, ils savent chercher les crédentials dans les vaults ...
>13) Et pour plein d'actions, y'a pas besoin de plus d'une phrase. Enfin, une doc complète mais succincte vaut mieux qu'une doc jamais écrite ou que personne ne lit

Faut-il calibrer la documentation technique pour la rendre plus exploitable par des [[grands modèles de langage|intelligence artificielle]]? 

2 réponses à faire à cette question 
1. on ne devrait jamais donner pour seul accès à la doc technique un chatbot. La doc technique devrait être accessible directement pour un usage non médié par une IA (interrogation avec des booléens plutôt)
2. Il n'y a pas de différence entre écrire de la doc technique pour des humains ou pour des machines : plus la doc est claire et structurée et plus elle sera également efficace à travers un chatbot
(voir commentaires envoyés suite à ce post : https://infosec.exchange/@samsav/112210764944623942)
$\newline$
# bibliographie
$\newline$







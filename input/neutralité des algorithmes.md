---
title: neutralité des algorithmes
subtitle:
author: Damien Belvèze
date: 21-08-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: [loyauté des algorithmes]
tags: [algorithmes]
---
> Commençons par nous défaire de l'idée qu'il y a des calculs ou des données neutres. Ceux-ci ne sont que le reflet des idéologiques qui les mettent en oeuvre

([[@guillaudAlgorithmesContreSociete2025]], p28)

> Les algorithmes sont des opinions encapsulées dans du code 

Cathy O'Neil, Algorithmes, la Bombe à retardement, 2018

On discute souvent de la neutralité des algorithmes et il est reconnu que les algorithmes reflètent les préjugés et les biais inhérents à leurs concepteurs ou aux données qui ont permis de les rendre efficaces ([[machine learning]]).
Pour autant, si on conteste par exemple le [[Pagerank]] de Google, il est difficile de définir ce que serait un classement neutre des résultats de recherche. 
En l'absence d'une telle définition, il est plus exact de parler de **loyauté des algorithmes**
Un algorithme loyal dit ce qu'il fait et fait ce qu'il dit. 
[[Dominique Cardon]] donne quelques exemples d'algorithmes déloyaux dans [[@cardonCultureNumerique2019]], p401

- un site de comparateurs de vols qui augmente artificiellement le prix d'un vol quand ce vol est sans alternative pour le consommateur
- un site de réservation de voitures avec chauffeurs qui affiche des véhicules à des endroits où ils ne sont pas dans la proximité du consommateur pour convaincre celui-ci de recourir à ses services.

Le [[RGPD]] prévoit une obligation d'**[[explicabilité]] des décisions algorithmiques**, mais quand ces algorithmes fonctionnent avec du machine learning, il est bien souvent beaucoup plus commode de constater qu'ils sont efficaces que d'expliquer pourquoi ils le sont. 
(voir [[prolétarisation#illetrisme numérique ou e-gnorance]])

# neutralité des algorithmes et populisme

La critique des banques et des institiutions financières est un thème très ancré chez les populistes. Les médiations humaines qui font tourner ces instititutions sont accusées, non sans raison, d'être biaisées, orientées pour les uns vers leurs propres intérêts (ploutocratie), pour les autres, d'être trop sujets aux aléas de la politique, aux pressions démocratiques, etc.

Les [[libertarianisme|libertariens]] utilisent cette critique pour promouvoir les [[crypto-monnaie|cryptomonnaies]] , comme le [[bitcoin]], censées assurer une neutralité algorithmique. 

>Sur le plan politique, enfin, [Jon Baldwin](https://www.nature.com/articles/s41599-018-0065-0/) analyse le trope réactionnaire contenu dans la fétichisation du réseau associée à Bitcoin, dont l’un des axes de pensée est qu’un processus algorithmique pourrait assurer la gouvernance des sociétés de manière plus effective que des institutions démocratiques collectives

(source: [[@hadjadjiBitcoinChevalTroie2023]])

# renforcement des inégalités sociales par les algorithmes

La vie d'un individu est aujourd'hui de plus en plus sujette à chaque étape à des traitements générés par des [[grands modèles de langage|intelligences artificielles]]. On sait que ces intelligences ont été entraînées sur des ensemble de données qui reflétaient déjà les biais des collecteurs de données. Le fait de faire tourner ces IA (en invoquant la "neutralité" de l'artefact par rapport à l'arbitraire supposé de l'homme) va aggraver ces biais et renforcer les inégalités de traitement entre hommes et femmes (voir [[biais de genre]]) et entre blancs et personnes de couleur, notamment, ou encore entre classes privilégiées et classes populaires (cf. Parcoursup) (lire à ce sujet le concept d'"ouroboros statistique" avancé par Kate Crawford dans [[@crawfordContreatlasIntelligenceArtificielle2023]], p155)



# bibliographie


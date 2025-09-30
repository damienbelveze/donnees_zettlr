---
title: stéganographie
subtitle: 
id: 20250105_stéganographie
author: Damien Belvèze
date: 2025-01-05
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - cryptographie
---
# Histoire

dans [[Hérodote]] (livre 5), Histiée rase le crâne d'un esclave, tatoue le message sur la peau, envoie le message traverser les lignes ennemies une fois que ses cheveux ont repoussé, l'esclave est mis à nu par les soldats mais sans conséquence. Le correspondant d'Histiée rase à nouveau le crâne de l'esclave et peut voir le message tatoué

[[@lafourcade15EnigmesLudiques2022]], p97

# Stéganographie numérique

stéganographie et tatouage numériques : la dissimulation des données

 La stéganographie est un procédé de [[Cryptographie]] permettant de dissimuler un message dans un autre message, notamment dans une image.

l’art d’enterrer son argent dans un jardin (cryptographie : l’art de le mettre dans un coffre-fort)

encre sympathique

 Méthode des bits de poids faible

 pixel = triplet d’intensité RVB R = suite [[binaire]]

Premier bit : bit de poids fort, dernier bit : bit de poids faible

195 -> 193 : différence indétectable à l’oeil

Ecrasement du bit faible

compression de l’image à dissimuler - 1 bit écrasé : indétectable - 4 bits écrasés : on commence à voir l’image sous-jacente

Attaque par compression : ne résiste pas à la compression

watermarking : suivre les usages d’un document : protection des droits d’auteur

identification de la copie qui a servi à la fraude Game of Thrones

[stirmark](https://www.petitcolas.net/watermarking/stirmark/) : évaluation du logiciel de stéganographie

- Attaques de robustesse : 
- attaque sel et poivre
- transformée en ondelettes discrètes : application de filtres sur l’image d’origine
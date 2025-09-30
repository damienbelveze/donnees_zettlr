---
title: Lodex
subtitle: Démonstration Lucile Bourguignon (INIST-CNRS)
id: 20250911_Lodex
author: Damien Belvèze
date: 2025-09-11
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags:
  - visualisation_données
---
sources d'import : fichier, lien vers server externe, API
loader : script de chargement des fichiers dans Lodex adapté à leur format

dédoublonnage automatique en entrée à partir du champ URI, on peut élire une autre colonne de dédoublonnage que l'URI (par exemple, colonne HAL-ID)

appliquer un modèle de structuration : 1 page d'accueil, paramétrage de métadonnées dans une page de ressource, une page de graphiques

transformers : application de convertisseurs
"ajouter une opération" > choisir un transformer
par exemple transformer *truncate* pour ne retenir que YYYY sur des données YYYY-MM-DD 
*replace* / *replace_regex* (remplacer / remplacer avec des expressions régulières, voir [[expression régulière|regex]]), ex : "fr" -> "français"

transformer multi-valué : séparer les valeurs pour pouvoir créer des séparations (*split*)

pour créer des graphiques, sélectionner routine (accès au catalogue des routines)
la routine pour les graphiques les plus simples s'appelle *distinct_by*, sélectionner ensuite le type de graphique (par exemple diagramme en barres)

*graph_by* : routine pour les graphes de réseau
choisir ensuite graphiques réseau pour faire un graphe de collaborations entre auteurs

recherche et facettes : définir quels champs le lecteur peut afficher, sélectionner pour adapter les visualisations



$\newline$
# bibliographie
$\newline$







---
title: Cartographie thématique avec R
subtitle: Introduction à la production de cartes statiques, d'atlas et de cartes interactives, formation de Florent Demaroes
id: 20250902_Cartographie thématique avec R
author: Damien Belvèze
date: 2025-09-02
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags:
  - R_logiciel
  - programmation
---
voir [[cartographie]]

données vectorielles : polygones, lignes, points (bois, cours d'eau, bornes incendie)

données raster : chaque pixel est une information (degré d'occupation d'un sol par exemple)

carte [[choroplethe]], cartes en symboles proportionnels, cartes en oursin, cartes en crayonné, cartes en stalagmites (concentrations), cartogrammes (dilatation et rétractation de certaines unités spatiales), cartes en relief, cartes en perspectives. 

chaîne de traitement de l'information géographique dans R : environnement mature, on dispose dans R d'un grand nombre de [[packages]] spécialisés dans la cartographie.

> L’utilisation de R pour la cartographie n’est pas un choix évident. L’utilisateur qui souhaite faire une simple carte aura plus vite fait de la produire avec un logiciel de cartographie classique

Vrai en 2014, mais aujourd'hui on peut utiliser R pour faire de la cartographie avancée en gagnant du temps. 

Principes de [[sémiologie graphique]] (Jacques Bertin, années 60)
effectifs en symboles proportionnels
valeurs en aplats de couleur (cartes choroplètes) ; l'addition des valeurs est impossible sur un même fond de carte. 

découpages administratifs en France
13 régions, 96 départements en métropole, 332 arrondissements, 1257 EPCI (cf. Métropoles, communautés de communes), 2054 cantons, 34800 communes + circonscriptions législatives, sections cadastrales, quartiers, bassins hydrographiques...

quels formats associés : 

formats vectoriels : format [[shapefile]] (dbf, prj, shp, shx) date des années 80 ; si on perd 1 des 4 fichiers, le jeu de données est inutilisable. 

geopackage : peut comporter une plus grande variété de données. 

geojson : format conçu pour échanger des données géographiques sur le web.

wms : web map service
structure d'url ([[API]]) 
choix parmi les différentes projection (Mercator, Lambert)
Le SHOM diffuse ses données en WMS

tuiles xyz : [[OpenStreetMap|OSM]]
l'URL est bcp plus simple mais on ne peut choisir que la projection Mercator ; assez figé, on ne peut pas choisir le style, il faut préciser le niveau de zoom (1 : planisphère, 22 plus petite proportion de l'espace)
affichage extrêmement rapide par le serveur (on n'a qu'à indiquer le niveau de zoom)

Il existe désormais des web map tile services  qui réemploie les intérêts des tuiles xyz pour un affichage plus rapide. 

exemples cartes topographiques de l'IGN

couches raster : derrière chaque pixel on a une valeur (par exemple l'altitude d'un point)

carto positron : fonds de carte épuré sur lesquelles on va pouvoir supperposer nos données. 

wfs : web feature service
derrière une URL on a une liste de couches et on choisit celle qu'on veut télécharger. 

## où trouver des données SIG ? 

https://hackmd.io/@hOaFaD2DS4WcOzNXU6j7vg/SJwpLFT4B

coordonnées géographiques

coordonnées sexagésimales (degrés, minutes, secondes) -> coordonnées décimales

projection Lambert93 pour la cartographie nationale : la Lambert pour la France, en tant que représentation conique permet de respecter les limites générales des territoires de la même latitude que la France pour éviter la déformation observable dans Mercator

EPSG attribue à chaque système de référence de données un code

code EPSG Lambert93 : EPSG = 2154

possibilité de personnaliser la carte dans R avec [[Inkscape]] 

Formats de données dans R et packages associés

rgdal apparu en 2003 interface entre R et Gdal + Pro
2005 : sp (special) formats vectoriels
2008 : possibilité d'utiliser des données sp dans ggpolt2 ([[Hadley Wickham]])
2010 : rgeos 
2010 package permettant les données géographiques dans R au format raster

rgdal package retiré du CRAN fin 2023
package sp obsolète mais toujours présent dans le CRAN

aujourd'hui package sf (simple feature) par l'auteur de sp ; sf rassemble sp, rgeos et rgdal
compatibilité avec les opérateurs du tidyverse. 

```shell
# chargement dépendance système : 
sudo apt-get -y install libudunits2-dev libssl-dev libabsl-dev
sudo apt-get -y install r-cran-s2 ===
```

Après avoir chargé les dépendances système, il faut charger les dépendances logicielles propres à R

```r
#chargement dépendances logicielles depuis R
install.packages("s2")
install.packages("units")
install.packages("sf")
```

Les premières colonnes de sf comportent les variables, la dernière colonne ("geom") comporte les coordonnées des sommets du polygone.

le format raster a donné lieu au package raster puis le package [[terra]]. 

terra lancé en 2020 gère les formats matriciels et les formats vectoriels. Permet de traiter des jeux de données volumineux. 

# fonctions de base de R pour la carto

ces fonctions de base ne sont pas tributaires de l'obsolescence des packages, meilleur pour la reproductibilité (pas d'argument qui change de nom ou est devenu obsolète)

choisir des packages
Combien de développeurs portent le projet ? il vaut mieux qu'il n'y ait pas qu'une seule personne
statut : universitaires, CNRS : emplois un peu plus stables ? 
ces packages reposent-ils sur des dépendances obsolètes (par exemple sp remplacé par sf) ?
Quelques exceptions : certains packages sortent un peu de nulle part et qui proposent des fonctions  uniques

paramètres de la fenêtre graphique
(pos = position)
1  bas, 2, gauche, 3 haut, 4 droit

coordonnées de la fenêtre graphique (normalized device coordinates, ndc)

coin gauche bas : 0,0
coin gauche haut : 1,0
coin droit haut : 1,1
coin droit bas : 0,1

![](images/fenêtre_graphique_R.png)

### packages à larges spectre

mapsf : cartographie des objets sf
(remplace cartography développé par Timothée Giraud et Nicolas Lambert)
cartes bivariées : taille des symboles et discrétisation de ces symboles 
**mapsf** permet depuis la dernière version d'afficher des données raster. 

**tmap** (thematic maps), de Martijn Tennekes
possibilité de basculer en mode web
(carte statique -> carte interactive)

**ggspatial** (lié à ggplot2) prend en charge les données spatiales vectorielles et raster , propose des fonctions de légende

**oceanis** (chargés de mission INSEE) cartographie des données gérées par l'INSEE. Le seul paquet qui permet de gérer efficacement le traitement des flux bidirectionnels (paramétrage de la taille des flêches et de leurs longueurs), intéressant pour représenter des mobilités. 

### Packages liés à un type de carte spécifique

**linemap** (Timothée Giraud). Cartes en stalagmites, n'accepte que des données raster en entrée.

**tanaka** en complément avec les packages mapsf et terra. 

**CartogramR** (Florent Demoraes et Pierre-André Cornillon) produit des [[anamorphoses]] en fonction des valeurs présentes dans la base de données. 

**cartogram** cartogramme de Dorling : symboles proportionnels pour qu'aucun symbole ne se supperpose à un autre en essayant de maintenir les relations de voisinnage initial
cartogram d'Olson : on garde la physionomie de chaque objet mais on la dilate ou on la rétracte en fonction de la valeur. 
Dorling : bcp utilisé pour les cartes électorales

**recmap** cartogrammes rectangulaires (tous les objets sont des rectangles qui ne se chevauchent pas en dépit des contraintes d'adjacence) : cartogramme de Demers pour la carto électorale

### production de cartes interactives

**leaflet** javascript dans R ; syntaxe assez verbeuse. 

**mapview** utilise le package leaflet de façon plus aisée pour l'utilisateur (syntaxe plus concise)

**mapdeck** payant (nécessite compte payant à mapbox) tiges extrudées en perspective.
par exemple avions qui partent d'un lieu en particulier. 

**happign** (Paul Carteron) permet de télécharger des images WMS au format raster et des couches vectorielles à partir de flux WFS produits par l'IGN.
Le package évolue au fur et à mesure que les URL des jeux de données
Les scan25 (topo 1/25000) ne sont pas en accès libre depuis le site de l'IGN. Certaines régions ont acheté les diffusions des scan25 (celles de Bretagne sont trouvables sur GeoBretagne)

**maptiles** (Timothée Giraud). Permet de télécharger des tuiles xyz quelque soit le fournisseur (il faut lui indiquer l'URL et on rajoute cette URL à maptiles ce qui permet d'afficher les fonds de carte depuis ce site) on récupère un format spatraster interopérable avec terra. 

### packages comportant des fonctions de visualisation

**spatstats** analyse des semi-points (données ponctuelles : prélèvements dans le sol avec des concentrations de nitrate par exemple, analyse d'échantillons sous la forme de points) ce package n'utilise pas les objets sf. permet de faire du lissage de données. 

### publication de cartes sur le web

Rstudio propose de publier les cartes dans une certaine mesure sur https://rpubs.com ; modèle freemium, il faut payer pour faire des cartes privées et obtenir plus d'espace.  





$\newline$
# bibliographie
$\newline$







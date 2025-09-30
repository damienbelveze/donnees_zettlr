---
title: OpenStreetMap
subtitle:
author: Damien Belvèze
date: 17-03-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - Open Street Map
  - OSM
tags:
  - cartographie
  - programmation
---


outil libre de [[cartographie]]
Les associations en faveur du libre utilisent depuis longtemps OpenStreetMap, les institutions s'y sont mises quand en 2018, Google a commencé à faire payer les sites qui ont beaucoup de visiteurs pour leur utilisation de Googlemaps (cf. [article du Monde](https://www.lemonde.fr/chronique-des-communs/article/2018/06/01/hausse-des-tarifs-de-google-maps-on-a-plus-que-jamais-besoin-d-alternatives-libres_5307968_5049504.html?utm_term=Autofeed&utm_campaign=Echobox&utm_medium=Social&utm_source=Twitter#link_time=1527839164))

OpenStreetMap est soutenue par une communauté d'utilisateurs très active ce qui lui a donné dans bien des cas un avantage sur Google Map ([exemple de la cartographie du Cameroun](https://twitter.com/OSMCameroun/status/1085939637770702848))


# Importer des données d'OSM

## avec R

importer dans [[R (logiciel)|R]] (en tant qu'objets [[Cartographie thématique avec R|sf]]) des objets provenant d'OpenStreetMap dans une emprise : ça se fait avec le package [osmdata](https://www.openstreetmap.fr/osmdata-le-portail-de-la-donnee-osm/)

```r
# 7 - Extraire des données OpenStreetMap_
library(osmdata)
# 7.1 - Créer un nouvel objet contenant les communes du département du Lot._
com46 <- Occitanie[Occitanie$INSEE_DEP == "46", ]
plot(st_geometry(com46))
# Définition d'une emprise spatiale (rectangulaire) en coordonnées géographiques_
emprise <- opq(bbox = st_bbox(st_transform(st_buffer(com46, 10000), 4326)))
# Récupération des pharmacies situées dans l'emprise_
available_features()
View(as.data.frame(available_tags("amenity")))

pharmacies <- add_osm_feature(opq = emprise, key = 'amenity', value = "pharmacy")
# conversion du jeu de données récupéré au format sf et extraction des points correspondant aux pharmacies_

pharmacies.sf <- osmdata_sf(pharmacies)

View(pharmacies.sf)

pharmacies.sf.pts <- pharmacies.sf$osm_points

View(pharmacies.sf.pts)

# auteur du script : Florent Demoraes

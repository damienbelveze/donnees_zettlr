---
title: Interopérabilité des formats de données
subtitle:
id: 20230608_Interopérabilité des formats de données
author: Damien Belvèze
date: 2023-06-08
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: [interoperability]
tags: [données_recherche]
---

# netCDF pour les données physiques et géographiques

**format auto-documenté**

[[données de la recherche]] variant selon la profondeur, l'altitude, la latitude, la longitude ou le temps > netCDF [[@libesNetCDFFormatFichier2023]]

netCDF (network common data form) est un standard de description des données qui date des années 80 (créé par la NASA) et est largement partagé aujourd'hui. Ce standard facilite la réappropriation des données en encapsulant dans un même fichier à la fois les données et des informations sur ces données (métadonnées)

Par exemple, la donnée *temperature* est décrite de la manière suivante : 
- unité de mesure (Celsius ou Kelvin)
- nom standard

parties d'un fichier netCDF

- dimensions (par exemple, temps, longitude, latitude et hauteur)
- variables (données et métadonnées)
- informations générales (date de publication, nom du propriétaire des données, et conditions de réutilisation)

# Conversion de formats propriétaires en formats libres

## Bio-imagerie : 

>Les données brutes sont issues des capteurs des microscopes. Ces appareils génèrent des images accompagnées de leurs paramètres d’acquisition. Ces informations se présentent souvent sous la forme de fichiers dans des formats propriétaires peu exploitables et peu interopérables en l’état (.lif pour Leica Microsystems, .czi pour Carl Zeiss, .nd2 pour Nikon, .vsi pour Evident...). Un connecteur est nécessaire pour ouvrir de tels fichiers de manière autonome, sans passer par le logiciel constructeur. Le plus répandu est la bibliothèque Java Bio-Formats [55] permettant de lire ces formats de fichiers d’images. La communauté peut cependant faire face à des formats de fichiers un peu plus retors, comme le .mrxs (mode de compression JPEGXR pour les contrastes fluo), qui doit être converti en .zarr, avant une nouvelle conversion en .ome.tiff [56]. Ainsi les données sont conservées, mais nous avons constaté certaines modifications au niveau des métadonnées. En vue de l’analyse, il est recommandé de s’assurer que la donnée brute validée et sauvegardée sur le support de stockage soit accessible en lecture seule pour éviter qu’elle ne soit ni modifiée ni supprimée. Seul le porteur du projet pourra disposer des droits en lecture/écriture.

voir fichier [[TIFF]]

([[@lebonGuideBonnesPratiques2025]])

## analyse de données qualitatives

format nvivo
voir échanges sur la liste code4lib : https://lists.clir.org/cgi-bin/wa?A1=ind2503&L=CODE4LIB#27









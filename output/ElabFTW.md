---
title: ElabFTW, le cahier de laboratoire numérique
subtitle: 
author: Damien Belvèze
date: 26-11-2021
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - données_recherche
---

# Introduction

ElabFTW est un [[cahiers numériques|carnets de laboratoire]] libre développé par Nicolas Carpi, régulièrement mis à jour (v5.0) et enrichi par une communauté d'utilisateurs (communauté internationale),  validé par le [[COSO]] en mai 2022, avril 2023 installation du logiciel à l'Université de Lorraine

démo : https://demo.elabftw.net/experiments.php

toutes les informations sont accessibles sur le site : https://demo.elabftw.net/experiments.php (authentification JANUS)

Sources des informations présentes dans cette note : 

- Source 1: Marie Herbet (DATACC, Université de Lyon 1, novembre 2022, journée organisée à Rennes par l'Université de Rennes à l'ISCR)
- Source 2: Laëtitia Bracco & Elodie Papin (Univ Lorraine) + Maria Grazia Santangelo (Univ Grenoble) (visio organisée par l'Atelier de la donnée de Lorraine, 18/01/2024)

# Principales fonctionnalités d'ElabFTW

Rappeler l'intérêt d'un cahier de laboratoire avec les cahiers de labo de Marie Curie : 
https://gallica.bnf.fr/ark:/12148/btv1b10536281j.r=cahier%20de%20laboratoire%20marie%20curie?rk=21459;2

attachement au papier dans le cadre des expériences "sur paillasse", mais ces notes  prises sur le papier peuvent être plus avantageusement saisies dans un cahier de labo que dans [[Microsoft Word]]
![](fonctions_cahier_labo.JPG)

Elabftw en cours de labellisation pour devenir l'outil de référence du CNRS

[eLabFTW](https://datacc.elab.one/login.php)

objectif des cahiers numériques et en l'occurrence d'ElabFTW : 

![](elabftw1.JPG)

![](ElabFTW2.JPG)

![](ElabFTW3.JPG)

![](ElabFTW5.JPG)
La difficulté de prise en main du logiciel n'est pas dans la maîtrise des fonctionnalités, mais dans la manière dont on va concevoir la structure de l'expérience (qu'est-ce qui ressort des ressources, comment les expériences s'organisent les unes par rapport aux autres dans les différents projets)

- Fournit une [[sauvegarde de données]] numérique (mais ElabFTW n'est pas fait pour de l'[[stockage des données|archivage de données]])
-   Centralise les données
-   Permet de compiler les données (export en différents formats).
-   Est accessible à distance de façon sécurisée et participe ainsi à améliorer le suivi des manips et des projets ainsi que l’encadrement des équipes.
-   Facilite le [[travail collaboratif]] grâce au partage d’expériences, de modèles d’expériences et d’une base de données commune à l’équipe.
-   Intègre un moteur de recherche
-   Assure la traçabilité des expériences par l’authentification de chaque utilisateur et la datation des expériences à l’aide d’un horodatage certifié (système intégré à l'outil) mais redoublé par certaines universités par un service tiers agréé (cf. université de Lorraine).

## Usage à l'Université de Grenoble

Usage d'ElabFTW à l'UGA en 244 utilisateurs, 65 cahiers, 1244 expériences. Accès par la fédération d'identité (CAS), double-authentification possible mais pas obligatoire.
Le CNRS utilise le protocole JANUS+ avec une clé [[FIDO]]. Un accès à ElabFTW avec ce mode de double authentification est possible.

processus d'ajout d'une équipe : envoyer une demande par mail
désignation d'un administrateur qui va ajouter des utilisateurs ou d'autres administrateurs.

## Usage à l'Université de Lorraine

DSI : mise à jour et déploiement
Atelier de la Donnée : pilotage, aide et présentation
adhésion au support payant (souscription et mécénat, 1985 euros/an)
Horodatage (valeur juridique) fixé avec la direction de la Valorisation : partenariat avec une entreprise payante. système pas tellement 
désactivation de l'horodatage par chaîne de blocs (juristes pas convaincus)

Instance de production + bac à sable

Instance de production (chiffres du 18 janvier 2024) : 
- Equipes : 65 
- Membres : 405 
- expériences : 1124 
11% d'actifs parmi ces membres (connexion dans le mois écoulé + au moins 5 expériences)


logiciel de [[cahiers numériques]] adapté à la chimie de synthèse, produit par un chercheur de l'institut Curie.
critères pour le choix d'une solution : 

le pour des petites institutions qui n'ont pas la masse critique pour négocier

autre solution libre (plus axé chimie, elab est plus générique) : [chemotion](https://pubchem.ncbi.nlm.nih.gov/source/1195)
expériences exportables en .eln entre Chemotion et ElabFTW

# Les fonctionnalités d'ElabFTW 

page expérience : liste des expériences avec les noms des administrateurs de l'expérience.




éditeur de l'expérience
statut de l'expérience (à venir, en cours, terminée)
eLabView est un outil générique pas d'application métier.

[intallation d'ElabFTW à l'Université de Lorraine](https://factuel.univ-lorraine.fr/node/23166) 

Possibilité de lier des objets de la [[base de données]]. 
Dans la base de données, on peut créer une grande quantité de type d'objets
possibilité de joindre un fichier (image, graphique : spectre, jeu de données déjà traité)

- édition du code ([[R (logiciel)]])
- dupliquer 
- export PDF
- export en format zip de l'expérience
- partager des liens vers une vue
- horodatage de l'expérience : cela permet de clarifier les contributions de chaque auteur en cas de litige
- certifier avec la [[blockchain]] (si on ne fait pas certifier par une agence externe. L'horodatage par un tiers permet de s'assurer que l'Université ne réécrit pas tout l'historique)

pas de synchro avec [[R (logiciel)]], copier/coller le texte de R dans elabFTW
coloration syntaxique de R disponible dans la solution

La création de templates oblige les jeunes chercheurs à ne pas oublier de noter des aspects importants de l'expérience.
Ce qui prend du temps c'est de créer les premiers templates, après on peut les dupliquer facilement.

Q: Peut-on connecter ces [[cahiers numériques]] avec le [[Plan de gestion des données|Plan de gestion de données]] ? 
R: Cela n'est pas encore possible, mais on peut formaliser les choses dans le logiciel de telle sorte que leur export soit réutilisable directement ou le plus simplement possible dans le PGD
On ne peut pas importer dans cette solution le spectre (format pas disponible), passer le spectre en PNG. 



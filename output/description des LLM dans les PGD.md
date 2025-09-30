---
title: description des LLM dans les PGD
subtitle:
id: 20250920_description des LLM dans les PGD
author: Damien Belvèze
date: 2025-09-20
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags:
  - intelligence_artificielle
  - données_recherche
---
Un nombre grandissant de projets de recherche incluent la création ou la constitution d'un grand modèle de langage (Large Language Model, ou LLM). 
Les modèles de langage incluent du code et des jeux de données, ce sont des objets mixtes qu'il est difficile de classer entre PGD et PGL.

# Description des données

## données réutilisées



## 1. description des processus ayant permis de collecter des données ou d'en réutiliser

### 1.1 Comment les données vont-elles être produites ou comment ont-elles été réutilisées 

L'entraînement d'un LLM repose sur des données qui ont été collectées quelque part. La nature de ces données, l'endroit où elles ont été collectées doivent être mentionnées. 
Par exemple [ce jeu de données comportant des QCM](https://huggingface.co/datasets/cais/mmlu) est importé depuis le site huggingface, et pèse 104MB. Sa réutilisation est réglée par la licence MIT et ses auteurs sont Dan Hendrycks, Collin Burst et al.
Les données en question sont des QCM en anglais provenant de diverses disciplines qui sont accessibles sur différents sites web.

### 1.2 Quelles données (type, format, volumes) de données vont-elles être collectées ou produites ? 

## 2. Documentation et qualité des données

### 2.1 quelles métadonnées accompagneront les données ?

#### 2.1.1 Quelles métadonnées vont permettre aux autres chercheurs d'identifier les jeux de données produits ?

#### 2.1.2 Quels standards de métadonnées vont être utilisés ?

Pour trouver les standards de métadonnées à utiliser en fonction du contenu, chercher sur le site [Fairsharing](https://fairsharing.org)

Par exemple, métadonnées standard pour les images biomédicales = [REMBI](https://fairsharing.org/523)

**
#### 2.1.3 Liens avec les schémas de métadonnées existant dans la discipline (thesaurus)

#### 2.1.4 Informations sur la manière dont les données vont être traitées au cours du projet (structure des fichiers, version de contrôle, conventions de nommage des fichiers)

[[conventions de nommage]]

#### 2.1.5 Quelles autres informations sont utiles pour la réutilisation de ces données (y compris à des fins de reproductibilité)

[[Interopérabilité des formats de données]]

#### 2.1.6 indication sur la disponibilité des infomations citées plus haut (notebooks, fichier READme, etc.)
### 2.2 Quelles mesures de contrôle vont être opérées sur les données



## 3. conservation et sauvegarde pendant le processus de recherche

voir [[@lebonGuideBonnesPratiques2025]]

### 3.1 Comment les données vont-elles être sauvegardées et conservées pendant le processus de recherche

emplacements pour la sauvegarde et la conservation, régularité de la [[sauvegarde de données]]

Ce qu'on risque à ne pas le faire correctement : https://forschungsdaten-thueringen.de/stories/articles/backup-is-key-eng.html
(data horror studies or scary tales : https://forschungsdaten-thueringen.de/rdm-scarytales/articles/overview.html)


### 3.2 Quelles mesures de protection vont être appliquées aux données pendant le processus de recherche

### 3.2.1 récupérations en cas d'accident

#### 3.2.2 distribution des accès, protocole d'accès

Fédération d'identité (Shibboleth) ?
Accès en [[SSH]] ?

#### 3.2.3 Conservation de données personnelles ou sensibles : comment vont-elles être protégées ? quel modèle de menace

chiffrement pour résister à une attaque informatique ? qui détiendra la clé de déchiffrement ? Comment ne pas la perdre ? 

chiffrement de bout en bout des dossiers et documents collaboratifs, voir [[Cryptpad]]

#### 3.2.4 Quelle protection institutionnelle en oeuvre pour la sécurisation de ces données

déclaration de collecte de données personnelles auprès de la DPO (voir [[RGPD]])

## 4. Obligations éthiques et code de conduite

### 4.1 Le cas des données personnelles

#### 4.1.1 collecte des formulaires de consentement

#### 4.1.2 Coûts et protocoles d'anonymisation

#### 4.1.3 Choix anonymisation ou pseudonymisation des données

voir [[pseudonymat]] et [[Anonymat|anonymisation]]

#### 4.1.4 Procédure d'accès aux données personnelles

### 4.2 propriété intellectuelle

voir formation [[Droit des données de recherche]]

#### 4.2.1 qui aura l'accès aux données, qui est le propriétaire des données

#### 4.2.2 Accès restreint ou ouvert aux données partagées ? 

#### 4.2.3 Quels sont les autres droits en jeu

Droits sur les logiciels utilisés créant des droits sur les données produites

Question (données-inter_réseaux) : Un capteur va être développé avec des calculs embarqués. Les algorithmes sont entrainées sur des BDD en partie "propriétaires" (BDD fournis par des naturalistes). A noter que certaines BDD propriétaires seront enrichies via une prestation dans le cadre du projet. Ce capteur va être développé au stade d'un prototype puis transféré vers une entreprise. Ce transfert vers une entreprise pose question relativement au fait que les propriétaires des BDD ne souhaitent pas qu'il y ait un usage commercial.  
  La convention de partage des BDD (BDDp pour celles des propriétaires et BDDp++ pour celles augmentées des données de la prestation) doit préciser la licence d'exploitation. Et dans le cas où celle-ci était CC-BY-NC-SA, quelle serait la contrainte pour l'entreprise?

Réponse (Eric Quinton) : 
Dans un cas comme celui-ci, pour se prémunir de toute interprétation ou recours, il faudrait demander aux naturalistes qui ont fourni les bases de données un accord pour l'utilisation de leurs infos dans le but d'entraîner l'algo et ses évolutions, si c'est possible. Il me semble également qu'il serait préférable que le code de l'algo soit publié en open-source, avec une licence de type LGPL, pour que toute amélioration soit portée à la communauté : cela resterait conforme au fait que les données ne sont pas utilisées à des fins commerciales (l'algo reste libre). Seule la partie physique du capteur et l'implémentation de l'algo sont commercialisées, étant entendu que d'autres personnes peuvent également réaliser ce type de travail.

Cas des données d'apprentissage (deep learning) : propriété revenant au concepteur de l'algorithme ou bien aux auteurs (pas toujours bien identifiés) des multiples jeux de données qui constituent par fusion les données d'apprentissage ?

Question : est-ce qu'un modèle d'apprentissage pour une IA, c'est un jeu de données ou bien est-ce encore un produit de recherche différent qui doit plutôt être considéré comme un logiciel ? Pour les modèles d'Océrisation nécessaires à Kraken pour fonctionner, il est prévu de les mettre à disposition à la communauté des utilisateurs de Kraken sur un github où on peut les trouver.  

#### 4.2.4 restrictions éventuelles à la réutilisation sur les données ré-utilisées

### 4.3 Questions éthiques

#### 4.3.1 Comment la nature des données d'un point de vue éthique peut avoir un impact sur leur conservation ou leur réutilisation ?

voir document de la commission européenne sur les aspects éthiques [[@europeancommissionGuidanceHowComplete2019]]  : cette checklist est faite pour aider les chercheurs à trouver des financements, mais les réponses qui y sont apportées vont conditionner une plus ou moins grande ouverture des données

#### 4.3.2 Quels standards en matière d'éthique ont été utilisés pour autoriser la collecte d'informations

Référence aux [[comités d'éthique]], dépôt des projets de collecte de données et des protocoles d'expérimentation sur [[Prospero]], etc.

## 5. Partage des données et conservation sur le long terme

### 5.1 Ouverture des données, restrictions et embargos

Quelle licence appliquer au jeu de données
S'ils s'agit de données publiques, on n'a le choix en France qu'entre Etalab et ODbL[[@ginouvesPourquoiCommentOu]]

#### 5.1.1 trouvabilité des données

Quel entrepôt ? délivre des DOI ? [[modération]] de l'accès aux données ? indexation du jeu de données dans un catalogue ? 

Faut-il donner le même titre au dataset qu'à l'article : using the exact same title for both your paper and the underlying dataset; even if you don’t get the two mixed up, other people and computer algorithms probably will


#### 5.1.2 période de conservation des données

période pendant laquelle les données vont être conservées ([[cycle de vie de la donnée]]), coût de la conservation pendant cette période

#### 5.1.3 échéance de la mise en accès des données

préciser s'il y aura un embargo à la réutilisation de ces données et de quelle durée, justifier cet embargo (publication ? dépôt de brevet ?)

> il faut pouvoir argumenter pour préciser pourquoi des données sont fermées mais il est toujours possible de fixer un embargo, de se réserver l’exclusivité des données utilisées pendant une durée déterminée. A l’expiration de l’embargo, ces données seront accessibles et utilisables par toutes et tous

source: [[@ginouvesPourquoiCommentOu]]

#### 5.1.4 Les données seront-elles restreintes à certains publics

et si oui sur quel critère, comment demander à avoir accès, quelles informations fournir ?

### 5.2 Comment les données finales ont été sélectionnées et comment seront-elles conservées sur le long-terme

#### 5.2.1 Quelles données devront ne pas être communiquées ou détruites et pour quelles raisons ? 

#### 5.2.2 Préciser le processus de sélection des données qui seront conservées sur le long terme

#### 5.2.3 Indiquer quelques pistes de réutilisation des données ou quelles communautés trouveraient de l'intérêt à réutiliser ces données

#### 5.2.4 Où les données ont-elles été déposées (si pas dans un répertoire de données)

### 5.3 Quelles méthodes ou logicielles sont nécessaires pour obtenir les données

#### 5.3.1 Comment a t-on facilité à l'utilisateur l'extraction des données

importance des logiciels libres

#### 5.3.2 autres précisions sur les manières d'accéder aux données

### 5.4 identifiants pérennes pour les jeux de données

Veiller à ce que l'entrepôt de données permette d'obtenir un [[DOI]]

## 6. Responsabilités dans la gestion des données

### 6.1 Qui sera responsable du traitement, de la conservation et du partage des données 

(nom, rôle, fonction, institution)

#### 6.1.1 Préciser les différents rôles et interventions

#### 6.1.2 Dans un cadre multi-établissement, comment sont partagées les opérations sur les données

#### 6.1.3 Qui est responsable du DMP et de sa révision 

#### 6.1.4 quelle échéance pour la prochaine révision du DMP

### 6.2 Quelles ressources pour vérifier que les données sont [[FAIR]]

#### 6.2.1 Coûts du traitement de la donnée










$\newline$
# bibliographie
$\newline$







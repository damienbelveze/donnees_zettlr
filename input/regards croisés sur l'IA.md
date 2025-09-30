---
title: RAGaRenn
subtitle: "Regards croisés sur l'IA : RGPD, Propriété intellectuelle, sécurité informatique"
id: 20240612_RAGaRenn
author: Damien Belvèze
date: 2024-06-12
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - RGPD
  - sécurité_informatique
  - propriété_intellectuelle
---
En présence de Vincent Repain (sécurité informatique), Justine Gorriz (DPO UR), Lucie Dupont (propriété intellectuelle)

# sécurité informatique et IA

- infection
- infiltration
- manipulation

phase d'entraînement (on abreuve le modèle d'une grande quantité)
phase de test (on corrige la partie d'entraînement)
phase de production (on utilise le modèle)

**infection** : injection dans les données d'entraînement de données qui seraient fausses, biaisées. Exemple classique dans le cas d'un entraînement supervisé (entraînement supervisé : injections de données avec des mots-clé, exemple tas de photos de chat étiqueté "chat"). L'infection consiste à injecter des tas de photos de chat étiquetés "souris".

**Exfiltration** : vol de données. Exfiltration des données du modèle ou bien des paramètres du modèle. Un modèle c'est très long et très coûteux à entraîner, ça coûte beaucoup d'argent, donc ça a beaucoup de valeur. 

**manipulation** : tromper le modèle. 
modèle à reconnaissance visuelle : un attaquant qui aurait connaissance des paramètres du modèle, peut faire croire à l'IA qu'un panneau stop, n'est pas un panneau stop.

# Administration

cas d'usages : aide à la rédaction, aide à la recherche documentaire interne, aide à la gestion des stockes, aide au développement informatique, aide à la centralisation des règles juridiques. 

## recommandations SSI

(recommandations de l'ANSSI)

- Respecter les mêmes règles de sécurité que pour des applications qui ne sont pas des IA (filtrage de ports, contrôle des autorisations d'accès)
- s'assurer de la sécurité des IA externes
- Prévoir un mode dégradé des services métier sans système d'IA
- contrôler les productions de l'IA (ne jamais croire ce que nous dit une IA, il faut toujours contrôler le résultat). Les développeurs informatiques ont tendance à sur-estimer les compétences IA à créer du code sécurisé et à sous-estimer ses propres compétences à produire du code sécurisé
- faire produire du code lisible. l'IA produit des variables A,B,C,D... dont l'usage devient vite illisible si le code est long. 

## RGPD

[[RGPD]] ne pas entraîner des IA avec des données à caractère personnel.

RGPD, article 22: Droit à ne pas faire l'objet d'une décision automatisée. Toutes les décisions doivent être revérifiées par un humain. Les caméras algorithmiques ne reconnaissent pas une partie de la population parce qu'elles n'avaient été entraînées à reconnaître que des hommes blancs. 

## propriété intellectuelle

adopter des solutions d'IA Open Source pour éviter des problèmes de licence (favoriser les outils sous [[licences libres]])

- etablir des politiques strictes de gestion et de protection des données sensibles. 
- établir un cadre de gouvernance robuste pour la prose de décision automatisée. Systèmes explicatifs : apporter la preuve qu'une intervention humaine a été faite pour contrôler la décision automatisée. 
- Mettre en place des politiques institutionnelles de [[propriété intellectuelle]]. Réglement de co-propriété : à qui appartient le prompt initial, à qui appartient le modèle ? à qui appartient le serveur sur lequel il est hébergé
- Respecter un cadre éthique pour l'utilisation de l'IA. Utiliser des IA dont l'analyse des biais sera une priorité. 

# Pédagogie

## Sécurité informatique

Sensibiliser les étudiants et les enseignants aux risques liés
ne pas donner d'informations internes dans les sujets de cours ou d'examens.
On considère que toute info livrée dans un prompt a le statut d'information fuitée. Ne pas donner d'information interne à l'établissement. 

## RGPD 

pas de notation de l'étudiant par IA sans contrôle de l'enseignant. 

droit à l'information : les personnes doivent savoir qu'une IA a été utilisée dans une décision le concernant. Droit d'opposition : possibilité de l'étudiant de sortir de ce système de notation semi-automatisé. 

ne pas entraîner l'outil d'IA avec des données personnelles d'étudiants

## propriété intellectuelle

Intégrer la logique que l'enseignant-chercheur gardent la propriété de tout ce qu'ils créent. 

utiliser le système d'IA explicable

Former à l'utilisation de l'IA au regard de la propriété intellectuelle.

# recherche

aide à la rédaction de documents, aide à la compilation et à l'analyse des résultats de recherche, recherche de plagiat et de contrefaçon, aide à la diffusion des résultats, aide au développement d'IA

## sécurité informatique et IA

Création d'IA : cloisonner chaque phase de l'IA dans un environnement propre et dédié
Protéger les données et les fichiers d'entraînement
Ne pas ré-entrainer le modèle directement en production

## RGPD

focus sur les données sensibles
risque d'erreur sur la communauté scientifique
risque de plagiat involontaire de la part de chercheurs qui pensaient la source fiable et donc un risque de reprises de fausses informations
vérifier ses sources afin d'éviter la diffusion de fausses informations. 





$\newline$
# bibliographie
$\newline$







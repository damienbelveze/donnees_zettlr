---
title: accompagnement valorisation d'un code source
id: 20250606_accompagnement valorisation d'un code source
author: Damien Belvèze
date: 2025-06-06
tags:
  - code_source
  - réplicabilité
  - conteneurisation
---
<!--
(shortcut Ctrl+shif+F8)
-->

Alexandre Coche a fait une demande auprès d'ARDoISE et de la SATT pour obtenir de l'aide afin de réaliser deux tâches en partie convergentes : 

- présenter dans les meilleures conditions son code source au prix du logiciel libre du COSO (catégorie meilleur espoir) - candidature à faire avant le 9 juin
- augmenter le niveau de réplicabilité de son code

Le temps de travail qu'a représenté ce suivi est le suivant : 

1 heure pour le premier rendez-vous (28 mai 13h-14h)
2h pour l'exécution du code et les premières tentatives de conteneurisation
1h30 (Martin et moi lors du second rendez-vous 5 juin 15h30-17h)
## 1. Questions génériques

###  1.1 Quel est le type de logiciel dont il s'agit ?

Le code source Geop4th utilise plusieurs briques libres pour faciliter le traitement de données géospatiales. [Il est disponible au téléchargement depuis la forge gitlab.com](https://gitlab.com/AlexandreCoche/geop4th)

Ce code source a été développé en Python et comporte des librairies qui proviennent de deux gestionnaires de paquets : pip pour ce qui est exclusivement Python, conda pour le reste (paquets accessibles via l'outil libre Miniconda)
Son fonctionnement se fait à travers un IDE Python qui est Spyder, le code intègre l'installation de Spyder, mais d'autres IDE peuvent être utilisés selon le souhait de l'utilisateurice
### 1.2 Estimation du volume des données ? (pour prévoir les besoins en stockage)

non pertinent

### 1.3 Questions juridiques : régime juridique particulier ? RGPD ? Droit d'auteur ?

non pertinent
### 1.4 Ouverture du logiciel 

Le logiciel est ouvert et utilisable en licence GPL 3.0

### 1.5 Besoin d'accompagnement pour un PGL ?

Le PGL a été présenté à Alexandre Coche, mais à ce stade (version relativement mature), il était plus pertinent de faire un codemeta pour un versement du logiciel dans Software Heritage
### 1.6 Besoin d'un carnet Hypothèses ?

pas pertinent

### 1.7 Demande d'accompagnement à la réplicabilité des données

L'auteur a spontanément mis en place plusieurs bonnes pratiques pour faciliter la réutilisation de son logiciel : 
- usage d'un outil de contrôle de version
- rédaction d'une documentation détaillée, notamment sur les prérequis et les procédures d'installation
- mis en place d'un environnement virtuel avec conda

J'ai testé l'installation du code source sur mon ordi Linux (Ubuntu 24.04) avec la dernière version de Miniconda3 et fait remonter les soucis que j'ai rencontrés à l'auteur en vue de lui permettre de compléter sa documentation. 
J'ai pu constater globalement que le logiciel s'exécutait sur ma machine moyennant l'ajout de commandes intermédiaires (installation de l'IDE Spyder)

Après en avoir montré l'intérêt à Alexandre Coche, Martin et moi avons essayé de conteneuriser GeoPath avec Docker en misant sur un fichier requirements.txt réalisé avec ```pip -m freeze``` plutôt que sur la liste des dépendances présentes dans le fichier environnement.yml mais nous nous sommes heurtés au fait que si les dépendances Python étaient correctement chargées à travers pip, ce n'était pas le cas pour des dépendances qui n'étaient accessibles que via conda.  
J'ai prévu de soumettre ce cas à Sébastien Rey-coyrehourcq le 11 juin 2025

A titre d'information, je reproduis ici le Dockerfile qui a été constitué au cours de l'entretien : 

```bash
FROM python:3.11-slim
RUN apt-get update && apt-get install -y git
RUN git clone https://gitlab.com/AlexandreCoche/geop4th.git
#RUN mkdir -p ~/miniconda3
#RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh 
#RUN bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 
#RUN rm ~/miniconda3/miniconda.sh
WORKDIR /geop4th
ADD install/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3","src/__init__.py"]
```

## 2. Dépôt du logiciel dans un entrepôt

l'auteur du code source a été invité à ajouter un fichier codemeta à son repo et à archiver celui-ci dans Software Heritage. 
De même nous lui avons conseillé de signaler l'archive de son code source dans HAL en utilisant le fichier codemeta et le SWHID.
Je lui ai montré comment procéder. 

### 2.1 Documentation des données : les données sont-elles déjà  documentées sous un format standard ?
## 3. Traitement de données à  caractère personnel ou sensibles

### 3.1 Déclaration du traitement des données à  caractère personnel ou sensibles : recommander une prise de contact avec le ou la déléguée à  la protection des données de l'établissement afin de compléter cette déclaration.

### 3.2 Recueil du consentement

### 3.3 Anonymisation ou pseudonymisation

### 3.4 Chiffrement des données
### 3.5 Gestion des accès aux données : qui aura accès aux données ? Différences selon les membres de l'équipe ? Types d'accès potentiels.

### 3.6 Questions éthiques


## 4. Lieu de stockage

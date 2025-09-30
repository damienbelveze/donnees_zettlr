---
title: Sauvegarder et contrôler les versions de son travail introduction à Git et Gitlab
subtitle: introduction à Git et Gitlab
id: 20250829_Sauvegarder et contrôler les versions de son travail introduction à Git et Gitlab
author: Damien Belvèze
date: 2025-08-29
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---
voir [[stockage des données|sauvegarde de données]]

Prévoir une clé USB


# 1. Le désastre des manuscrits de thèse perdus

## introduction

La presse se fait l'écho d'appels désespéré de doctorant.e.s à la recherche de leur ordinateur volé (ou perdu) le plus souvent dans un train ou une gare et qui contient 3, 4 ou 5 ans de recherches. 
On a du mal à concevoir aujourd'hui que des doctorant.e.s fassent 3, 4 ou 5 ans de recherche sans faire de sauvegardes de leurs travaux, mais comme ces faits arrivent tous les ans il est nécessaire de consacrer un peu de temps à faire le point sur cette question. 

Sans aller jusqu'à ces cas extrêmes, quel.le doctorant.e n'a pas fait face à la perte de certaines données ou de certains textes soit à cause de la perte de matériels (clés USB, disques externes, ordinateurs), soit suite à de mauvaises manipulations (effacement de fichiers valides)

C'est un problème qui concerne tout le monde et il faut appliquer les bonnes routines qui minimiseront au maximum la perte de données. C'est l'objet de cette formation. 

## Manuscrit + données

Quoi sauvegarder : tout le disque dur (Time Machine pour Mac sauvegarde tout) ? ou seulement les fichiers les plus importants en rapport avec ma thèse ?

On peut trouver un intérêt à sauvegarder tout le disque dur, mais ici on va se limiter aux documents importants pour la thèse : 
- le manuscrit lui-même
- les données

Manuscrit de thèse

Majoritairement du texte, volume limité

Données

Toute sorte de fichiers, pouvant être très volumineux. 
Ces fichiers peuvent être partagés avec d'autres chercheurs/chercheuses

ARDoISE : atelier de la donnée Rennais ; on est là pour vous aider à héberger vos données (et à prévoir des copies de ces données)

Les options en matière d'hébergement des données sont nombreuses et dépendent fortement du contexte : ces données sont-elles sensibles ? Combien de personnes travaillent sur ces données ? sont-elles volumineuses ? 

Ces questions sont à définir dans le cadre d'un PGD et à résoudre avec ARDoISE. 

# 2. la règle des 3,2,1

## Idée n°1 : faire des copies systématiques sur un disque externe

(disque dur ou clé USB)

### Avantages : 

le geste technique est relativement simple

# Inconvénients

(faire trouver les inconvénients)

Investir dans un disque dur externe est utile mais pas très économique (environ 100 euros)

Les mémoires Flash sur les disques externes et surtout sur les clés USB périment vite après un certain nombre de réécriture : les clés deviennent assez vite illisibles. 

matériel sujet à des pertes (surtout les clés USB)
cf. la clé qui passe à la machine à laver :
https://www.babelio.com/livres/Lhomme-La-clef-Revelations-sur-la-fraude-fiscale-du-siec/727530
  
  On doit se promener avec ses moyens de sauvegarde et on risque de les perdre en même temps que l'ordinateur qui contient le document maître

Les sauvegardes ne sont pas automatiques : difficile de tenir à jour les fichiers de copie

## idée n°2 : stocker une copie sur un cloud

### avantages

on n'est pas vraiment limité en place, en tout cas pour le manuscrit de thèse

Les services de cloud proposent souvent des moyens de partage

bonne synchronisation entre la machine et le serveur (clients de synchronisation)

## inconvénients

les sauvegardes sur le cloud ne sont pas entièrement sûres, la dépendance à un tiers (application de GCU qui changent tout le temps) est trop grande si en parallèle d'autres sauvegardes ne sont pas faites sur des outils dont on dispose : 
https://www.seuros.com/blog/aws-deleted-my-10-year-account-without-warning/

Cloud commercial (Dropbox, Microsoft OneDrive, Google Drive, etc.) 
A éviter pour des questions de confidentialité. 
Ces services numériques sont la tête de pont de la Tech américaine. Espionnage industriel + cas des données personnelles (solutions hors RGPD). A noter que cette question concerne aussi les sauvegardes sur des machines propriétaires (MacOS et Windows de plus en plus lié à du cloud, tout ce que vous faites sur votre ordi est enregistré à distance par défaut)
Privilégier des systèmes libres (Linux, FreeBSD, etc.)

Cloud institutionnel : pratique quand on y a accès, mais, on perd l'accès à tout quand on quitte l'institution (institut, université, école)
Comptes moins provisoires : CNRS par exemple.

Recherche de Tiers de confiance. 

## idée n°3 : une copie en local sur un disque externe, une copie sur un cloud

### avantages

seconde copie disponible en cas d'urgence
une copie se trouve ailleurs que chez soi

### inconvénients

complexe à mettre en oeuvre
synchroniser n'est pas sauvegarder ; les clouds par défaut synchronisent. 
on reste en partie tributaire d'un tiers








## 2.2 distinguer synchronisation et sauvegarde

C'est bien d'avoir plusieurs copies de son travail, mais c'est important aussi qu'elles soient à jour. Pour autant, est-ce que tout synchroniser est une bonne idée ?

**"syncing is not backup"**

Par sauvegarde, on entend sauvegarde des dernières versions d'un document. 
Dans le cas de la synchronisation, le fichier original et les copies sont automatiquement mis à jour. 

La synchronisation a un avantage évident : pas de delta entre les différentes copies, toutes sont parfaitement à jour. 

Mais, si l'un de mes fichiers est corrompu, cette corruption s'étend à toutes les copies synchronisées avec celui-ci. 
Si je fais une erreur et que j'efface un fichier, toutes les copies seront automatiquement effacées sans rémission si aucune sauvegarde n'a été faite. 

Une bonne stratégie consiste donc à 

- varier les supports de sauvegarde (ordinateur, disque externe, serveur)
- maintenir une copie synchronisée entre l'ordinateur en local et le serveur
- conserver une sauvegarde relativement à jour sur un disque externe
- gérer les versions sur le serveur et en local pour être sûr de pouvoir remonter le temps en cas de problème. 





## 2.3 Corruption des fichiers

Qu'est-ce qui cause la corruption des fichiers ? 

## 2.4 Faire des sauvegardes sur un autre disque

rsync et borg permettent de faire des sauvegardes ; ce sont des applications qui peuvent être ajoutées à des programmes, notamment des programmes qui reposent sur des opérations automatisées avec une récurrence dans le temps. 
En revanche, si la destination des sauvegarde n'est pas un serveur mais un disque externe, il faut que ce dernier soit monté pour que cela fonctionne. 

#### borg

(pour Linux)
Soit une clé de sauvegarde (nom = 5897-73DF) connectée et montée sur l'ordi.

```shell
borg init -e none /media/dbelveze/5897-73DF/borg
# initialisation d'un dossier de sauvegarde 'borg' sur cette clé
```

Ce dossier une fois désigné comme dossier de destination, on va pouvoir faire une sauvegarde depuis le dossier source (mettons que le dossier source s'appelle backup_phd et se trouve sur le bureau)

```shell
borg create /media/dbelveze/5897-73DF/borg::20250901_1 ~/Bureau/backup_phd
# le nom 20250901_1 précise la version de sauvegarde, par convention il s'agit de la première version réalisée le 1er septembre 2025, on peut cependant mettre le nom qu'on veut. 
```

## 2.5 Synchroniser des fichiers

**[Freefilesync](https://freefilesync.org/)** Multiplateforme, très simple d'usage : peut-être utilisé en [[lignes de commandes]] mais est plutôt conçu pour être utilisé au moyen d'une [[interface graphique]]
(demo : ordi vers clé USB)


**Syncthing**. Logiciel libre et multiplateforme qui permet de synchroniser en [[p2p]] des dossiers et les fichiers qui les contiennent d'un ordinateur vers un ordi distant), sans passer par un Cloud (pour rappel : le Cloud est toujours l'"ordinateur de quelqu'un d'autre") et de manière [[chiffrement|sécurisée]] (protocole TLS)
[manuel simple d'usage](https://www.justgeek.fr/syncthing-134749/) 
démo : synchronisation d'un fichier d'un ordi Linux vers un ordi Windows.


# 3 Git en tant qu’outil de contrôle de version

Git est un outil de contrôle de version. 
Comme pour Borg, toutes les versions d'un même document sont conservées (sauf suppression volontaire d'un commit ce qui est rarement un besoin)
Les différents *commits* sont des états d'un même document. Ils sont identifiés par des empreintes.
Il est possible de les nommer, de les retrouver en remontant le temps et de les restaurer. 

Git comporte un répertoire (tree) qui enregistre ces commits. 
Plusieurs forges logicielles fonctionnent avec Git, mentionnons Gitea, gitlab et la plus connue de toutes Github (aujourd'hui propriété de Microsoft)
Ces produits permettent d'exposer en ligne des travaux qui font l'objet d'un contrôle de version en local sur son ordinateur. 
un entrepôt (repository) git (ou github quand il est poussé vers cette plateforme) peut être gardé privé ou bien peut-être publié (si la forge le permet), il peut être dans l'un et l'autre cas ouvert à des collaborations avec d'autres utilisateurs de git plus ou moins étendues. 
Comme ici on s'occupe de sauvegardes personnelles, on va mettre de côté l'aspect collaboratif de git et des plateformes github et gitlab qui constituent pour autant un aspect très important de ces outils. 
Notons que si Git est le plus souvent utilisé pour versionner du code, rien n'empêche de l'utiliser pour versionner du texte !

démonstration : 

création d'un compte sur Framagit (Framasoft comme tiers de confiance) ; sur cette plateforme on peut créer actuellement jusqu'à 42 repos (projets).

commandes utilisées : 

création d'un repo sur Framagit
clonage de ce repos (``git clone repo``)
désignation de la branche vers laquelle on va envoyer les modifications (``git branch -M main``)
ajout d'un document, y compris dans le registre (`git add document ou git add * )
préparation du commit avec le message de commit (``git commit -m "first commit"``)
envoi vers le repo en ligne (``git push -u origin main``)
Deuxième modification (mêmes commandes que précédemment)
retour au premier état : git revert (Possibilité de revenir en arrière à tout moment.)

Ensemble des commandes présentes ici : https://damienbelveze.github.io/h5p_standalone/git_tuto/git_tuto.html









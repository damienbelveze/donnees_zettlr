---
title: Docker
subtitle: 
id: 20241209_Docker
author: Damien Belvèze
date: 2024-12-09
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - reproductibilité
  - réplicabilité
  - programmation
  - code_source
---
# définition 

outil de conteneurisation qui facilite la réplicabilité (cf. [[reproductibilité]]) du [[code source]] créé en 2012 par Ludovic Courtès.

Les images Docker ne peuvent pas être versées dans [[Software Heritage]], mais les dockerfiles seuls oui.


# Les concepts fondamentaux : images et conteneurs

## Les images

image : package qui inclut le [[code source]], le [[dépendances|software stack]] (pile logicielle), les dépendances système, l'environnement d'exécution, les variables système et tout ce qui est nécessaire pour l'exécution d'un programme

- l'image est **immuable** : on ne peut pas la modifier, il faut la recréer
- elle est **constituée de différentes couches** . Chaque instruction du dockerfile constitue une couche, c'est la raison pour laquelle, afin d'économiser de la mémoire, il ne faut pas que les instructions soient trop redondantes (par exemple au lieu d'indiquer dans le Dockerfile : 
```dockerfile
RUN apt update && apt install -y python3
RUN apt install -y python3-pip
```
utiliser plutôt : 
```dockerfile
RUN apt update && apt install -y python3 python3-pip
```
(autre possibilité, utiliser le multistage : )
- elle est **portable** : elle peut facilement être partagée et distribuée via un répertoire
- **création** : les images sont construites à partir d'un Dockerfile en utilisant la commande ```docker build -t <tag image> <chemin>``` (docker build -t war_cemeteries .     :  crée à partir du répertoire courant (.) où se trouve un Dockerfile une image dont le tag est war_cemeteries)

## les conteneurs

un conteneur est un environnement isolé dans lequel on exécute une image docker

- le conteneur est **modifiable**. On peut le démarrer, le déplacer, l'exécuter, le supprimer (sans supprimer l'image). On peut les modifier pendant leur exécution
- le conteneur est isolé et est exécuté sur la machine hôte de façon isolée, toutefois, contrairement à une [[machine virtuelle]], Docker s'appuie en partie sur le système hôte pour exécuter le conteneur.
- **éphémère** : les conteneurs sont conçus pour être éphémères : on peut en créer autant que de besoin et les supprimer ensuite
- **création** : les conteneurs sont créés à partir des images, en utilisant la commande ```docker run <image>``` (docker run war_cemeteries : démarre un conteneur en partant de l'image tagguée war_cemeteries)

En résumé une image Docker est un modèle pour créer un conteneur, alors qu'un conteneur est une instance en cours d'exécution de ce template



voir support d'introduction à Docker ([ANF24 SIST](https://sist.pages.in2p3.fr/anf24-docker/))



# Installation de Docker

## sur Ubuntu

installation du moteur de Docker : 
https://docs.docker.com/engine/install/ubuntu/
ajout de l'usager au groupe docker pour ne pas avoir à utiliser toujours docker en mode root : 
https://docs.docker.com/engine/install/linux-postinstall/


# construire un conteneur Docker avec Guix

voir [[Guix|guix]]

```shell
guix pack --format=docker -m outils-projet.scm
```
crée une image Docker à partir des informations contenues dans le fichier outils-projet.scm [[@capitoledulibreGNUGuixEnvironnements2023]]






$\newline$
# bibliographie
$\newline$







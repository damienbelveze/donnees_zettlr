---
title: conteneurisation d'un script R
subtitle: 
id: 20250607_conteneurisation d'un script R
author: Damien Belvèze
date: 2025-06-07
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
  - conteneurisation
---

# 1. composition du dossier à conteneuriser

Le script à conteneuriser est en ligne accessible depuis le gitlab d'Humanum : 

```shell
git clone https://gitlab.huma-num.fr/dbelveze/printemps_donnee.git
```
Le dossier code comporte un script en Python à conteneuriser (écrit par Marco Milanesio)

Le dossier code_r comporte un script en Rmarkdown que j'ai écrit. C'est ce dernier que nous allons conteneuriser, le script est présent dans le ficher war_cemeteries.Rmd ; lorsqu'on exécute ce script (knit), on obtient le fichier war_cemeteries.html

Le script war_cemeteries réalise deux opérations principales : 

1. Il récupère depuis Wikidata la liste des cimetières militaires allemands gérés par l'association "Volksbund Deutsche Kriegsgräberfürsorge" avec leurs coordonnées géographiques
2. Il dispose ces cimetières sur une carte

Les packages pour R explicitement demandés par le script sont : 
- le package WikidataR : pour récupérer dans R les données issues de Wikidata au moyen d'une requête en sparql . L'installation de WikidataR se fait sans difficultés.
- le package Leaflet : pour utiliser les coordonnées géographiques récupérés à l'étape précédente afin de porter les cimetières présents dans Wikidata sur une carte openstreetmap. 

Depuis quelques temps, l'installation du package Leaflet est devenue considérablement plus compliquée que par le passé. 
Leaflet a besoin que le package *[[terra]]* ait été préalablement chargé dans R. 
Le package *terra* a besoin que d'autres packages comme *raster* ou *gdal* aient été préalablement chargés et ainsi de suite. 

Pour installer Leaflet dans R (version 4.4), il convient donc de passer par les étapes suivantes : 

1. installer les packages nécessaires pour installer terra. 
```shell
add-apt-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update
sudo apt-get install libudunits2-dev libgdal-dev libgeos-dev libproj-dev libsqlite3-dev
```

2. Dans R installer *terra*
3. Puis installer *leaflet*

Lorsque ces packages sont bien installés, on peut exécuter le script et l'output est le fichier war_cemeteries.html

En développant le code, j'ai créé un environnement virtuel avec le package Renv. 

Ce package permet de saisir toutes les dépendances requises pour exécuter le script R ou Rmarkdown avec une seule commande dans la console de R : 

```r
renv::snapshot()
```

Cette commande crée un dossier Renv et un fichier renv_lock qui constitue un registre de ces packages et de leur version. 

Un développeur qui récupèrerait ce script n'aurait qu'à utiliser Renv de son côté pour charger les bonnes dépendances et les installer sur sa version de R (si tant est que les packages en question demeurent disponibles dans les repos comme celui du CRAN ou d'autres)
La commande a utiliser pour restaurer cet environnement virtuel et symétrique de la première est 

```r
renv::restore()
```

On a vu que cette commande ne permettrait pas à elle seule de charger les packages leaflet et terra parce que celles-ci ont besoin d'autres dépendances qui ne sont pas prises dans le Renv.lock mais peuvent être chargées avec un terminal de commande depuis le *repository* ubuntugis

De là la nécessité pour faciliter le partage du code source de passer par une conteneurisation. 

# 2. écriture du Dockerfile

Un Dockerfile à la racine du dossier qui contient le script à conteneuriser est nécessaire pour que l'image du script puisse être réalisée

la structure du Dockerfile qui sert en quelque sorte de recette pour la fabrication de cette image est la suivante : 

```Dockerfile
FROM image de R
WORKDIR définition d'un environnement de travail
RUN exécution de scripts qui vont permettre de charger différents
CMD commande finale à exécuter (en l'occurrence, exécution du script R ou Rmarkdown)
```

Lorsqu'on a installé Docker sur sa machine, en utilisant le terminal on peut en se plaçant dans le répertoire qui contient le script et le Dockerfile exécuter la commande suivante : 

```shell
docker build -t nom-image .
```
Bien sûr on peut ajouter un chemin vers le Dockerfile ou bien envoyer la commande depuis un autre endroit qu'à la racine du dossier à conteneuriser (.)

En cas de problème rencontré par Docker pour accéder à Internet et installer les paquets demandés, essayer : 

```shell
docker build --network=host -t nom-image .
```

Cela devrait permettre de construire l'image qu'on va utiliser pour la partager. 

Voici le Dockerfile réalisé pour fabriquer une image avec du dossier code_r : 

```Dockerfile
FROM rocker/r-ver:4
RUN echo 'options(repos = c(CRAN = "https://cloud.r-project.org"))' >>"${R_HOME}/etc/Rprofile.site"
RUN apt-get update && apt-get install -y \
software-properties-common \
libudunits2-dev \
libgdal-dev \
libgeos-dev \
libproj-dev \
libsqlite3-dev \
pandoc \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
#LABEL Damien Belvèze <damien.belveze@univ-rennes.fr>
RUN R -e "install.packages('renv', repos = c(CRAN = 'https://cloud.r-project.org'))"
COPY . .
#WORKDIR /code_r
#COPY . /code_r
#COPY renv.lock renv.lock
#RUN mkdir -p renv
#COPY .Rprofile .Rprofile
#COPY renv/activate.R renv/activate.R
#COPY renv/settings.json renv/settings.json
RUN R -e "renv::restore()"
CMD ["R", "-e","rmarkdown::render('war_cemeteries.Rmd', output_file = 'html_document')"]
```

En cas de problème avec l'installation de pandoc, voir la solution [ici](https://tarleb.com/posts/tip-install-in-docker/) (comment intégrer pandoc à un pipeline pour du [[CI/CD]]) ou Docker : 

```shell
COPY --from=pandoc/minimal:2.19.2 /pandoc /usr/bin/pandoc
```


Pour l'image de R à partir de laquelle construire notre image à nous, j'ai utilisé au final  rocker/r-ver:4 
Rocker/r-ver est une image largement utilisé pour reproduire du code avec R et on trouve fréquemment cette image dans les dockerfiles. La version 4 n'est pas la dernière (latest) mais [a été mise à jour en mai 2025](https://hub.docker.com/layers/rocker/r-ver/4/images/sha256-9d6d61d41018e989e06a17af9fb3503baa050f7833b0b0e39bbc084eed0c94cc. J'ai créé mon image en juin, un mois plus tard. 
Au début je me suis dit que le mieux était d'utiliser après le FROM la version de R que j'utilisais R 4.4.3. 
Toutefois, les builds échouaient parce que la commande ``renv::snapshot()`` fixait dans le Renv.lock un package MASS présent dans le CRAN et qui n'était pas chargeable depuis une version antérieure à R 4.5.
Cela n'empêchait pas le script d'être exécuté en local, en revanche, cela entravait la construction d'une image avec Docker ; à chaque fois le chargement des paquets depuis le renv.lock achoppait au moment de charger MASS 3.58 depuis le CRAN sur une image de base R 4.5.
J'ai mis à jour ma version de R et suis passé à la version 4.5 (à la suite de quoi, j'ai du mettre à jour ou recharger tous les paquets déjà chargés) et j'ai changé d'image de référence pour faire un build de mon code ; je suis passé à rocker et à r-ver:4
J'ai vérifié que mon installation me permettait d'exécuter le script sur cette nouvelle version, j'ai fait un snapshot avec Renv pour saisir les dépendances utilisées dans le registre Renv.lock et j'ai réalisé l'image avec Docker. 

En utilisant la commande RUN suivi de ces lignes : 
```Dockerfile
RUN apt-get update && apt-get install -y \
    software-properties-common \
    libudunits2-dev \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    libsqlite3-dev \
    pandoc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```
je charge dans mon conteneur les packages qui sont nécessaires pour installer le package terra et le package leaflet (voir plus haut)

Pour être en mesure d'installer dans mon conteneur les packages présents dans le Renv.lock j'ai besoin au préalable d'y installer Renv depuis le CRAN :
```Dockerfile
RUN R -e "install.packages('renv', repos = c(CRAN = 'https://cloud.r-project.org'))"
```
Ensuite je vais organiser mes fichiers et dossiers dans le conteneur. 
Je vais commencer par définir un espace de travail :
```Dockerfile
WORKDIR code_r
```
Le dossier code_r doit recevoir les fichiers sur lesquels je travaille, avec la commande COPY, je vais y envoyer tous les fichiers à la racine du conteneur
```Dockerfile
COPY . /code_r
```
sauf le renv.lock et le /Rprofile qui sont embarqués dans le conteneur mais restent à sa racine. Je crée un dossier Renv dans le conteneur pour y envoyer tous les fichiers qui se trouvent actuellement dans code_r/renv/ :

```Dockerfile
COPY renv.lock renv.lock
RUN mkdir -p renv
COPY .Rprofile .Rprofile
COPY renv/activate.R renv/activate.R
COPY renv/settings.json renv/settings.json
```
Comme j'ai préalablement embarqué mon fichier renv.lock, que j'ai chargé dans mon conteneur le package Renv pour r-ver, que j'y ai copié tous les fichiers nécessaires à Renv pour fonctionner (sous le répertoire Renv), je suis désormais en mesure de faire la commande renv::restore() pour installer dans l'image R du conteneur tous les packages nécessaires à l'exécution du script. 

```Dockerfile
RUN R -e "renv::restore()"
```
R précise que la commande doit se faire dans R, -e précise que ce qui suit s'exécute comme une commande dans la console de R et non dans le shell ou comme un fichier à exécuter. 

La commande finale a pour but d'exécuter le script Rmd comme on le ferait dans R : 

```Dockerfile
CMD ["R", "-e","rmarkdown::render('war_cemeteries.Rmd', output_file = 'html_document')"]
```
Attention à bien distinguer les guillemets doubles "" qui séparent les éléments de la commande, des guillements simples ' ' qui identifient les noms de fichiers. Si on confond les deux dans cette commande, cette dernière ne pourra pas s'exécuter correctement et un message d'erreur de syntaxe Json apparaîtra dans le terminal. 


# Partage de l'image Docker

La commande suivante réalisée dans un terminal dans le même dossier où se trouve le fichier Dockerfile :
```shell
docker build -t coder .
```
permet donc de créer une image qu'on va tagguer (-t) avec le nom *coder*
Une fois cette image construite, je peux la voir dans la liste des images disponibles au moyen de la commande : 

```shell
docker images
```
cela donne : 

| REPOSITORY | TAG    | IMAGE ID     | CREATED         | SIZE   |
| :--------- | :----- | :----------- | :-------------- | :----- |
| coder      | latest | 340d8a55dd94 | 11 minutes  ago | 2.04GB |

Si je veux exécuter l'image *coder* à partir de n'importe quel emplacement sur mon ordinateur, je n'ai qu'à passer la commande suivante dans le terminal : 

```shell
docker run coder
```

En revanche, l'opération a lieu dans mon conteneur et pas dans mes dossiers habituels, ce qui fait que je ne vois pas directement le résultat de l'opération.

Si je souhaite copier le résultat de l'exécution du script dans le conteneur (le fichier war_cemeteries.html) dans un répertoire de mon ordinateur, je dois d'abord récupérer le nom de mon image avec la commande 

```shell
docker ps -a
```
(affiche les images actives présentes dans Docker, celles pour lesquelles j'ai fait un *run*)

J'obtiens comme résultat dans mon terminal : 

| CONTAINER ID | IMAGE | COMMAND                | CREATED       | STATUS     | PORTS         | NAMES      |
| :----------- | :---- | :--------------------- | :------------ | :--------- | :------------ | :--------- |
| 3b3919f105af | coder | "R -e 'rmarkdown::re…" | 6 minutes ago | Exited (0) | 6 minutes ago | sad_darwin |

Le nom sad_darwin a été arbitrairement assigné à mon image, je vais l'utiliser pour faire la copie du fichier depuis mon conteneur vers mon espace de travail. J'ouvre le terminal de commande à l'endroit où je veux faire ma copie et je tape la commande suivante : 

```shell
docker cp sad_darwin:/code_r/war_cemeteries.html .
```
le fichier war_cemeteries.html apparaît bien à ce endroit. 

Si je souhaite partager l'image avec un tiers, je peux en faire une archive et la lui envoyer. 
La génération de l'archive .tar se fait avec la commande ``docker save``

```shell
docker save -o ./code_r/coder.tar coder
```
Fait de l'image coder un fichier coder.tar dans le dossier /code_r

Si je dispose d'un compte sur Dockerhub, je peux aussi l'envoyer sur ce repository avec la commande ``docker push`` afin que d'autres, au besoin l'y trouvent et la récupèrent avec la commande symétrique ``docker pull``

Pour cela je procède en deux temps : 
1. taguer l'image
2. l'envoyer (push) vers dockerhub

Cela suppose bien entendu que j'ai un compte (facile à créer) sur Dockerhub. 

la commande docker images ne donnait pas de numéro de version à mon image parce que je ne lui en ai pas donné (ce sera donc par défaut la dernière version : 'latest')

Mon nom d'utilisateur de Docker est dbelveze ; je vais associer ce nom d'utilisateur avec l'image de la façon suivante : 

```shell
docker save -o ./code_r/coder.tar coder
```
Si ce n'est pas encore fait, je vais m'identifier sur le site dockerhub : 

```shell
docker login
```
et une fois identifié, je vais faire un push de cette image vers ce répertoire : 

```shell
docker push dbelveze/coder:v1.0
```
le tag v1.0 ici me permet d'identifier cette image comme la première version chargée sur Dockerhub (il y en aura peut-être d'autres à suivre)

Mon image est désormais prête sur dockerhub (https://hub.docker.com) pour être partagée avec d'autres. 


# autres commandes docker

supprimer toutes les images qui ne sont pas en cours d'exécution : 

```shell
docker system prune -a

# WARNING! This will remove:
#  - all stopped containers
#  - all networks not used by at least one container
#  - all images without at least one container associated to them
#  - all build cache
```











$\newline$
# bibliographie
$\newline$







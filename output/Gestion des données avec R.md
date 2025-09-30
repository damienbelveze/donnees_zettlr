---
title: Gestion des données avec R
subtitle: 
id: 20240829_Gestion des données avec R
author: Damien Belvèze
date: 2024-08-29
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - édition_scientifique
  - données_recherche
  - programmation
---
Traduction du guide de Nabeel Sidiqqi sur Programming Historians [Data wrangling and management in R](https://programminghistorian.org/en/lessons/data_wrangling_and_management_in_R)

# Prérequis

Cette leçon comporte quelques prérequis sur votre compréhension de [[R (logiciel)|R]]. Si vous n'avez pas été au bout des [bases de R avec des données tabulées](https://programminghistorian.org/lessons/r-basics-with-tabular-data), je vous suggère de le faire d'abord. Avoir une expérience dans un autre langage de programmation peut aussi vous aider. Si vous souhaitez savoir par où commencer, je vous recommande de parcourir les excellents tutoriels de *Programming Historian* sur [[Python]].

# Objectifs de la leçon

A la fin de cette leçon, vous serez en mesure de :

  1. comprendre comment organiser vos données pour qu'elles soient *ordonnées* et pourquoi c'est important.   
  2. comprendre le paquet [[dplyr]] et l'utiliser pour manipuler et administrer les données  
  3. se familiariser avec l'opérateur [[pipe]] dans R et observer comment il peut vous aider à créer du code plus lisible  
  4. apprendre à travailler sur des exemples de base de manipulation de données pour acquérir les fondements de l'analyse exploratoire des données  

# Introduction

Les données que vous trouverez "dans la nature" sont rarement dans un format qui rend possible une analyse et vous aurez à les manipuler avant d'explorer les questions que vous souhaitez leur poser. Cette manipulation peut prendre plus de temps que l'analyse elle-même ! Dans ce tutoriel, nous apprendrons quelques techniques de base for manipuler, gérer et administrer nos données dans R. Notamment, nous nous fonderons sur la philosophie des ["données propres"](https://www.jstatsoft.org/article/view/v059i10)(*tidy data*) telle que l'a présentée Hadley Wickham. (voir aussi : https://tidyr.tidyverse.org/articles/tidy-data.html)

Selon Wickham, la donnée est "propre" quand elle répond à ces trois critères : 

  1. Chaque observation dans une ligne.
  2. Chaque [[variable]] dans une colonne.
  3. Chaque valeur a sa propre cellule.
  
Remplir ces critères nous permet de juger si la donnée est organisée ou pas. Ces critères nous fournissent également un schéma standard et un ensemble d'outils pour gérer les formes les plus communes de désordre dans les données :

  1. les entêtes de colonnes sont des valeurs et pas des noms de variables   
  2. plusieurs variables sont stockées dans une même colonne
  3. des variables sont présentes à la fois dans les colonnes et dans les lignes
  4. une seule unité d'observation est présente dans plusieurs tables
  
Avantage peut-être encore plus important, garder nos données dans ce format propre nous permet d'utiliser une galerie de paquets dans le ["tidyverse"](http://tidyverse.org/), qui ont été spécifiquement conçus pour fonctionner avec des données propres. En nous assurant que nos données en entrée et en sortie sont propres, nous n'auront qu'un petit nombre d'outils à utiliser pour résoudre un grand nombre de questions. De plus, nous pouvons combiner, manipuler et scinder des jeux de données comme bon nous semble.

Dans ce tutoriel, nous traiterons particulièrement le paquet [*dplyr*](https://cran.r-project.org/web/packages/dplyr/index.html) du tidyverse. Mais cela vaut la peine de mentionner brièvement quelques autres paquets que nous utiliserons : 

- [**magittr**](http://magrittr.tidyverse.org/) : ce paquet donne accès à l'opérateur pipe et rendre le code plus facile à lire.   

- [**ggplot2**](http://ggplot2.tidyverse.org/) : ce paquet utilise la [*"grammaire des graphiques"*](http://www.springer.com/us/book/9780387245447) pour vous permettre de donner des visualisations simples à réaliser de vos données.    

- [**readr**](http://readr.tidyverse.org/) : ce paquet met à disposition un import plus rapide et intuitive de données tabulées, comme des fichiers csv.     

- [**tibble**](http://tibble.tidyverse.org/) : ce paquet nous donne accès à une nouvelle conceptualisation des tableaux de données qui seront plus simples à traiter et à imprimer.  

Si vous ne l'avez pas déjà fait, vous devriez installer et charger le "tidyverse" avant de commencer. Assurez-vous en outre que vous disposez de la [dernière version de R](https://cran.rstudio.com/) et de la [dernière version de Rstudio](https://www.rstudio.com/products/rstudio/download/) installées sur votre système d'exploitation.

Copiez le code ci-dessous dans Rstudio. Pour les exécuter, il vous faut mettre ces lignes en surbrillance et presser Ctrl+enter (ou Cmd+enter sur Mac OS):
  
```{r echo=TRUE, include=TRUE}

# Installer les bibliothèques tidyverse et charger ces bibliothèques
# Ne vous inquiétez pas si cela prend un peu de temps 

install.packages("tidyverse", repos = "http://cran.us.r-project.org")
library(tidyverse)
```


# Un exemple du fonctionnement de dplyr

Utilisons un exemple pour voir comment dplyr peut nous aider en tant qu'historien : importons les données de recensement décennal des Etats-Unis entre 1790 et 2010. Téléchargez les données en [cliquant ici](https://programminghistorian.org/assets/introductory_state_example.csv) et placez le fichier téléchargé dans le dossier que vous utiliserez pour traiter les exemples présentés dans ce tutoriel. 

Etant donné que les données sont présentées dans un fichier csv, nous allons utiliser la commande read_csv() comprise dans le paquet [readr](https://cran.r-project.org/web/packages/readr/vignettes/readr.html) du tidyverse.

```{r echo=TRUE, include=FALSE}
# Importer le fichier CSV et le sauvegarder dans la variable us_state_populations_import
# Assurez-vous que le chemin vers le fichier est bien défini
library(tidyverse)
us_state_populations_import<-read_csv("introductory_state_example.csv")
```

Après avoir importé les données, vous remarquerez qu'elles sont disposées en trois colonnes : une pour la population, une pour l'année et une pour l'État. Ces données sont d'emblée dans un format propre, ce qui nous permet de nous livrer à une multitude d'explorations. 

Pour cet exemple, créons une visualisation de la croissance de la population en Californie et dans l'État de New York afin d'avoir une meilleure compréhension des migrations vers l'Ouest. On va utiliser dplyr pour filtrer nos données, de telle sorte qu'elles ne contiennent que les informations relatives aux États qui nous intéressent et on va utiliser ggplot2 pour visualiser cette information. Cet exercice n'a d'autre but que de nous donner une idée de ce que dplyr peut faire, ne vous en faites pas si vous ne comprenez pas le code utilisé à ce stade : 

```{r echo=TRUE }
# Filtrer le jeu pour ne traiter que les données relatives à la Californie et à l'État de New York
california_and_new_york_state_populations<-us_state_populations_import %>%
  filter(state %in% c("California", "New York")) 

# possibilité aussi d'utiliser la fonction subset de base de R 
# California_population <-subset(california_and_new_york_state_populations, reg_name == "California")


# Editer le graphique des courbes de population de la Californie et de l'État de New York
ggplot(data=california_and_new_york_state_populations, aes(x=year, y=population, color=state)) +
  geom_line() +
  geom_point()
```

Comme on peut le voir, la population de la Californie a cru de façon considérable comparée à celle de l'État de New York. Cet exemple en particulier peut sembler évident, compte tenu de l'histoire des migrations aux Etats-Unis, mais le code en lui-même nous procure une base à partir de laquelle poser une foule de questions semblables. Par exemple, avec une modification rapide du code, on peut créer un graphique équivalent pour deux autres États comme le Mississipi et la Virginie. 

```{r echo=TRUE }
# Filtrer le jeu pour ne traiter que les données relatives au Mississippi et à la Virginie
mississippi_and_virginia_state_populations<-us_state_populations_import %>%
  filter(state %in% c("Mississippi", "Virginia"))

# Éditer le graphique des courbes de population du Mississippi et de la Virginie
ggplot(data=mississippi_and_virginia_state_populations, aes(x=year, y=population, color=state)) +
  geom_line() +
  geom_point()
```

La possibilité de faire des changements rapides dans le code et de réanalyser nos données est un élément fondamental de l'analyse exploratoire de données (AED). Plutôt que d'essayer de "prouver" une hypothèse, l'analyse exploratoire de données nous aide à mieux comprendre nos données et à les interroger. Pour les Historiens, l'AED nous apporte un moyen aisé de savoir quand on peut approfondir un sujet ou bien quand on doit reprendre de la hauteur, et c'est un sujet sur lequel R excelle.

# L'opérateur Pipe

Avant de jeter un coup d'oeil à dplyr, nous devons examiner ce qu'est l'opérateur pipe (%>%) dans R, car nous l'utiliserons souvent dans nos exemples. Comme mentionné plus haut, l'opérateur pipe fait partie du paquet [magrittr](https://cran.r-project.org/web/packages/magrittr/vignettes/magrittr.html) mis au point par [Stefan Milton Bache](http://stefanbache.dk/) et [Hadley Wickham](http://hadley.nz/) et est inclus dans le tidyverse. Son nom rend hommage au peintre surréaliste René Magritte qui, dans son oeuvre "La trahison des images", a représenté une pipe célèbre en plaçant en dessous la légende "ceci n'est pas une pipe". 

L'opérateur pipe nous permet de passer ce qui est à gauche du pipe comme la première variable de la fonction qui est donnée à droite. Bien que cela puisse paraître étrange au premier abord, une fois que vous l'aurez appris, vous trouverez qu'il rend votre code plus lisible en vous évitant d'enchâsser vos opérations les unes dans les autres. Ne vous inquiétez pas si tout cela vous semble encore confus pour l'instant ; ça va s'éclairer progressivement avec des exemples. 

Supposons que nous ayons un intérêt à obtenir la racine carrée de la valeur pour la population de chaque État, puis d'en faire la somme et finalement la moyenne. A l'évidence, cette mesure ne nous sert à rien, mais cela permet de montrer à quel point un code  réalisé avec R peut rapidement devenir difficile à lire. 
Normalement, nous pourrions enchâsser ces opérations : 

```{r echo=TRUE, include=TRUE}
mean(sum(sqrt(us_state_populations_import$population)))
```

Comme on peut le voir, avec des commandes enchâssées, il est difficile de se rappeler combien de parenthèses doivent être fournies et cela donne un code assez pataud. Pour minimiser cela, certains vont créer des vecteurs temporaires entre chaque appel de commandes. 

```{r echo=TRUE, include=TRUE}
# Obtenir la racine carrée de la population de chaque Etat

sqrt_state_populations_vector<-sqrt(us_state_populations_import$population)

# Obtenir la somme de toutes les racines carrées des variables temporaires

sum_sqrt_state_populations_vector<-sum(sqrt_state_populations_vector)

# obtenir la moyenne de la variable temporaire

mean_sum_sqrt_state_populations_vector<-mean(sum_sqrt_state_populations_vector)

# Afficher la moyenne

mean_sum_sqrt_state_populations_vector
```

Vous obtenez certes la même réponse, mais de façon beaucoup plus lisible. En revanche, cela peut rapidement encombrer votre espace de travail si vous oubliez de supprimer les vecteurs temporaires. L'opérateur pipe fait tout cela oour vous. Voici le même code mais avec l'opérateur pipe : 

```{r echo=TRUE, include=TRUE}
us_state_populations_import$population%>%sqrt%>%sum%>%mean
```

C'est bien plus simple à lire, et vous pourriez même rendre cette commande encore plus claire en l'écrivant sur plusieurs lignes : 

```{r echo=TRUE, include=TRUE}
# assurez-vous que l'opérateur soit à la fin de la ligne
us_state_populations_import$population%>%
    sqrt%>%
    sum%>%
    mean
```

Notez que les vecteurs ou les tableaux que crée l'opérateur pipe sont supprimés lorsque le processus est achevé. Si vous souhaitez les conserver, vous devrez en faire de nouvelles variables :

```{r echo=TRUE, include=TRUE}

permanent_sqrt_and_sum_state_populations_vector <- us_state_populations_import$population%>%sqrt%>%sum%>%mean
permanent_sqrt_and_sum_state_populations_vector
```

# Il nous faut un nouveau jeu de données

Maintenant que nous comprenons comment fonctionne le pipe, nous sommes en mesure de commencer à examiner et manipuler des données. Malheureusement, pour les historiens, il n'y a que peu de jeux de données disponibles ; peut-être pourriez-vous contribuer à ce que cela change en diffusant vos propres données ! Nous allons partir du paquet de [données historiques](https://www.google.com/search?q=cran%20historydata) créé par [Lincoln Mullen](http://lincolnmullen.com/)

Allons-y, installons et chargeons ce paquet : 

```{r echo=TRUE, include=FALSE }
# installer le paquet historydata
install.packages("historydata", repos = "http://cran.us.r-project.org")

# charger le paquet historydata
library(historydata)
```

Ce paquet contient un échantillon de données historiques. Les données de recensement qu'on a utilisées plus tôt font partie de cet échantillon. Jusqu'à la fin de ce tutoriel, on va particulièrement travailler avec le jeu de données early_colleges qui contient des données sur les *Colleges* fondés avant 1848. Commençons par charger les données et y jeter un coup d'oeil : 

```{r echo=TRUE, include=TRUE }
# Vérifiez avant d'exécuter ce code que le paquet historydata a bien été installé et chargé

data(early_colleges)
early_colleges
```

Comme vous pouvez l'observer, ce jeu de données contient le nom actuel de chaque *college*, son nom à l'origine, la ville et l'État dans lequel il a été fondé, la date de sa fondation et l'organisation qui le parraine. Comme on l'a vu plus haut, avant de commencer à travailler sur ce jeu de données, il est important de penser à la façon dont on va organiser ces données. Voyons si certaines de nos données ne se trouveraient pas dans un format "impropre". Voyez-vous des cellules qui ne répondraient pas aux trois critères que remplissent les données "propres" ?

Si vous avez répondu le parrainage de Harvard, vous avez la bonne réponse. En plus de mentionner le premier parrainage de ce *college*, la cellule comporte l'information de son changement de parrainage en 1805. Habituellement, on veut conserver dans nos données autant d'information que possible, mais pour rester dans la perspective de ce tutoriel, nous allons modifier la colonne pour ne conserver que les parrainages lors de la fondation. 

```{r echo=TRUE, include=TRUE }
early_colleges[1,6] <- "congregational"
early_colleges
```
A présent que nos données se présentent dans un format propre, nous pouvons leur donner forme avec le paquet dplyr. 

# Qu'est-ce que Dplyr ?

[Dplyr](https://cran.rstudio.com/web/packages/dplyr/vignettes/dplyr.html) est un autre élément du tidyverse qui met à votre disposition des fonctions utiles pour manipuler et transformer des données. Parce que nous gardons nos données "propres", nous n'avons besoin que d'un nombre réduit d'outils pour les explorer.
Comparé à R seul, utiliser dplyr est souvent plus rapide et vous garantit que si les données en entrée sont propres, les données transformées le seront aussi, et ce qui est peut-être encore plus important, dplyr facilite la lecture de votre code et utilise des "verbes" qui sont intuitifs la plupart du temps. Chaque fonction dans dplyr correspond à l'un de ces verbes, dont les plus importants sont : filtrer(*filter*), sélectionner(*select*), arranger(*arrange*), muter(*mutate*) et récapituler(*summarise*, avec le *s* de l'orthographe britannique). Parcourons-les un à un pour voir comment ils fonctionnent dans la pratique.

## select

Si on regarde les données comprises dans early_colleges, on peut observer qu'il y a un grand nombre de "NA" dans la colonne des noms originaux. NA ([[Not Available]]) signifie qu'on n'a aucune donnée correspondante et qu'on pourrait vouloir visualiser nos données en soustrayant cette colonne. la fonction *select* de dplyr nous donne la possibilité de le faire. On prend le tableau de données qu'on veut manipuler comme le premier argument, suivi d'une liste qui indique quelles colonnes on souhaite conserver : 

```{r echo=TRUE, include=TRUE}
# supprime la colonne des noms originaux en utiliser select()
# Notez que vous n'avez pas à préfixer le nom de la colonne par un $
# dplyr traite automatiquement la virgule comme un AND

select(early_colleges, college, city, state, established, sponsorship)
```

Allons encore plus loin et voyons cpmment on peut écrire ceci en utilisant l'opérateur pipe (%>%) :

```{r echo=TRUE, include=TRUE}
early_colleges%>%
    select(college, city, state, established, sponsorship)
```
Devoir référencer toutes les colonnes qu'on veut conserver juste pour se débarrasser d'une seule est un peu fastidieux. Nous pouvons à la place utiliser le symbole moins ( - ) pour signifier que nous voulons enlever une colonne.

```{r echo=TRUE, include=TRUE}
early_colleges%>%
  select(-original_name)
```

## filter


La fonction filter() réalise la même chose que la fonction select() à ceci près qu'au lieu de choisir le nom d'une colonne, on peut utiliser filter() pour filtrer les lignes qui réalisent une certaine condition. Par exemple, on peut visualiser tous les *colleges* qui ont existé avant la fin du 18ème siècle. 


```{r echo=TRUE, include=TRUE}
early_colleges%>%
  filter(established < 1800)
```

## mutate

La commande *mutate* vous permet d'ajouter une commande à votre tableau de données. Ici nous avons la ville et l'État qui se trouvent dans deux colonnes séparées. Nous pouvons utiliser la commande "coller" pour combiner ces deux chaînes de caractères en une seule tout en gardant un séparateur. Plaçons ces deux informations dans une seule et même colonne intitulée "location".

```{r echo=TRUE, include=TRUE}
early_colleges%>%mutate(location=paste(city,state,sep=","))
```
Encore une fois, il faut vous rappeler que dplyr ne conserve pas les données  ni ne manipule le document original. A la place, il crée un tableau de données temporaire à chaque étape. Si vous souhaitez le conserver, vous devez lui associer une variable permanente. 

```{r echo=TRUE, include=TRUE}
early_colleges_with_location <- early_colleges%>%mutate(location=paste(city,state, sep=","))

# Voir le nouveau tableau avec la colonne "location" ajoutée
early_colleges_with_location
```

## arrange

La fonction *arrange()* nous permet d'ordonner nos colonnes d'une autre façon. Pour l'instant, les *colleges* sont organisés par année de fondation en ordre croissant. Plaçons les par ordre décroissant. Dans notre cas, à partir de la fin de la Guerre américano-mexicaine :

```{r echo=TRUE, include=TRUE}
early_colleges%>%
  arrange(desc(established))
```

## Summarise

La dernière fonction-clé de dplyr est *summarise()* (n'oubliez pas, avec un s comme dans la forme britannique). Summarise() occupe une fonction ou une opération et est habituellement utilisé pour créer un tableau de données qui contient des données statistiques récapitulatives destinées à fournir des graphiques. Nous allons l'utiliser pour calculer la date de fondation moyenne des *colleges* avant 1848

```{r echo=TRUE, include=TRUE}
early_colleges%>%summarise(mean(established))
```

## Et si nous compilions ces fonctions ?

Maintenant que nous avons parcouru les cinq principaux verbes de dplyr, nous pouvons les utiliser pour créer rapidement une visualisation de nos données. Allons-y,  créons un graphique en barres pour afficher le nombre de *colleges* laiques ou religieux fondés avant la guerre de 1812: 

```{r echo=TRUE, include=TRUE}
secular_colleges_before_1812<-early_colleges%>%
  filter(established < 1812)%>%
  mutate(is_secular=ifelse(sponsorship!="Secular", "no", "yes"))

ggplot(secular_colleges_before_1812) +
  geom_bar(aes(x=is_secular, fill=is_secular))+
  labs(x="est-ce que le college est laïque ?")
```

Encore une fois, en n'apportant qu'une modification rapide à notre code, nous pouvons aussi visualiser le nombre de *colleges* laïques par rapport au nombre de *colleges* religieux fondés depuis le début de la Guerre de 1812 : 

```{r echo=TRUE, include=TRUE}
secular_colleges_after_1812<-early_colleges%>%
  filter(established > 1812)%>%
  mutate(is_secular=ifelse(sponsorship!="Secular", "no", "yes"))

ggplot(secular_colleges_after_1812) +
  geom_bar(aes(x=is_secular, fill=is_secular))+
  labs(x="Est-ce que le college est laïque ?")
```

# Conclusion

Ce tutoriel devrait vous mettre sur la bonne voie pour bien concevoir l'organisation et la manipulation de vos données avec R. Plus tard, vous souhaiterez sans doute progresser en visualisation de vos données. Je vous recommande de regarder le paquet [ggplot2](https://ggplot2.tidyverse.org/) pour trouver des outils qui fonctionneront bien avec dplyr. De plus vous pouvez être tenté d'examiner quelques autres fonctions accessibles dans dplyr pour affiner vos compétences. Dans les deux cas, ce guide vous permet de disposer d'une bonne base pour aller plus loin et couvrir les problèmes courants que vous pourriez rencontrer dans la gestion de données.

---

### Sur l'auteur
Nabeel Siddiqui est un Professeur Assistant en médias numériques à l'Université de Susquehanna

---

### Citation suggérée
Nabeel Siddiqui, "Gestion et manipulation des données avec R", traduit par Damien Belvèze, Programming Historian en français 2 (2024),

___

# ajouts concernant dplyr

## Rename

pour renommer des colonnes

```r
> df1 = data_frame(index = 1:5, value = c(10, 20, 30, 40, 50))
> df1
# A tibble: 5 x 2
  index value
  <int> <dbl>
1     1    10
2     2    20
3     3    30
4     4    40
5     5    50

> newname = 'blau'
> newname2 = 'wheee'

> df1 %>% rename(!!newname := value, !!newname2 := index)
# A tibble: 5 x 2
  wheee  blau
  <int> <dbl>
1     1    10
2     2    20
3     3    30
4     4    40
5     5    50
```

```r
#créer une autre colonne avec le contenu d'une colonne existante

# chargement de dplyr et stringr
library(dplyr)
library(stringr)

# création du dataframe

df1 = data_frame(index = 1:5, inscrits = c(20, 17, 21, 15, 13), presents = c(20,16,20,8,12), duree = c(2,2,2.5,3,6))

# copie du contenu de la colonne duree dans une nouvelle colonne total_heures 

> df1 %>%
+     dplyr::mutate(total_heures = str_extract(duree, "[^_]+$"))
```

```r
# changer l'ordre des colonnes (colonne présents avant colonne inscrits)
df2 <- df1 %>% relocate(presents, .before = inscrits)
```

```r
# séparer une cellule en plusieurs avec la fonction separate
# sépare une cellule formatée comme une date DD/MM/YYYY en trois colonnes : année, mois, jour
> df4 <- separate(df3, col = date, sep = "/", into = c('annee', 'mois', 'jour'), remove = FALSE)

```

```r
# recoder les mois (01 = janvier, 02 = février)
> df4 <-df4 %>% mutate(mois = recode(mois, `01` = 'janvier', `02` = 'février', `03` = 'mars', `04` = 'avril', `05` = 'mai', `06` = 'juin', `07` = 'juillet', `08` = 'août', `09` = 'septembre', `10` = 'octobre', `11` = 'novembre', `12` = 'décembre'))
```



$\newline$
# bibliographie
$\newline$







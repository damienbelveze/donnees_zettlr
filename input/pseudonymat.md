---
title: pseudonymat
date: 2024-06-01
tags:
  - cryptographie
  - sociologie
  - méthode_scientifique
---
Le pseudonymat consiste à masquer l'[[identité]] d'une personne en lui attribuant un code généré aléatoirement selon un procédé cryptographique. Il diffère de l'anonymat dans la mesure où ce dernier empêche d'attribuer un acte ou un propos à une personne physique. 

# Différence entre anonymat et pseudonymat

Le [[RGPD]]  définit ainsi le pseudonymat : 

>Les données à caractère personnel qui ont fait l’objet d’une pseudonymisation et qui pourraient être attribuées à une personne physique par le recours à des informations supplémentaires devraient être considérées comme des informations concernant une personne physique identifiable.

Dans le cas de [[TousAntiCovid]], l'application utilise le pseudonymat et non l'[[Anonymat]]

M. Dupond est malade = nominatif
La personne ty-57io58 est malade = pseudonyme
456098 personnes qui ont répondu au questionnaire sont malades en ille de France = anonyme

Les commentateurs qui critiquent le prétendu anonymat des plateformes de réseaux sociaux s'en prennent en réalité à des formes de pseudonymat, par ailleurs assez simples en général à identifier pour des services de police.
Les propos outranciers sur le web sont souvent associés au pseudonymat qui désinhiberaient les individus, mais dans la réalité, la majorité des propos répréhensibles sont tenus sur twitter par des comptes qui sont liés à l'[[identité]] véritable de leur propriétaire


# anonymisation située et usage sociologique du pseudonymat

Depuis les années 60 (Michel Crozier) et particulièrement depuis la montée en puissance des récits de vie depuis 1997, les chercheurs en sociologie, considérant la spécificité des parcours des enquêtés ont tendance à utiliser des prénoms fictifs pour distinguer entre eux les enquêtés (exigence de singularité) tout en protégeant leur anonymat (exigence de respect de la [[Vie privée|vie privée]]). Ce travail fait partie des tâches silencieuses de l'écriture en sociologie.

La pseudonymisation des personnes interrogées correspond également à une tentative d'écarter la question d'un phénomène social de tel ou tel individu pour l'amener au niveau d'une caractéristique sociale partagée. Ainsi d'après Félicien Faury qui écrit à partir de la matière d'entretiens avec des électeurs et électrices ponctuelles ou régulières du Rassemblement National (FF ne fait pas ici de différence entre anonymat et pseudonymat) : 

> en effaçant ou en changeant les noms propres, le chercheur entend rompre avec le caractère idiosyncrasique de son enquête et fait l'hypothèse , épaulé en cela par d'autres études existantes, que les tendances qu'il décrit sur le terrain ont leurs équivalents dans d'autres groupes et en d'autres lieux comparables. D'un point de vue plus normatif, l'anonymisation a aussi pour avantage d'orienter le regard (et donc y compris le regard critique) vers des processus généraux et collectifs, sans donner l'impression de "pointer du doigt" un territoire précis ou certaines conduites individuelles

(source: [[@fauryElecteursOrdinairesEnquete2024]], p32)

En note de bas de page (p32), l'auteur indique qu'afin de garantir l'anonymat des personnes interrogées, en plus de modifier les noms, il a du parfois aussi modifier "certaines informations biographiques, sociales et géographiques (tout en conservant leur cohérence sociologique)", geste qui relève plutôt d'une forme d'anonymisation que de simple pseudonymisation.

Les pseudonymes choisis doivent correspondre avec le profil social de la personne enquêtée (prénom français ou étranger, à consonance locale ou pas, représentatif d'une [[classe sociale]] ou d'une classe d'âge, etc.)
C'est ce qu'on appelle l'**anonymisation située** (il s'agit en fait d'une pseudonymisation qui vise à exprimer les spécificités sociales de la personne enquêtée)[[@Coulmontpetitpeuplesociologues2017]]

Pour réaliser cette pseudonymisation située, le sociologue Baptiste Coulmont propose un [outil](http://coulmont.com/bac/index.html) qui croise des données sociologiques : âge et niveau de réussite au bac (entre passage et mention très bien)
On entre un prénom et on obtient des prénoms présentant la même fréquence et le même niveau de réussite au bac.

# pseudonymiser des données avec R 

utiliser le [package digest](https://cran.r-project.org/web/packages/digest/digest.pdf) pour le [[R (logiciel)|logiciel R]]

```r
library(digest)
df$Nom <- character(nrow(df$Nom))
df$Prenom <- character(nrow(df$Prenom))
for(i in 1:nrow(df)) df$Prenom[i] <- digest::digest(df$Prenom[i], algo = "sha256")
# pseudonymisation de deux colonnes Nom et Prénom dans un dataframe
```

---
title: anonymat
subtitle:
author: Damien Belvèze
date: 04-27-2021
link_citations: true
aliases: [anonymat, anonymisation, anonymiser, anonyme, anonymes]
tags: [données_recherche, cryptographie]
---

# anonymat dans la loi

Jurisprudence de la CJUE favorable à l'obligation des Etats de se mettre en conformité avec les règlements Européens sur la préservation de la vie privée : pas de conservation de l'[[IP]] notamment. Cette jurisprudence s'inverse en avril 2024, ce qui permet aux Etats de ne plus être en contradiction avec le Droit Européen tout en continuant de collecter les données personnelles des internautes et notamment leurs IP[[@quadraturedunetSurveillanceHadopiJustice2024]]. 

# anonymat vs pseudonymat

L'anonymat est la propriété d'une information qui ne permet pas d'identifier une personne. A ne pas confondre avec le [[pseudonymat]], généralement utilisé sur les [[réseaux sociaux]] numériques et qui consiste à voiler l'[[identité]] de la personne qui poste l'information. 

## la confusion anonymat / pseudonymat

Pour avancer leur agenda autoritaire, et en faisant porter des risques aux populations exposées qui trouvent dans le pseudonymat un moyen de s'exprimer sans s'exposer aux haters, un certain nombre de politiques alimentent cette confusion entre anonymat et pseudonymat, comme l'écrit ( à propos d'une des nombreuses déclarations d'Emmanuel Macron sur le sujet) Marc Rees dans NextInpact [[@reesEmmanuelMacronAutres2022]] : 

> Une nouvelle fois le président de la République, aujourd’hui candidat à sa réélection, revient à la charge contre « _l’anonymat_ » en ligne, qu’il mélange allègrement avec le pseudonymat, entretenant la confusion sur le sujet.

>Si le premier empêche de remonter à l’origine de l’internaute derrière le clavier, le second se contente d’imposer un voile sur l’identité que peuvent lever les autorités judiciaires, en réclamant les adresses IP au prestataire, puis l'identification de cette adresse auprès des fournisseurs d'accès.


# l'anonymisation de données personnelles

Anonymiser un jeu de données consiste donc non pas à pseudonymiser les enregistrements mais à faire disparaître les informations nominatives tout en essayant de rendre difficiles les opérations de réidentification. 

Plus les [[données personnelles]] contenues dans un fichier sont nombreuses et plus les risques de [[réidentification]] sont importants. 

Une application comme [l'observateur de l'anonymat](https://cpg.doc.ic.ac.uk/observatory/explore) permet de se rendre compte de cela. 

## la réidentification

Le premier cas de réidentification impliquant des [[données de santé]] à une large échelle (un état américain) date de 2001. 
En croisant deux fichiers (un fichier d'assurance "anonymisé") et une liste électorale, [Latanya Sweeney](https://en.wikipedia.org/wiki/Latanya_Sweeney) a permis la réidentification du gouverneur de l'Etat de Massachussets



![anonymisation / pseudonymisation](images/RGPD5.png)

![pseudonymisation](images/RGPD6.png)
[source](https://www.inist.fr/nos-actualites/stockage-des-donnees-recherche/)

# Comment anonymiser des données de recherche

pour la présentation sur [[Zenodo]][,voir ici](https://zenodo.org/record/5717856)

## Présentation d'Arx par Louis-Philippe Sondeck

Présentation de Louis-Philippe Sondeck :
![[202002_sondeck_FDLN.pdf]]


## débats sur l'anonymisation des données de santé (16 janvier 2024)

**individualisation**: impossible d'isoler
**corrélation**: impossible de relier des jeux de données distincts sur un individu ou un groupe
**[[Inférence]]**: impossible de déduire de nouvelles informations sur un même individu

**individualisation**: impossible d'isoler
**corrélation**: impossible de relier des jeux de données distincts sur un individu ou un groupe
**Inférence**: impossible de déduire de nouvelles informations sur un même individu


voir : https://www.health-data-hub.fr/sites/default/files/2022-09/Guide%20d%E2%80%99%C3%A9valuation%20du%20caract%C3%A8re%20anonyme%20d%E2%80%99un%20jeu%20de%20donn%C3%A9es%20v2%20%281%29.pdf

Le modèle d'[[évaluation des risques]] de ré-identification proposé par le HDH est-il approuvé par la CNIL ? Je m'interroge parce qu'il semble entériner une notion relative de la donnée anonyme (ce qui intéressant mais nécessite une gestion spécifique).

Faire une analyse de risque globale standard. Evaluer la probabilité de survenue de l'événement de réidentification et la gravité de cet événement en termes d'impact sur la personne. 

Risque négligeable, modéré, important
négligeable : diffusion en accès libre
modéré : diffusion en accès contrôlé
important (=données pseudonymisées) : les équipes doivent régler le partage au coup par coup

## Présentation d'Amnesia par Martin Amouzou

(notes de la formation doctorale du 22 janvier 2024)

charger Amnesia, R et [[Rstudio]] sur les classes mobiles

inférence : possiblité de déduire de nouvelles informations sur un individu à partir d'une donnée

individualisation : possibilité d'isoler un individu dans un jeu de données

corrélation : possibilité de relier entre eux des ensemble de données distinctes concernant un même individu

notion d'identifiants // quasi-identifiants

pseudonymisation // anonymisation

<!-- pseudonymisation voir Coulmont -->


anonymisation = [[RGPD]] off
<!-- mais déclaration de traitement obligatoire -->

### techniques

#### Randomisation

modifie altère la véracité des données, rend moins précis les attributs, protège de l'inférence - > ajout de bruit et permutation

##### Ajout de bruit

insertion de valeurs factices (loi Gaussienne, loi Uniforme)
bcp plus applicables aux données numériques (ceux qui avaient 27 ans se retrouvent avec 30, 26 ou 29 ans)

<!-- pas de création de nouveaux enregistrements -->

Cette technique à elle seule ne suffit pas à anonymiser les données, notamment pour empêcher l'inférence ou l'individualisation

<!-- compromis précision / anonymat -->

##### permutation

La donnée générale ne change pas 

| id  | ballon |
| :-- | ------ |
| A   | vert   |
| B   | bleu   |
-> 

| id  | ballon |
| :-- | ------ |
| A   | bleu   |
| B   | vert   |
#### généralisation

on généralise les attributs d'une personne 54 ans -> entre 50 et 55 ans

##### k-anonymat

s'assurer qu'au moins k individus ont les mêmes caractéristiques (quand k=2, 2 individus au moins doivent avoir les mêmes attributs) 
Le k-anonymat est une technique qui élimine les caractéristiques uniques

limites : le choix du paramètre k est très déterminant
si k est trop petit, il y a un risque d'inférence
si k est trop grand, la donnée va perdre en granularité
Cette stratégie est inadaptée pour de grands volumes de données, parce que dans ce cas on n'a pas assez de vue synthétique sur les données pour faire des groupes et diminuer les variables unifiantes.

source : https://www.dpo-partage.fr 

##### L-diversité

Chaque groupe d'individus ayant les mêmes caractéristiques possède au moins L valeurs pour un attribut donné

objectif : empêcher les attaques par inférence qui visent à déduire des valeurs pour d'autres attributs à partir de certaines valeurs d'attributs

Chaque groupe d'individus partageant les mêmes caractéristiques, doit avoir au moins deux maladies différentes représentées.

<!-- inverse de la k-anonymisation ? -->

Comment vérifier que l'anonymisation a été efficace, comment faire ? 

individualisation, inférence, corrélation

<!-- comment on s'y prend concrètement ? Quelle évaluation approfondie / mettre en place des scénarios pour montrer qu'on y n'arrive pas -->

Démonstration d'Amnesia avec les jeux de données de démonstration de l'éditeur

séparateur, anonymisation check

hiérarchies : fichiers de généralisation fournies par l'attribut âge et salaire

En fonction de la nature du risque, 

# Comment fonctionne Amnesia

(extrait d'une déclaration de traitement faite pour la DPO de l'Université de Rennes en 2024)

Les chercheurs qui collectent des données personnelles sont incités par leurs financeurs à appliquer les principes de la science ouverte sur les données, et doivent donc les rendre « aussi ouvertes que possible, aussi fermées que nécessaires ». Les données de recherche comportant des donnnées personnelles ne peuvent être partagées que de manière restrictive, sur présentation d’un projet par d’autres professionnels de la recherche dans le cadre des exceptions prévues par le RGPD. Pour un usage plus large et plus ouvert, ces données, quand cela est possible, doivent être anonymisées selon des méthodes standard. Amnésia propose de tester sur le jeu de données qu’on lui soumet plusieurs méthodes pour choisir celle qui permettra de traiter les données pour obtenir le meilleur compromis entre la finesse et l’utilisabilité du résultat final et l’exclusion des risques de réidentification.

Amnesia est un logiciel libre, dont les sources sont disponibles sur Github et qui doit être téléchargé pour être utilisé en local, de telle sorte que les données personnelles ne sont envoyées sur aucun serveur pour être traitées.

Amnesia ne collecte pas de données personnelles mais traite les données qu’on lui soumet (par chargement direct ou via une API) pour les anonymiser en utilisant le k-anonymat, et sa variante le km-anonymat, qui est reconnu comme méthode standard pour l’anonymisation de jeux de données.

Amnesia utilise des algorithmes qui réalisent de manière fiable ces deux méthodes d’anonymisation et produisent des versions secondaires de ces données dans lesquelles les risques de réidentification ont été considérablement réduits. L’algorithme procède par généralisation de certaines variables afin qu’aucun individu dans le jeu de données ne présente une combinaison d’attributs unique. Le résultat du processus conserve un potentiel de réutilisation satisfaisant en dépit de cette nécessaire généralisation.

Ces deux méthodes sont considérées dans la littérature scientifique à ce jour comme étant appropriés à réduire considérablement les risques de réidentification. Toutefois, un rapport du GT29 de l’Union Européenne, montrait que le k-anonymat ne supprimait pas totalement les risques de réidentification par inférence, ce que la méthode dite « L-diversité » qui veille à ce que ne demeure ’aucune variable qui ne soit systématiquement correlée dans le jeu de données avec aucune autre. Or Amnesia ne dispose pas d’algorithme permettant d’utiliser cette méthode contrairement à un autre outil libre téléchargeable Arx.

En nous basant à la fois sur les usages que nous avons constatés (en 2022, la DPO de l’INSA Rennes faisait la promotion d’Amnesia, le logiciel est porté par une organisation scientifique rattachée à l’Union Européenne), et sur une étude indiquant qu’Amnesia est plus user-friendly que Arx et plus facile à appréhender pour des chercheurs (Haghversian, 2022) nous proposons d’utiliser Amnesia dans les formations doctorales et de guider les chercheurs vers cette solution, en attendant de recueillir un avis plus éclairé de la part de chercheurs et chercheuses spécialisées dans les techniques d’anonymisation. Nous n’excluons pas pour autant de remplacer Amnesia par Arx si ces avis vont de ce côté, auquel cas une nouvelle déclaration de traitement sera déposée pour Arx

**Références :**

- Groupe de travail « article 29 » sur la protection des données. (2014). _Avis 05/2014 sur les Techniques d’anonymisation_ (0829/14/FR WP216). (lien [[@groupedetravailarticle29surlaprotectiondesdonneesAvis0520142014]]))

- Haghverdian, P. (2022). _An Empirical Investigation On The Quality Of Open Source Anonymization Tools_. Bleckinge Institute of Technology.(lien [[@haghverdianEmpiricalInvestigationQuality2022]])



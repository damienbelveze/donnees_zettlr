---
title: synthèse des recommandations et ressources pour améliorer le partage, la conservation et la diffusionb du code source
subtitle: mode d'emploi à l'intention des collègues des Ateliers de la Donnée
date: 20250212
bibliography: biblio.bib
csl: ieee.csl
tags:
  - code_source
  - programmation
---
  Le jeu Nomic est un jeu de logique inventé par Peter Suber qui peut se jouer en ligne (ou dans la vraie vie) et fait du changement de règle sa mécanique essentielle.

Durant leur tour, chaque joueur peut proposer un changement de règle et le soumettre au vote des participants :

  

Les règles sont séparées en deux catégories : immuables et muables

Les règles de départ sont immuables

Les règles nouvelles sont muables

Une règle immuable ne peut être modifiée

À chaque tour, un joueur peut proposer, modifier ou supprimer une règle muable. Il peut également rendre une règle muable immuable ou inversement.

Chaque modification proposée est soumise au vote des participants.

  

Puis le joueur lance un dé et en fonction des règles en vigueur gagne ou perd des points. Le jeu s'arrête quand un joueur obtient 100 points (règle qui peut elle-même être revue à la baisse ou à la hausse).

  

Notre question de recherche a sans doute peu ou pas d'intérêt scientifique, mais supposons que nous la formulions de cette manière :

  

"Quelle stratégie adopter, en matière de proposition de règles, pour avoir les meilleures chances de l'emporter en moins d'une heure et en tablant sur le fait que les autres joueurs ont aussi cette contrainte".

  

Supposons que nous voulions développer un logiciel permettant d'établir cette stratégie.

Le jeu se déroulant en ligne sur des forums ouverts, il faudra dans un premier temps télécharger des données, les pseudonymiser, puis les analyser.

Supposons que le programme ait déjà incorporé ces tâches et qu'il reste à déterminer les stratégies gagnantes à partir de ces données.

  

Que faut-il faire pour que notre programme soit réplicable ?

  

# Travaux préliminaires

  

## faire un état de l'art

  

Tout d'abord, il faut s'assurer qu'un tel programme n'existe pas déjà ou n'a pas été tenté.

Il convient donc de faire un état de l'art des publications sur le sujet. Par exemple, on peut voir que quelques études computationnelles sur le jeu Nomic existent déjà.

[Celle-ci](https://ieeexplore.ieee.org/abstract/document/6803266) par exemple utilise un encodage informatique des règles du jeu proche du langage Prolog.

  

Il peut y avoir de cas de figure :

  

1. nous considérons que cette étude invalide notre projet et nous décidons de lancer nos forces sur un autre projet entièrement différent.

2. nous considérons que cette étude ne répond pas à notre question de recherche et nous poursuivons notre projet (en tenant compte de ces travaux d'une manière ou d'une autre car ils n'en demeurent pas moins intéressants à exploiter)

3. nous considérons que cette étude répond déjà en partie à notre question de recherche. Mais nous considérons que le logiciel doit être recodé dans un autre langage que celui utilisé dans l'étude (pour en faciliter l'appropriation par exemple)

4. Nous observons que le code de cette étude n'est pas réplicable et nous décidons de revoir le code source entièrement pour le rendre à nouveau utilisable.

  

Les cas 3 et 4 illustrent que la conception d'un nouveau programme ne répond pas toujours à la nécessité de créer un nouveau logiciel, mais parfois à celle de maintenir l'utilisation d'un logiciel existant, soit en remplaçant les parties du code et les dépendances devenues obsolètes, soit parfois en le recodant dans un autre langage parce que le langage originel est devenu obsolète ou bien est utilisé par une communauté trop restreinte.

  

Pour la suite, nous nous situons dans le cas n°1 ; nous maintenons notre question de recherche et notre volonté de créer un programme pour tenter d'y répondre.

  

L'état de l'art signifie que nous allons aussi nous intéresser aux logiciels qui répondent à des questions proches pour des jeux en ligne pas trop éloignés de Nomic. Nous allons repérer dans ces études des bibliothèques (libraries) qui sont régulièrement exploitées, à divers étapes du traitement des données. Et nous pourrons ainsi intégrer certaines d'entre elles dans notre programme. Par exemple, si nous constatons que beaucoup d'analystes de jeux en ligne utilisent Drools comme gestionnaire de règles métiers pour analyser des stratégies à partir de scénarios de jeux, nous pouvons trouver de l'intérêt à utiliser ce logiciel, voire si notre code source est en Python, une bibliothèque Python qui permette d'utiliser Drools comme [celle-ci](https://github.com/PapiHack/python-drools-sdk)

  

## Etablir une preuve de concept

  

Afin de s'assurer de la viabilité du projet, il peut être intéressant de prendre un échantillon de parties de Nomics en ligne et de coder les règles, puis de créer un code source qui fera un lien entre des règles et des victoires en essayant de mesurer l'impact de ces règles sur les victoires obtenues sur la base du nombre de points rapportés par la règle à celui ou celle qui l'a proposée et du temps de jeu restant après que la règle ait été adoptée.

Cette preuve de concept correspond à l'idée *quick and dirty* et répond à deux questions : ça fonctionne à petite échelle (mettons sur 10 parties), voilà comment ça fonctionne et voilà dans quel sens on devrait aller pour que ça fonctionne à plus grande échelle (mettons sur 1000 parties).

  

## Penser déjà à la valorisation du jeu

  

Nous nous situons dans le cadre de la Science Ouverte. Par conséquent, nous n'avons pas pour but de rendre notre code source inaccessible pour pouvoir en faire une exploitation commerciale. Même si une exploitation commerciale peut en être faite, d'une manière ou d'une autre, le code doit rester FAIR : trouvable, accessible, interopérable et réutilisable.

Il reste néanmoins un grand nombre de choix à opérer pour réaliser cet objectif.

Il est donc important qu'en tant que concepteurs du logiciel, nous nous interrogions sur le cadre général dans lequel s'inscrit notre activité de chercheurs et chercheuses, et à titre accessoire de développeurs et développeuses : qu'elles soien énoncées par notre laboratoire, notre université ou le service de valorisation de celle-ci (SATT) des règles ou des pistes de valorisation (terme à ne pas entendre au strict sens de valorisation commerciale) peuvent déjà exister et il importe d'indentifier en amont ces interlocuteurs et de prendre contact avec eux, notamment pour décider de la licence à appliquer, car un code source sans licence explicite ne sera de toute façon pas réutilisable d'un point de vue légal.

  

# Planification

  

## L'intérêt du PGL

  

Dans une certaine mesure, planifier un logiciel ressemble à planifier une collecte de données. La question du stockage, des accès et de la licence se posent dans les deux cas. Il y a bien sûr la question de la licence, encore que les licences utilisées dans l'un ou l'autre cas soient bien différentes.

  

Mais la comparaison s'arrête là.

En effet, contrairement aux données qui finiront par trouver une forme de stabilité, le logiciel est susceptible d'évoluer sur un temps beaucoup plus long, au delà de l'expérience et de la publication pour lequel il a été conçu. Des aspects de gouvernance du logiciel sur le temps long peuvent entrer en jeu : qui répondra encore aux usagers qui viendront rapporter des bugs lorsque le projet aura été mené à son terme ?

  

De la même manière qu'une équipe de chercheurs et de chercheuses peut anticiper les questions relatives à la collecte, au stockage, au traitement et à la valorisation des données en constituant un Plan de Gestion des Données, ainsi l'équipe qui s'apprête à développer du code à tout intérêt à remplir dès le début du projet un Plan de Gestion de Logiciel.

  

Le PGL est l'outil qui permet de mettre à plat certaines difficultés qui ne tarderont pas à se présenter, particulièrement si l'équipe de recherche implique des chercheurs de différentes unités.

  

En effet, les outils et contextes de développement dont disposent les membres de cette équipe peuvent être très variables :

  

Certain.e.s utilisent Linux comme système d'exploitation, d'autres MacOS ou Windows. Les gestionnaires de paquets de chacune ou chacun peuvent différent et avec eux les versions disponibles sur les ordinateurs des mêmes briques logicielles, ce qui induit à court terme des problèmes de réplicabilité entre chercheurs et chercheuses partenaires du projet.

Il y a aussi la question de la forge à utiliser si plusieurs établissements partenaires disposent de forges propres (en général conçues avec le logiciel gitlab). La forge qui sera choisie devra permettre la publication du code et l'accès avec droits de modification à des personnes parties prenantes du projet mais extérieures à l'établissement qui l'héberge.

  

Dans l'équation entre aussi le choix du langage de programmation. C'est un choix très important et très coûteux en temps et ressources à opérer, car réécrire du code d'un langage à l'autre, nécessite de revoir aussi toutes les dépendances. Il ne doit donc pas se faire à la légère. L'état de l'art que nous avons mentionné plus haut est important pour parvenir à une décision collégiale, notamment dans le cas où tous les collaborateurs et collaboratrices pourraient ne pas avoir le même niveau de maîtrise des différents langages possibles.

  

Python et R étant les deux langages qui restent les plus populaires parmi les communautés scientifiques (par là nous entendons des personnes dont le métier est de faire de la recherche pas des logiciels), nous nous baserons sur eux pour fournir les prochains exemples.

  

# Développement du code

  

## Garder son code simple

  

Si certain.e.s comparent le code à la poésie, il s'agit ici plutôt d'écrire de la prose. Une prose relativement lourde et peu élégante, de telle sorte qu'elle évite les erreurs et surtout qu'elle évite aux personnes qui réutiliseront notre code de faire des erreurs et de mauvaises interprétations en voulant l'adapter à leur projet.

  

Pour être plus précis, plus le code source qui sera produit sera court et plus vous pourrez vous permettre de le rendre complexe par exemple pour éviter qu'il soit trop long et trop côuteux à exécuter d'un point de vue écologique, ou tout simplement parce qu'il est plus satisfaisant pour l'esprit d'écrire un code indemne de redondance, de la même manière que répéter plusieurs fois le même mot dans une phrase lui donne un aspect disgracieux sauf quand cela est fait dans des endroits stratégiques à des fins rhétoriques.

  

Inversement, plus le code à écrire promet d'être long et plus nous devrons déployer des efforts pour le rendre compréhensible et donc simple à lire, non seulement pour d'autres, mais aussi pour nous-mêmes un peu plus tard.

  

En raison de la demande de nouvelles fonctionnalités ou des bugs constatés (ces derniers étant souvent dus à une complexité mal maîtrisée et encore plus souvent résolus non pas par une relecture et réécriture attentive mais l'ajout d'un patch qui rajoute de la complexité), il y a une pente naturelle du code à devenir de plus en plus complexe et c'est une chose à laquelle il faut pouvoir résister.

  

D'où la recommandation de Bert Hubert (@hubertLongTermSoftware2024) :

  

> Write super boring code. Write naive but obvious code. “Premature optimization is the root of all evil”. If it was too simple, you can always make it more complex later. And that moment might never arrive. Don’t write clever code until you simply have to. You will not ever regret writing code that was simple

  

## limiter le nombre de dépendances autant que possible

  

la logique du logiciel libre est de construire du code à partir de briques logicielles conçues par d'autres développeurs et maintenues depuis, parfois tant bien que mal, par quelques individus qui luttent pour y consacrer du temps, sachant qu'ils ou elles ne tirent pas leurs revenus de cette activité dans la grande majorité des cas.

Compte tenu de cet écosystème, il y a donc un problème de stabilité et même de pérennité de certaines dépendances, sans parler du problème de sécurité que cela comporte, car des agents mal intentionnés peuvent très bien offrir leurs services à des gestionnaires de dépendances croulant sur les demandes de nouvelles fonctionnalités ou les rapports de bugs.

Supposons que dans notre code sur Nomic, on doive traiter un faire pivoter un tableau de données. Avant de recourir à un package pour faire cela, peut-être vaut-il mieux se demander s'il n'y a pas une fonction dans le coeur de R ou de Python qui permet de réaliser cela. Si c'est le cas, cela fera toujours une dépendance et donc un aléa en moins à peser sur la pérennité du code.

  

## décrire les variables

  

Même si le code comporte peu de variables, il est toujours préférable de rendre les variables intelligibles.

  

Par exemple, si dans le jeu Nomic, une règle proposée ("que les jets de dés pairs valent seulement la moitié de leur valeur seulement) passent du statut "changeable" à "en vigueur, plutôt que d'écrire :

  

```python

  

def update_rs(di, hpr_rule, vn, pn):

maj = vn > pn / 2

  

if maj and hpr_rule == 'mutable':

hrp_rule = 'enforced'

if hpr_rule == 'enforced' and di % 2 == 0:

di = di // 2

return hpr_rule, di

  

```

Il sera plus pratique pour soi-même et plus lisible et compréhensible d'écrire :

  

```python

  

def update_rule_status(dice, helf_points_rule, votes_number, players_number):

majority = votes_number > players_number / 2

  

if majority and half_points_status == 'mutable':

half_points_rule = 'enforced'

if half_points_rule == 'enforced' and dice % 2 == 0:

dice = dice // 2

return half_points_rule, dice

  

```

D'autant qu'une grande partie des erreurs dans le code tient aux erreurs liées au nom de variable

Dans l'exemple plus haut, il y a une variable mal orthographiée (hrp_rule au lieu de hpr_rule)

  

## Documenter le code

  
  

C'est une antienne bien connue que le code autant que les données de recherche devraient être suffisamment docucmentées, non seulement pour ses collaborateurs/trices, mais aussi pour d'autres équipes ou même soi-même plus tard.

Il convient d'être plus précis et d'indiquer ce qui doit en priorité être documenté et commenté.

  

Ainsi, expliquer quelle fonction et quels arguments traitent tel ou tel jeu de données est très utile, mais il est souvent encore plus utile d'indiquer pourquoi cette fonction et ces arguments et pourquoi ont été choisis et pourquoi pas d'autres. Pour reprendre le terme avancé par Bert Hubert : quelle philosophie, partagée par les développeurs du code source préside à son développement.

  

cela peut se faire dans un apparat du code (un fichier README par exemple), mais dans une certaine mesure, il peut être utile de le faire dans le code lui-même, ligne à ligne, en utilisant la syntaxe prévue par le langage choisi pour commenter (un # dans le cas de Python comme de R ou toute autre forme syntaxique prescrite par ce langage). Le commentaire ne se présente pas comme une paraphrase du code mais comme son explication (@rougierCodeFAIR2025):

  

> The goal [of commenting] is not to rephrase the code, but to explain the reasoning that lead to the code. For example, if the code computes the square root of a number, that number must be positive, and a comment may be required to explain why the number is always positive in this specific context.

  
  

```python

  

def update_rule_status(dice, half_points_rule, votes_number, players_number):

# cette fonction n'est appliquable qu'à la règle de division du résultat pair par deux

majority = votes_number > players_number / 2

# majority est distinct de qualified majority (votes_number > 0,6*players_number)

if majority and half_points_status == 'mutable':

half_points_rule = 'enforced'

# enforced désigne le statut d'une règle changeable qui entre en vigueur selon le vote de la majorité

if rule_status == 'mutable' and dice % 2 == 0:

dice = dice // 2 # la règle de la division des résultats ne vaut que pour les chiffres pairs.

return rule_status, dice

  

```

  

## documenter les API

  

Supposons que notre base de données est en ligne et compte un nombre extrêmement important de règles inventées et votées par les joueurs et joueuses d'un grand nombre de parties.

Pour télécharger ces règles, on pourrait avoir besoin d'API.

Ces API doivent elles être elles aussi documentées au moyen d'exemples.

  

Par exemple :

API pour obtenir toutes les règles qui changent la valeur du dé :

  

**api//nom.de.domaine/nomic/rules?filter=dice_values**

  

API pour obtenir toutes les règles qui sont liées à un lancer de dé de 1 ou de 6 :

  

**api//nom.de.domaine/nomic/rules?filter=dice_values:("one"OR"six")**

  

évidemment, ces api ne mènent à rien, elles ont une valeur purement illustrative.

  

Il est crucial que la documentation de l'API soit mise à jour autant que le code, de telle sorte que l'API du logiciel se comporte exactement comme la documentation l'indique.

  

## Utiliser des environnements virtuels

  voir [[environnement virtuel]]

Le code source que l'on crée sur un ordinateur a un biotope particulier : les programmes déjà téléchargés sur l'ordinateur et certaines paramétrages dus au système d'exploitation.

Changez lui son biotope (en l'exécutant sur l'ordinateur de votre collègue par exemple) et vous pourrez constater que le code aura souvent du mal à fonctionner. Cela va se traduire soit dans la demande de chargement de dépendances supplémentaires soit par un message d'erreur sans alternative.

Pour voyager un code a donc besoin de garder une partie de son biotope avec lui.

La deuxième chose, après son fichier README qui doit accompagner un code source, c'est l'inventaire de ses dépendances.

Cet inventaire peut être réalisé au moyen d'un environnement virtuel.

  

Même si l'on ne songe pas immédiatement à partager son code, développer le code source dans un environnemet virtuel permet d'éviter des conflits entre certaines dépendances. En effet, les dépendances nécessaires pour le fonctionnement du code source seront chargées dans l'environnement et non pas sur le système. Aucun risque donc qu'une dépendance plus ancienne ne vienne interférer.

  

R et Python disposent chacun de *librairies* permettant de créer des environnements virtuels (*venv* dans le cas de Python et *renv* dans ce lui de R)

  

## Tester le code source

  

Le test fait partie intégrante du processus d'intégration continue, nous y reviendrons, mais pour des personnes extérieures au groupe de développeurs qui souhaitent simplement tester le logiciel et comprendre comment il fonctionne, il convient de leur mettre à disposition un jeu de données. Il peut s'agir de données réelles (un échantillon de l'ensemble des données collectées) ou bien de données synthétiques forgées de toutes pièces à des fins pédagogiques et pour ne pas diffuser de données réelles si celles-ci doivent être protégées.
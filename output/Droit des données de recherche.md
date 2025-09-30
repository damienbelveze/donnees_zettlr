---
title: Droit des données de recherche
subtitle: Formation URFIST 7 et 8 mars 2024
id: 20240307_Droit des données de recherche
author: Conférence de Lionel Loubet, notes de Damien Belvèze
date: 2024-03-07
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - propriété_intellectuelle
  - données_recherche
---
Lionel Loubet, juriste, droit des contrats et de la propriété intellectuelle

## 0.1 Objectifs de la formation :

- comprendre les enjeux et identifier les problématiques juridiques  
- Anticiper et prévenir les risques au sein de mon organisation  
- Utiliser le support de formation et la synthèse des ateliers  

[Liste des questions posées par les membres des ateliers des données](https://mensuel.framapad.org/p/formation-droit-des-donnees-de-la-recherche-a6gw?lang=fr)

Définition des données de recherche par l'OCDE (très présente dans les supports de formation)

données d'observation, expérimentales, simulation numérique, données dérivées issues de la [[Fouille de texte]], [[code source]] 

# 1 Data Mining, web scraping, OSINT


## 1.1 Théorie

Atelier webscraping et méta-analyse de données (2h)
en France on a un régime clair sur ce qu'est la [[Fouille de texte]]
directive européenne complète sur le sujet. 
Loi Lemaire (2016) crée un régime d'exception au [[droit d'auteur]] pour le TDM, mais les décrets d'application ne sont jamais parus car le Conseil d'Etat s'est opposé à leur parution.
fouille de texte source d'insécurité au niveau du droit d'auteur. 
L'auteur d'une oeuvre a toujours un droit exclusif de reproduction sur son oeuvre. Une fouille de texte est considérée comme une reproduction de l'oeuvre

![](images/TDM_cadre_légal.png)
"à des seules fins de recherche scientifique", si cette recherche est financée par des fonds privés, ça n'entre pas dans ce cadre. 

fouille de textes dans Europresse sur les Gilets Jaunes dans la presse : fouille de texte illicite ?
Réponse Amélie Barrio : dans l'abonnement payé, nous n'avons pas négocié cet usage, uniquement celui de *fair use* avec consultation et pas constitution de corpus

aspirer des données provenant de réseaux sociaux de façon manuelle ou avec un script. Cet usage est à distinguer du data mining parce que ce n'est pas du 
contenu couvert par le droit d'auteur

[[scraper|scraping]] de réseaux sociaux : zone grise - insécurité juridique, mais ce n'est pas illicite en soi
<!-- Après, des firmes comme X défendent leur "propriété" (nos messages) contre le scraping de firme comme OpenAI -->

synthèse des usages: 
![](images/scraping_aspect_legal.png)

Il y a eu un [contentieux avec LinkedIn](https://www.village-justice.com/articles/prospection-commerciale-scraping-donnees-sur-linkedin-est-legal,40218.html)
Par ailleurs LinkedIn pose un problème en matière de données personnelles.
L'extraction réalisée est-elle sur une partie quantitativement substantielle. 
consulter les CGU du réseau (la pratique -parfois définie un peu autrement- sera explicitement interdite dans certains cas)

jurisprudence : 

![](images/jurisprudence_numerique.png)

ClearView AI scraping de photos (données personnelles) pour entraîner une [[grands modèles de langage|intelligence artificielle]] génératrice d'images.
Aviation BV : société de comparateur de prix de vols (nécessite du scraping), compagnie condamnée au prétexte que ce scraping n'était interdit dans les CGU des compagnies de vol (dont RyanAir qui avait porté plainte). Toutes ces règles sont les mêmes en France et dans les pays de l'UE. 

Aux USA les choses sont un peu différentes (cf. LinkedIn vs HiQ labs) le juge a donné raison au scraper au motif que les infos sur LinkedIn étaient publiquement accessibles (# hacking) et que les usagers les remplissaient volontairement. 

![](images/scraping_bonnes_pratiques.png)

Scraping de HAL : les CGU le permettent mais les articles sont placés sous des licences différentes (CC:by, droit d'auteur)
<!-- voir Christophe Bénavent qui fait du scraping sur TEL -->
Utiliser les API prévues à cet effet. Les API servent aux fournisseurs à éviter d'être scrapés et à définir le périmètre des données qui sont téléchargeables.

API : RDG, OpenAlex, HAL, Istex

Pas d'exemple de projet de recherche dont les chercheurs soient poursuivis pour avoir fait du TDM et du web scraping. Le déclencheur des poursuites, c'est un enjeu commercial pour des sociétés dont les marchés sont les mêmes (=utilisation parasite du scraping)

### 1.1.1 OSINT

C'est un peu comme du web scraping mais avec une cible. 
aucun cabinet ne peut garantir de la légalité ou de l'illégalité de la chose dans l'absolu. Il faut voir au cas par cas. 
Question ARDoISE Sur l'OSINT, je me pose la question suivante : étant donné qu'il s'agit d'une pratique commune aux journalistes et à certains chercheurs, quand on voit que les bonnes pratiques chez les journalistes pour éviter d'être bloqués est de protéger son IP avec un VPN ou le réseau Tor, pourquoi le chercheur ne pourrait pas utiliser lui-même ces outils qui servent à avancer masqués (https://www-cairn-info.passerelle.univ-rennes1.fr/revue-i2d-information-donnees-et-documents-2021-1-page-25.htm)

notion d'accès libre : ce n'est pas parce qu'une donnée est en accès libre qu'on peut la scraper ou la compiler pour faire des bases de données. Le statut de l'accès d'une information ne détermine pas la légalité d'une méthode pour exploiter cette information. 

## 1.2 cas pratique 1

### 1.2.1 Sujet

on est personnel de recherche dans une université, retenu dans une équipe autour d'un projet ANR ; Projet portant sur le déploiement du réseau 4G en France. 
Pour réaliser un work package, il s'agit d'extraire des avis de clients d'opérateurs mobiles depuis Google Maps. il s'agit d'extraire et d'analyser ces données par IA. 
Est-ce qu'on a le droit de récupérer des avis de clients sur Google ; ai-je besoin d'une autorisation particulière,  si oui à qui s'adresser ?    

#### 1.2.1.1 propriété intellectuelle

Il existe une API développée par Google, mais ça ne règle pas entièrement ni le problème des CGU ni le problème des données personnelles. 

Dans les CGU il est précisé que l'API donne accès à des informations qui sont la propriété d'autres acteurs (par exemple de TrustPilot) et qui nécessitent d'obtenir des accords supplémentaires (cf. extrait des CGU : 

"Vos contenus peuvent être protégés par des droits de propriété intellectuelle et des droits immatériels. Par exemple, vous disposez de droits de propriété intellectuelle sur les contenus originaux dont vous êtes l'auteur, comme les avis que vous rédigez.") [https://policies.google.com/terms](https://policies.google.com/terms)

#### 1.2.1.2 question des données personnelles

Par ailleurs, la question des données personnelles intervient dès la collecte. 
Mais comme il s'agit d'avis publics, ça ne nécessite pas le recueil du consentement et par ailleurs la finalité du projet de recherche est statistique et donc les données au final seront anonymisées (cf. article 89 du RGPD)

### 1.2.2 Choix fait par l'équipe de recherche

Le projet porte sur l'analyse technique de la couverture du réseau plutôt que sur la satisfaction du client. L'équipe a identifié la bonne API sur le site Google For Developers, où l'on peut passer un contrat avec Google pour accéder à l'API. De la lecture des CGU, on déduit que les avis présents sur Google Maps sur les opérateurs sont des avis qui sont rattachés à Google et n'appartiennent qu'aux personnes qui ont émi ces avis. 

#### 1.2.2.1 propriété intellectuelle

Certains extraits sont potentiellement soumis aux droits d'auteurs, précisent les CGU. Pour les revues de clients, l'équipe a supposé que ces commentaires n'étaient pas suffisamment originaux pour relever du droit d'auteur.
#### 1.2.2.2 données personnelles

Voir comment l'API est configurée : si les noms des personnes qui ont déposé un avis est une donnée obligatoire, cela pose problème. De fait, il a été possible d'extraire les données sans les métadonnées identifiantes (= principe de minimisation de la collecte propre au RGPD)

Par contre il restait à enlever les données quasi-identifiantes ou possiblement identifiantes dans le corps des avis eux-même. Le caractère identifiant de ces mentions dans les avis (par exemple nom de rue) ont été mesurés sur un axe problématique de 1 à 10 (10 = très problématique ; doit être effacé). Le travail de suppression de ces données a été réalisé pour partie par des humaines pour partie par une IA. 

Le traitement des données collectées a fait l'objet d'un formulaire de traitement envoyé au DPO de l'établissement. Le DPO a répondu que finalement ce [[traitement de données]] n'était pas assimilable à un traitement de données personnelles et n'a pas été inscrit au registre des traitements de l'établissement. 

#### 1.2.2.3 Avis des autres membres du groupe

Ne pas oublier qu'à des fins de recherche (art. 89, RGPD), certaines données peuvent être collectées, ce qui ne serait pas possible dans d'autres cas. S'il demeure trop d'aléas juridiques par rapport au caractère identifiant des données collectées, on peut aussi faire une demande d'autorisation à la CNIL. 

Si on n'a pas d'API, il est très difficile de faire du web scraping sur des systèmes comme Google.

### 1.2.3 cas pratique 2

Etude de cohorte (1955-1965) analyse du parcours d'une vie de génération ; identifier les grandes tendances d'évolution socio-professionnelles
données démographiques + retracer des parcours de vie type (personae)
Pour faire ce travail, on a une équipe de recherche qui a accès à trois sources de données.  

1. on a des données publiques produites par l'INSEE (recensement, mortalité)  
2. données contenues dans des archives publiques qui ne sont pas en libre-accès   
3. données issues du public cible contenues sur le site web Copains d'Avant  

Quelles précautions à prendre pour gérer ces données. 

Pour les données publiques de l'INSEE https://api.insee.fr/catalogue/
Archives Publiques : sur le site des Archives de France, aucune autorisation du service n'est présentée comme nécessaire pour des utilisateurs qui souhaiteraient réutiliser des archives publiques (mais les archives en question ne sont-elles pas protégées par un délai de communication (50 ans) qui nécessite une autorisation ? En théorie, non, mais en pratique, il faut passer soit par le conservateur, soit par une commission - penser à s'adresser à l'archiviste de l'établissement)
Accès aux matricules militaires : on ne peut pas y accéder si on ne prouve pas son lien de parenté. Faire une demande en  tant que chercheur ou chercheuse au conservateur des Archives Départementales. Ce sont les AD qui autorisent ces accès.
3e avis : A priori non librement communicable. Pour certaines finalités de recherche, les données d'état civil conservées pour une durée inférieure à 75 ans, une autorisation spécifique est nécessaire.  Protection délai de communicabilité, si accès avant faire  une demande de dérogation et de condition de réutilisation. dérogation d'accès : [https://francearchives.gouv.fr/article/26287581](https://francearchives.gouv.fr/article/26287581)  [https://siafdroit.hypotheses.org/659](https://siafdroit.hypotheses.org/659)

Sur les délais de communicabilité : [https://francearchives.gouv.fr/fr/article/26287562](https://francearchives.gouv.fr/fr/article/26287562)

Copains d'Avant : assez fermé. Ces données vont être très compliquées à exploiter (données très identifiantes), les CGU ne permettent pas d'aspirer ces données. On ne peut pas inclure Copains d'Avant dans les sources de cette recherche, il va falloir se tourner vers d'autres sources de données.
Voir Progedo (condition d'accès https://www.progedo.fr/donnees/donnees-confidentielles/ )

# 2 Droit des données personnelles

Atelier Collecte, traitement et diffusion de données personnelles dans un projet de recherche

question INED : la CNIL demande des durées de conservation mais l'INED les diffuse autant de temps que nécessaire pour les chercheurs. Contradiction latente entre un intérêt scientifique et un intérêt réglementaire. 
LL : absence d'indicateurs dans le RGPD pour fixer des durées de conservation.

Conservation des messages envoyés sur les réseaux sociaux par des personnes politiques : l'anonymisation est impossible sans perte de sens des données. 

## 2.1 définition et commentaire des notions juridiques

[[RGPD]] voté en 2016 entré en vigueur en mai 2018. Un règlement, pas une directive. En cas de doute on peut directement accéder au RGPD. 
Le RGPD se combine avec la Loi Informatique et Libertés issue de celle qui a créé la [[CNIL]] (1974 : [« Safari ou la chasse aux Français »](https://www.cnil.fr/sites/cnil/files/atoms/files/le_monde_0.pdf), Le Monde, 1974)

**Données à caractère personnel**
([[données personnelles]]) : données permettant d'identifier directement ou indirectement une personne (voir définition sur le site de la CNIL). Une adresse postale et une adresse IP sont considérées comme des données personnelles.


**traitement des données** : définition très extensive désigne toute manipulation de données personnelles

le **responsable du traitement** est la personne qui réalise ce traitement et lui assigne une finalité.

**sous-traitant** : organisme qui délègue à un autre acteur le soin de traiter les données personnelles qu'il a collectées. Le sous-traitant est un simple exécutant au service du responsable de traitement. 

**données sensibles** des données personnelles qui portent sur les opinions, appartenances syndicales, religieuses, orientation sexuelle, origine raciale, ethnique, données génétiques, état de santé, [[données biométriques]].
## 2.2 Droits et obligations issus du RGPD 

![](images/droits_RGPD.png)

Droit à l'information : 

![](images/droit_information_RGPD.png)
Quand on a donné son consentement on doit quand même être informé de son droit. 

analyse des flux de patients dans les salles d'attente des blocs opératoires. 
Certaines personnes se sont opposées à ce traitement en disant qu'il pouvait préjudiciable à leur prise en charge

![](images/RGPD_droit_acces.png)
droit à l'oubli et à l'effacement limité par le droit de l'information du public (cf. liberté de la presse)
Demandes de déréférencement sur les moteurs de recherche. Arrêt Google Spain : une personne a le droit de se faire déréférencer sur une partie des articles qui le concernent et qui sont indexés par Google. 
Droit à la portabilité
Principe du consentement préalable : il faut recueillir ce consentement sur un document séparé ; le responsable du traitement doit être transparent sur les finalités du traitement. Limite d'âge au consentement individuel = 15 ans, en dessous on doit demander le consentement aux responsables légaux. Il revient au responsable du traitement de prouver qu'il a correctement recueilli le consentement des personnes.

Question d'Elodie Papin: possibilité de créer un compte pour une personne sans son consentement (cf. inscription des chercheurs sur la plateforme de [[cahiers numériques|carnets de laboratoire]] ?
Réponse : pas possible si c'est à l'échelle de l'établissement. Pousser à la création d'un compte au moment de la première connexion (par un popup)

Quelles obligations pour le responsable du traitement

principe de minimisation de la collecte. 

![](images/traitement_licite.png)

La mission d'intérêt public ne se justifie pas par le statut du traitant (chercheur dans le public), mais pas référence à une mission d'intérêt public porté par l'établissement. Si un chercheur d'une université publique mène des recherches pour une fondation, il doit justifier l'intérêt public de sa démarche

intérêt légitime : si la recherche est dans la lignée d'une suite de travaux sur plusieurs années par exemple. 

Le traitement des données sensibles est par défaut interdit mais si la personne a donné son consentement exprès et spécifique ou bien si la personne a donné accès à ses données sensibles par ailleurs, et si votre recherche est justifiée par un intérêt légitime

![](images/donnees_sensibles_traitement.png)

bases légales : 
- consentement OU 
- intérêt légitime
- mission d'intérêt public

Le consentement n'est pas donc requis à chaque fois. Mais on recommande de le faire chaque fois que c'est possible (principe de transparence). 

L'intérêt légitime se distingue de l'intérêt public motivé dans la mesure où il n'est pas défini dans le RGPD mais doit être argumenté par le responsable de traitement. C'est le recours des opérateurs de recherche privée qui ne peuvent pas compter sur la mission d'intérêt public. [Exemple donné par la CNIL](https://www.cnil.fr/fr/recherche-scientifique-hors-sante-quelle-base-legale-pour-un-traitement-de-recherche) : 
> une recherche utilisant des données personnelles et menée par le département R&D d’une société privée qui vise à étudier les algorithmes de calcul de risques financiers pourrait être fondée sur base légale de l’intérêt légitime.

Consentement "éclairé". Ce caractère "éclairé" peut être remis en question dans le cadre du droit d'opposition. 
Différents types de consentement : 
Ne pas confondre le consentement de participation à la recherche (consentement éthique, ce n'est pas RGPD), le consentement comme base légale RGPD et le consentement pour le traitement de données sensibles.

Pour le consentement comme base légale RGPD, les personnes pouvant retirer leur consentement, cela implique des potentielles difficultés pour gérer le retrait du consentement, je recommande d'utiliser plutôt la mission d'intérêt public dans tous les cas où c'est possible pour éviter de gérer les consentements. Le principe de transparence sera tout de même parfaitement respecté grâce à des mentions d'information qui seront diffusées aux participants à la recherche.

## 2.3 anonymisation et pseudonymisation : quelles méthodes ? quels impacts ? 

voir [[pseudonymat]] et [[Anonymat]]

délai de réponse du Comité du Secret Statistique :
Pour l'accès aux fichiers pseudonymisés (diffusés par l'Ined et l'ADISP), environ 15 jours, pour l'accès aux données détaillées via CASD, environ 1 à 2 mois

risque de réidentification des données pseudonymisées
Avec l'anonymisation on est sur un processus irréversible (pas de réidentification possible), par conséquent les données après avoir été anonymisées ne sont plus sujettes au RGPD (perte sèche de données, mais après on peut les partager comme on veut)

demander au financeur la prise en charge financière de cette charge que représente l'anonymisation (ressource informatique, compétences, temps de travail) (et indiquer cette demande dans le [[Plan de gestion des données|Plan de gestion de données]])

Possibilité de déposer des données pseudonymisées dans RDG avec un formulaire pour justifier de l'accès. Un participant indique que c'est exclu par les CGU de Recherche Data Gouv. 

[Accéder aux données couvertes par le secret statistique](https://callisto-formation.fr/course/view.php?id=223)

## 2.4 définir une durée de conservation adaptée

## 2.5 collecte et traitement de données sensibles

![](images/donnees_sante_aipd.png)

Attention au Cloud : Cloud Act (2018). L'Etat américain se donne le droit de fouiller dans ces données. 
Débat sur le Health Data Hub opéré par Microsoft

## 2.6 Cas pratique 1

projet d'enquête sur le rapport des collégiens et des lycéens avec les activités sportives
l'équipe de recherche mène des entretiens de 45 minutes avec chaque élève et ces entretiens seront analysés. 
En plus de ça, la tutelle souhaite recourir à un sous-traitant pour mener une partie des entretiens.
Est-ce que le RGPD s'applique bien ?
Quelles autorisations je dois solliciter ? auprès de qui ?
Comment je dois formaliser mon contrat avec le sous-traitant sur le sujet des données personnelles

oui ça entre dans le cadre du RGPD (les collégiens parlent de leurs pratiques personnelles). Il s'agit de mineurs, donc les autorisations parentales sont requises pour les collégiens (pour les lycéens s'ils ont plus de 15 ans ils donnent eux-mêmes l'autorisation : https://www.cnil.fr/fr/recommandation-4-rechercher-le-consentement-dun-parent-pour-les-mineurs-de-moins-de-15-ans)
Un entretien oral transcrit est également soumis au droit d'auteur. Il faut aussi recueillir une autorisation au titre du droit d'auteur que les parents devront donner pour les collégiens jusqu'à 15 ans. 
Pour le formalisme, il faut faire signer deux papiers (le RGPD doit faire l'objet d'un consentement spécifique)
Ces consentements doivent être conservés (en même temps que les tables de correspondance autant de temps que les données de recherche elles-mêmes)
C'est une bonne pratique de transmettre les questions par avance aux parents d'élève.
Contrat avec le prestataire : on doit s'assurer qu'il ne va pas faire n'importe quoi sachant qu'on sera responsable du traitement réalisé par le sous-traitant. On doit obtenir un accord positif du sous-traitant sur les clauses du contrat : durée de conservation sur les serveurs du sous-traitant, traitement des données selon les instructions du responsable du traitement, information du resp traitement en cas de brêche, vol de données sur les serveurs du sous-traitant. 
Modèles de contrats de sous-traitance : https://www.cnil.fr/fr/sous-traitance-exemple-de-clauses

Que se passerait-il si l'enquête portait sur le rapport des enfants à leurs pratiques religieuses. 
Il s'agit de données sensibles et il faut justifier que la recherche est d'intérêt public. Il va falloir préparer davantage le terrain. Une analyse d'impact doit être réalisée (voir modèles d'analyse d'impact)

vu sur le site de la CNIL : 

"Le responsable de traitement devra démontrer:

- la condition de « nécessité » pour la mission d’intérêt public ;
- la présence de motifs d’intérêt public importants ;
- que l’intérêt public est défini par le droit national ou le droit européen.

Pour mobiliser cette exception, la loi Informatique et Libertés exige un texte, par exemple un décret en Conseil d’État après [avis de la CNIL](https://www.cnil.fr/les-avis-de-la-cnil "Les avis de la CNIL - Nouvelle fenêtre")."

4. L’utilisation des données est nécessaire à la recherche publique

Certaines utilisations de données peuvent être nécessaires à la **recherche publique,** sous réserve que des motifs d'intérêt public important les rendent nécessaires (nécessite un avis de la CNIL). Pour être considérée comme une recherche publique, celle-ci doit respecter certains critères [précisés dans le code de la recherche](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027747800/ "Article 112 - Code de la recherche - Chapitre 2 : Objectifs et moyens institutionnels de la recherche publique - Légifrance - Nouvelle fenêtre").

## 2.7 Cas pratique 2

Un chercheur souhaite savoir comment stocker un certain volume de données provenant d'une clinique, il se trouve que ces données sont des données de flux de patients (nom, prénom, date de passage dans la clinique, soin que le patient va recevoir). Ces données sont échangées par mail. L'objectif de ce projet est d'améliorer les flux de patients dans cette clinique. 

Première réaction du DPO de l'organisme de recherche quand il a connu le cas : contraindre les membres du projet à faire une pause dans le projet pour discuter avec les responsables de cette clinique, au moins sur le volet des données personnelles, les autres données peuvent continuer à être traitées. contact avec le DPO de la Clinique qui n'était pas non plus au courant. Organisation d'une session d'information avec les membres du projet pour poser le cadre et formaliser les relations entre chercheurs et DPO des deux côtés. Définition de la Clinique comme responsable du traitement. Définition du chercheur comme sous-traitant. Accord sur des clauses de sous-traitance (production d'un contrat de sous-traitance)
En outre, il a été précisé que ces données ne pourraient plus être déposées sur les serveurs sans sécurité supplémentaire. Travail avec les RSSI des deux établissements pour la création d'une DMZ (bulle sécurisée) sur les serveurs de la Clinique, bulle à laquelle les chercheurs ont reçu des accès uniques.
Comme il s'agissait de données sensibles et qu'aucune analyse d'impact n'a été faite une analyse d'impact a été faite et envoyée à la CNIL (qui n'a pas envoyé de message suite au fait que cette analyse d'impact avait été envoyée a posteriori)
Question de la validité d'un consentement a posteriori
Ce n'est pas recommandé de demander un consentement pour une collecte qui a déjà été faite ; en terme d'éthique de la recherche, ça pose plus de problèmes que ça n'en résout. 

Données de santé : quel régime s'applique sur des données recueillies par des chercheurs européens auprès de personnes non-européennes 

Isabelle Zablit ( Directrice de projets Europe et international à la délégation ministérielle au Numérique en Santé) : "Tout le monde n'a pas encore intériorisé que c'est la réglementation de l'Etat du responsable du traitement qui s'applique (en l'occurrence le RGPD pour les chercheurs européens) et pas la réglementation du pays d'où proviennent ces données (réglementation US très libérale qui ne rend pas obligatoire le consentement du patient). CNIL et RGDP s'appliquent aussi aux recherches réalisées ailleurs" ( Colloque Les données personnelles pour la recherche en Santé publique : usage, protection, partage (16 janvier 2024) (voir [[données de santé]])



# 3 Droit des bases de données

2 régimes de propriété (propriété d'une voiture différente de la propriété intellectuelle d'une base de donnée). 
<!-- Difficile d'expliquer aux producteurs de données qu'ils n'en sont pas propriétaires au titre de la propriété intellectuelle, mais en même temps on leur dit que les employeurs sont propriétaires (dont il y aurait une propriété intellectuelle sur les données finalement ?) -->
Différents niveaux de structuration de la base de données (base de données relationnelle = très structurée / base NOSQL = peu structurée)




# 4 données de la recherche dans les publications scientifiques

Les données sont-elles couvertes par le droit d'auteur. Oui si elles sont originales (schémas, représentations graphiques, photos, extraits vidéos)
Quand on partage des données de ce type-là il faut vérifier qu'on est conforme au droit d'auteur. 
vérifier que la licence permet la réutilisation a priori (par exemples les images de Wikipédia sont réutilisables en CC by SA)
[[domaine public]] : expiration des droits 70 ans après la mort de l'auteur de la photo (sans compter les années de guerre).

En Sciences Exactes, il est très fréquent de devoir signer un [[accord de confidentialité]] avec les entreprises chez qui on va faire de la recherche. Cet accord limite fortement la publication des données (lien avec le Secret des Affaires).

Peut-on reproduire les figures qu'on a publiées dans une autre publication ? Dans bien des cas, on a laissé les droits de reproduction à l'éditeur, donc pas si simple. Intérêt de la [[Retention Rights Strategy|stratégie de rétention des droits]] pour l'ouverture des résultats de la recherche. 

Ne pas envoyer les données aux éditeurs sans s'assurer qu'on pourra continuer d'en faire ce qu'on souhaite.
Il est plus sûr de déposer les données sous embargo dans un entrepôt avec une certaine licence avant d'en envoyer une copie à l'éditeur. 
![](images/transfert_donnees_editeurs.png)

# 5 L'ouverture des données de la recherche dans le cadre de la science ouverte

## 5.1 incitations, injonctions à l'ouverture

distinguer ce qui relève des régimes légaux et ce qui se rapporte à la politique du MESR

atelier Open Data et Science Ouverte

incitation ou injonction à publier des données ? Il y a énormément de littérature sur le sujet e plusieurs logiques qui se superposent et on peut assez facilement s'y perdre ; confusion entre démarche éthique de la science et base légale.

Les trois sources de l'injonction à la publication des données :

Le **Code de la recherche** comporte des injonctions sur les données de recherche

La **Loi pour une République Numérique** 2016 qui introduit l'article L.133 du Code de la Recherche : les administrations publiques doivent publier leurs données (au delà des seuls organismes de recherche). Même si un auteur a cédé ses droits, dans un délai variable selon sa discipline, il peut rendre accessible une version (AAM) open access de son article (ne s'applique pas aux actes de colloques ou ouvrages).

![](images/article_code_recherche.png)
voilà pour les publications, et pour les données ? 

![](images/donneees_ouverture.png)



Les **obligations issues des financeurs** de la recherche (ANR et commission européenne)

La Science Ouverte et le PNSO relèvent de l'incitation. but : permettre la [[reproductibilité]] de la recherche. Une démarche en faveur du citoyen contribuable (on paie des impôts et on récupère des données et des publications en open access). Sciences participatives. 
Partage des données en opendata (par exemple données d'une régie publique des transports) : déploiement de services autour de ces données. Données ouvertes = levier de croissance.

régime général de l'[[open data]] : les établissements de recherche n'y dérogent pas. On ne peut pas faire payer pour accéder aux données. Quelques exceptions : l'IGN qui a une activité commerciale (inscrite dans le CRPA par la loi Velter. Idem pour Météo France. 
Données de Météo France finalement mises à disposition du public https://twitter.com/StanGuerini/status/1722558587250098657

Obligations issues des financeurs

ANR (depuis 2019)
![](images/ANR_PGD.png)
Standards [[FAIR]]

Actuellement pas de contrôle de l'ANR sur les PGD fournis, mais ça va sans doute se mettre en place prochainement. Le datapaper peut être considéré comme un PGD. Le PGD ressort de la catégorie d'un rapport quand le datapaper compte comme publication

[décret sur l'intégrité scientifique de 2021 fait référence aux PGD](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044411360) mais depuis que ce décret a été introduit [dans le Code de la recherche en 2024](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000044411360/2024-03-04/), la référence aux PGD n'y apparaît plus. 
Si la loi ne va pas plus loin et que le décret est toujours applicable, alors on doit en tenir compte. 

La politique du MESR et les PNSO successifs vont dans le même sens que la législation (heureusement)

## 5.2 Formats et standards de partage

standards appliqués en conformité avec les droits de tiers (vérifier qu'on ne contrevient pas à des droits de tiers quand on partage les données)

Licences pour les données : 
D.323-2-1 On prescrit d'utiliser soit la licence Etalab, soit la licence ODBL

On est plus libre pour les codes sources : GNU/GPL, CeCILL, Eclipse Public Licence, European Union Public Licence

<!-- CC0 s'applique dans toutes les législations en s'harmonisant avec elles : si la législation nationale empêche d'abandonner les droits moraux, ceux-ci restent conservés, tous les autres droits sont laissés (https://direct.mit.edu/dint/article/2/1-2/199/10013/Licensing-FAIR-Data-for-Reuse ) CC0 est vraiment un standard pour le partage des données en dehors de l'Europe -->

### 5.2.1 Cas pratique 

divulgation de matière polluante dans l'atmosphère. : analyse des fumeroles sortant des cheminées d'une usine. 
projet ANR , deuxième phase de rédaction du PGD, (1er version light), présence d'un consortium avec une clause de confidentialité stricte de 5 ans conséquence conflit entre politique ANR et le consortium rédigé.
Qu'est-ce qui prime ? est-ce que c'est l'accord de consortium signé ? est-ce que c'est l'engagement vis à vis de l'ANR ? 

L'accord de consortium prime sur les principes de l'ANR (dont l'un est aussi fermé que nécessaire) mais de fait, c'est un échec collectif sauf pour l'industriel. ça fait mal au coeur d'envoyer un PGD qui indique qu'aucune donnée ne sera diffusable pendant 5 ans. Beaucoup d'argent public qui sera peut-être utile à l'industriel, mais pas du tout au public. 
L'employeur avait surtout la préoccupation de répondre à un appel à projet et à trouver un financement pour avoir des recettes que de faire progresser la connaissance du public sur la qualité de l'air. Les publications ont pu être faites parce qu'elles ne portaient pas sur les données mais sur la manière dont elles avaient été collectées et traitées, donc les chercheurs et chercheuses y ont quand même un peu trouvé leur compte. 

Quand les appels à projet ne sont pas retenus, on a une explication de l'ANR sur la raison du refus, mais on n'a pas de cas de refus de l'ANR de continuer à subventionner la recherche suite à l'envoi d'un PGD.

Pour autant l'[[ANR]] commence à relire les PGD et bloque la tranche suivante des financements tant que la version à 6 mois n'a pas été validée

Un chercheur en SHS a publié ses résultats de recherche (articles) sur plusieurs supports qui lui sont propres et 6 mois après la publication l'éditeur chez qui il a publié souhaitent qu'il retire ces textes. 
Préciser : l'article a t-il été financé a minima sur 50% par des fonds publics ? Est-ce que le fait que le chercheur est payé par le contribuable (sans parler d'un projet de recherche financé par une agence publique) suffit à indiquer que l'étude a été financé par le public ? (cas particulier des doctorants en thèse CIFRE)
Il faudrait vérifier que le chercheur a bien diffusé dans un format ouvert (avec une licence [[creative commons]]) ?


<!-- diffusion ouverte et creative commons ne vont pas nécessairement de pair dans le cadre de HAL. Quand on dépose un papier on peut choisir une licence CC:by ou ne pas choisir de licence ouverte (le petit nombre de juristes qui déposent effectivement leur texte intégral dans HAL n'utilisent quasiment jamais de CC:by à ma connaissance). -->
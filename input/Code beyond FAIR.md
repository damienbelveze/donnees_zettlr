---
title: Code beyond FAIR
subtitle: 
id: 20241217_Code beyond FAIR
author: Nicolas Rougier
date: 2024-12-17
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - journée_ARDoISE
  - code_source
---
Code Share beyond FAIR
Nicolas Rougier, directeur de recherche INRIA, co-fondateur de [RE-Science](http://rescience.org/x)

the importance of transparency and reproducibility (Haibe-Kains, et al. 2020)

Réticences de Nature à rendre le code accessible. 

2024 publication d'Alphafold3 dans Nature
Demande envoyée à Nature pour avoir le code source. 
On est en 2024, tout ce qui est open code c'est connu depuis pas mal d'année, mais on est encore dans la difficulté de partager du code qui a fait l'objet d'une publication chez certains éditeurs. 

The [[Excel]] error that changed history (austérité en Europe, tout ça repose sur une erreur créée par Excel)
Il n'y avait pas de code mais il y avait une feuille excel avec un formatage valeur > date (et il y avait aussi du [[cherry-picking]])

Randall Leveque : raisons pour lesquelles les gens ne voudraient pas partager leur code si c'était des maths [[@levequeTopTenReasons]]

1. Ma preuve est trop moche, je ne veux pas la rendre publique
2. Je n'ai pas travaillé tous les détails
3. ce n'est pas vraiment moi qui l'ai fait, c'est mon étudiant
4.  je ne veux pas avantager ceux avec qui je suis en compétition
5. je ne partage pas parce que c'est ma propriété intellectuelle et que je veux en faire commerce plus tard
6. ajouter les preuves allongerait inutilement la publication
7. De toute façon, on ne trouvera pas de [[Révision par les pairs|reviewers]] si on les oblige à répliquer le code, c'est déjà assez dur de trouver des bons reviewers, mais là, ce serait quasiment impossible avec cette exigence
8. Ma preuve est liée à des preuves qui n'ont pas encore fait l'objet de publication, donc si je la publie, elle ne suffira pas en elle-même à comprendre ce qui est en jeu ici
9. Dès que les gens auront accès à mes preuves, ils vont vouloir poser davantage de questions sur les manières dont je m'y suis pris pour les obtenir et je n'aurai pas le temps de leur répondre. 

Comment fait-on pour partager le code. 

[[FAIR]] principles créés pour les données, ça ne fonctionne pas si bien que ça pour le logiciel. Reprendre les principes FAIR pour l'adapter au logiciel : FAIR4RS (Barker et al, Nature, 2022)

Il faut que le soft puisse être exécuté et réutilisé. 
Est-ce que je peux faire tourner le soft de quelqu'un d'autre : c'est compliqué 

Collberg University of Arizona : est-ce que je peux faire tourner le code [[@collbergRepeatabilityComputerScience2015]]

[[reproductibilité]] : est-ce qu'on peut faire tourner deux fois un logiciel : 
Prenez un de vos papiers de plus de 10 ans où il y avait du code et essayez de le faire tourner : the ten years reproducibility challenge
- oubli comment le programme fonctionne
- changement de machine
- changement des librairies

[[Roberto di Cosmo]] a retrouvé son code sur Software Heritage et a pu le faire tourner 10 ans après. 

Ne pas laisser le code sur les [[forge logicielle|forges logicielles]]
Google code RIP 2015
Gitorious RIP 2015
Github, RIP 20??
(embrace, extend, extinguish)

code d'Appollo 11 réalisé par Margaret Hamilton conservé sur Software Heritage

défi sur un vieux code 32 ans : FLOSS permet de diffuser du code avec des [[licences libres]]
cf Les 4 règles de [[Richard Stallman]]

Free software = "Libre" : free as free speech, not free as a free beer

critique du FAIR4RS : dans ce papier les auteurs expliquent que le logiciel n'a pas besoin d'être reviewée ni d'être reproductible : Nicolas Rougier s'oppose à cette vision du logiciel qui manifeste une incompréhension sur ce qu'est le code source. 

Problème du [[logiciel libre]] : Fernando Perez : manque de reconnaissance dans l'académie mais aussi dans l'industrie.  
cf. faille [[hearbleed]], cf [[backdoor|XZutils]] 

chercheurs et autres parties prenantes

nécessité de publier le code = minimum requis : même ce minimum n'est pas évident. nécessité de maîtriser les forges et le contrôle de version ([[Git]])

[[licences libres|licence libre]] : c'est bien s'il y en a une et s'il n'y en a pas, ce n'est pas la fin du monde. Pas de licence = vous n'avez aucun droit en tant que réutilisateur. 

Documenter = [[programmation lettrée]], mettre des commentaires dans votre programme. 

Exécution : quelles sont les [[dépendances]] de votre programme. utiliser la conteneurisation avec [[Docker]] ou autre. 

au niveau des parties prenantes : 

institutions = supporter le développement (mettre à disposition des ingénieurs)
[[Numpy]] : librairie fondamentale mais l'ESR paie t-il un ingénieur pour faire fonctionner cette librairie pour [[Python]] ?

archivage avec [[Software Heritage]] et publication avec [[HAL]]
 renforce l'open source, en tant que [[Révision par les pairs|reviewer]], N. Rougier insiste que le [[code source]] soit accessible pour que le papier soit publié ; Nature répond avec une fin de non-recevoir. Les protocoles sont vérifiés, mais trop souvent le code source ne l'est pas. 
En France, il y a pas mal de choses qui se passent sur les forges, projet de forge ESR pour remplacer dans une certaine mesure [[Github]]. 
Prix de la [[Science Ouverte]] du [[logiciel libre]]. 

Importance de conserver le code source pour les années à venir. 

$\newline$
# bibliographie
$\newline$







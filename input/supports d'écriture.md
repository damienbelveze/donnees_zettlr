---
title: supports d'écriture
subtitle:
id: 20230712_supports d'écriture
author: Damien Belvèze
date: 2023-07-12
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---

### [L'écriture de la thèse : règles et outils](https://uat.callisto-formation.fr/course/view.php?id=247# "Edit topic name")


## En Local ou dans le Cloud ?


Premièrement, vous devez choisir un support de référence pour votre écriture.

Ce support sera géré soit en local au moyen d'un logiciel téléchargé sur votre ordinateur (Emacs, Texlive, Word, [[LibreOffice]], [[VS Code]]...) soit il sera hébergé dans le Cloud (Google Doc, Overleaf, Office365)

  L'avantage de ce deuxième choix est que le produit de votre travail sera sauvegardé facilement. Pourtant, la rédaction dans le cloud (c'est-à-dire "sur l'ordinateur de quelqu'un d'autre") met en jeu la propriété de votre travail. Google Drive peut à loisir scanner et réutiliser votre texte pour ses propres fins et se permet également de supprimer sans bruit les textes les moins modifiés.  

Le CNRS recommande d'éviter le recours au Cloud en dehors de ses serveurs.  

## Traitement de texte ou éditeur de texte ?  

Nous sommes très habitués aujourd'hui à traiter notre texte avec des outils comme Word ou LibreOffice qui gèrent des opérations de façon invisible pour l'usager. Ces outils nous proposent un éditeur [[wysiwyg]] (_What you see is what you get_) plutôt séduisant, mais qui trouve vite ses limites en terme d'édition.  

Le recours au texte simple au moyen d'éditeurs de textes constitue une bonne introduction à la rédaction académique. Il vous est par exemple possible de rédiger votre thèse en [[markdown]], d'en proposer des états différents à votre directeur de thèse qui ne travaille qu'avec Word en convertissant votre document maître dans ce format et au final de produire un document PDF correspondant aux exigences académiques (en passant par une phase d'édition du texte avec LaTeX si les besoins en matière d'édition sont très spécifiques).

## Libre ou propriétaire ?

Dans le cadre de la [[Science Ouverte]], les [[logiciels libres|logiciel libre]] sont privilégiés à des fins de transparence et de [[reproductibilité]]. Dans la mesure où leur code ne peut être audité, le résultat obtenu est parfois difficilement compréhensible, ce qui peut susciter des erreurs, notamment dans une feuille de calcul. C'est sans doute un risque moins prégnant pour les traitements de texte.  

Nous recommandons l'usage de formats libres et pour ce qui concerne les traitements de texte, l'usage de LibreOffice, mais si vous êtes férus de Word, n'oubliez pas de partager votre texte en format DOCX pour qu'il soit lisible sur d'autres supports d'écriture que Word. Ce n'est pas aux personnes qui n'utilisent pas Word de se justifier de ne pas disposer de licence, c'est à vous de justifier le fait d'avoir recours à un logiciel propriétaire qui pose des problèmes d'inclusion et de transparence.

## Un fichier ou plusieurs fichiers ?  

Cela dépend de vous. Le PDF reste le format le plus populaire pour publier une thèse. Les données de recherche que vous allez produire  et que vous citerez dans le cours de votre thèse doivent cependant être déposées sur un serveur dédié à ce type de conservation.

Le PDF peut néanmoins être issu d'une [[compilation]] de plusieurs fichiers : un document comportant le texte, un autre comportant les références, un autre encore le style bibliographique choisi par l'auteur pour s'appliquer aux références. Les illustrations de la thèse peuvent se trouver dans un dossier à part, chaque image étant appelée par un lien depuis le document maître.  

[[Kieran Healy]] distingue deux façons de concevoir ce travail de compilation entre des fichiers de données, d'images et de références d'une part et un document maîtrise de l'autre : le modèle "Bureau" et le modèle "Ingénieur".

## Modèle Office vs Modèle Ingénieur

|Modèle Office|Modèle ingénieur|
|---|---|
|le document maître est réalisé sur un traitement de texte (par exemple word)|le document maître est réalisé en texte simple (plain text) sans mise en forme|
|le document maître incorpore le produit (graphiques) des traitements statistiques réalisés sur les données. les images sont également incorporées au document.|le document maître est relié aux données elles-mêmes et les traitements de données se font directement dans le document, les graphiques peuvent être ainsi produites à partir des données au moyen de commandes intégrées au texte (cf. logiciel R). Le document maître appelle les images qui constituent des fichiers qui restent indépendants de lui et peuvent être modifiées à part.|
|il existe un fichier par version du document maître (pas de contrôle de version automatisé)|le versionnage est pris en charge par un outil de contrôle de version (Git)|
|Le document peut être directement partagé avec un utilisateur de traitement de texte|pour être partagé, le document doit être compilé dans un format utilisé par le relecteur.|
|La mise en page se fait directement dans le document maître (fonctions "édition de style" du traitement de texte)|La mise en page se fait par compilation entre le document maître en texte simple et une feuille de style réalisée avec un traitement de texte. On peut ainsi appliquer plusieurs mises en page successives avec plusieurs feuilles de style sans que cela n'affecte en rien le document maître|
|Il n'est pas aisé de convertir le document maître dans un autre format que son format natif, si ce n'est en PDF|toutes les conversions du document maître en texte simple sont possibles et peuvent se faire aisément via des formats comme LaTeX ou HTML qui servent de standards de conversion. A partir de sa thèse on pourrait sans trop de difficulté réaliser un site web par exemple, ce qui est exclu si on part d'un document word.|
inspiré de [[@healyPlainPersonGuide2019]]


  
  

  

Les usages sont nombreux et sont souvent en prise avec les manières de faire dans chaque discipline. Le travail de Kieran Healy montre cependant que de plus en plus de chercheurs en Sciences Sociales ont besoin du modèle "Ingénieur" qui est plutôt pratiqué à l'origine en Sciences Exactes pour des questions de transparence et de reproductibilité et que le modèle Ingénieur gagne du terrain dans les Sciences Humaines et Sociales, nonobstant la résistance de formats propriétaires comme Word de Microsoft.

$\newline$
# bibliographie
$\newline$







---
title: données de santé
subtitle: 
id: 20240116_données de santé
author: Damien Belvèze
date: 2024-01-16
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - Données de santé
  - Health Data
  - health data
tags:
  - donnees_recherche
---
voir [[données en biologie]]
échange de données de santé non anonymisées, voir [[bulles sécurisées]]


[[conférence Clément Debruyère]]

[[SNDS]]
# Colloque Les données personnelles pour la recherche en Santé publique : usage, protection, partage (16 janvier 2024)

## Le futur espace européen des données de santé (Isabelle Zablit - DNS)

Délégation Numérique en Santé : gouvernance du numérique en santé en France (feuille de route 2023-2027)

Cadre propice au développement pour le numérique en santé implique l'espace européen

COVID, passe sanitaire -> mobilité des citoyens en Europe : une Europe de la Santé n'est possible que grâce à un numérique de la santé commun. 
authentifier ce partage de données de santé entre les Etats.

projet de règlement sur les données de santé (projet EHDS) (règlement = obligatoire à l'ensemble des Etats). L'idée est de donner accès aux praticiens d'un pays au dossier des données de santé de visiteurs citoyens d'un autre pays européen sans coût pour ces médecins.
Ce règlement préconise un cadre harmonisé pour l'accès aux données de santé et porte sur les caractéristiques obligatoires pour les logiciels permettant ce partage et cette mise en réseau.
décembre 2023 : négo en trilogue de ce projet de règlement européen, le texte doit entrer dans le droit européen avant les élections européennes de juin.

convergence réglementaire souhaitable avec le [[RGPD]]

entrée en vigueur progressive, les principes éthiques du partage de données font partie du texte.
Le stockage des données de santé doivent être stockées au sein de l'Europe (principe de territorialité). Ces répertoires de données de santé européen doivent pouvoir être utilisables à des parties tierces (hors de l'Europe)

Droit d'opposition. Harmonisation des demandes d'accès : data permit ou data request (accès à des données sensibles ou accès à des données statistiques). Possibilité d'avoir un health data authority par Etat, voire par Länder. Délais de trois mois pour délivrer les autorisations d'accès.
L'infrastructure est déployée pour partager les parcours de soin, 13 pays ont déjà ouvert sur ce réseau leur point d'accès, dont la France : Historique médical, prescriptions. En France, on peut déjà consulter le dossier du patient en français et dans la langue d'origine des ressortissants de 7 pays européens.
déploiement prévu pour l'ensemble de l'UE + Ukraine, Islande et Norvège. Possibilité de récupérer ses médicaments dans des pharmacies à l'étranger quand on ne dispose pas de la prescription (à partir du dossier sur ce réseau)

Q: Quel accompagnement des chercheurs sur l'usage de l'Espace européen des données de santé (parallèle avec ce que la [[CNIL]] fait vis à vis du [[RGPD]] et des chercheurs) ?

R: changement de certains workflows de chercheurs/ Il est prévu de financer des actions d'accompagnement et de formation (délégués au numérique en santé à l'oeuvre sur cette tâche). L'accompagnement se nourrit des questions émises par les chercheurs. C'est une matière qui permet de nourrir cet accompagnement.

Q: Deux autorités sont prévues pour faire marcher cette infrastructure, est-ce que cela va encore retomber sur les épaules de la CNIL
R: décision pas encore prise

Q: comment procéder pour accéder à des données de patients américains, québecois, ou sud-américains (au delà de l'UE). 
R: Tout le monde n'a pas encore intériorisé que c'est la réglementation de l'Etat du responsable du traitement qui s'applique (en l'occurrence le RGPD pour les chercheurs européens) et pas la réglementation du pays d'où proviennent ces données (réglementation US très libérale qui ne rend pas obligatoire le consentement du patient). CNIL et RGDP s'appliquent aussi aux recherches réalisées ailleurs.

Le règlement rend obligatoire le partage des catégories de données (y compris les données du [[Quantified Self]] ?). Mettre à disposition des données n'est pas la même chose que gérer les accès à ces données. Les données peuvent être rendues partageables, mais les modalités d'accès peuvent être restreintes.

le règlement prévoit une seule demande d'accès à un Health Data Authority Body pour obtenir accès à toutes les données identifiées dans tous les entrepôts repérés comme intéressants pour le projet de recherche.

Q: Bases de données de prescription pour la médecine ; qu'en est-il côté médecine vétérinaire ? 
R: ne sait pas, mais probable que ça vienne un jour.

Rôle du concentrateur ou tiers de confiance dans le cadre d'une étude multicentrique. Pour une étude monocentrique, le CNAM suffit pour chaîner la demande avec le SNDS (Système National des Données de Santé)

Q: question sur le rôle des sous-traitants dans le traitement des données : collaborations scientifiques en réalité : comment leur rôle s'inscrit dans ce paysage.
R de la CNIL : les organismes d'appartenance sont conjointement responsables des traitements. Quand l'INSERM transfère des données à un autre partenaire, il devient de ce fait même un sous-traitant d'une étude dont le partenaire devient le responsable de traitement.

Q: si je veux traiter des données d'une enquête réalisée par la statistique publique, est-ce que j'ai besoin de faire des formalités au niveau de la CNIL ? Je pense notamment aux enquêtes qui ne sont pas accessibles via Quetelet, mais celles où il faut passer le CASD (donc qui contiennent parfois des variables plus sensibles) mais qui ne sont pas chainées avec le SNDS. Merci !
R: il faut réaliser cette formalité auprès de la CNIL dès lors que ça touche la santé. 
Si l'entrepôt dispose d'un portail d'information et a prévenu les patients à leur arrivée dans le service, les données médicales peuvent y être entreposées et utilisées sans autre formalité auprès de la [[CNIL]] (dans cas cas on est dans le cadre d'une demande [[MR004]])

Q: Est-ce qu'on sera obligé d'accéder aux demandes des industries du tabac ou de Total à travers ce nouveau règlement
R: cela devra être précisé par la gouvernance qui n'est pas encore mise en place. 
(la personne répond à côté : l'accès de Total ou des industries du tabac à des données de santé n'est pas une question technique mais politique). Même question pour l'usage des données de santé en lien avec l'IA.
En France, le SNDS dispose de référentiels pour répondre à ces questions.

même question sur les données de santé sexuelle et reproductive (avortement) : comment faire pour que les anti-choix n'aient pas accès à ces données ? 
R: ici et contrairement au parcours de soin on n'est pas sur de la donnée identifiante mais de la donnée anonymisée ou pseudonymisée. 

Q:Discussion sur la notion d'intérêt public du traitement. Est-ce que cette notion est toujours discutée ou bien est-ce qu'elle a été évacuée des discussions
R: renvoi au [[RGPD]] : finalités autorisées et finalités interdites


## Accès aux données de la UKbioBank

Données de la UK Biobank
**Emmanuelle Genin** (Inserm)

## Le cadre réglementaire de la protection de données personnelles utilisées à des fins de recherche et de santé publique (Manon De Fallois - CNIL)


Cohorte CONSTANCES

partagée par conception 221 000 volontaires
données dans le SNDS depuis 2007




$\newline$
# bibliographie
$\newline$







---
title: Comment réussir à migrer de X (Twitter) à Mastodon
subtitle: 05-03-2021
id: 20230821_de_Twitter_a_Mastodon
author: Damien Belvèze
date: 2023-08-21
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
---
voir [[Premiers pas avec Mastodon]]


Cette séance est conçue pour des chercheurs et des doctorants. 
Elle doit durer 90 minutes. 
# Brève chronologie de Twitter et de son usage par les chercheurs :

Cette chronologie peut être éditée sous la forme d'une timeline. Les événements ont été choisis pour aider les chercheurs à synthétiser les avantages et les limites de Twitter pour leur activité et faciliter l'activité suivante. On peut à sa guise rajouter des événements qui sont marquent des évolutions importantes de la plateforme ou qui ont des conséquences sur le travail que font les chercheurs sur Twitter. 

**2006** : naissance du réseau social, fondé par Jack Dorsey. Plateforme de micro-blogging ( à l'époque où le blog personnel était une sorte de norme et où Facebook permettait d'écrire des messages longs)  

2009 : rachat de Friendfeed par Facebook. Ce rachat fait migrer de nombreux chercheurs présents sur Friendfeed vers Twitter[[@claveyMastodonRefugePour2023]].

**2010** : Le cas \#ArsenicLife. Twitter devient un lieu d'échange important et de discussions sur la qualité des études. [[@yeoCaseArseniclifeBlogs2017]]  

**2015** : à l'occasion de la COP21, présentation par des chercheurs du Tweetoscope climatique, une représentation visuelle des comptes actifs qui permet de voir la twittosphère climato-sceptique en action.   

**2016** : campagne et victoire de Trump aux élections présidentielles. Usage permanent du réseau social par le candidat puis Président pour motiver les franges extrémistes de son parti.   

**2017**: une équipe de recherche estime l'importance des bots sur le réseau Twitter à une fourchette comprise entre 9 et 15% du total des comptes créés [[@varolOnlineHumanBotInteractions2017]].   

**2017** : mise au point du code de Mastodon par Eugen Rochko et ouverture des premiers comptes en France.  

**2020-2021** : Twitter, vecteur important de la désinformation sur le COVID. L'équipe de Twitter réagit en ajoutant des messages sur la possibilité que les informations relayées soient fausses.   
Pour autant, il serait abusif d'indiquer que Twitter a fait circuler en majorité de la fausse information sur la maladie. Le réseau a permis aussi l'échange d'informations valables à une échelle planétaire, comme l'indique l'universitaire danois Michael Bang Petersen ([[@kupferschmittMuskReshapesTwitter2022]]): 

> I believe it has played important roles in the dissemination of knowledge globally and between scientists and the public during, for example, the pandemic.

**janvier 2021** : Twitter ferme le compte de Donald Trump (révélation du pouvoir de censure de Twitter pour tout le personnel politique). Certains pays comme le Nigéria censurent Twitter sur leur réseau.  

**septembre 2022** : Musk fait une première offre mais renonce temporairement à acheter Twitter à cause selon lui d'une trop grosse proportion de bots sur la plateforme.  

**Octobre 2022** : le processus d'acquisition reprend.   

**Janvier 2023**: Musk achète officiellement Twitter, licencie l'équipe dirigeante et la moitié des salariés.  

Quelques mois plus tard, il rebaptise Twitter X, en référence à sa lettre fétiche, sans proposer d'alternative pour les mots tweets, et retweets. au 21 août 2023, le [[nom de domaine]] de X est toujours twitter.com  

**août 2023** une enquête parue dans Nature fait état de 9200 réponses de chercheurs et chercheuses sur leur pratique de Twitter après la dégradation de l'application par son nouveau propriétaire : 7% d'entre eux déclarent avoir cessé d'utiliser Twitter, 46% indiquent avoir changé de plateforme pour envoyer des messages. Ils/elles ont choisi Mastodon, Bluesky ou Tiktok [[@vidalvaleroThousandsScientistsAre2023]].  

**août 2023** : les publicités à caractère politique qui avaient été bannies de Twitter par l'équipe de Jack Dorsey sont réintroduites par E. Musk dans X [[@TwitterAutoriseNouveau2023]]

**Septembre 2023** : Les conditions d'utilisation de X(Twitter) sont mises à jour pour permettre une plus grande collecte de données personnelles pour nourrir des IA, répondre aux demandes des employeurs, envoyer de la publicité ciblée [[@claveyIABiometrieParcours2023]].  

 **février 2024** : Mastodon atteint le chiffre de 13 millions d'utilisateurs

**mars 2024** : L'attaque portant sur la dépendance XZUtils (dépendance du protocole OpenSSH) est publiée sur Mastodon avant d'être relayée sur Twitter. 

**juin 2024** premiers retours sur la migration des scientifiques de Twitter vers d'autres plateformes : quand les chercheurs quittent Twitter pour Mastodon, ils n'y restent pas et se tournent plutôt vers d'autres réseaux (LinkedIn, Bluesky, Instagram)
([[@FailedMigrationAcademic]])


Rappel des modifications apportées par Elon Musk à Twitter au cours des six derniers mois :

- E. Musk rend payant les comptes certifiés ($8 par mois). Ce premier changement a peu de conséquences pour les chercheurs qui contrairement aux femmes et aux hommes politiques n'ont pas pour pratique de faire certifier leurs comptes.   
- il limite le nombre de lectures de tweets pour les comptes certifiés et encore plus pour les comptes non certifiés (ces derniers pourront lire 10 fois moins de tweets par jour que les détenteurs de comptes payants)
- il ferme l'API qui permettait aux chercheurs d'extraire de larges stocks de tweets pour analyser le discours sur Twitter.   
- il coupe les liens entre Twitter et les applications tierces et réserve l'[[interopérabilité]] de Twitter avec des outils de veille comme Nitter ou Tweetdeck aux comptes Blue (=comptes certifiés et payants)  
- il fait baisser drastiquement le coût de la modération et rémunère n'importe quel tweet qui fait du buzz, y compris les tweets postés par des néo-nazis [1]. Il réouvre les comptes qui avaient été suspendus par la précédente équipe, dont celui de Trump et de propagandistes notoires de l'alt-right. A contrario, il fait suspendre les comptes de journalistes qui ne lui sont pas favorables (New York Times, CNN) tout en développant une doctrine du "free speech".  
- il fait supprimer les liens des profils vers des applications concurrentes (Mastodon et Facebook).  
- Musk promet de réserver la double authentification ([[double authentification|2FA]]) aux comptes Blue, ce qui pourrait constituer une menace sérieuse d'usurpation d'identité pour tous les comptes non payants.   
- Twitter a pendant un temps bloqué l'accès en recherche aux personnes qui ne disposent pas de compte (c'était déjà le cas sur d'autres plateformes comme Instagram). Aujourd'hui les usagers ne disposant pas de comptes ne peuvent toujours pas voir les [[thread|threads]] (série de tweets sur un même sujet).  
- Musk promet de bannir de Twitter en tant qu'injure les mots *cis* et *cisgenre*, ce qui si la menace était mise à exécution, pourrait entraver la communication des études sur les LGBTQI+ ; globalement, à chaque annonce de ce type, Musk confondant ses détestations avec la politique de modération de Twitter, les risques de censure sont permanents. Le slogan du *free speech* doit permettre à l'extrême droite de se sentir sur Twitter comme chez elle, mais ne s'applique visiblement pas aux utilisateurs qui représentent le point de vue *liberal* (comme on dit aux USA).  
- Musk ralentit le trafic depuis Twitter vers les médias qu'il déteste (cf. [article du Washington Post](https://www.washingtonpost.com/technology/2023/08/15/twitter-x-links-delayed/)).  
- dernière trouvaille du nouveau propriétaire de Twitter renommé X : Musk a annoncé le 17 août qu'il désactiverait la fonction de blocage qui permettait aux utilisateurs de se protéger contre le harcèlement en ligne. Poster sur Twitter des informations en rapport avec le changement climatique devrait se solder dans les mois à venir par des offensives en règle de climatosceptiques contre lesquelles les utilisateurs, chercheurs ou pas, auront de plus en plus de mal à se protéger [[@liberationElonMuskVeut]].  

# Ce dont les chercheurs ont besoin à travers une plateforme comme Twitter

Demander aux chercheurs de répondre eux-mêmes à cette question, et proposer à leur approbation les éléments de la liste ci-dessous qui n'apparaîtraient pas dans leur propositions.

- utiliser un espace de discussion dépassionné. C'était l'objet des sociétés savantes avant qu'elles ne deviennent à la fin des années 90 des entreprises à but essentiellement lucratif : 

   > Their first purpose was no more, then onely the satisfaction of breathing a freer air, and of conversing in quiet one with another, without being ingag’d in the passions, and madness of that dismal Age”
   
(source the History of the Royal Society of London, cité par Bjorn Brems [[@bremsFediverseOpportunityLearned2023]])

- **utiliser un réseau social *loyal**** . Loyauté d'un logiciel : il dit ce qu'il fait et et il fait ce qu'il dit. Twitter est un réseau très peu transparent dans la mesure où des algorithmes filtrent en amont, sans qu'on ait son mot à dire, les tweets produits par les personnes qu'on suit. Contrairement à un protocole ouvert comme le RSS, l'algorithme de Twitter inscrit ses propres biais dans ce qui vous est donné à lire.  Des chercheurs ont ainsi montré que l'algorithme de Twitter vous expose à des informations qui  présentent un [[biais de négativité]] beaucoup plus important (+49%) que ce que postent réellement les gens que vous suivez ([[@bouchaudCrowdsourcedAuditTwitter2023]]). L'algorithme favorise les informations négatives pour susciter l'indignation et la colère qui poussent à un taux d'engagement plus fort (et donc du temps passé sur la plateforme en plus et davantage de monétisation)  
- **donner de la visibilité à leurs publications** pour faire progresser sa carrière.  
- **trouver de l'aide auprès de leurs pairs** (cela inclue la possibilité de nouer des coopérations ou de trouver des opportunités d'emploi comme sur linkedIn ou ResearchGate, mais au quotidien, c'est aussi le partage de routines pour mener à bien le travail universitaire).  
- **discuter d'articles publiés avec leurs pairs** (cf. encore une fois \#arseniclife).  
- **transmettre leurs trouvailles auprès d'un large public dans le monde entier** et ainsi augmenter l'information des internautes sur certains enjeux importants C'est une dimension très importante : si les chercheurs massivement se déportaient sur Mastodon mais que les autres usagers restaient sur Twitter, le débat science / société serait compromis et on y perdrait des deux côtés. Il faut donc espérer que le public non-chercheur va également quitter Twitter pour investir les mêmes réseaux que ceux où se déplacent les chercheurs actuellement [[@kupferschmittMuskReshapesTwitter2022]].   
- **Engager des conversations avec les décideurs** pour orienter l'activité législative dans un sens conforme aux avancées de la science. (même question que pour le vaste public : les journalistes et les politiques se sentiront-ils/elles contraint.e.s au bout d'un moment de quitter Twitter ? Cela dépendra sans doute de la sensibilité politique de leur parti ou de la ligne de leur journal).  
- **rendre compte de conférences** auxquelles on a pu se rendre à d'autres collègues (live-tweeting).  
- **analyser les discours et les échanges** sur la plateforme sociale (en accédant à des ensemble de posts). Si l'accès à ces données issues des serveurs de Twitter coûte aujourd'hui cher à la communauté scientifique, est-ce que les réseaux alternatifs et décentralisés seront en mesure de fournir les masses d'information qu'on pouvait attendre d'un service de microblogging centralisé ?   

Ce que les chercheurs souhaitent trouver sur un réseau social, ils ne peuvent déjà plus le trouver sur Twitter. 
Ces chercheurs sont donc en train de considérer qu'en dépit du temps qu'il leur a fallu dans certains cas pour construire leur réseau d'abonnés sur Twitter et leur écosystème de veille sur ce réseau, il paraîtra demain plus coûteux de rester que de quitter cette plateforme. 

Aussi si les chercheurs, comme n'importe quel autre type d'usagers ou de communautés, reste sur des plateformes qui les espionnent et revendent leurs données à des publicitaires, sur des plateformes qui dégradent leur service de jour en jour, ce n'est pas à cause de la dopamine et des effets addictifs que cette plateforme prétend mettre en oeuvre sur le cerveau humain, mais bien plutôt parce que le chercheur est enfermé avec d'autres, ses collègues plus ou moins proches, dans cet espace social et qu'en partir signifie reconstruire une communauté ailleurs au risque de perdre au passage une partie du réseau et des affinités qu'il a construites sur cette plateforme : 

> # market (22 Apr 2024)

  
[![](https://i0.wp.com/craphound.com/images/22Apr2024.jpg?w=840&ssl=1)](https://pluralistic.net/2024/04/22/kargo-kult-kaptialism/)
[Paying for it doesn't make it a market](https://pluralistic.net/2024/04/22/kargo-kult-kaptialism/#dont-buy-it): But competition does.

Plus les chercheurs vont quitter la plateforme et plus la désinformation y sera comme chez elle, plus le nouveau propriétaire de Twitter va abaisser les barrières de la modération et de la censure au "hate speakers" et plus le temps consacré à éviter les meutes complotistes, négationnistes et libertariennes va croître au détriment du temps nécessaire à la communication sur son travail.

Si se maintenir sur Twitter pour un chercheur va devenir de plus en plus difficile, il lui reste deux possibilités : 
1. trouver d'autres moyens de valoriser sa production sur le web que par les réseaux sociaux (cf. blogs scientifiques)  
2. trouver un autre réseau social, plus accueillant. C'est la deuxième option qui va être explicitée dans ce qui suit à propos du Fédivers et de Mastodon. L'étude de Nature mentionnée plus haut, indique d'ailleurs que Mastodon est la première destination des chercheurs qui quittent Twitter (46,9% des comptes migrants) devant LinkedIn (34,8%) et Instagram (27,6%)  
# Mastodon et le fediverse comme alternative possible à X (ci-devant Twitter). 

## le Fediverse, qu'est-ce que c'est ? 

le [[Fediverse]] est un réseau décentralisé . 
Ce réseau, le Fédivers (Fediverse), fédère plusieurs instances tournant avec le même logiciel ([[Mastodon]], mis au point par Eugen Rochko). Le Fediverse permet de faire tourner d'autres logiciels que Mastodon (Peertube et Diaspora par exemple) selon un protocole unique, ActivityPub. Donc quand on devient utilisateur de Mastodon, on ne va pas à proprement parler "sur Mastodon", mais sur le Fédivers.
Pour en savoir plus sur ce réseau qu'est le Fédivers, nous vous recommandons de suivre le [cours ouvert consacré à ce sujet](https://librecours.net/module/lownum/fediverse/fed02c01fediverse.xhtml)

Le protocole d'échange sur le Fédivers est le suivant : 

nomutilisateur@nomservice  
par exemple : dbelveze@mamot.fr  
Mamot (https://mamot.fr) est l'instance de Mastodon maintenue par la Quadrature du Net sur le Fédivers. Pour communiquer avec moi, il faut préciser mon nom d'utilisateur et le service que j'utilise (en l'occurrence une instance de Mastodon qui a pour adresse mamot.fr)

Si on y réfléchit bien, ce n'est guère différent de ce qui se passe pour le courriel (choix de l'hébergeur de la messagerie personnel)[[@viniacourtQuatreChosesSavoir2023]]

Noter qu'un tiers pourrait se faire passer pour moi en ouvrant un compte dbelveze@autreinstance.fr. Dans un service décentralisé, il n'y a pas de possibilité d'utiliser une autorité de vérification centralisée. Par conséquent, vous ne pouvez pas vous opposer à ce que des personnes malveillantes créent d'autres comptes avec vos identifiants sur d'autres instances, mais au moyen d'un lien sécurisé, vous pouvez en revanche diriger votre public de lecteurs d'un site sur lequel vous avez la main vers votre compte authentique sur Mastodon. Cette fonctionnalité a été mise en place en 2018 [[@rochkoMastodonReleased2018]]. 

## Choix de l'instance et modération

Les instances sont plus ou moins grandes , tenues par des acteurs très différents. Dans certains cas, c'est une association avec plusieurs salariés, dans d'autres, c'est une personne unique sur son propre serveur. Chaque instance a sa propre politique de modération, ce qui peut dans certains cas déconcerter les utilisateurs de réseaux centralisés. 

Il faut néanmoins préciser que la majorité de votre lectorat sur Mastodon proviendra d'autres instances que la vôtre. Si vous êtes sur une instance A, vous pourrez sans problème suivre une personne qui est sur une instance B et réciproquement. 
Il est possible de ne suivre que le fil provenant de son instance, mais la chose a peu d'intérêt. 

Voici la charte de modération de l'instance Mamot.fr : https://mamot.fr/privacy-policy

Les administrateurs de l'instance conservent les posts que l'on n'efface pas soi-même (c'est le cas dans toutes les instances)
les administrateurs peuvent avoir accès aux messages directs (privés entre utilisateurs). C'est le cas aussi chez Twitter, mais il y a très peu de chances que les admins de Twitter vous connaissent, ça peut être le cas en revanche des admins de l'instance que vous avez choisie. Martin Clavey a développé cette réflexion sur Mastodon et dans un article de Nextinpact ([[@claveyMastodonRefugePour2023]]) : Dans la mesure où les messages privés ne sont pas chiffrés et peuvent être vus par les admins d'une instance et si demain - les société savantes ouvrant de nouvelles instances - des chercheurs ou des personnels travaillant pour des collectifs de chercheurs peuvent avoir accès aux messages privés d'autres chercheurs, possiblement concurrents ou engagés dans une controverse, cela pourrait avoir des conséquences néfastes pour la communauté d'utilisateurs. 

Les admins, à qui revient la tâche de modérer les échanges en cas de besoin,  peuvent décider de bloquer un post, sans pour autant être incriminés de censure (dans la mesure où vous pourriez créer votre propre instance pour dire ce que vous voudriez), on en reparlera plus loin.
La charte comporte des interdits classiques : propos racistes, homophobes, transphobles, sollicitations sexuelles non désirées, messages à caractère porno, [[doxxing|doxing]].  Certains termes assimilables à du racisme ou de l'homophobie ("racisme anti-blanc" ou "hétérophobie") sont également proscrits, ainsi que la publication de propos diffamatoires ou calomnieux. Les comportements de harcèlement sont difficiles à repérer ; à partir de quand plusieurs messages critiques peuvent-ils être dénoncés comme du harcèlement ? Faut-il arrêter de mentionner la personne quand on critique son travail ? Faut-il s'arrêter quand la personne souhaite ne plus être importunée par notre critique, même quand on ne la mentionne plus (avec un @) ? Ces questions sont délicates d'autant plus lorsqu'on est un.e "expert.e" sur un sujet très débattu et qu'on se sert de son impact sur les réseaux sociaux, faute d'une autorité universitaire reconnue, pour vendre des interventions en public et des conférences ou monétiser des vidéos sur Youtube. Ces profils sont concurrents dans une sorte de course à la visibilité qui est le parallèle de la course que se livrent parfois les chercheurs entre eux [^3] . La visibilité de l'un se fait souvent au détriment de celle de l'autre.  

Les administrateurs de Mastodon (en prenant comme contre-exemple Twitter) insistent souvent sur le fait de ménager la susceptibilité des personnes que l'on ne connaît pas sur le réseau, la prise en compte du statut ou de la sensibilité de chacun.e. D'où la recommandation d'user de messages de prévention (content warning ou CW), pour éviter de réveiller des traumatismes, être compréhensif à l'égard des phobies courantes (serpents, rats, araignées), ne pas divulgâcher, ne pas poster d'images sans CW qui peuvent inciter à la consommation d'alcool ou de stupéfiants.

les mesures de modération mises en oeuvre sont les suivantes : selon la gravité ou la récurrence, envoi d'un message de prévention par les admins, invisibilisation du post, blocage si le compte est sur une autre instance, suppression du compte s'il se trouve sur l'instance en question. 

Voir charte de Sciences.re : https://social.sciences.re/about

Comparer la charte de Mamot ou de Sciences.re avec par exemple celle d'Octodon : https://octodon.social/about 
Moralité : avant de choisir une instance, lisez la charte de modération de cette instance !

Même lorsque les chartes sont précises et développées, les équipes de modération sont souvent restreintes, voire parfois réduites à une seule personne qui gère en plus l'instance, comme ont l'a dit plus haut. Il est donc très possible que des comptes soient invisibilisés ou que le vôtre soit suspendu suite à un jugement fait dans la précipitation et informé par les biais de la ou des personnes qui modèrent la plateforme. Les problèmes de censure évoqués sur Twitter peuvent donc se retrouver sur Mastodon mais vont plus affecter telle ou telle instance que telle autre. 
La censure sera rendue d'autant plus facile sur Mastodon que les modérateurs comme on l'a vu peuvent toujours vous dire d'aller voir ailleurs sur une autre instance qui vous permettra quand même d'utiliser Mastodon. Ce n'est pas le cas sur Twitter : quand une décision vous en exclut, vous perdez l'accès à l'ensemble de votre communauté, et seule une décision de Twitter peut vous restituer dans vos droits de lecteur et de contributeur sur ce réseau. 

### Et pour des institutions, comment la question se pose ? 

instances de chercheurs : 
- fediscience
- sciences.re
- scholar.social


En France, de plus en plus d'universités mettent leur compte Twitter en veille, sans pour autant créer de compte sur Mastodon, contrairement à l'Allemagne où des universités ou des bibliothèques ont été nombreuses à se créer un compte sur une instance de Mastodon 
[requête Wikidata](https://w.wiki/9XsJ) 

Est-ce un trait lié au tropisme centralisateur de notre pays que de passer à côté des alternatives décentralisées qui pourraient nous rendre plus libres ? 

Des universités hollandaises se sont mises à utiliser une instance de Mastodon dédiée aux études supérieures et à la recherche. Les étudiants, enseignants et chercheurs de ces universités peuvent se connecter à ce réseau au moyen de leur compte universitaire : https://dashboard.surfconext.nl/apps/9977/saml20_sp/abouthttps://dashboard.surfconext.nl/apps/9977/saml20_sp/about

## changer d'instance sans perdre ses followers, mode d'emploi

1. S'inscrire sur une nouvelle instance 
2. Sur la nouvelle instance : Aller sur Compte (Account) -> Changer d'un autre compte (Moving FROM another account)  
3. Entrer les identifiants de l'ancien compte  
4. Sur l'ancienne instance, aller sur le compte -> Changer de compte (Moving TO another account)  
5. Entrer les identifiants du nouveau compte et envoyer

<iframe src="https://mastodon.social/@Gargron/103393780267601137/embed" width="400" allowfullscreen="allowfullscreen" sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox allow-forms"></iframe>
# Des instances pour les chercheurs ?

Il n'existe pas d'instance qui aurait l'ambition d'accueillir les chercheurs ou institutions de recherche du monde entier.
Il peut être utile de suivre les changements d'instances de certains chercheurs. D'où ils partent (et pourquoi ils partent de cette instance, s'ils s'expriment à ce sujet) et où ils vont.

Une [page sur Github](https://github.com/nathanlesage/academics-on-mastodon#serverscommunities) répertorie les instances utilisées par des chercheurs en fonction de sujets disciplinaires : choisissez l'instance qui vous semble à la fois pertinente pour vous et digne de confiance (vous n'avez que la charte de modération pour vous faire une idée, si vous ne connaissez personne sur Mastodon).
Le service https://instances.social peut aussi vous aider à choisir votre instance en fonction du nombre d'utilisateurs que vous souhaitez avoir dans votre instance, de ce que ces utilisateurs peuvent afficher ou pas et des centres d'intérêt partagés par ces utilisateurs (a priori).
Au pire, si vous vous trompez et souhaitez changer d'instance, vous pourrez le faire tout en conservant votre activité passée sur la première instance [^2]. 
Jusqu'au 2 juillet, quand vous veniez de Twitter, un service gratuit (Twittodon) permettait de retrouver automatiquement sur Mastodon les comptes d'une partie de vos contacts qui avaient migré depuis Twitter, mais dans la mesure où Musk a fermé ses API, le service ne fonctionne plus (https://twitter.com/twittodon_com). Si vous connaissez quelqu'un que vous suiviez sur Twitter, il va falloir taper son nom d'utilisateur dans le moteur de recherche de Mastodon (généralement, les gens utilisent le même nom d'utilisateur sur les deux réseaux sociaux).

L'instance Fediscience (https://fediscience.org/explore) accueille beaucoup de scientifiques du monde entier dont probablement certains qui ont du quitter Twitter en raison du harcèlement pratiqué par les [[climato-scepticisme|climato-dénialistes]]. L'ancienne présidente du GIEC, Valérie Masson-Delmotte a choisi ce canal pour s'exprimer sur le bouleversement climatique.

Sachez également que Sciences.re héberge un grand nombre de comptes d'universitaires francophones. 
Au pire, si vous vous trompez et souhaitez changer d'instance, vous pourrez le faire tout en conservant votre activité passée sur la première instance [^2]. 

# bonnes pratiques sur Mastodon

valoriser les bonnes réponses reçues en les éditant dans notre question : 

https://neuromatch.social/@elduvelle/114726463359539895

autres bonnes pratiques #Mastodontips

# Premiers pas sur Mastodon

## Se créer un compte sur une instance

créez-vous un compte sur Mastodon (création du compte, ajout d'un avatar, d'une bannière, d'un petit texte introductif)
Pour plus de sécurité et si vous disposez de votre smartphone, activer la double authentification. Si vous ne disposez pas d'un outil pour la double authentification sur votre smartphone, téléchargez en un (authy ou TOTP authenticator / FreeOTP disponible sur F-Froid). Cette étape est facultative, mais néanmoins conseillée.

Si vous souhaitez suivre votre compte Mastodon depuis votre smartphone, vous pouvez télécharger l'appli Mastodon depuis le PlayStore d'Android, l'AppStore d'Apple ou F-droid pour les systèmes libres.

## Poster des messages et interagir avec d'autres comptes

Mastodon vous permet d'envoyer des messages de 500 caractères maximum.
Pour désigner ces messages, on parle ici de **post** parce que la terminologie pour désigner un message sur Mastodon est fluctuante. Un anglais, un tweet est un *toot* sur Mastodon, et en français, on traduit souvent toot par "pouet" (bruit de klaxon). On peut dire que le mot "post" issu des blogs peut aussi convenir comme terme générique à l'ensemble des plateformes sociales. Généralement un "retweet" se traduit par un *boost* quand on parle de Mastodon. 

Pour conserver un post qui vous intéresse, utilisez l'étoile (équivalent de la fonction like sur Twitter) si vous souhaitez que l'auteur du post soit prévenu de votre intérêt pour ce post ou bien "signet" (bookmark) si vous souhaitez ajouter ce post à une liste de messages qui restera privée. Plus d'infos sur ces fonctionnalités [ici](https://fedi.tips/how-do-i-do-likes-and-re-tweets-in-mastodon-and-what-are-bookmarks/)

Postez l'un de vos articles, exposition, réalisation avec un petit texte de présentation. Utiliser le hashtag \#premierpost2023 pour reconnaître les posts utilisés par les autres apprenants.
likez ou repostez les posts des autres apprenants. Envoyez-leur des messages si vous êtes inspiré.e. 
Changer de statut pour chaque post (pour en savoir plus sur les statuts de visibilité des posts, consultez [cette page du cours](https://librecours.net/module/lownum/fediverse/fed02c11masto02.xhtml) sur le Fédivers que nous avons déjà mentionnée)
Créez votre première liste de comptes en partant d'un thème qui vous tient à coeur (recherche par hashtag)

Il est possible de programmer un toot au moyen de l'application https://plan.fedilab.app/ 

## Trouver des comptes à suivre

Faites des recherches par hashtags en lien avec vos centres d'intérêt. 
Si vous travaillez en Sciences Economiques, voici une liste de chercheurs qui se sont inscrits sur Mastodon : https://ideas.repec.org/i/emastodon.html

# Faire des recherches dans Mastodon

recherche dans la bibliothèque. Jusqu'à présent on ne peut pas restreindre sa recherche aux favoris mais avec le filtre *in:library* on peut restreindre la recherche à la "bibliothèque" c'est à dire à ses posts, repouets, ses bookmarks et ses favoris ([source](https://github.com/mastodon/mastodon/issues/21352)) 


## interagir avec des comptes d'autres plateformes

### Threads

### Bluesky 

<iframe src="https://mastodon.social/@o_simardcasanova/112654229489581104/embed" width="400" allowfullscreen="allowfullscreen" sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox allow-forms"></iframe>


# Conclusion

Vous vous habituerez bien vite à l'interface et aux fonctionnalités de Mastodon ainsi qu'aux usages du réseau.
Twitter avait la dimension d'un bien commun informationnel qui aurait pu évoluer dans un sens positif, vers de nouvelles formes d'échange de savoirs et une meilleure information du public, mais aux mains d'entrepreneurs millionnaires, cette évolution ne pouvait se faire que dans le sens d'une plus grande captation et monétisation de nos données avec les excès que cette forme de capitalisme engendre et que l'on retrouve également chez Meta (Facebook, Instagram) ou Tiktok. La situation a empiré, quand Twitter est tombé dans les mains d'un homme dont on peut dire qu'il n'est pas seulement capitaliste et enclin à maximiser sa marge de profit et celle de ses actionnaires au détriment de notre intérêt à tous, mais qu'il est en plus impulsif et autoritaire de tempérament. Sur le plan politique, Musk est le trait d'union entre le capitalisme de plateforme et les idées libertariennes et racistes de l'alt-right. Pour un chercheur, jusqu'en 2022, la question était de savoir si la mention de son article pouvait trouver sa place entre un chaton et une licorne. A présent, la même question se pose, mais cette fois entre un post masculiniste et un thread complotiste.

[^1]: voir https://masto.ai/@nickmartin/110919378294378823
[^2]: Le logiciel Mastodon rend est possible de demander et recevoir (à l'adresse mail utilisée pour la création du compte) une archive de son activité. En exportant cette archive d'un compte et en l'important dans le nouveau compte, on ne perd rien de son activité passée. 
[^3]: course organisée par la raréfaction des postes dans l'enseignement supérieur et le système d'évaluation mis en oeuvre par les agences de recherche. (voir à ce sujet l'article de Boris Grésillon sur AOC[[@gresillonPortraitChercheurModerne2021]])
$\newline$
# bibliographie
$\newline$







---
title: Twine
subtitle:
author: Damien Belvèze
date: 05-08-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: [twinery, twine, Interactive Digital Storytelling, IDS]
tags: [serious_games, programmation]
---
# Installation

```
sudo snap install twinejs
```

## problème d'installation sur Ubuntu

résoudre l'erreur "ENOENT  mkdtemp no such file or directory /user/..."

suivre la méthode suivante : 

1. install nodejs et npm
2. entrer la commande "npm install"
```bash
npm install
npm cache clean --force
npm install -g npm
npm install
```
Si la première commande suscite une erreur, essayer d'abord : 
```shell
npm init --yes
```
Si l'erreur persiste, par exemple on obtient un message indiquant un manque d'interopérabilité entre la version de npm et la version de node : 

```shell
dbelveze@pr030165:~$ npm install -g npm
npm ERR! code EBADENGINE
npm ERR! engine Unsupported engine
npm ERR! engine Not compatible with your version of node/npm: npm@11.2.0
npm ERR! notsup Not compatible with your version of node/npm: npm@11.2.0
npm ERR! notsup Required: {"node":"^20.17.0 || >=22.9.0"}
npm ERR! notsup Actual:   {"npm":"9.2.0"}

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/dbelveze/.npm/_logs/2025-03-19T14_22_04_958Z-debug-0.log
```

Dans ce cas, on n'arrivera pas à charger la version 20 de node avec npm (maximum : version 18 dans ce registre), essayer avec nvm : 

```shell
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
source ~/.bashrc
# install nvm
```
puis charger avec nvm nouvellement installé la dernière version de node.js : 

```shell
nvm install 20
```
L'installation devrait se faire correctement. 
Il ne devrait plus y avoir de problèmes d'interopérabilité entre npm et node.js 
et il ne devrait plus y avoir d'erreur enoent en utilisant Twine. 


source: https://stackoverflow.com/questions/20753550/error-message-enoent-no-such-file-or-directory
# Twine dans l'enseignement


poster réalisé pour les JNF 2022

![[20220111_poster_twine_V2.pdf]]



logiciel libre permettant de construire des récits interactifs ("jeux dont vous êtes le héros")
moteur de jeu narratif inventé par Chris Klimas en 2009 et sorti des limbes par la game-designeuse Anna Anthropy en 2012 ([[@friedhoffUntanglingTwinePlatform]])
Ce moteur est utilisable par des gens qui ne savent pas coder pour construire des jeux où la narration occupe une part importante. 
D'ailleurs, le jeu n'est pas d'abord conçu pour des développeurs (à l'exception de sa version éditée en [[lignes de commandes|ligne de commande]] [Twee](https://twinery.org/cookbook/twine1/editor/choosing_between_twine_and_twee.htm)mais place l'emphase sur l'écriture de l'histoire : 

>Putting the emphasis on 'writers,' rather than 'developers' or 'game-makers,' implies that creating  this kind of interactive experience is not limited to those with technical ability. This point is emphasized by the reference materials' attitude to code. The materials do not assume that code is inherently valuable or that all users will be interested in learning it (or able to learn it at all) ([[@friedhoffUntanglingTwinePlatform]])

Twine permet d'exposer sous une forme ludique des sujets qui exigent de la réflexion ou de l'[[empathie]] (voir pour cette dernière la manière dont la communauté [[LGBTQ ]]a investi la plateforme)

Mémo de la syntaxe[[@reseaucyber-baselacq-orthezMemoTwine2021]]

Exemple de jeu sérieux sur le management des données de recherche conçu avec Twine : [https://rdm-games.gitlab.io/rdm-adventure/](https://rdm-games.gitlab.io/rdm-adventure/)


# vocabulaire : 

- story

- passage

- texte : un passage peu être fait de texte seul ou de texte associé à des valeurs ou des commandes (dans ce cas, on parle de hook). Dans tous les cas, le texte peut être formaté en [[Markdown]]

- hook : un texte entre crochets auquel on accole une valeur (présentation, condition)

>A **hook** is a section of passage prose enclosed in `[` or `]`, or preceded with `[=`. The main purpose of hooks is that they can be visually or textually altered by special data values called **changers**. Changers are usually placed in front of hooks to change them.

```harlowe
(if: $anneau_vole)[Comme on pouvait s'y attendre, l'anneau a été volé.]
```

```harlowe
(transition:"slide-right")[le texte glisse vers la droite]
```
- command

- changer : change un hook (en changeant le style de la police par exemple)

````harlowe
`L'ombre (text-style: "shadow")[s'étend] sur toi!`
````

- variable

une variable peut être un entier, mais peut aussi être un nom ou un événement : si le fait d'avoir rencontré un moine ou pas est important dans la suite du jeu on peut écrire au passage de la rencontre

- variable pour l'embranchement

Vous rencontrez un moine

````harlowe
(set: $moine to true)
````

`````sugarcube

<< set $moine to true >>

`````

et plus tard : 

Si vous avez rencontré un moine
`````harlowe
(if: $moine is true)[le moine vous a amené ici]
(else:)[vous êtes arrivé ici par hasard]
`````

une commande permet de fixer une variable

```harlowe
(set: $endurance to 10)

```
et de la modifier en cours de jeu

```harlowe
(set: $endurance to it - 4)[ce coup vous fait perdre 4 points d'endurance]

```
Pour afficher une variable dans du texte, il n'y a pas besoin de commande particulière (mais on peut aussi utiliser la commande (print: $variable) : 

```harlowe
Il ne vous reste plus que $sous sous
```

une variable peut être plusieurs choses : une valeur mais aussi un changer : 

```harlowe
(set: $robotic to (font:'Courier New'))
$robotic[Hi, it's me. Your clanky, cold friend.]
```

tous les hooks précédés de la variable $robotic seront désormais écrits en Courier New

# les liens

Utiliser les wikiliens pour relier les passages
Pour des liens de retour au passage précédent, voir [[Twine#créer un inventaire avec un passage dédié à cela]]
Lorsque vous changez le nom d'un passage, le lien qui mène à ce passage en est affecté, ce qui est plus pratique que dommageable, cela sert à renommer des passages facilement sans générer de liens cassés. 


# la sidebar de Sugarcube

possibilité de supprimer la sidebar : 


````javascript
UIBar.destroy();
````

Supprimer la sidebar uniquement pour certains passages marqués par une balise (par exemple, balise "bar")
Dans le CSS : 

```css
/* balise destinée à cacher la sidebar*/

.bar #ui-bar {
	display: none;
}
```
## gérer un inventaire

### gérer un inventaire avec un dictionnaire

````harlowe
(set: $inventaire to (a: "épée", " bouclier", " lance"))
`````

afficher l'inventaire

````harlowe
Vous disposez des éléments suivants (print: $inventaire) dans votre besace
`````

ajouter un objet à un inventaire

````harlowe
vous ramassez le miroir et le mettez dans votre sac

(set: $inventaire to $inventaire + (a: "miroir"))

````

supprimer un objet dans l'inventaire

````harlowe
votre lance se casse en deux

(set: $inventaire to $inventaire - (a: "lance"))

````

### créer un inventaire avec un passage dédié à cela

Avec le dialecte Sugarcube, une sidebar permettant de sauvegarder sa progression ou de repartir à zéro s'affiche à droite.
Si on veut la supprimer tout au long du jeu, dans la feuille javascript de l'histoire, entrer le code 

Dans la sidebar, vous pouvez créer des liens, par exemple vers un inventaire. 
Dans ce cas, créer un passage isolé StoryCaption (respecter la casse du nom du passage)
Inscrire le sous-titre Inventaire (par exemple: ```
```html
<h1>Inventaire</h1>
```

Puis afficher les objets qui peuvent être acquis au cours de l'aventure sous la forme de conditions : 

```sugarcube
<<if $couteau is true>> couteau <</if>>
<<if $enveloppe_kraft is true>> enveloppe kraft <</if>>
<<if $silencieux is true>> silencieux <</if>>
<<if $polaroid is true>> polaroid <</if>>
```
Chaque fois que dans un passage, un objet est acquis, utiliser set : 
```sugarcube
un couteau traîne sur la table, vous vous en saisissez. 
<<set $couteau to true>>
```
cela fera apparaître le couteau dans l'inventaire
Faire la même chose pour enlever un objet de l'inventaire

````sugarcube
En se servant du couteau comme levier, la lame se casse. il est devenu inutilisable 
<<set $couteau to false>>
````

Pour revenir au dernier passage visité avant l'ouverture de l'inventaire, utiliser la fonction ``return`` ou bien une autre fonction , ``previous()`` , dans un bouton : 

```sugarcube
<<button "retour" `previous()`>><</button>>
```

## système de magasin

voir [[Twine système de magasin]]


# modifier l'affichage de l'histoire ou de tel ou tel passage
## modifier la feuille de style de l'Histoire 

cliquer en bas à gauche sur le titre de l'histoire. 
Choisir "Modifier le style de l'histoire"

ajouter le CSS correspondant à ses voeux : 

- format des citations : 

````css
{
  quotes: '“' '”' "‘" "’";
}
````

- couleur de fond : 

````css
tw-story {
  background-color: #fff;
  color: #000;
}
`````

- image de fond pour l'ensemble des passages

````css
tw-story {
  background-image:url("lien");
  background-size:cover;
}
````

- image de fond pour les passages balisés "ciel"
- 
````css
body.ciel {
	background-image: [img[black_sky.jpg]];
   background-size: cover; 
}
````

* police, taille des caractères :

````css
body, tw-story  {  
font-family: Palatino;  
font-size: 18px;  
font-color: #fefe9c;  
}
````


- taille maximale de l'image :
````css
img {
  max-width: 80%;
}
````

- format et couleur des liens :

````css

.glossary tw-link {
  color: inherit;
  font-weight: inherit;
  text-decoration: underline dotted #197fe6; /*#9f5810;*/
}

````

Supprimer la sidebar dans la version Sugarcube

````css
#ui-bar   {
display: none;   
}
````

Modifier le format de l'Histoire = changer la syntaxe du code (par défaut Harlowe 3.2)

# Exemples

## liens entre les passages

faire un lien vers un autre passage
```harlowe
Do you [[make this -> first proposal]] or [[that -> second proposal]]
```

```sugarcube
Do you [[make this|first proposal]] or [[that|second proposal]]
```


Copier-coller le texte d'un passage dans un autre passage

````html
{
passage1
}(display: "passage2")
````

Adapter un passage en fonction des passages déjà visités avec la fonction "visited" : 

```sugarcube
<<if !visited("bakery") && !visited("garden")>>
	<span style="color:blue;">This is blue text because neither the bakery nor the garden has been visited.</span>
	
<<elseif visited("bakery") && !visited("garden")>>
	<span style="color:red;">This is red text because the bakery has been visited but not the garden.</span>
	
<<elseif !visited("bakery") && visited("garden")>>
	<span style="color:green;">This is green text because the garden has been visited but not the bakery.</span>
	
<<else>>
	<span style="color:purple;">This is purple text because both the bakery and the garden have been visited.</span>
<</if>>
```

## animer le texte
Faire apparaître du texte en cliquer sur les mots

```harlowe
Voulez vous exclure ou inclure ce terme dans le titre : (click: "exclure")[: terme exclu.] (click: "inclure")[: terme inclu]
```

faire clignoter un mot
```harlowe
(text-style: "blink")[Votre texte ici]
```


## échapper

voir [[échapper]]

Possibilité d'utiliser dans l'éditeur la fonctionnalité Verbatim : le texte en verbatim ignore le balisage sous jacent. On peut aussi mettre le texte entre apostrophes : 

````sugarcube ou harlowe
`$score` 
````

## Lier des événements à des pressions de touche

Utiliser la fonction JQuery [[Keydown]] (anciennement Keypress)


## ajouter des conditions


````harlowe
(if: visits is variable)[{
texte
}](else:)[{
texte
}]
````

````harlowe
{
  (if: $variable contains "texte")[
    (display: "passage1")
  ](else:)[
    (display: "passage2")
  ]
}
`````

prise en compte de la visite d'un passage antérieur dans un embranchement

le passage antérieur une fois visité comporte la variable 
A= true
texte = entre crochets
``
```sugarcube
<<if $A>>  
    [[ok, va au passage B->B]]
<<else>>
    [[ok, va au passage C->C]]
<</if>>
```



Bonnes ou mauvaises réponses à une question :

````harlowe
    I mean, I ask you. What exactly is a *data management plan* when it’s at home?</q></p>
  <p>The professor’s mocking tone has you smiling in sympathy before you realise the question was not rhetorical, and you are expected to answer.</p>
  <ul>
    <li><q>(link: 'I’m sorry, I’m not entirely sure myself.')[
      (set: $response to 0)
      (set: $feedback's DMP to it + (a: '0 (out of 4) for not knowing what a data management plan is. Don’t worry, this is easily fixed!'))
      (go-to: 'DMP purpose')]</q></li>
    <li><q>(link: 'It’s a detailed handbook for how data will be handled during the project.')[
      (set: $response to 2)
      (set: $feedback's DMP to it + (a: '2 (out of 4) for your definition of a data management plan. They are more of an outline than a detailed handbook, and also discuss how data will be handled *after* the project.'))
      (go-to: 'DMP purpose')]</q></li>
    <li><q>(link: 'It’s where you outline how data will be managed at each stage of the project and beyond.')[
      (set: $response to 4)
      (set: $feedback's DMP to it + (a: '4 (out of 4) for your definition of a data management plan.'))
      (go-to: 'DMP purpose')]</q></li>
    <li><q>(link: 'It’s where you outline the procedures you will use for managing data during the research project.')[
      (set: $response to 3)
      (set: $feedback's DMP to it + (a: '3 (out of 4) for your definition of a data management plan. They also discuss how data will be handled *after* the project.'))
      (go-to: 'DMP purpose')]</q></li>
    <li><q>(link: 'It’s a plan for managing data.')[
      (set: $response to 1)
      (set: $feedback's DMP to it + (a: '1 (out of 4) for your wittily unhelpful definition of a data management plan.'))
      (go-to: 'DMP purpose')]</q></li>
  </ul>
}


`````


if, else-if, else : 

````harlowe
  <p>I see you went for the (if: $training_cycle contains "second")[first](else-if: $training_cycle contains "third")[second](else:)[third] option.</p>
`````



## Gérer les scores

baisser ou augmenter un score

````bash
(set: $score to it - 1)
`````

lier un score à un profil de performance

```harlowe
{
  (if: $score < ($max_score / 3))[(set: $rank to "Data&nbsp;Novice")]
  (else-if: $score < (2 * $max_score / 3))[(set: $rank to "Data&nbsp;Wrangler")]
  (else:)[(set: $rank to "Data&nbsp;Boffin")]
  (set: $displayed_score to $score)
}
```

Pour permettre à l'apprenant d'imprimer son score et de l'envoyer à l'enseignant :


````
Vous voici arrivé au terme de cette aventure [[print $nom]]

Votre score est de [[print $score]]

Cliquer ci-dessous pour imprimer votre score et envoyer le document à votre enseignant : 

<button onclick="window.print()">Imprimer le score</button>

````


## Fixer des variables en cliquant sur des objets

### définition de la variable : 

>En informatique, une variable est un symbole (habituellement un nom) qui renvoie à une position de mémoire dont le contenu peut prendre successivement différentes valeurs pendant l'exécution d'un programme

(source: Wikipédia)

### types de variables

3 types de variables : 

- les booléennes (vrai ou faux)
- les strings (chaînes de caractères)
- les valeurs (numérique)

### définir une variable

````harlowe
(set: $nomdemavariable to "string" ou 1 ou true)
````

```sugarcube
<<set $nomdemavariable to "string" ou true>>
```

exemple : 

```sugarcube
<<set $argent to 500>>
```

```sugarcube
<<set $arc to true>>
```
modifier une variable numérique en cours de jeu

```harlowe
(set: $nomdevariable to it +1)
```

````sugarcube

<<set $score to $score -= 4>>

<<set $chance to $chance **= 2>>
````

augmente le score de 4 points, double les points de chance.


Demander au joueur de fixer la variable avec PROMPT

````harlowe
(set: $name to (prompt: "Quel est ton nom?", "Mimi Exemple"))
````
Mimi exemple remplit le champ de réponse

Demander au joueur de faire un choix entre deux options

````harlowe
il y a un pommier et un prunier
voulez-vous manger une (link: "pomme")[(set: $fruit to "pomme") (goto: "arbre")] ou une (link: "prune")[(set: $fruit to "prune") (goto: "arbre")]

````

passage "arbre"
````harlowe
(if: $fruit is "pomme")[vous avez mangé une pomme empoisonnée, vous mourrez sur le coup]
(else:)[ce fruit est délicieux, vous en mettez quelques autres dans votre sac]
````

```sugarcube
<<if $fruit is "pomme">> Vous avez mangé une pomme empoisonnée, vous mourrez sur le coup
<<else>>Ce fruit est délicieux, vous en mettre quelques autres dans votre sac>>
<</if>>
```
Attention pour Sugarcube à ne pas oublier la balise de fermeture ``<</if>>``

# définir des zones cliquables sur une image

voir [[image mapping]]
voir [comment rendre des zones cliquables en html à partir d'une image](https://www.w3schools.com/htmL/html_images_imagemap.asp)
remplacer la balise href par data-passage="nom du passage"




# Mettre en scène un combat

système de combat avec Harlowe

```harlowe

(if: (either:0,1) is 0)[
[Le gobelin vous inflige une blessure qui vous fait perdre 2 points de vie
(set: $vie to $vie-2)]
(if: $vie<1)[[[vous êtes mort|mort]]]
(else:)[tentez un [[nouvel assaut|combat]] ou [[fuyez|fuyez]]]
]
(else:)[
[Vous infligez une blessure au gobelin et lui faites perdre 2 points de vie
(set: $viegobelin to $viegobelin-2)]
(if: $viegobelin<1)[vous avez vaincu le Gobelin, passez à [[l'étape suivante|gobelin mort]]]
(else:)[tentez un [[nouvel assaut|combat]] ou [[fuyez|fuyez]]]
]

```

système de combat avec Sugarcube : 

```
<<set $ballesP38 to $ballesP38 - 1>>
<<set $tir = random(1,5)>>

<<if $tir + $adresse > 10>>
    Votre tir a fait mouche. L'individu s'écroule frappé à la tête par une balle. Vous vous rapprochez de l'[[estaminet]].
<<else>>
    <<set $tir_inconnu to random(1,3)>>
    Vous manquez votre cible. Il vous reste $ballesP38 balles dans le chargeur. 
    Un coup de feu part de l'estaminet. 

    <<if $tir_inconnu == 1>>
        L'individu vous manque également. Souhaitez-vous prendre la [[tangente]] ou bien [[répliquez-vous|nouveau tir]] une nouvelle fois aux tirs de votre assaillant ?
    <<elseif $tir_inconnu == 2>>
        Une balle vous frappe alors que vous essayez de changer d'angle de tir. 
        <<set $santé to $santé - 5>>
             <<if $santé < 1 >>la balle a traversé le poumon, vous respirez difficilement. La dernière chose que vous entendez sont les pas de l'inconnu qui s'approchent de vous pour vous donner le coup de grâce. Vous ne connaîtrez jamais l'identité de celui qui aura eu raison de vous. Votre aventure s'arrête là.
             <<else>>La balle vous a traversé l'épaule gauche. Vous serrez les dents et vous parvenez à lever à nouveau votre pistolet vers l'origine des coups de feu. Il est encore le temps de [[fuir|tangente]] ou de [[riposter|nouveau tir]]
             <</if>>
    <<else>>
        La balle vous frappe en plein front et ne vous laisse aucune chance. Votre aventure se termine là. 
    <</if>>
<</if>> 
```
# Incruster du son, des gifs, des vidéos

## gif
```html
<img src="gifs/decouragement.gif" autoplay>
```

# Animer un dialogue

## fonction keydown

la fonction keydown (javascript) permet d'attendre qu'une touche soit tapée par l'usager pour afficher du texte : 

```javascript
<script>
(function () {
var i=0;
	$(document).keyup(function (e) {
    	document.getElementById(i).style.display="block";
    	i++;
	});
}());
window.scrollTo(0, document.body.scrollHeight);
</script>

  @@color:white;
  Tapez sur n'importe quelle touche pour afficher les dialogues.

<div id="0" style="display:none">
  @@color:green;   
- Hey salut $name ! T’as déposé sur l’espace cours de Madame Green ton devoir sur les microplastiques ? 
@@
   </div>
<div id="1" style="display:none">  
@@color:black;
Aucun répit décidémment. D'emblée il attaque sur le sujet qui t'inquiète le plus depuis la veille. 
Tu décides de lui dire la vérité : 
- Oui, je l’ai déposé, mais je ne comprends pas, j’ai reçu un mail de la prof pour me dire que le logiciel anti-plagiat de l’université, Plagiator, avait détecté du plagiat sur mon devoir. @@
</div>     
<div id="2" style="display:none">
  @@color:green;
- Ah bon, mais qu’est-ce que ça veut dire ? Tu as copié ou tu n’as pas cité tes sources ? Mais alors, tu n’auras pas la moyenne ?” @@
</div>
<div id="3" style="display:none">
@@color:black;
- Je ne sais pas trop, la prof me laisse 24 heures pour me rattraper et retravailler le devoir.@@
</div>
<div id="4" style="display:none">
   @@color:green;
- Ouah, le stress. Tu vas devoir refaire tout le travail en fait ? J'aimerais pas être à ta place...@@
</div>
<div id="5" style="display:none">
 @@color:black;
- Oui, bon si tu n'as rien de plus constructif à me dire, autant qu'on en reste là... Merci beaucoup, je suis bien flippé.e maintenant.@@
</div>
<div id="6" style="display:none">
  @@color:green;
- Attends je voulais pas en rajouter, mais c'est vrai que c'est chaud et il te reste plus beaucoup de temps. Tiens, je pense que, tu devrais en parler à Camille. C'est LA personne qui pourrait t'aider à gérer ça. Sur un truc de ce genre, je l'ai fait l'an dernier et ça m'a carrément sauvé la mise.@@
</div>
<div id="7" style="display:none"> 
@@color:black;
- Ouais, merci pour le tuyau; je vais voir. @@
</div>
<div id="8" style="display:none"> 
   @@color:green;
Tu me tiens au courant ? @@
<div id="9" style="display:none">
@@color:black; 
- Ouais, ouais, j'ai ton mail. Je vais voir, merci et Ciao.@@
</div>
<div id="10" style="display:none">
  @@color:black; 
Tu as maintenant une décision à prendre : soit tu vas voir [[Camille|choix du genre]], soit tu décides de prendre un peu de temps pour revoir l'ensemble de ton travail et [[identifier les points les plus problématiques|révision]] @@
</div>
```

<video src="fichier.mp4" width="640" height="480" autoplay></video>

# Twine audio

```
→ Given the following (best done in the StoryInit special passage)
<<cacheaudio "bgm_space" "media/audio/space_quest.mp3" "media/audio/space_quest.ogg">>

→ Start playback
<<audio "bgm_space" play>>

→ Start playback at 50% volume
<<audio "bgm_space" volume 0.5 play>>

→ Start playback at 120 seconds in
<<audio "bgm_space" time 120 play>>

→ Start repeating playback
<<audio "bgm_space" loop play>>

→ Start playback and fade from 0% to 100% volume
<<audio "bgm_space" volume 0 fadein>>

→ Start playback and fade from 75% to 0% volume
<<audio "bgm_space" volume 0.75 fadeout>>

→ Start playback and fade from 25% to 75% volume
<<audio "bgm_space" volume 0.25 fadeto 0.75>>

→ Start playback and fade from 25% to 75% volume over 30 seconds
<<audio "bgm_space" volume 0.25 fadeoverto 30 0.75>>

→ Start playback and goto the "Peace Moon" passage upon ending normally
<<audio "bgm_space" play goto "Peace Moon">>

→ Pause playback
<<audio "bgm_space" pause>>

→ Stop playback
<<audio "bgm_space" stop>>

→ Mute playback, without changing the current playback state
<<audio "bgm_space" mute>>

→ Unmute playback, without changing the current playback state
<<audio "bgm_space" unmute>>

→ Change the volume to 40%, without changing the current playback state
<<audio "bgm_space" volume 0.40>>

→ Seek to 90 seconds in, without changing the current playback state
<<audio "bgm_space" time 90>>
```

# Tester des passages de Twine

pour tester dans le navigateur, ouvrir la console (F12)

réponse obtenue sur le Discord de Twine : 

>The next release is going to include a navigation input in the debug bar. For now, you can always open the developer tools, go to the console, and then run `SugarCube.Engine.play("passage name")`. To get to the console:

- In most browsers you can press F12 then switch to the Console tab if you're not already on it.
- In Chromium-based browsers CTRL+SHIFT+J opens the developer tools straight to the console.
- In Firefox browsers CTRL+SHIFT+K opens the developer tools straight to the console.

# bibliographie


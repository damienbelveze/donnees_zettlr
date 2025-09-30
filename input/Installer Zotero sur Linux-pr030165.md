---
title: installer Zotero sur Debian
subtitle: 
id: 20240718_installer Zotero sur Debian
author: Damien Belvèze
date: 2024-07-18
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - zotero
---



Les notes qui suivent peuvent être utiles pour télécharger Zotero sur différentes distributions de Linux et sur les chromebooks sur lesquels l'utilisateurice a activé au préalable le sous-système Linux[¹].

J'ai rédigé ces notes à partir de mon expérience avec Debian 12 (1 install en juillet 2024) et Ubuntu 24 (1 install en octobre 2024 et 1 en janvier 2025)
Je les ai rédigées sans omettre d'étape (j'espère) et en commentant autant que nécessaire afin que la chose soit faisable pour une personne qui ne manie pas de terminal et n'ait aucune expérience avec les ordis qui fonctionnent sous Linux.

On trouvera en annexe de ces notes le fonctionnement de base d'un terminal pour GNU/Linux (assez similaire avec l'invite de commandes de Windows)

Pour installer Zotero sur une distribution GNU/Linux et sur Debian en particulier, on peut suivre les [indications diffusées sur le forum de Zotero](https://www.zotero.org/support/installation) :

Toutefois cette page du forum proposait (le 18 juillet 2024 dernier lorsque j'ai réalisé une installation) de télécharger un exécutable de Zotero .deb depuis [un repository](https://github.com/retorquere/zotero-deb)
Je ne suis pas parvenu à télécharger ce package (message d'erreur m'indiquant que le paquet .deb n'était pas dispo à cet endroit)
J'ai donc suivi la première alternative qui proposait de télécharger l'archive depuis la page de téléchargement de Zotero.

# Téléchargement depuis un gestionnaire de paquets

Il est possible de télécharger Zotero depuis synaptic (snap) et aptitude (apt), mais j'ai parfois rencontré des problèmes sur les versions téléchargées avec ces gestionnaires. Je préfère donc télécharger les versions depuis le site de Zotero. 
Par ailleurs, comme l'a montré Marceau, Synaptic n'est pas capable de délivrer un paquet récent (compatible ARM) pour les utilisateurs de Chromebooks

# Télécharger Zotero depuis le site officiel

Lorsqu'on utilise un ordi qui fonctionne sous GNU/Linux pour accéder au site de Zotero, c'est une archive tar.bz2 qu'il nous est proposée de télécharger

[D'après Dan Stillman](https://forums.zotero.org/discussion/114768/available-for-beta-testing-zotero-for-windows-on-arm, l'un des développeurs de Zotero, cette version 7 a été conçue pour des ordis ayant une architecture ARM (comme les chromebooks entre autres, mais aussi certains ordis qui habituellement fonctionnent avec Windows). C'est celle que j'installe sur mes ordis pro et perso qui ont une architecture AMD. Donc je pense que ce paquet peut convenir à toutes les installations qui utilisent Linux comme système principal, sous-système ou sous la forme de machine virtuelle. Cela-dit, je n'ai pas encore eu l'occasion de l'essayer sur un chromebook. 

Le mode d'installation suivant devrait donc convenir autant aux chromebooks (dès lors que le sous-système est activé) qu'aux autres ordis 

## Etape 1 : télécharger l'archive

aller sur https://zotero.org/download
Le site affichera le package correspondant au système d'exploitation. 
En l'occurrence, ce qu'on va télécharger en cliquant sur le bouton est le package Zotero-6.0.35_linux-x86_64.tar.bz2
Cette archive est désormais présente dans le dossier Téléchargements

## Etape 2 : extraire l'archive dans le dossier opt

Il est possible de charger l'archive Zotero ailleurs, mais mieux vaut ne pas le laisser dans Téléchargements (fichiers transitoires). La documentation propose d'installer Zotero dans le dossier opt/, j'ai choisi de la suivre sur ce point.

Pour accéder au dossier opt/, il peut être nécessaire d'avoir les droits d'administration sur sa machine (pour les connaisseurs, être un *sudoer*). Si une commande ne fonctionne pas à cause d'un problème de droit, ajouter devant cette commande *sudo* ce qui va permettre à l'utilisateur de s'identifier avec ses droits d'admin et passer à un niveau de droits plus élevé.

on ouvre le terminal (avec les touches Ctrl+Alt+T, voir Annexes)
on va se localiser au niveau du dossier *Téléchargements* (avec la commande *cd*)

```bash
cd ~/Téléchargements
```
Le ~ évite d'écrire Home/Téléchargements.

Si besoin, à la place de ~/Téléchargements utiliser le nom du dossier de téléchargement tel qu'il se présente sur l'ordinateur de la personne (par exemple ~/Downloads).

Attention les majuscules et les minuscules comptent dans les noms de fichiers : si vous écrivez ~/**t**éléchargements, vous ne pourrez pas accéder à ce répertoire.

pour afficher le contenu d'un répertoire, on utilise la commande *ls* (juste entrer ls dans le terminal)

on devrait ainsi voir s'afficher dans le terminal l'archive téléchargée : Zotero-6.0.35_linux-x86_64.tar.bz2

On va envoyer ce fichier vers le répertoire *opt* avec la commande "move" (*mv*) : 

```shell
mv Zotero-6.0.35_linux-x86_64.tar.bz2 /opt/
```
On va aller se placer cette fois au niveau du dossier opt

Je ne suis pas très doué pour naviguer dans l'arborescence de Linux. Voici comment je procède pour accéder au dossier opt : 
```shell
cd --
```
me ramène à l'accueil
Pour remonter plus haut dans l'arborescence, j'utilise la commande cd suivie de deux points : 
```shell
cd ..
```
me permet d'accéder au Home
un autre 
```shell
cd ..
```
me permet d'accéder au niveau racine où on va afficher les dossiers disponibles avec ls. 
Pour se positionner dans opt, taper *cd opt*
En cas de souci, réessayer avec : 
```shell
cd /opt/
```
Refaire *ls* pour voir les dossiers disponibles. Notre archive devrait s'y trouver. 

On va extraire l'archive avec la commande suivante : 
```shell
tar -xf Zotero-6.0.9_linux-x86_64.tar.bz2
```
On obtient un dossier de plus à ce niveau : Zotero-6.0.9_linux-86_64

S'il y a une erreur dans le processus de décompression, c'est peut-être à cause d'une dépendance manquante [^1]

Comme on va devoir insérer ce nom dans un fichier, j'ai tendance à renommer ce fichier pour qu'il soit plus court à entrer avec la commande mv :

```shell
mv Zotero-6.0.9_linux-x86_64 Zotero_linux
```
le fichier Zotero_linux n'existant pas dans ce répertoire, le fichier issu de l'archive sera renommé Zotero_linux.

On n'est pas obligé de renommer ce package, mais ça me paraît plus simple. Attention, ce renommage aura des conséquences sur la manière dont les chemins seront définis dans le lien symbolique (voir ci-dessous)

placez-vous à l'intérieur du dossier Zotero_linux (*cd Zotero_linux*), puis affichez la liste des sous-dossiers et fichiers de l'application (*ls*) 

# faire entrer Zotero dans le lanceur d'application

A ce stade, on peut déjà lancer Zotero en exécutant la commande : 

```shell
./zotero
```
"./" est utilisé dans un terminal pour exécuter un script. 

On ne va pas en rester là parce que c'est très frustrant de devoir exécuter Zotero depuis cet endroit seulement. 
Donc il reste à faire deux choses : 
- indiquer au lanceur où se trouve l'icone Zotero  
- Faire un lien depuis cet endroit où se trouve le fichier de lancement zotero.desktop vers l'endroit où sont listées les applications qui s'affichent dans le lanceur. On appelle cela faire un lien symbolique (dans la doc du forum Zotero, c'est le verbe *symlink* utilisé pour les personnes averties)  

1. indiquer au lanceur où se trouve l'icone Zotero

exécuter le script set_launcher_icon [²] : 

```shell
./set_launcher_icon
```
Rien ne se passe en apparence. S'il n'y a pas de message d'erreur, c'est bon.

2. Faire le lien symbolique. 

L'emplacement des raccourcis dans le lanceur est le suivant : 
~/.local/share/applications/

la commande à faire est donc la suivante : 

```shell
ln -s /opt/Zotero_linux/zotero.desktop ~/.local/share/applications/zotero.desktop
```
ou bien pour Ubuntu 24 : 

```shell
ln -s /opt/Zotero_linux/zotero.desktop /usr/share/applications/zotero.desktop
```

Là encore rien n'est censé se passer au niveau du terminal. 
Par contre, quand vous allez dans le menu des applications, à partir de maintenant, vous devriez voir apparaître Zotero dans la liste des applications disponibles. Si l'icone n'apparaît pas, redémarrez, elle devrait apparaître une fois l'ordi redémarré.
Si ça n'apparaît toujours pas, c'est parce que le lien vers l'icone Zotero a été perdue dans la création du fichier zotero.desktop (voir [^4] et annexe2)


# Mise à jour de Zotero sous Linux

testé avec Ubuntu 24 : 

Vérifier que Zotero est bien sous /opt/ (et pas ailleurs)

donner accès en écriture aux fichiers de configuration : 

```bash
sudo chmod -R a+rwx /usr/bin/zotero && sudo chmod -R a+rwx /opt/zotero
```

Ouvrir Zotero, dans Aide > vérifier les mises à jour. Charger les mises à jour. 

# Annexe 1 : fonctionnement d'un terminal sur Linux

Un terminal sur Linux, Mac ou Windows permet de passer des commandes directement sans utiliser d'interface graphique. Lorsque aucun store n'a été chargé sur un ordi Linux ou bien lorsque le store ne comporte pas l'application souhaitée, il est nécessaire d'utiliser ce terminal à un moment ou à un autre pour installer le logiciel après l'avoir téléchargé. 

**ouvrir le terminal**
Pour ouvrir le terminal, appuyer en même temps sur Ctrl+Alt+T

Pour avoir dans le menu contextuel (clic droit) l'option "ouvrir un terminal ici" (Open Terminal Here), il va être nécessaire de le paramétrer avec Nautilus. Pour Ubuntu 24, suivre les [instructions du manuel](https://ubuntuhandbook.org/index.php/2023/05/open-terminal-other-emulator-ubuntu/) utilisateur d'Ubuntu


**la touche tab**
Pour aller plus vite en saisissant les noms de fichiers, vous pouvez utiliser la touche Tab. Par exemple si le fichier que vous mentionnez dans la commande est Zotero_linux-x86_64 et s'il y a un autre fichier au même niveau qui s'appelle Zotero_translators (admettons), il suffit d'écrire Zotero_l + Tab pour que le nom du premier fichier apparaisse en entier. 

**Copier, coller**
Ctrl+C ne suffira pas : appuyer simultanément sur Maj+Ctrl+C. Idem pour Ctrl+V qui devient Maj+Ctrl+V
Sur Mac remplacer la touche Ctrl par la touche "command".

**afficher rapidement les commandes antérieures**
Sur n'importe quel terminal de n'importe quel système d'exploitation, pour retrouver une ligne de commande déjà passée (ce qui évite de l'écrire), remonter dans l'historique des commandes avec la touche "flèche vers le haut".

## Annexe 2 : zotero.desktop

```text
[Desktop Entry]
Name=Zotero
Exec=bash -c "$(dirname $(realpath $(echo %k | sed -e 's/^file:\\/\\///')))/zotero -url %U"
Icon=/opt/zotero_linux/icons/icon128.png
Type=Application
Terminal=false
Categories=Office;
MimeType=text/plain;x-scheme-handler/zotero;application/x-research-info-systems;text/x-research-info-systems;text/ris;application/x-endnote-refer;application/x-inst-for-Scientific-info;application/mods+xml;application/rdf+xml;application/x-bibtex;text/x-bibtex;application/marc;application/vnd.citationstyles.style+xml
X-GNOME-SingleWindow=true
```

Si l'icone n'apparaît pas dans le lanceur, c'est que le chemin attribué à icon n'est pas le bon. Vérifier que le chemin indiqué mène bien à l'icone.

---
[¹]: Voir ici pour savoir comment activer le sous-système Linux sur un chromebook : https://support.google.com/chromebook/answer/9145439?hl=en
[2]: par exemple bzip2 n'est pas installé, dans ce cas, la commande tar ne va pas fonctionner. Vérifier que c'est bzip2 qui a été utilisé pour compresser l'archive ( $ file zotero...tar.bz2), vérifier que bzip2 est bien installé ($ bzip2 --version), si ce n'est pas le cas, installer bzip2 ($ sudo apt install bzip2), mettre à jour les paquets ($ sudo apt update) et recommencer la décompression avec $ tar -xf zotero...tar.bz2

[3]: au besoin le faire en tant qu'administrateur s'il y a un message du type "zotero.desktop is not writable"

[^4]: Vérifier dans ce cas le chemin vers l'icone dans zotero.desktop (voir Annexe2 du présent document)




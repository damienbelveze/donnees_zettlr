---
title: stéganographie pour Marin
subtitle: l'art de dissimuler un texte dans une image
author: Damien Belvèze
date: 2025-07-01
---


Marin,  

On va faire aujourd'hui un peu de stéganographie.  

La stéganographie, c'est l'art de cacher un message dans une image.  

C'est un procédé qui  existe depuis l'antiquité mais qui est d'autant plus facile aujourd'hui que le numérique permet de faire complètement disparaître derrière l'image.  

# 1. utiliser steghide

Pour faire de la stéganographie avec Linux on peut utiliser le logiciel steghide.  

Vérifie si steghide n'est pas déjà installé sur ta machine en faisant :  
```shell
 steghide --version  
```

  Si tu as un message du genre "*La commande « steghide » n'a pas été trouvée, mais peut être installée avec :  sudo apt install steghide*" c'est que le logiciel n'est pas installé.  

Si tu as un numéro de version, c'est qu'il est installé et que je n'ai pas eu le temps de l'enlever de l'ordi.  

S'il n'est pas installé, tu peux l'installer de la manière suivante :

D'après il faut mettre à jours les paquets déjà installés depuis le répertoire APT (c'est une bonne pratique à conserver avant de charger de nouveaux paquets de APT pour être sûr d'avoir les dernières versions des paquets qu'on souhaite et pas d'anciennes versions)

```shell
sudo apt update
```

Une fois cela fait, on peut installer steghide depuis APT : 

```shell
sudo apt install steghide
```
Taper O(Oui) pour accepter le chargement

Les commandes de base sont : 

- **`embed`**: demande à steghide de dissimuler des données
- **`-cf couverture.jpg`**: indique l'image qui servira de couverture.
- **`-ef texte_a_cacher.txt`**: pointe vers le fichier qui contient les données à cacher

exemple de commande : 

```shell
steghide embed -cf couverture.jpg -ef texte_a_cacher.txt
```

Steghide demande la création d'un mot de passe ou d'une phrase de passe. 

Pour extraire les données cachées dans une image on dispose d'autres commandes : 

```shell
steghide extract -sf image.jpg
```

Cela extrait le texte de l'image (si on a le mot de passe)

# 2. Exercice

## Exercice 1 : réception d'un texte chiffré dans une image

Retrouve le texte caché dans l'image que je t'envoie :

(tu trouveras l'image en copie jointe à ce mail)

Tu trouveras le mot de passe pour ouvrir l'image dans le lien qui suit : 

## Texte 2 : envoi d'un texte chiffré dans une image

sélectionne une image du jour sur le site d'images en licence libre de Wikimédia Commons : https://commons.wikimedia.org/wiki/Commons:Picture_of_the_day

Charge-la sur ton bureau

Ecris un texte dans un fichier en .txt

utilise steghide pour cacher le contenu du fichier .txt dans l'image. 

Envoie-moi le mot de passe ou la phrase de passe au moyen du service en ligne quick forget : 

https://quickforget.com/

Quickforget est très utile car on ne doit jamais envoyer via une messagerie des mots de passe non périssables ; il faut partir du principe que tôt ou tard ta messagerie sera piratée et prévoir le coup. 

l'attaquant va taper "mot de passe" dans ta messagerie pour récupérer ce qu'il peut récupérer. Si tes mots de passe échangés le sont au moyen de liens périmés comme ceux de QuickForget, tu limites la casse car l'attaquant ne peut pas récupérer de mot de passe en sondant ta messagerie. 

envoie moi le tout (lien dans le message + image en fichier joint) à ma messagerie damien.belveze@telemak.fr

N'hésite pas à m'envoyer des messages sur mattermost si tu es bloqué. 





---
title: sauvegarde de données
subtitle: 
id: 20240409_sauvegarde de données
author: Damien Belvèze
date: 2024-04-09
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - back up
  - backup
tags:
  - données_recherche
---
à distinguer de l'[[archivage]]

> Yesterday,  
   All those backups seemed a waste of pay.  
   Now my database has gone away.   
Oh I believe in yesterday. 
>Suddenly,  
There's not half the files there used to be,  
 And there's a milestone  
 hanging over me  
 The system crashed so suddenly.
 I pushed something wrong  
 What it was I could not say.
>Now all my data's gone  
 and I long for yesterday-ay-ay-ay.
 Yesterday,  
 The need for back-ups seemed so far away.  
 I knew my data was all here to stay,  
 Now I believe in yesterday.

(source : https://literatur.social/@fiee/113764124413099652)

![](images/data_hygiene.png)

(extraits de [[@kjorveziroskiTechnicalSkillsAre2025]])

faire attention à la perte de données due a l'obsolescence des disques durs par rapport aux évolutions des lecteurs installés sur les ordinateurs. 

ne pas tout confier au Cloud : 
![](images/whole_cloud_back_up_strategy.png)
stockage local + cloud : 

les sauvegardes sur le cloud ne sont pas entièrement sûres, la dépendance à un tiers est trop grande si en parallèle d'autres sauvegardes ne sont pas faites sur des outils dont on dispose. 

voir suppression "sauvage" de fichiers par AWS ([[@boudihAWSDeletedMy2025]])

![](images/best_storing_option.png)
mettre en place un système de synchronisation avec les disques durs. 
![](images/storage_location_hybrid.png)
de la sauvegarde de documents mais pas de sauvegarde de l'histoire de leurs modifications (tout changement est immédiatement appliqué à la copie en ligne : "sync is not a backup")

Meilleure méthode : 3/2/1 : 

![](images/3_2_1_storage_method.png)
github is not enough as a cloud service : 

![](images/github_is_not_enough.png)
github : les terms of service peuvent changer à votre désavantage. 
pas de solution universelle pour gérer l'automatisation des synchronisations, en trouver une qui va avec son système d'exploitation. 


# syncing is not backup

si on synchronise des fichiers et qu'un fichier est corrompu, tous les fichiers équivalents sur les autres ordinateurs seront corrompus et il n'y aura pas de possibilité de revenir à un état antérieur du fichier, c'est la raison pour laquelle on dit couramment que la synchronisation de fichiers n'est pas équivalente à la sauvegarde. 

## sauvegardes avec borg

Borg, (borg backup) est un outil de sauvegarde de fichiers qui intègre la déduplication, la compression et le chiffrement. Outil disponible pour Linux, FreeBSD et MacOS

- **déduplication** : l'outil ne sauvegarde pas plusieurs fois un même fichier, mais plusieurs états différents d'un fichier (voir [[déduplication]])
- **compression** : au moment de la sauvegarde, il est possible de choisir un algorithme de compression pour réduire la taille des fichiers sauvegardés
- **chiffrement** : il est possible de chiffrer les documents sauvegardés si ces documents peuvent 

installation : 

```shell
sudo apt update
sudo apt install borgbackup
```

Initialiser un répertoire de sauvegarde 
(supposons que le dossier de destination de la sauvegarde soit sur une clé USB appelée USB DISK)
Nous allons appeler ce dossier borg_backup

```shell
borg init -e none /media/dbelveze/'USB DISK'/borg_backup
# si on veut chiffrer, remplacer none par l'algo de chiffrement (par exemple repokey)
```

créer la sauvegarde : 

```shell
borg create /media/dbelveze/'USB DISK'/borg_backup::20250821 ~/'Bibliothèque Calibre'
# les deux arguments de borg create sont le dossier destination de l'archive et le chemin du dossier à archiver

# pour compresser et avoir des stats, rajouter --stats et -C suivi d'une méthode et d'un niveau de compression, par exemple : zstd,10
```

Il peut être plus simple de se situer au niveau du dossier qu'on veut sauvegarder et ensuite d'ajouter un . (répertoire courant) dans la commande : 

![](images/borg_1.png)

possibilité d'exclure des types de fichiers : 
```shell
borg create --stats -C zstd,10 --exclude '*.pdf' /media/dbelveze/'USB DISK'/borg_backup::20250821-2 .
# la sauvegarde exclut tous les pdf
```

Lister les sauvegardes faites : 

```shell
borg list /media/dbelveze/'USB DISK'/borg_backup
```

récupérer les données sauvegardées

borg extract /media/dbelveze/'USB DISK'/borg_backup::20250821-2  

On récupère la deuxième sauvegarde qui a été faite le 21 août 2025

(source : https://youtu.be/q_OdTOuvP4A?feature=shared)


# synchronisation des sauvegardes

entre plusieurs serveurs : 
- FreeFileSync : https://freefilesync.org/ , usage d'un script (https://freefilesync.org/manual.php?topic=schedule-batch-jobs#windows)
- SyncBackFree (https://www.2brightsparks.com/download-syncbackfree.html)

# sauvegarde de pages web

sauvegarder le contenu d'une page web dans un seul fichier : https://addons.mozilla.org/fr/firefox/addon/single-file/
(incluant la [[CSS]] et tous les autres fichiers), voir https://framapiaf.org/@sebsauvage/114693586773902448



$\newline$
# bibliographie
$\newline$







---
title: synchroniser
subtitle:
id: 20250331_synchroniser
author: Damien Belvèze
date: 2025-03-31
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - synchronization
  - synchronisation
tags:
  - programmation
  - sauvegarde
---
synchroniser des fichiers consiste à avoir exactement les mêmes fichiers dans deux emplacements distants. 
Il ne s'agit pas exactement d'une copie. Lorsqu'on copie un répertoire dans un autre, on remplace également dans le dossier de destination les fichiers qui ont été inchangés, ce qui, avec de longs fichiers, peut s'avérer coûteux en temps et en ressource, tandis que la synchronisation n'ajoute que le delta entre le dossier source et le dossier destination. 

> Divers outils de sauvegarde des données sont couramment utilisés dans les environnements informatiques, tels que BackupPC [51], Cobian Backup [52], Bacula [53], et rdiff-backup [54]. Parmi eux, Rsnapshot, basé sur rsync, permet également de réaliser des sauvegardes incrémentielles efficaces sur les systèmes Linux/UNIX.

([[@lebonGuideBonnesPratiques2025]])

# synchroniser avec rsync

de base dans Ubuntu 24

```shell
rsync -av /chemin/dossier/source /chemin/dossier/destination
```

## synchroniser des fichiers quand on monte un disque dur ou une clé USB

supposons un dossier sur le bureau 

vérification du nom (label) de la clé USB et de son point de montage : 

```shell
lsblk
```

ici il s'agit d'une clé USB qui a pour label PHILIPS UFD et point de montage /media/dbelveze/PHILIPS UFD dans sda1

- écrire un nouveau fichier dans systemd (usb-sync.service)
```shell
[Unit]
Description=Sync my_ideas folder to USB Philips
Requires=media-usb.mount
After=media-usb.mount

[Service]
Type=oneshot
ExecStart=/usr/bin/rsync -av --delete /home/dbelveze/Bureau/my_ideas/ '/media/dbelveze/PHILIPS UFD/my_ideas/'
ExecStart=/usr/bin/notify-send "USB Sync" "Synchronization completed"
User=dbelveze
Group=dbelveze

[Install]
WantedBy=media-sub.mount
```


- Ecrire un nouveau fichier dans udev (99-usb-sync.rules) (/etc/udev/rules.d/99-usb-sync.rules)
```bash
ACTION=="add", KERNEL=="sda1", ENV{ID_FS_LABEL}=="PHILIPS UFD", RUN+="/bin/systemctl start usb-sync.service"
```

remettre à jour les règles de démarrage : 

```shell
sudo systemctl daemon-reload
sudo udevadm control --reload-rules
```


# synchroniser avec FreeFileSync

FreeFileSync : https://freefilesync.org/ , usage d'un script (https://freefilesync.org/manual.php?topic=schedule-batch-jobs#windows)

# synchroniser avec Rsnapshot

[Rsnapshot](https://rsnapshot.org/) basé sur Rsync



$\newline$
# bibliographie
$\newline$







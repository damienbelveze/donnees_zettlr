---
title: Mattermost
subtitle:
id: 20250623_Mattermost
author: Damien Belvèze
date: 2025-06-23
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: []
---

# Installer Mattermost

```shell
curl -fsS -o- https://deb.packages.mattermost.com/setup-repo.sh | sudo bash
sudo apt install mattermost-desktop
sudo apt upgrade mattermost-desktop
```

installer la bonne version qui va bien avec les versions chargées sur le serveur avec lequel on veut discuter (pas forcément la dernière) : 

https://github.com/mattermost/desktop/releases?page=2

Pour bloquer les mises à jour du client si le serveur continue d'exiger une version ancienne, on peut bloquer la version de ce paquet, comme de n'importe quel autre en suivant cette méthode : 

```shell
sudo apt-mark hold mattermost-desktop
```

## Installer une version ancienne de Mattermost

Télécharger le package en tar.gz
décompresser dans les téléchargements et envoyer les fichiers dans /opt/
```shell
tar -xvf mattermost-desktop...tar.gz
sudo mv ~/Téléchargements/mattermost-desktop... /opt/mattermost/ 
```
on peut d'ores et déjà exécuter le client en cliquant sur mattermost.desktop qui est un binaire

Pour faire entrer mattermost dans le lanceur d'applications. 

aller dans usr/share/applications
écrire un fichier : 
```shell
sudo cat > markdown-desktop.desktop

[Desktop Entry]
Name=Mattermost
Exec=/opt/mattermost/mattermost-desktop %U
Terminal=false
Type=Application
Icon=mattermost-desktop
StartupWMClass=Mattermost
Comment=Mattermost
MimeType=x-scheme-handler/mattermost;
Categories=Network;InstantMessaging;
``` 

Vérifier les chemins (attention aux majuscules aux noms de dossiers)
Si l'application apparaît dans le lanceur mais que le logiciel n'est pas exécuté, 
vérifier qu'on peut exécuter directement l'application depuis le terminal : 

```shell
/opt/mattermost/mattermost-desktop
```
si on a ce genre de résultat : 

>[14875:0903/140057.093201:FATAL:setuid_sandbox_host.cc(163)] The SUID sandbox helper binary was found, but is not configured correctly. Rather than run without sandboxing I'm aborting now. You need to make sure that /opt/mattermost/chrome-sandbox is owned by root and has mode 4755. Trappe pour point d'arrêt et de trace (core dumped)

cela veut dire qu'on n'a pas la propriété sur une partie du programme (chrome sandbox), il faut revendiquer en tant que superutilisateur cette propriété : 

```shell
sudo chown root:root /opt/mattermost/chrome-sandbox
sudo chmod 4755 /opt/mattermost/chrome-sandbox
```

réessayer d'exécuter via le terminal puis tester à nouveau le lanceur. 



# Désinstaller Mattermost

https://webhostinggeeks.com/howto/how-to-uninstall-mattermost-on-ubuntu/



$\newline$
# bibliographie
$\newline$







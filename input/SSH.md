---
title: SSH
date: 2023-12-29
tags:
  - cryptographie
---


(**secure shell Protocol**) tunnel sécurisé de communication entre une machine client et un serveur. 
une connexion en ssh à un serveur depuis un terminal permet d'envoyer et de recevoir des données sans compromettre l'intégrité, la confidentialité et l'authenticité de ces échanges. 
Le ssh repose sur du [[Chiffrement asymétrique]] (double jeu de clé)

possibilité d'utiliser SSH pour connecter deux machines clientes (grâce à Remmina pour Linux [[@veronicaexplainsConnectRemotePCs2021]])


# Se créer une clé ssh

``
$ ssh-keygen
``

demande un password et crée le jeu de clé

va créer une clé [[RSA]] 3072 bits dans le répertoire ~/.ssh 

  - ~/.ssh/id_rsa  
  - ~/.ssh/id_rsa.pub
  - .ssh/config

ssh est un dossier caché, pour l'afficher Ctrl+H

envoyer la clé publique sur la page de l'hébergeur qui gère le serveur. 

à partir de ce moment on peut se connecter en ssh : 

login : nomduserveur@ipduserveur
mot de passe : password

On peut rajouter une ligne dans /etc/hosts pour donner un nom au serveur

| IP du serveur | nom du serveur |

de sorte qu'à l'avenir on n'aurai qu'à s'identifier en tapant : 

ssh nom du serveur + password

# se créer une clé SSH pour son ordinateur avec Windows

![](images/ssh_key.png)

Source :  https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

Ajouter la clé à Github :  https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

# réinstaller la clé sur un PC

## GNU/Linux

Ubuntu : Ctrl+H pour afficher les fichiers cachés > sous .ssh, charger les clés privées, publics et les hôtes reconnus (par exemple : id_ed25519.asc / id_ed25519.pub et know_host)

## Windows

créer un dossier C:/user/.ssh
y télécharger la clé publique et la clé privée
(par exemple : id_ed25519 et id_ed25519.pub)
y créer un fichier config : 

```bash
# Read more about SSH config files: https://linux.die.net/man/5/ssh_config
Host remote_ssh
    HostName github.com
    User git
    IdentityFile C:/Users/dbelveze/.ssh/id_ed25519
```
la clé publique doit avoir été chargée dans Github préalablement

Si le système n'arrive pas à utiliser la clé nouvellement installée dans l'agent, entrer la commande suivante : 

```shell
ssh -vT git@github.com
```
Cela permettra d'activer la clé en l'authentificant
(source : https://stackoverflow.com/questions/57734669/gitgithub-com-permission-denied-publickey)

# utiliser SSH pour se connecter à Git

intérêt d'une connexion en SSH à [[git]] plutôt que d'une connexion https

- vous n'exposez pas de mot de passe (sur le serveur d'un tiers), puisque vous utilisez une clé privée hébergée par votre ordinateur en lien avec la clé publique qui est sur le serveur. Vous avez seulement besoin d'une phrase de passe pour activer votre clé privée.
- une clé privée est plus longue et moins trouvable, même avec la force brute qu'un mot de passe

utiliser SSH pour se connecter à un repository [[Github]] ou [[Gitlab]]
passer d'un mode d'authentification par mot de passe / token à un mode d'authenfication SSH : 

```bash 
git remote rm origin    
git remote add origin git@personal:username/repository.git
```

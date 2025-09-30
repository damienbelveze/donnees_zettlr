---
title: Raspberry Pi
subtitle:
author: Damien Belvèze
date: 15-01-2022
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: []
tags: [programmation]
---


# Kit (achat décembre 2020)

![[cout_raspberrypi4.pdf]]

# configuration
fichier config 

``````
gpu_mem=16
start_file=recovery.elf
fixup_file=fixup_rc.dat

hdmi_drive=2

[pi4]
start_file=recover4.elf
fixup_file=fixup4rc.dat
``````

config plus avancée : 

```txt
# For more options and information see
# http://rpf.io/configtxt
# Some settings may impact device functionality. See link above for details

# uncomment if you get no picture on HDMI for a default "safe" mode
#hdmi_safe=1

# uncomment this if your display has a black border of unused pixels visible
# and your display can output without overscan
#disable_overscan=1

# uncomment the following to adjust overscan. Use positive numbers if console
# goes off screen, and negative if there is too much border
#overscan_left=16
#overscan_right=16
#overscan_top=16
#overscan_bottom=16

# uncomment to force a console size. By default it will be display's size minus
# overscan.
#framebuffer_width=1280
#framebuffer_height=720

# uncomment if hdmi display is not detected and composite is being output
#hdmi_force_hotplug=1

# uncomment to force a specific HDMI mode (this will force VGA)
#hdmi_group=1
#hdmi_mode=1

# uncomment to force a HDMI mode rather than DVI. This can make audio work in
# DMT (computer monitor) modes
#hdmi_drive=2

# uncomment to increase signal to HDMI, if you have interference, blanking, or
# no display
#config_hdmi_boost=4

# uncomment for composite PAL
#sdtv_mode=2

#uncomment to overclock the arm. 700 MHz is the default.
#arm_freq=800

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Uncomment this to enable infrared communication.
#dtoverlay=gpio-ir,gpio_pin=17
#dtoverlay=gpio-ir-tx,gpio_pin=18

# Additional overlays and parameters are documented /boot/overlays/README

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

[pi4]
# Enable DRM VC4 V3D driver on top of the dispmanx display stack
dtoverlay=vc4-fkms-v3d
max_framebuffers=2

[all]
#dtoverlay=vc4-fkms-v3d

# NOOBS Auto-generated Settings:
```



# accès SSH

Sur le raspberry pi, valider la connexion par SSH 
(préférences > configuration du Rpi > Interfaces > SSH : activé)
dans Pi créer un fichier ssh vide (ssh.txt puis enlever txt)

Aller dans le terminal de la machine distante (sur Windows, utiliser Putty pour se connecter au Rpi)
Dans Putty entrer l'IP du Rpi (consulter IP sur l'administration du routeur)
Dans un terminal Linux : ssh pi@IP
``````
ssh pi@IP

``````
(laisser port 22)
IP : 192.168.1.11

utilisateur : pi
mot de passe :  si laissé par défaut : raspberry

Supprimer l'accès SSH en root en suivant la [procédure suivante](https://www.howtogeek.com/768053/how-to-ssh-into-your-raspberry-pi/) : 
``````
sudo raspi config
``````
sélectionner : 
3. Interface options : configure connections to peripherals
P2 SHH

éditer le fichier config du ssh avec nano (en mode administrateur)

``````
sudo nano /etc/ssh/sshd_config
``````

sous 
``````
#PermitRootLogin prohibit-password
``````
(qu'on laisse en commentaire), ajouter 
``````
PermitRootLogin no
``````

enregistrer et quitter nano

# mémoire

pour mesure le taux d'utilisation de la carte SD : 

``````
df -h
``````


-h permet d'afficher les valeurs en Gigabytes et Megabytes

# chargement de logiciels

## snap

``````
sudo apt-update
sudo apt install snapd
``````

nécessité de rebooter le Rpi

`````
sudo reboot
``````
 installer Snap

 ``````
 sudo snap install core
 ``````
 Pour installer un logiciel présent dans Snap (Inkscape par exemple)

 ``````
 sudo snap install inkscape
 ``````
 [source](https://snapcraft.io/install/inkscape/raspbian)

On peut charger certains logiciels (par exemple Scratch ou [[LibreOffice]] depuis Préférences > Recommended Software)



# bibliographie


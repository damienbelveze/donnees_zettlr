---
title: chemin (path)
subtitle: 
id: 20231211_chemin (path)
author: Damien Belvèze
date: 2023-12-11
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
---
# Expression du chemin

chemin absolu / chemin relatif
## Chemin dans R
```r
setwd("D:\\Home\\dbelveze\\Desktop")
```
voir [[R (logiciel)|R]]
Pour ne pas avoir à référencer toujours des chemins absolus, utiliser la fonction set work directory : 
```r
setwd("D:\\Home\\dbelveze\\Desktop")
```

# Modifier le PATH dans Windows

Dans la barre de démarrage, entrer SystemPropertiesAdvanced.exe

Enregistrement de mon path le 5/01/2024
(cmd > %userprofile%\Downloads\variables_env.txt)
```tex

ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\dbelveze\AppData\Roaming
ChocolateyInstall=C:\ProgramData\chocolatey
ChocolateyLastPathUpdate=133489428579346410
ChocolateyToolsLocation=C:\tools
citeproc=C:\Users\dbelveze\citeproc
CommonProgramFiles=C:\Program Files\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=PR030165
ComSpec=C:\WINDOWS\system32\cmd.exe
DriverData=C:\Windows\System32\Drivers\DriverData
HOMEDRIVE=C:
HOMEPATH=\Users\dbelveze
JAVA_HOME=C:\Program Files\Eclipse Adoptium\jre-20.0.1.9-hotspot\bin
LOCALAPPDATA=C:\Users\dbelveze\AppData\Local
LOGONSERVER=\\VMPDC03
MOZ_PLUGIN_PATH=C:\Program Files (x86)\Foxit Software\Foxit PDF Editor\plugins\
NUMBER_OF_PROCESSORS=8
OneDrive=D:\Home\dbelveze\OneDrive - Universit� de Rennes 1
OneDriveCommercial=D:\Home\dbelveze\OneDrive - Universit� de Rennes 1
OS=Windows_NT
Path=C:\Program Files\Eclipse Adoptium\jre-20.0.1.9-hotspot\bin;C:\tools\ruby31\bin;C:\Program Files\Python310\Scripts\;C:\Program Files\Python310\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\MiKTeX\miktex\bin\x64\;C:\texlive\2022\bin\win32;C:\Program Files\Pandoc\;C:\Program Files\Git\cmd;C:\Program Files\Calibre2\;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Program Files\PuTTY\;C:\Program Files (x86)\Gpg4win\..\GnuPG\bin;C:\Program Files\dotnet\;C:\Users\dbelveze\AppData\Roaming\local\bin;C:\Users\dbelveze\AppData\Local\Programs\Quarto\bin;C:\Users\dbelveze\AppData\Local\Microsoft\WindowsApps;;C:\Users\dbelveze\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\dbelveze\AppData\Roaming\npm;C:\Users\dbelveze\AppData\Roaming\cabal\bin;C:\tools\ghc-9.8.1\bin;
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW;.RB;.RBW
PROCESSOR_ARCHITECTURE=AMD64
PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 140 Stepping 1, GenuineIntel
PROCESSOR_LEVEL=6
PROCESSOR_REVISION=8c01
ProgramData=C:\ProgramData
ProgramFiles=C:\Program Files
ProgramFiles(x86)=C:\Program Files (x86)
ProgramW6432=C:\Program Files
PROMPT=$P$G
PSModulePath=C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
PUBLIC=C:\Users\Public
RTOOLS42_HOME=C:\rtools42
SESSIONNAME=Console
STACK_ROOT=C:\sr
SystemDrive=C:
SystemRoot=C:\WINDOWS
TEMP=C:\Users\dbelveze\AppData\Local\Temp
TMP=C:\Users\dbelveze\AppData\Local\Temp
UATDATA=C:\WINDOWS\CCM\UATData\D9F8C395-CAB8-491d-B8AC-179A1FE1BE77
USERDNSDOMAIN=UR.LOCAL
USERDOMAIN=UR
USERDOMAIN_ROAMINGPROFILE=UR
USERNAME=dbelveze
USERPROFILE=C:\Users\dbelveze
windir=C:\WINDOWS
ZES_ENABLE_SYSMAN=1
_MSYS2_BASH=C:\tools\msys64\usr\bin\bash.exe
_MSYS2_PREFIX=x86_64
```

ajouter Rstudio dans le PATH : ``C:\Program files\Rstudio``

longueur des paths pour Windows, max 255 caractères (voir [[conventions de nommage]])

ajout d'une variable pour [[Pandoc]] :[https://pp4rs.github.io/2017-uzh-installation-guide/pandoc/#verify-your-install](https://pp4rs.github.io/2017-uzh-installation-guide/pandoc/#verify-your-install)

# ajouter des logiciels dans le PATH de Linux

ajouter pour un profil : .profile dans le Home
ajouter pour le système entier (tous usagers) : etc/profile

ajouter une ligne dans l'un ou l'autre de ces fichiers : 

```shell
sudo export PATH=$PATH:/usr/local/software/bin
# indiquer le chemin vers les fichiers binaires du logiciel (ici on part du principe que le logiciel a été installé dans usr/local/ et qu'il s'appelle software)
```

Pour activer ce chemin, deux solutions : 
1. redémarrer l'ordi
2. faire un ```sudo source(~/.profile)``` ou bien ```sudo source(etc/profile)```
3. Vérifier que le chemin est bien ajouté, ouvrir un terminal dans le Home et taper : 
```shell
software --version
```
si on a la version du logiciel en question, il a correctement été installé, le chemin a bien été ajouté (source : installation de go https://go.dev/doc/install)


# bibliographie
$\newline$







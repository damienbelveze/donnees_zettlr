---
title: VS code et Ollama
subtitle: 
id: 20240607_VS code et Ollama
author: Damien Belvèze
date: 2024-06-07
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
  - python
  - IA
---
Ollama en local + le modèle de langage StarCoder en local fournit une bonne alternative à Copilot, outil payant de Microsoft pour générer du code depuis un éditeur de texte en IA. 

Etapes à suivre :

1. Charger Ollama sur sa machine (depuis https://ollama.com)
2. Faire le lien avec le modèle de langage souhaité
3. charger Starcoder2:3B sur la machine

Pour un ordinateur de bureautique, le [[LLM]] StarCoder 2 3B ("3 milliards de paramètres" ; 1,7 GigaBit) peut être téléchargé et fonctionner sans difficulté en local. 

Ouvrir un terminal de commandes (Powershell pour Windows par exemple)

```bash
ollama pull starcoder2:3B
```
Cela installera Starcoder en local

2. Dans VSCode, installer l'extension *Continue*

3. Choix du modèle

StarCoder2 (léger, en local), Deepseek-coder (lourd, via une API)

Deepseek-coder:33B- = modèle trop large pour être hébergé sur un ordinateur de bureautique : connexion avec un serveur où le modèle est hébergé.

Définir les accès à ces deux modèles dans le fichier de configuration de l'extension Continue (dans VSCode)

Dans VSCode, ouvrir la palette (par défaut Ctrl+Shift+P)

Modifier le fichier config.json de l'extention *Continue* (Continue: open config.json)

ajouter les lignes concernant le modèle choisi. 

Pour Starcoder en local : 

```json
{
      "title": "Starcoder2",
      "provider": "ollama",
      "model": "starcoder2-3b",
      "systemMessage": "You are an expert software developer. You give helpful and concise responses."
    },
```

Pour Deepseek, l'accès doit avoir lieu en API depuis un serveur distant : 

```json
    {
      "title": "Deepseek",
      "provider": "ollama",
      "model": "deepseek-coder:33b",
      "apiBase": "URL du serveur/ollama",
      "requestOptions": {
        "headers": {
          "Authorization": "Basic entrer ici la clé fournie par l'administrateur du serveur"
        }
      }
    },
```

voir également [fichier écrit par Olivier Wong](Continue_deepseek_config.json). Ce fichier doit être chargé dans l'extension Continue pour VSCode (config.json)



A partir du moment où ces deux modèles sont disponibles (par exemple starcoder2 en local et/ou deepSeek via une API), pour appeler l'un ou l'autre, utiliser Ctrl+I (raccourci par défaut de l'extension Continue)

Cela ouvre un champ pour le prompt. Il est possible de passer d'un modèle à l'autre dans l'interface de chat (menu déroulant en bas à droite)

Vérifier avant d'utiliser n'importe quel modèle hébergé sur un serveur qu'on a bien accès au serveur en question  (VPN)

Exemple de prompt : 

```prompt

prompt the user to provide a folder path. Within this folder, in the different files, count all the words beginning with "art", Create a CSV file in the same folder called art.csv. In art.csv  create two columns with the following headers : column A = words, column B = files.  In column A list all occurrences found of words beginning with "art", in column B, provide the name of the files  where these occurrences were found. Occurrences count should be put at the end of the document after a line break
```
Avec Deepseek, VScode répond de la manière suivante : 

```python
import os
import csv
from collections import defaultdict
def get_art_words(filepath):
    art_words = []
    with open(filepath, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.startswith('art'):
                    art_words.append(word)
    return art_words
def main():
    folderpath = input("Please provide a folder path: ")
    result = defaultdict(list)
    for filename in os.listdir(folderpath):
        filepath = os.path.join(folderpath, filename)
        if os.path.isfile(filepath):
            art_words = get_art_words(filepath)
            for word in art_words:
                result[word].append(filename)
    with open(os.path.join(folderpath, 'art.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Words', 'Files'])
        for word, filenames in result.items():
            writer.writerow([word, ', '.join(filenames)])
    with open(os.path.join(folderpath, 'art.csv'), 'a') as f:
        f.write('\nOccurrences count: %s' % sum([len(files) for files in result.values()]))
if __name__ == "__main__":
    main()
```
Exécuter le code Python avec [un jeu de fichiers approprié](https://github.com/damienbelveze/become_more_visible/tree/main/data) (pour l'éditeur de Python en ligne https://www.online-python.com/, indiquer le lien vers l'espace cloud) pour vérifier que le code est bon. 
Ce code ne peut être vérifié avec l'extension code-runner de VScode. En effet, celle-ci ne fonctionnera pas si le code comprend la demande faite à l'usager d'indiquer un chemin. 

voir [[paramétrage d'un système de prompt]]

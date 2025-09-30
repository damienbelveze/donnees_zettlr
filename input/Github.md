---
title: Github
subtitle: 
id: 20240229_Github
author: Damien Belvèze
date: 2024-02-29
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
---
# Github Actions

infrastructure as a service (IaaS). Les opérations de traitement sont exécutées sur un serveur distant. 
Possible de faire fonctionner des workflows distincts en plus du workflow principal qui convertit les documents .md en pages .html
L'usage de github actions suppose l'existence d'un index dans le repo (index.html)

Workflow de conversion d'un document html en document pdf : 

```yaml
name: Pandoc Conversion

on:
  push:
    branches:
      - main # or whichever branch you want to monitor for changes

env:
  GITHUB_USERNAME: damienbelveze
  GITHUB_EMAIL: damien.belveze@univ-rennes.fr

jobs:
  pandoc_conversion:
    runs-on: ubuntu-latest

    steps:
    
    - name: Set user.name and user.email
      run: |
        git config --global user.name "$GITHUB_USERNAME"
        git config --global user.email "$GITHUB_EMAIL"

    - name: Remove existing presentation.pdf file (if it exists)
      run: |
        if [ -e presentation/presentation.pdf ]; then
          git rm presentation/presentation.pdf
          git commit -m "Remove existing presentation.pdf file"
          git push origin ${GITHUB_REF}
        fi

    - name: Checkout repository
      uses: actions/checkout@v2
      with:
        fetch-depth: 0 # Ensure the entire history is fetched, required for fetching submodules

    - name: Install Pandoc and LaTeX packages
      run: |
        sudo apt-get update
        sudo apt-get install -y pandoc texlive-latex-recommended texlive-xetex texlive-luatex

    - name: Convert HTML to PDF
      id: pdf_conversion
      run: |
        pandoc --pdf-engine=xelatex presentation.html -s -o presentation/presentation.pdf

    - name: Upload generated PDF as artifact
      uses: actions/upload-artifact@v2
      with:
        name: presentation_pdf
        path: presentation

    - name: Checkout repository again (to modify the committed files)
      uses: actions/checkout@v2
      with:
        fetch-depth: 0 # Ensure the entire history is fetched, required for fetching submodules

    - name: Download generated PDF artifact
      id: pdf_download
      uses: actions/download-artifact@v2
      with:
        name: presentation_pdf
        path: presentation

    - name: Create and push commit with the generated PDF
      uses: actions/github-script@v5
      with:
        github-token: ${{secrets.GITHUB_TOKEN}}
        script: |
          const fs = require('fs');
          const path = require('path');
          const childProcess = require('child_process');

          // Create a new Git commit with the generated PDF
          const addAndCommit = (repoPath, filePath) => {
            childProcess.execSync(`cd ${repoPath} && git add ${filePath}`);
            childProcess.execSync(`cd ${repoPath} && git commit -m "Automatically generated PDF from Pandoc"`);
          };

          // Push the new Git commit to the remote repository
          const pushChanges = repoPath => {
            childProcess.execSync(`cd ${repoPath} && git push origin ${process.env.GITHUB_REF}`);
          };

          const repoPath = process.env.GITHUB_WORKSPACE;
          const pdfFilePath = path.join(repoPath, 'presentation.pdf');

          if (fs.existsSync(pdfFilePath)) {
            addAndCommit(repoPath, 'presentation.pdf');
            pushChanges(repoPath);
          } else {
            console.log('Error: presentation.pdf not found');
          }
```


# horodatage

discussion sur la réécriture possible dans Github de l'historique des commits (https://infosec.exchange/@todd_a_jacobs/112210906842861618) à la faveur de l'analyse du cas d'usage XZ (modification du [[timestamp]]) pour déguiser une intervention frauduleuse.

# Taille

Les repositories de github peuvent peser au plus 50 MB
Pour connaître la taille d'un repo, interroger avec [[cURL]]
la [[REST API]] de Github

```shell
`curl -L \ -H "Accept: application/vnd.github+json" \ -H "Authorization: Bearer <YOUR-TOKEN>" \ -H "X-GitHub-Api-Version: 2022-11-28" \ https://api.github.com/repos/OWNER/REPO`
```

# Github codespaces

environnements de développement ("[[VS Code|VScode]] en ligne") permettant de faire du code et de le distribuer sous forme de containers de façon plus ou moins [[reproductible]]. Sans activité, les codespaces de github sont supprimés automatiquement. 



$\newline$
# bibliographie
$\newline$







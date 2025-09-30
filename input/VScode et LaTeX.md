---
title: VScode et LaTeX
subtitle: 
id: 20240708_VScode et LaTeX
author: Damien Belvèze
date: 2024-07-08
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
---
L'extension pour VScode *LaTeX workshop* permet de générer du texte en LaTeX et de le compiler (en PDF par exemple) dans l'éditeur VScode

voici un document minimal

```tex
\documentclass[12pt]{article}

\usepackage[utf8]{inputenc}

\usepackage[T1]{fontenc}

\usepackage[english]{babel}

\usepackage{ifpdf,newtxtext,newtxmath}

  

\usepackage{csquotes}

\usepackage[backend=biber, style=ieee]{biblatex}

\addbibresource{biblio.bib}
\title{comment faire fonctionner Zotero avec LaTeX}
\author{Damien Belvèze}
\begin{document}
\maketitle
insérons ici une référence \cite{claveyMastodonRefugePour2023}
\printbibliography
\end{document}
```

Le document biblio.bib

comporte uniquement la référence suivante : 

```tex
@article{claveyMastodonRefugePour2023,

  entrysubtype = {magazine},

  title = {Mastodon Refuge Pour Communiquer Librement Sur La Recherche ?},

  author = {Clavey, Martin},

  date = {2023-03-14},

  journaltitle = {NexInpact},

  url = {https://www.nextinpact.com/article/71227/mastodon-refuge-pour-communiquer-librement-sur-recherche},

  urldate = {2023-08-24},

  file = {C:\Users\dbelveze\Zotero\storage\TIRFEQX8\mastodon-refuge-pour-communiquer-librement-sur-recherche.html}

}
```

En compilant le code, grâce à [[biber]] qui gère les références en biblatex, on obtient bien un PDF avec une biblio correctement formatée. 

[[@besanconSneakedReferencesCooked2023]]

Toutefois, pour rendre cela possible, il convient de modifier les settings de VScode en suivant les indications présentées sur ce [forum](https://tex.stackexchange.com/questions/154751/biblatex-with-biber-configuring-my-editor-to-avoid-undefined-citations/502183#502183)

La modification apparaîtra ainsi dans les settings : 

```json
// this is for the LaTex workshop extension
// (from : https://tex.stackexchange.com/questions/154751/biblatex-with-biber-configuring-my-editor-to-avoid-undefined-citations/502183#502183)

"latex-workshop.latex.recipes": [
      {
          "name": "xelatex -> biber -> xelatex*2",
          "tools": [
              "xelatex",
              "biber",
              "xelatex",
              "xelatex"
          ]
      },      
  ],
  "latex-workshop.latex.tools": [{
      {
          "name": "pdflatex",
          "command": "pdflatex",
          "args": [
              "-synctex=1",
              "-interaction=nonstopmode",
              "-file-line-error",
              "%DOC%"
          ]
      },
      {
          "name": "bibtex",
          "command": "bibtex",
          "args": [
              "%DOCFILE%"
          ]
      },
      {
        "name": "biber",
        "command": "biber",
        "args": [
            "%DOCFILE%"
        ]
    },
    {
        "name": "xelatex",
        "command": "xelatex",
        "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
        ]
    }
}
]
```

pour compiler avec biber dans Texmaker, il faut configurer Texmaker dans ce sens : https://youtu.be/u-NtlKOAsnE?feature=shared

$\newline$
# bibliographie
$\newline$






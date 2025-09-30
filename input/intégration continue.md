---
title: intégration continue
subtitle: 
id: 20241107_intégration continue
author: Damien Belvèze
date: 2024-11-07
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases:
  - CI/CD
tags:
  - programmation
---


# gitlab-ci

(voir [[Site de chercheur#gitlab-ci]])

l'intégration continue est consommatrice de ressources pour ne pas lancer le CI à chaque commit envoyé, inscrire une condition dans le pipeline : 

```yaml
workflow:
  rules:
    - if: $CI_COMMIT_MESSAGE =~ /\[publish\].*/i
      when: always
    - when: never
# le CI ne se déclenche que lorsque le message de commit comporte le terme [publish], voir https://gricad-gitlab.univ-grenoble-alpes.fr/so-shs/outils-collaboratifs-gitlab/demos/ci-example-basics
```

# exemples de CI\CD

conversion de fichier markdown en html : 

```yml
# default:

image: fastexitlane/pandoc-latex
stages:
- build
- deploy
#before_script:
# These lines are commented out because the image should have these tools installed.
# - mkdir -p public
build_html:
stage: build

script:
- pandoc guide_fr.md --metadata title="guide fr" -o guide_fr.html --standalone
artifacts:
paths:
- guide_fr.html # Ensure this path is correct and exists after the script runs
only:
- main

deploy_to_pages:
stage: deploy

# needs: build_html # Ensure this job depends on the successful completion of build_html

script:

- mkdir -p public # Create the directory if it doesn't exist

- mv guide_fr.html public/guide_fr.html # Move the file to the expected path
artifacts:
paths:
- public
- 
only:
- main

```

publication de pages avec mkdocs

```yaml

pages:
  stage: test
  image: python:3.8.5-slim-buster
  script:
  - python -m pip install --upgrade pip mkdocs-bootswatch
  - mkdocs build
  - mv site public
  artifacts:
    paths:
    - public

```
(source : https://gricad-gitlab.univ-grenoble-alpes.fr/pole-calcul-formation/outils-collaboratifs-gitlab/demos/ci-example-basics)

intégration continue d'un document rédigé avec Quarto en page html

```yaml
variables:
  UBUNTU_VERSION: "22.04"
  QUARTO_VERSION: "1.3.450"
image: ubuntu:${UBUNTU_VERSION}
before_script:
  - apt-get update && apt-get -y install curl
  - curl -L -o ./quarto.deb https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb
  - dpkg -i ./quarto.deb && rm -f ./quarto.deb
  - quarto install --no-prompt extension quarto-ext/lightbox
pages:
  script:
    - quarto render . --output-dir=public/
  artifacts:
    paths:
      - public/
  only:
    - master
```

Intégration continue d'un document Rmarkdown (inclue un environnement virtuel avec [[Renv]]) 

```yaml
image: rocker/r-base:latest

pages:

	script:
		- apt-get update && apt-get install -y libcurl4-openssl-dev libssl-dev libxml2-dev pandoc
		- Rscript -e "install.packages('rmarkdown', repos = 'https://cloud.r-project.org')"
		- mkdir -p public
		- Rscript -e "install.packages('renv')"
		- Rscript -e "renv::restore()"
		- Rscript -e "rmarkdown::render('r_participation_formations_doctorales.Rmd', output_file = 'public/index.html')"
artifacts:
	paths:
		- public
only:
	- main # or 'master', depending on your branch
# ne pas oublier de faire un renv::snapshot() avant de committer
```

## ci pour Hugo 

par défaut : 
```yaml
default:

image: "${CI_TEMPLATE_REGISTRY_HOST}/pages/hugo/hugo_extended:latest"

  

variables:

GIT_SUBMODULE_STRATEGY: recursive
THEME_URL: "github.com/adityatelange/hugo-PaperMod"

HUGO_ENV: production

  

before_script:

- apk add --no-cache go curl bash nodejs

## Uncomment the following if you use PostCSS. See https://gohugo.io/hugo-pipes/postcss/

# - npm install postcss postcss-cli autoprefixer

  

test:

script:

- hugo

rules:

- if: $CI_COMMIT_BRANCH != $CI_DEFAULT_BRANCH

  

pages:

script:

- hugo

artifacts:

paths:

- public

rules:

- if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

environment: production
```


# ajout d'un workflow dans Github Pages

création d'un workflow : 
settings > Pages > Github Actions > create your own

Pour éditer les workflows :
https://github.com/username/repo/tree/branch/.github/workflows

![[CI_PANDOC2.yml]]

utilisation du code peaceiris/actions-gh-pages@v3 pour déployer le contenu du site




$\newline$
# bibliographie
$\newline$







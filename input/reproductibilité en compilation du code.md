---
title: reproductibilité en matière de compilation de code
date: 29/10/2023
aliases:
  - reproducible builds
tags:
  - reproductibilité
  - programmation
---
> An article about computational results is advertising, not scholarship. The actual scholarship is the full software environment, code and data, that produced the result.

(source:[[@buckheitWaveLabReproducibleResearch1995]])

# Répétabilité du code

Répétabilité du code un synonyme de reproductibilité, mais au niveau du code (répétabilité du code, reproductibilité de l'expérience)

> Research is _repeatable_ if we can re-run the researchers' experiment using the same method in the same environment and obtain the same results. A prerequisite for repeatability is for the research artifacts that back up the published results to be _shared_. Sharing for repeatability is essential to ensure that colleagues and reviewers can evaluate our results based on accurate and complete evidence.

(source: [[@collbergRepeatabilityComputerScience2015]])

**Rerunnable** : Can you re-run your program ?
One day, one week, one month, one year (just kidding) apart ?

**Repeatable** : Can you re-run your program and get same results ?
Did you save everything, including random seed ?

**Reproducible** : Can someone re-run your program and get same results ?
Did you save the [[dépendances]] ?

**Replicable** : Can someone reimplement your model and get same results ?
Did you describe everything ?

**Reusable** : Can someone reuse your program using different data ?
Is your software data-dependent ?

(source : [[@hinsenReScience2017]])


# Reproductibilité des compilations sous l'angle de la sécurité

Conférence de Christ Lamb, Debian Project leader depuis 2017, sur les compilations reproductibles (Reproducible Builds) le 9 janvier 2019 à 18h30 dans l'amphi de l'ISTIC à l'Université de Rennes 1.

texte d'annonce de la conférence : 

```
  
You think you're not a target? A tale of three developers...  
=============================================

If you develop or distribute software of any kind, you are vulnerable to whole categories of attacks upon yourself or your loved ones. This includes blackmail, extortion or "just" simple malware injection…  By targeting software developers such as yourself, malicious actors, including nefarious governments, can infect and attack thousands — if not millions — of end users!  
  
How can we avert this? The idea behind "reproducible" builds is to allow verification that no flaws have been introduced during build processes; this prevents against the installation of backdoor- introducing malware on developers' machines, ensuring attempts at  
extortion and other forms of subterfuge are quickly uncovered and thus ultimately futile.  
  
Through a story of three different developers, this talk will engage  
you on this growing threat to you and how it affects everyone involved in the production lifecycle of software development, as  
well as how reproducible builds can help prevent against it.  
  
Debian, openSUSE, Tails, Tor, Bitcoin, F-droid and coreboot/libreboot are examples of projects that have adopted reproducible builds or are pushing hard for their adoption.
```
<iframe width="560" height="315" src="https://www.youtube.com/embed/m0FudIwSuzM?si=nIisqIvpEuCP5viT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

cf. [[@lambReproducibleBuildsIncreasing2022]]

Download.exe /.deb /.rpm

  gets blackmails by an unknown person who introduces a different compiler

Download Source

Download.exe may make you download a compromised software

Modification des compilers lors du chargement des fichiers source : possibilité d’introduire des [[backdoors]] pendant le process

Carol

Quand on distribue des copies d’un logiciel, il faut s’assurer de la sécurité de l’ordinateur où le logiciel a été chargé avant d’être distribué

Most users install pre-compiled packages

can we trust the compilation process ?

Compromised mirrors.

Solution :

starting with the same source

ensure builds always have identical results

Compare results

compare [[checksum|checksums]]

If the checksum is different than the sig, then the binary has been changed

How to make Reliable Builds ?

Timestamps, build paths, non deterministic file ordering, users, groups may modify the final hash

Others advantages of reproducible builds than security and privacy ?

  

- Minimal differences on deliberate changes

- Cache ratio, save time, money & Co2

- remove build dependencies

Tests

vary :

hostname & domain name

different locales

filesystem

[[timestamp]]

isdebianreproducibleyet.com

diffoscope lets you know where a reproducible buid is available

diffoscope will not help to find backdoor in the [[code source|source code]], but backdoors in the compilation process

most common mistakes that make the build unreproducible with a compiler like GCC

1.Encoding timestamps

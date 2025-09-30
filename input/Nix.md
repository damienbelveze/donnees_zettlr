---
title: Nix
subtitle: 
id: 20250620_Nix
author: Damien Belvèze
date: 2025-06-20
link_citations: true
bibliography: biblio/Obsidian.bib
biblio_style: csl\ieee.csl
aliases: 
tags:
  - programmation
  - réplicabilité
---
Nix peut se présenter sous la forme d'un [[système d'exploitation]] Linux complet (NixOS) qui dispose de Nix comme gestionnaire de paquets ou d'un gestionnaire de paquets seul. 
Dans cette note, nous traiterons du gestionnaire de paquets (nix package manager)
Nix est le gestionnaire de paquets qui contient le plus de packages au monde, notamment plus que [[Guix]] également orienté [[reproductibilité]] : 

> Guix, like Nix, focuses on reproducibility, but Nix supports more CRANGuix, like Nix, focuses on reproducibility, but Nix supports more CRAN/Bioconductor packages and works across Windows, macOS, and Linux./Bioconductor packages and works across Windows, macOS, and Linux.

Nix en tant que gestionnaire de paquets peut être installé sur le [[WSL]] de Windows.

Nix permet d'avoir sur sa machine différentes versions d'un même package et des versions de deux packages différents qui pourraient entrer en conflit.

tous les packages chargés avec Nix vont dans le dossier ~/nix/store

Pour désinstaller le gestionnaire de paquets nix suivre la méthode utilisée ici : https://nix.dev/manual/nix/2.30/installation/uninstall.html

# commandes

ouvrir un shell nix : 
```shell
nix-shell -p
```

construire une image : 

```shell
nix-build nixpkgs#package
```

exécuter une image : 

```shell
nix run nixpkgs#package
```

erreur portant sur nix command ou flakes

```shell
nix --extra-experimental-features "nix-command flakes" build package
```
pour éviter d'avoir à taper cette commande à chaque fois, ajouter : 
experimental-features = nix-command flakes dans ~/.config/nix/nix.conf

# installer un package avec Nix

passer en nix-shell

```shell
nix profile install nixpkgs#docker
```

installer un package depuis github (pas forcément présent dans nixpkgs) : 

```shell
nix profile install github:owner/repo/pkg --profile ./path/to/directory
```

exemple (depuis https://github.com/damienbelveze/nix_code_r)

```shell
nix profile install github.com:damienbelveze/nix_code_r --profile ./code_r_nix
```

Si ça ne fonctionne pas, 

trouver le hash du package à charger : 

```shell
wget https://github.com/owner/package/archive/refs/heads/main.tar.gz -O package.tar.gz
```
on récupère l'archive du package depuis github et on va calculer son hash : 

```shell
nix-hash --type sha256 --flat nix_code_r.tar.gz
```

construire un flake : 

```shell
{
  description = "Install package from GitHub";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { self, nixpkgs }: 
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
      };
    in {
      packages.${system}.default = pkgs.stdenv.mkDerivation {
        pname = "nix_code_r";
        version = "main";

        src = pkgs.fetchFromGitHub {
          owner = "damienbelveze";
          repo = "nix_code_r";
          rev = "main";
          sha256 = "le hash récupéré avec la méthode ci-dessus";
        };

        buildInputs = [ ];
        installPhase = ''
          mkdir -p $out
          cp -r * $out/
        '';
      };
    };
}
```

$\newline$
# bibliographie
$\newline$







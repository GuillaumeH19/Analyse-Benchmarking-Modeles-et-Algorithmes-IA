# Analyse Expérimentale et Benchmarking de Modèles et Algorithmes d'IA (Chaiba Anfal / Huret Guillaume)

Ce Git présente les différents scripts de notre étude Analyse Expérimentale et Benchmarking de Modèles et Algorithmes d'IA qui compare les 3 algorithmes l'algorithme MAT-SMS, de Al-Dujaili et Sundaram, l'algorithme DEMO de Tušar and Filipič et l'algorithme RANDOMSEARCH-5 de Auger et al.

## DOI
[![DOI](https://zenodo.org/badge/795433842.svg)](https://zenodo.org/doi/10.5281/zenodo.11108653)

## Pré-Requis

Les différents scripts ont été testé en python 3.12.0, il faut que soit installé les bibliothèques pandas 2.1.3 et matplotlib 3.8.2.

```bash
pip install pandas==2.1.3
pip install matplotlib==3.8.2
```

## Données Initiales

Les données concernant la qualité et le temps d'exécution des différents algorithmes sont présent dans sous le dossier de chaque algorithme respectif. seront lu durant l'exécution grâce à la fonction OuvrirFichier lorsqu'on lui indique le problème sous le fichier .tdat.

## Exécution

Pour obtenir les différents graphes, il faut exécuter les différents scripts python par rapport aux différents étapes, les graphes seront sauvegardés dans le dossier Graphes.

## Contribution
Vous pouvez contribuer à l'étude en testant d'autres problèmes de la même manière que nous avons réalisé.

# Guide d'intégration - Chapitre 4 : Application CRISP-ML(Q)

## Fichiers créés

- `Chapitre4/chapitre4_crisp_application.tex` - Fichier principal du chapitre
- `test_crisp_chapter.tex` - Fichier de test pour compilation standalone

## Intégration dans le document principal

### Étape 1 : Ajouter l'input dans main.tex

Ajoutez la ligne suivante dans votre fichier `main.tex` à l'endroit approprié :

```latex
\input{Chapitre4/chapitre4_crisp_application.tex}
```

### Étape 2 : Créer la structure des images

Créez le répertoire pour les images :

```
Chapitre4/images/crisp/
```

### Étape 3 : Ajouter les images

Placez vos images dans le répertoire créé avec les noms suivants :

1. `zone_matelassage.png` - Vue de l'atelier
2. `planning_drive.png` - Capture du planning Excel
3. `interface_divatex.png` - Interface Divatex
4. `interface_gpro.png` - Interface G.Pro
5. `flux_information.png` - Schéma des flux (ou utiliser TikZ)
6. `dataset_extrait.png` - Tableau de données
7. `correlation_longueur.png` - Graphique de corrélation
8. `pipeline_preparation.png` - Pipeline de préparation (ou utiliser TikZ)
9. `prototype_interface.png` - Maquette du système IA
10. `comparaison_temps.png` - Graphique de performance

### Étape 4 : Remplacer les placeholders

Dans le fichier `chapitre4_crisp_application.tex`, remplacez chaque bloc :

```latex
\fbox{\parbox{0.8\textwidth}{\centering\vspace{3cm}
[Image à insérer~: Description]
\vspace{3cm}}}
```

Par :

```latex
\includegraphics[width=0.8\textwidth]{Chapitre4/images/crisp/nom_image.png}
```

## Utilisation des diagrammes TikZ (optionnel)

Pour les figures III.5 (flux d'information) et III.8 (pipeline), vous pouvez utiliser les templates TikZ commentés dans le fichier au lieu d'images PNG. Décommentez simplement le code TikZ et commentez le placeholder.

## Test de compilation

### Test standalone

Pour tester le chapitre seul :

```bash
pdflatex test_crisp_chapter.tex
```

### Test intégré

Pour tester avec le document complet :

```bash
pdflatex main.tex
```

## Structure du chapitre

Le chapitre contient :

- **Introduction** : Présentation de CRISP-ML(Q) et des 3 phases
- **Section 1** : Business Understanding
  - Sous-section 1.1 : Contexte de la planification
  - Sous-section 1.2 : Outils et technologies
  - Figures 1-5
- **Section 2** : Data Understanding & Analysis
  - Variables d'entrée et de sortie
  - Analyse statistique
  - Figures 6-7
- **Section 3** : Data Preparation
  - Étapes de nettoyage et normalisation
  - Figure 8
- **Section 4** : Modélisation et solution proposée
  - Aperçu du modèle et intégration
  - Figures 9-10

## Labels disponibles pour références croisées

- `\ref{chap:crisp-methodology}` - Chapitre principal
- `\ref{sec:crisp-business}` - Section Business Understanding
- `\ref{subsec:crisp-contexte}` - Contexte de la planification
- `\ref{subsec:crisp-outils}` - Outils et technologies
- `\ref{sec:crisp-data-understanding}` - Data Understanding
- `\ref{sec:crisp-data-preparation}` - Data Preparation
- `\ref{sec:crisp-modeling}` - Modélisation
- `\ref{fig:crisp-zone-matelassage}` - Figure 1
- `\ref{fig:crisp-planning-drive}` - Figure 2
- `\ref{fig:crisp-interface-divatex}` - Figure 3
- `\ref{fig:crisp-interface-gpro}` - Figure 4
- `\ref{fig:crisp-flux-information}` - Figure 5
- `\ref{fig:crisp-dataset-extrait}` - Figure 6
- `\ref{fig:crisp-correlation-longueur}` - Figure 7
- `\ref{fig:crisp-pipeline-preparation}` - Figure 8
- `\ref{fig:crisp-prototype-interface}` - Figure 9
- `\ref{fig:crisp-comparaison-temps}` - Figure 10

## Notes importantes

- Le fichier utilise l'encodage UTF-8
- La typographie française est respectée (espaces insécables avant `:` et `;`)
- Les unités sont formatées correctement (20~m, 7~m)
- Tous les environnements sont correctement fermés
- Tous les labels sont uniques et suivent la convention `crisp-*`

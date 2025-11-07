# Design Document - Section Outils et Bibliothèques pour Chapitre 3

## Overview

Cette section sera ajoutée au début du Chapitre 3 (après l'introduction, avant la Phase 1) pour présenter de manière structurée et académique l'écosystème technologique utilisé dans le projet. Elle servira de référence technique pour comprendre les choix d'implémentation et assurer la reproductibilité du projet.

## Architecture

### Structure de la section

```
\section{Outils et bibliothèques utilisés}
  \subsection{Introduction}
  \subsection{Écosystème Data Science et Machine Learning}
    \subsubsection{Bibliothèques de manipulation de données}
    \subsubsection{Bibliothèques de Machine Learning}
    \subsubsection{Bibliothèques de visualisation}
  \subsection{Frameworks de développement}
    \subsubsection{Backend et API}
    \subsubsection{Frontend et interface utilisateur}
  \subsection{Outils d'optimisation et d'ordonnancement}
  \subsection{Infrastructure et DevOps}
  \subsection{Stack technologique complète}
  \subsection{Justification des choix et intégration CRISP-ML(Q)}
```

### Positionnement dans le document

- **Emplacement**: Après `\section{Introduction}` et avant `\section{Phase 1 : Comprehension metier}`
- **Numérotation**: Sera automatiquement gérée par LaTeX
- **Longueur estimée**: 3-4 pages (environ 1500-2000 mots)

## Components and Interfaces

### Composant 1: Tableaux récapitulatifs

**Format LaTeX:**
```latex
\begin{table}[H]
\centering
\caption{Bibliothèques Python pour Data Science}
\begin{tabular}{|l|l|l|p{6cm}|}
\hline
\textbf{Bibliothèque} & \textbf{Version} & \textbf{Rôle} & \textbf{Justification} \\
\hline
pandas & 2.0.3 & Manipulation données & Standard industrie, performance \\
\hline
...
\end{tabular}
\end{table}
```

### Composant 2: Descriptions textuelles

Chaque outil sera présenté avec:
- **Nom et version**
- **Rôle dans le projet**
- **Justification du choix** (2-3 critères)
- **Alternatives considérées** (si pertinent)
- **Intégration avec autres composants**

### Composant 3: Diagramme d'architecture (optionnel)

Un diagramme TikZ montrant l'interaction entre les composants:
```
[Frontend React] <--> [API FastAPI] <--> [Modèles ML XGBoost]
                                    <--> [Optimiseur CP-SAT]
                                    <--> [Base de données]
```

## Data Models

### Catégories d'outils

1. **Data Science & ML**
   - pandas: Manipulation et analyse de données
   - NumPy: Calculs numériques et algèbre linéaire
   - scikit-learn: Preprocessing, métriques, validation
   - XGBoost: Algorithme principal de prédiction
   - matplotlib/seaborn: Visualisation

2. **Backend & API**
   - FastAPI: Framework web moderne et performant
   - Pydantic: Validation de données
   - uvicorn: Serveur ASGI

3. **Frontend**
   - React: Framework JavaScript pour l'interface
   - Recharts: Visualisations interactives
   - Axios: Communication HTTP

4. **Optimisation**
   - OR-Tools: Bibliothèque Google pour l'optimisation
   - CP-SAT: Solveur de contraintes

5. **DevOps & Infrastructure**
   - Docker: Conteneurisation
   - Git: Gestion de version
   - pytest: Tests automatisés

### Informations à documenter pour chaque outil

```
{
  "nom": "XGBoost",
  "version": "1.7.6",
  "categorie": "Machine Learning",
  "role": "Algorithme principal de prédiction des temps",
  "justification": [
    "Performance supérieure (R² = 0.84)",
    "Gestion native des valeurs manquantes",
    "Régularisation intégrée",
    "Interprétabilité via SHAP"
  ],
  "alternatives": ["Random Forest", "Gradient Boosting"],
  "integration": "Utilisé dans la phase Modeling de CRISP-ML(Q)"
}
```

## Error Handling

### Cohérence avec les autres chapitres

- Vérifier que les versions mentionnées correspondent à celles utilisées dans les chapitres 4, 5, 6
- S'assurer que les justifications sont cohérentes avec les analyses de performance du chapitre 4
- Valider que les outils mentionnés sont effectivement utilisés dans le projet

### Gestion des informations manquantes

- Si une version exacte n'est pas disponible, utiliser "~2.0" ou "dernière version stable"
- Si une justification n'est pas évidente, se baser sur les standards de l'industrie
- Documenter les hypothèses faites

## Testing Strategy

### Validation du contenu

1. **Vérification de complétude**
   - Tous les outils mentionnés dans les autres chapitres sont documentés
   - Aucun outil documenté n'est pas utilisé dans le projet

2. **Vérification de cohérence**
   - Les versions correspondent entre les chapitres
   - Les justifications sont alignées avec les résultats du chapitre 4
   - La terminologie est cohérente

3. **Vérification académique**
   - Le style d'écriture est formel et académique
   - Les affirmations sont supportées par des faits ou des citations
   - La structure est logique et facile à suivre

4. **Vérification LaTeX**
   - Les tableaux compilent correctement
   - Les références croisées fonctionnent
   - La mise en page est professionnelle

## Detailed Design

### Sous-section 1: Introduction (200 mots)

**Contenu:**
- Importance du choix des outils dans un projet ML
- Critères de sélection (maturité, performance, communauté, documentation)
- Lien avec la méthodologie CRISP-ML(Q)
- Organisation de la section

**Ton:** Académique, contextuel, justificatif

### Sous-section 2: Écosystème Data Science (600 mots)

**Contenu:**

**2.1 Bibliothèques de manipulation de données**
- **pandas 2.0.3**: DataFrames, manipulation, nettoyage
  - Justification: Standard industrie, riche API, performance
  - Utilisation: Phase Data Understanding et Data Preparation
  
- **NumPy 1.24.3**: Calculs numériques, arrays
  - Justification: Base de l'écosystème scientifique Python
  - Utilisation: Calculs matriciels, transformations

**2.2 Bibliothèques de Machine Learning**
- **scikit-learn 1.3.0**: Preprocessing, métriques, validation
  - Justification: API cohérente, documentation excellente
  - Utilisation: StandardScaler, train_test_split, métriques
  
- **XGBoost 1.7.6**: Algorithme principal
  - Justification: Performance (R²=0.84), régularisation, interprétabilité
  - Utilisation: Modèle de prédiction des temps
  - Alternatives considérées: Random Forest (R²=0.78), Gradient Boosting

**2.3 Bibliothèques de visualisation**
- **matplotlib 3.7.2**: Visualisations statiques
- **seaborn 0.12.2**: Visualisations statistiques
  - Justification: Intégration pandas, esthétique professionnelle
  - Utilisation: EDA, analyse de corrélations, distributions

**Format:** Tableau récapitulatif + descriptions textuelles

### Sous-section 3: Frameworks de développement (400 mots)

**Contenu:**

**3.1 Backend et API**
- **FastAPI 0.103.0**: Framework web moderne
  - Justification: 
    - Performance (async/await)
    - Documentation automatique (Swagger/OpenAPI)
    - Validation de données (Pydantic)
    - Type hints natifs
  - Alternatives: Flask (moins performant), Django (trop lourd)
  
- **Pydantic 2.3.0**: Validation de données
- **uvicorn 0.23.2**: Serveur ASGI

**3.2 Frontend et interface utilisateur**
- **React 18.2.0**: Framework JavaScript
  - Justification:
    - Composants réutilisables
    - Écosystème riche
    - Performance (Virtual DOM)
    - Communauté active
  
- **Recharts 2.8.0**: Visualisations interactives
- **Axios 1.5.0**: Communication HTTP

**Format:** Descriptions textuelles avec listes à puces

### Sous-section 4: Outils d'optimisation (300 mots)

**Contenu:**

- **OR-Tools 9.7**: Bibliothèque Google d'optimisation
  - Justification:
    - Solveur CP-SAT performant
    - Support contraintes complexes
    - Documentation complète
    - Gratuit et open-source
  
- **CP-SAT Solver**: Solveur de contraintes
  - Utilisation: Ordonnancement optimal des tables
  - Performance: Résolution en < 2 secondes pour 50 OF
  - Intégration: Phase Modeling de CRISP-ML(Q)

**Format:** Description textuelle + exemple d'utilisation

### Sous-section 5: Infrastructure et DevOps (200 mots)

**Contenu:**

- **Docker 24.0**: Conteneurisation
  - Justification: Reproductibilité, isolation, déploiement
  
- **Git 2.41**: Gestion de version
  - Justification: Standard industrie, collaboration
  
- **pytest 7.4.0**: Tests automatisés
  - Justification: Simplicité, fixtures, couverture

**Format:** Liste descriptive

### Sous-section 6: Stack technologique complète (200 mots)

**Contenu:**

Tableau récapitulatif complet avec toutes les technologies organisées par couche:

| Couche | Technologies | Rôle |
|--------|-------------|------|
| Data Science | pandas, NumPy, scikit-learn, XGBoost | Analyse et ML |
| Backend | FastAPI, Pydantic, uvicorn | API et services |
| Frontend | React, Recharts, Axios | Interface utilisateur |
| Optimisation | OR-Tools, CP-SAT | Ordonnancement |
| DevOps | Docker, Git, pytest | Infrastructure |
| Base de données | PostgreSQL, SQLAlchemy | Persistance |

**Format:** Tableau LaTeX professionnel

### Sous-section 7: Justification et intégration CRISP-ML(Q) (300 mots)

**Contenu:**

- Alignement des outils avec chaque phase CRISP-ML(Q):
  - **Phase 1 (Business Understanding)**: Outils de documentation et collaboration
  - **Phase 2 (Data Understanding)**: pandas, matplotlib, seaborn pour EDA
  - **Phase 3 (Data Preparation)**: pandas, scikit-learn pour preprocessing
  - **Phase 4 (Modeling)**: XGBoost, scikit-learn pour entraînement
  - **Phase 5 (Evaluation)**: Métriques scikit-learn, visualisations
  - **Phase 6 (Deployment)**: FastAPI, Docker pour production

- Critères de sélection appliqués:
  1. **Maturité**: Bibliothèques éprouvées avec historique stable
  2. **Performance**: Benchmarks et comparaisons objectives
  3. **Communauté**: Support actif, documentation, exemples
  4. **Compatibilité**: Intégration harmonieuse entre composants
  5. **Maintenabilité**: Code lisible, tests, évolutivité

- Bénéfices de la stack choisie:
  - Reproductibilité scientifique
  - Performance opérationnelle
  - Maintenabilité à long terme
  - Évolutivité du système

**Format:** Texte structuré avec listes numérotées

## Style Guidelines

### Écriture académique

- Utiliser un ton formel et objectif
- Éviter les superlatifs non justifiés ("le meilleur", "incroyable")
- Supporter les affirmations par des faits ou des citations
- Utiliser la voix passive quand approprié ("XGBoost a été sélectionné...")

### Formatage LaTeX

- Utiliser `\textbf{}` pour les noms d'outils
- Utiliser `\texttt{}` pour les noms de packages/modules
- Utiliser des tableaux `[H]` pour éviter les flottements
- Utiliser `\cite{}` pour les références académiques

### Cohérence terminologique

- "Bibliothèque" pour les packages Python
- "Framework" pour FastAPI, React
- "Outil" pour Docker, Git
- "Algorithme" pour XGBoost, CP-SAT
- "Solveur" pour CP-SAT spécifiquement

## Integration Points

### Avec Chapitre 4 (Modeling)

- Les performances mentionnées (R²=0.84) doivent correspondre
- Les hyperparamètres XGBoost doivent être cohérents
- Les alternatives comparées doivent être les mêmes

### Avec Chapitre 5 (Agile)

- Les technologies mentionnées dans les sprints doivent être documentées
- Les livrables techniques doivent correspondre aux outils

### Avec Chapitre 6 (Architecture)

- L'architecture décrite doit utiliser les outils documentés
- Les diagrammes doivent être cohérents
- Les endpoints API doivent correspondre à FastAPI

### Avec biblio.bib

- Ajouter des citations pour:
  - XGBoost: chen2016xgboost (déjà présent)
  - FastAPI: Documentation officielle
  - OR-Tools: Documentation Google
  - React: Documentation officielle

## Deliverables

1. **Fichier LaTeX modifié**: `Chapitre3/chapitre3.tex` avec la nouvelle section
2. **Compilation réussie**: Le document doit compiler sans erreurs
3. **Cohérence validée**: Vérification croisée avec les autres chapitres
4. **Style académique**: Relecture pour assurer le ton formel

## Success Criteria

- ✅ La section est complète et couvre tous les outils utilisés
- ✅ Les justifications sont objectives et basées sur des critères mesurables
- ✅ Les informations sont cohérentes avec les autres chapitres
- ✅ Le style d'écriture est académique et professionnel
- ✅ Les tableaux LaTeX sont bien formatés et lisibles
- ✅ La section s'intègre naturellement dans le flux du chapitre
- ✅ La longueur est appropriée (3-4 pages)

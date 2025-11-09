#!/usr/bin/env python3
"""
Script pour réorganiser le Chapitre 3 selon la nouvelle structure
"""

def main():
    print("🚀 Début de la réorganisation du Chapitre 3...")
    
    # Lire le fichier original
    with open('chapitre3_BACKUP_ORIGINAL.tex', 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Créer le nouveau contenu
    new_content = r"""\chapter{Intelligence Artificielle, Industrie 4.0 et Méthodologie CRISP-ML(Q)}\label{chap3:crispml}

\lhead{Chapitre III: IA, Industrie 4.0 et CRISP-ML(Q)}
\dominitoc 
\rhead{\thepage}
\minitoc

% ============================================================================
% SECTION 1: INTELLIGENCE ARTIFICIELLE ET INDUSTRIE 4.0
% ============================================================================

\input{Chapitre3/section1_ia_industrie40.tex}

% ============================================================================
% SECTION 2: OUTILS ET BIBLIOTHÈQUES
% ============================================================================

"""
    
    # Extraire la section Outils (lignes 79-716 environ)
    lines = original_content.split('\n')
    
    # Trouver le début de la section Outils
    tools_start = None
    for i, line in enumerate(lines):
        if r'\section{Outils et bibliothèques utilisés}' in line:
            tools_start = i
            break
    
    # Trouver la fin de la section Outils (début de Phase 1)
    tools_end = None
    for i, line in enumerate(lines[tools_start:], start=tools_start):
        if r'\section{Phase 1 : Comprehension metier' in line:
            tools_end = i
            break
    
    # Ajouter la section Outils
    if tools_start and tools_end:
        new_content += '\n'.join(lines[tools_start:tools_end])
    
    # Ajouter la section CRISP-ML(Q)
    new_content += r"""

% ============================================================================
% SECTION 3: MÉTHODOLOGIE CRISP-ML(Q)
% ============================================================================

\section{Méthodologie CRISP-ML(Q)}\label{chap3:crispml_methodology}

\subsection{Introduction à CRISP-ML(Q)}

La méthodologie CRISP-ML(Q) (\textit{Cross-Industry Standard Process for Machine Learning with Quality assurance}) \cite{studer2021towards} représente une évolution majeure du processus CRISP-DM (\textit{Cross-Industry Standard Process for Data Mining}) \cite{wirth2000crisp}, spécifiquement adaptée aux exigences et aux défis du Machine Learning moderne en environnement industriel.

\subsubsection{De CRISP-DM à CRISP-ML(Q)}

CRISP-DM, introduit en 1996, a longtemps été la méthodologie de référence pour les projets de Data Mining. Cependant, l'évolution rapide du Machine Learning et son déploiement en production ont révélé plusieurs limitations :

\begin{itemize}
    \item \textbf{Absence de considérations qualité} : CRISP-DM ne définit pas de critères de qualité formels
    \item \textbf{Déploiement sous-estimé} : La phase de déploiement est traitée superficiellement
    \item \textbf{Monitoring non intégré} : Pas de mécanismes de surveillance post-déploiement
    \item \textbf{Réentraînement non prévu} : Pas de processus pour gérer la dérive des modèles
\end{itemize}

CRISP-ML(Q) adresse ces limitations en intégrant :
\begin{itemize}
    \item \textbf{Portes de qualité (Quality Gates)} : Validation formelle à chaque phase critique
    \item \textbf{Monitoring continu} : Surveillance des performances en production
    \item \textbf{Gestion du cycle de vie} : Processus de réentraînement et de mise à jour
    \item \textbf{Traçabilité} : Documentation complète des décisions et des expérimentations
\end{itemize}

\subsubsection{Pourquoi CRISP-ML(Q) pour l'IA industrielle?}

L'adoption de CRISP-ML(Q) dans ce projet se justifie par plusieurs facteurs critiques :

\textbf{1. Rigueur et qualité}
\begin{itemize}
    \item Processus structuré garantissant la qualité à chaque étape
    \item Validation formelle via des portes de qualité
    \item Réduction des risques d'échec en production
\end{itemize}

\textbf{2. Reproductibilité}
\begin{itemize}
    \item Documentation standardisée des expérimentations
    \item Traçabilité complète des décisions
    \item Facilite la maintenance et l'évolution du système
\end{itemize}

\textbf{3. Alignement industriel}
\begin{itemize}
    \item Méthodologie reconnue et adoptée par l'industrie
    \item Compatible avec les standards qualité (ISO, Six Sigma)
    \item Facilite la communication avec les parties prenantes
\end{itemize}

\textbf{4. Gestion du cycle de vie complet}
\begin{itemize}
    \item Couvre toutes les phases du projet ML
    \item Intègre le déploiement et le monitoring
    \item Prévoit le réentraînement et l'amélioration continue
\end{itemize}

"""
    
    # Ajouter le diagramme CRISP-ML(Q)
    new_content += r"""
\subsection{Vue d'ensemble du processus CRISP-ML(Q)}

La figure \ref{fig:crispml_process} illustre le processus complet CRISP-ML(Q) avec ses 6 phases itératives et les boucles de rétroaction qualité.

\begin{figure}[H]
\centering
\begin{tikzpicture}[
    node distance=1.8cm,
    phase/.style={rectangle, draw, fill=blue!20, text width=3.2cm, text centered, rounded corners, minimum height=1cm, font=\small},
    arrow/.style={->, >=stealth, thick},
    quality/.style={rectangle, draw, fill=green!20, text width=2.8cm, text centered, rounded corners, minimum height=0.8cm, font=\footnotesize}
]

% Phases principales (colonne gauche)
\node[phase] (business) at (0,0) {1. Business\\Understanding};
\node[phase] (data) at (0,-2) {2. Data\\Understanding};
\node[phase] (prep) at (0,-4) {3. Data\\Preparation};
\node[phase] (model) at (0,-6) {4. Modeling};
\node[phase] (eval) at (0,-8) {5. Evaluation};
\node[phase] (deploy) at (0,-10) {6. Deployment};

% Fleches principales
\draw[arrow] (business) -- (data);
\draw[arrow] (data) -- (prep);
\draw[arrow] (prep) -- (model);
\draw[arrow] (model) -- (eval);
\draw[arrow] (eval) -- (deploy);

% Boucles de retroaction (a droite)
\draw[arrow, dashed, red] (eval.east) -- ++(1.5,0) |- (model.east);
\draw[arrow, dashed, red] (eval.east) -- ++(2,0) |- (prep.east);
\draw[arrow, dashed, red] (deploy.east) -- ++(2.5,0) |- (business.east);

% Quality gates (colonne droite)
\node[quality] (qg1) at (5,-2) {Quality Gate 1:\\Data Quality};
\node[quality] (qg2) at (5,-6) {Quality Gate 2:\\Model Quality};
\node[quality] (qg3) at (5,-10) {Quality Gate 3:\\Production};

\draw[arrow, dotted, green!60!black] (data.east) -- (qg1.west);
\draw[arrow, dotted, green!60!black] (model.east) -- (qg2.west);
\draw[arrow, dotted, green!60!black] (deploy.east) -- (qg3.west);

% Legende
\node[font=\footnotesize] at (0,-11.5) {Phases couvertes dans ce chapitre: 1-3};

\end{tikzpicture}
\caption{Processus CRISP-ML(Q) avec portes de qualité}
\label{fig:crispml_process}
\end{figure}

\textbf{Caractéristiques clés du processus :}
\begin{itemize}
    \item \textbf{Itératif} : Retours possibles vers les phases précédentes
    \item \textbf{Qualité intégrée} : Portes de qualité à chaque étape critique
    \item \textbf{Traçabilité} : Documentation complète des décisions
    \item \textbf{Reproductibilité} : Processus standardisé et automatisé
\end{itemize}

\subsection{Les six phases de CRISP-ML(Q)}

\subsubsection{Phase 1: Business Understanding}
Comprendre les objectifs business, définir les critères de succès, identifier les parties prenantes et les contraintes.

\subsubsection{Phase 2: Data Understanding}
Collecter, explorer et évaluer la qualité des données disponibles.

\subsubsection{Phase 3: Data Preparation}
Nettoyer, transformer et préparer les données pour la modélisation.

\subsubsection{Phase 4: Modeling}
Sélectionner et entraîner les algorithmes ML, optimiser les hyperparamètres.

\subsubsection{Phase 5: Evaluation}
Évaluer les performances du modèle, valider l'atteinte des objectifs business.

\subsubsection{Phase 6: Deployment}
Déployer le modèle en production, mettre en place le monitoring et le réentraînement.

\subsection{Portes de qualité (Quality Gates)}

Les portes de qualité constituent un mécanisme de validation formelle à trois moments critiques du processus.

\textbf{Quality Gate 1: Data Quality}
\begin{itemize}
    \item Complétude des données (> 95\%)
    \item Cohérence et validité
    \item Représentativité du problème
    \item Documentation du dictionnaire de données
\end{itemize}

\textbf{Quality Gate 2: Model Quality}
\begin{itemize}
    \item Performance sur données de test (R² > 0.75)
    \item Robustesse (validation croisée)
    \item Interprétabilité
    \item Documentation des expérimentations
\end{itemize}

\textbf{Quality Gate 3: Production Quality}
\begin{itemize}
    \item Performance en production stable
    \item Monitoring opérationnel
    \item Procédures de réentraînement
    \item Documentation utilisateur
\end{itemize}

"""
    
    # Ajouter les phases 1-3
    # Trouver Phase 1
    phase1_start = None
    for i, line in enumerate(lines):
        if r'\section{Phase 1 : Comprehension metier' in line:
            phase1_start = i
            break
    
    # Trouver Phase 2
    phase2_start = None
    for i, line in enumerate(lines[phase1_start:], start=phase1_start):
        if r'\section{Phase 2 : Comprehension des donnees' in line:
            phase2_start = i
            break
    
    # Trouver Phase 3
    phase3_start = None
    for i, line in enumerate(lines[phase2_start:], start=phase2_start):
        if r'\section{Phase 3 : Preparation des donnees' in line:
            phase3_start = i
            break
    
    # Trouver la fin de Phase 3
    phase3_end = None
    for i, line in enumerate(lines[phase3_start:], start=phase3_start):
        if r'\section{Phase 3 (suite) : Cadre' in line or r'\section{Synthese' in line:
            phase3_end = i
            break
    
    # Ajouter les phases
    if phase1_start and phase2_start:
        new_content += "\n% ============================================================================\n"
        new_content += "% SECTION 4: PHASE 1 - COMPRÉHENSION MÉTIER\n"
        new_content += "% ============================================================================\n\n"
        new_content += '\n'.join(lines[phase1_start:phase2_start])
    
    if phase2_start and phase3_start:
        new_content += "\n% ============================================================================\n"
        new_content += "% SECTION 5: PHASE 2 - COMPRÉHENSION DES DONNÉES\n"
        new_content += "% ============================================================================\n\n"
        new_content += '\n'.join(lines[phase2_start:phase3_start])
    
    if phase3_start and phase3_end:
        new_content += "\n% ============================================================================\n"
        new_content += "% SECTION 6: PHASE 3 - PRÉPARATION DES DONNÉES\n"
        new_content += "% ============================================================================\n\n"
        new_content += '\n'.join(lines[phase3_start:phase3_end])
    
    # Ajouter la section Qualité et Synthèse
    if phase3_end:
        new_content += "\n% ============================================================================\n"
        new_content += "% SECTION 7: CADRE D'ASSURANCE QUALITÉ\n"
        new_content += "% ============================================================================\n\n"
        new_content += '\n'.join(lines[phase3_end:])
    
    # Écrire le nouveau fichier
    with open('chapitre3.tex', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ Réorganisation terminée!")
    print("📄 Nouveau fichier: chapitre3.tex")
    print("💾 Backup original: chapitre3_BACKUP_ORIGINAL.tex")
    print("\n📊 Nouvelle structure:")
    print("  1. Intelligence Artificielle et Industrie 4.0 (NOUVEAU)")
    print("  2. Outils et Bibliothèques")
    print("  3. Méthodologie CRISP-ML(Q) (NOUVEAU)")
    print("  4. Phase 1: Compréhension Métier")
    print("  5. Phase 2: Compréhension des Données")
    print("  6. Phase 3: Préparation des Données")
    print("  7. Cadre d'Assurance Qualité")
    print("  8. Synthèse et Perspectives")

if __name__ == '__main__':
    main()

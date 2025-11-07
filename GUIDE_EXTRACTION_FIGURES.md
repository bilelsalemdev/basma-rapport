# Guide d'extraction des figures du PDF

## Vue d'ensemble

Ce guide vous aide à extraire les figures 28, 31, 34 et 35 du PDF `Optimisation intelligente de la planification de la production (3).pdf` pour les intégrer dans le Chapitre 3.

## Figures à extraire

| Figure | Contenu | Nom du fichier | Emplacement |
|--------|---------|----------------|-------------|
| **Figure 28** | 6 logos Data Science (pandas, NumPy, scikit-learn, XGBoost, matplotlib, seaborn) | `figure-28-data-science.png` | `Chapitre3/images/logos/` |
| **Figure 31** | 3 logos Backend (FastAPI, Pydantic, uvicorn) | `figure-31-backend.png` | `Chapitre3/images/logos/` |
| **Figure 34** | 3 logos Frontend (React, Recharts, Axios) | `figure-34-frontend.png` | `Chapitre3/images/logos/` |
| **Figure 35** | Logos DevOps/Optimization (OR-Tools, Docker, Git, pytest, PostgreSQL) | `figure-35-devops.png` | `Chapitre3/images/logos/` |

## Méthode 1: Capture d'écran (Rapide et simple)

### Étapes:

1. **Ouvrez le PDF** `Optimisation intelligente de la planification de la production (3).pdf`

2. **Trouvez la figure** en utilisant Ctrl+F et cherchez "Figure 28", "Figure 31", etc.

3. **Zoomez à 200-300%** pour une meilleure qualité

4. **Capturez l'écran:**
   - Windows: Appuyez sur `Win + Shift + S`
   - Sélectionnez précisément la figure (incluez la légende si nécessaire)

5. **Enregistrez l'image:**
   - Collez dans Paint ou un éditeur d'images
   - Enregistrez en PNG avec le nom approprié
   - Placez dans `Chapitre3/images/logos/`

### Exemple pour Figure 28:
```
1. Ctrl+F → "Figure 28"
2. Zoom 250%
3. Win + Shift + S → Sélectionner la figure
4. Coller dans Paint
5. Enregistrer sous: Chapitre3/images/logos/figure-28-data-science.png
```

## Méthode 2: Adobe Acrobat (Meilleure qualité)

### Étapes:

1. **Ouvrez le PDF** avec Adobe Acrobat

2. **Activez l'outil d'édition:**
   - Outils → Modifier le PDF

3. **Sélectionnez l'image:**
   - Cliquez sur la figure pour la sélectionner

4. **Exportez l'image:**
   - Clic droit → "Exporter l'image"
   - Choisissez PNG comme format
   - Enregistrez avec le nom approprié

## Méthode 3: PDF-XChange Editor (Gratuit)

### Étapes:

1. **Téléchargez PDF-XChange Editor** (gratuit)

2. **Ouvrez le PDF**

3. **Naviguez vers la figure**

4. **Exportez:**
   - Clic droit sur l'image → "Exporter l'image"
   - Format: PNG
   - Enregistrez avec le nom approprié

## Méthode 4: Script Python automatique

Si vous avez Python installé, utilisez ce script:

```python
import fitz  # PyMuPDF
import os

# Installation: pip install PyMuPDF

pdf_path = "Optimisation intelligente de la planification de la production (3).pdf"
output_dir = "Chapitre3/images/logos/"

# Créer le dossier si nécessaire
os.makedirs(output_dir, exist_ok=True)

# Ouvrir le PDF
doc = fitz.open(pdf_path)

# Figures à extraire (ajustez les numéros de pages selon votre PDF)
figures = {
    35: "figure-28-data-science.png",    # Page estimée pour Figure 28
    40: "figure-31-backend.png",         # Page estimée pour Figure 31
    45: "figure-34-frontend.png",        # Page estimée pour Figure 34
    50: "figure-35-devops.png"           # Page estimée pour Figure 35
}

for page_num, filename in figures.items():
    try:
        page = doc[page_num]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom pour meilleure qualité
        pix.save(os.path.join(output_dir, filename))
        print(f"✓ Extrait: {filename}")
    except Exception as e:
        print(f"✗ Erreur pour {filename}: {e}")

doc.close()
print("\nExtraction terminée!")
```

**Installation PyMuPDF:**
```bash
pip install PyMuPDF
```

## Vérification après extraction

Une fois les 4 figures extraites, vérifiez:

- [ ] Les 4 fichiers PNG sont dans `Chapitre3/images/logos/`
- [ ] Les noms de fichiers sont corrects:
  - `figure-28-data-science.png`
  - `figure-31-backend.png`
  - `figure-34-frontend.png`
  - `figure-35-devops.png`
- [ ] Les images sont lisibles et de bonne qualité
- [ ] Les images ne sont pas corrompues

## Compilation LaTeX

Après avoir extrait les figures, compilez le document:

```bash
cd rapport__2_
pdflatex main.tex
```

Le document devrait compiler sans erreurs et afficher les 4 figures extraites.

## Dépannage

### Problème: Je ne trouve pas la figure dans le PDF
**Solution:** 
- Utilisez Ctrl+F et cherchez "Figure 28", "Figure 31", etc.
- Parcourez le Chapitre 3 (généralement pages 30-60)
- Vérifiez la table des figures au début du document

### Problème: L'image est de mauvaise qualité
**Solution:**
- Augmentez le zoom à 300% avant la capture
- Utilisez Adobe Acrobat ou PDF-XChange pour extraction directe
- Essayez le script Python avec zoom 3x

### Problème: Le fichier est trop volumineux
**Solution:**
- Utilisez TinyPNG.com pour compresser
- Réduisez légèrement la résolution (mais gardez > 150 DPI)

## Modifications apportées au LaTeX

Les modifications suivantes ont été apportées à `Chapitre3/chapitre3.tex`:

1. **Figure Data Science (ligne ~162):** Remplacé 6 subfigures par une seule image `figure-28-data-science.png`
2. **Figure Backend (ligne ~210):** Remplacé 3 subfigures par une seule image `figure-31-backend.png`
3. **Figure Frontend (ligne ~240):** Remplacé 3 subfigures par une seule image `figure-34-frontend.png`
4. **Figure DevOps (ligne ~320):** Remplacé 4 subfigures par une seule image `figure-35-devops.png`
5. **Figure OR-Tools standalone:** Supprimée (maintenant incluse dans figure 35)

## Prochaines étapes

Une fois les figures extraites et le document compilé avec succès:

1. Vérifiez la qualité visuelle des figures dans le PDF généré
2. Continuez avec les tâches d'enrichissement du contenu (tâches 6-10)
3. Consultez `.kiro/specs/chapitre3-logos-enrichissement/tasks.md` pour les prochaines tâches

## Besoin d'aide?

Consultez:
- `Chapitre3/images/logos/README.md` - Instructions détaillées d'extraction
- `.kiro/specs/chapitre3-logos-enrichissement/design.md` - Documentation du design
- `.kiro/specs/chapitre3-logos-enrichissement/tasks.md` - Plan d'implémentation

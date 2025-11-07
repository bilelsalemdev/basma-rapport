# Guide d'extraction des figures du PDF

Ce document fournit les instructions complètes pour extraire les figures 28, 31, 34 et 35 du PDF existant `Optimisation intelligente de la planification de la production (3).pdf`.

## Approche révisée

Au lieu de télécharger des logos individuels, nous utilisons les figures déjà présentes dans le PDF existant. Cette approche garantit:
- ✅ Cohérence visuelle avec le document existant
- ✅ Gain de temps significatif
- ✅ Qualité et mise en page déjà validées
- ✅ Pas de problèmes de licences

## Figures à extraire

| Figure | Page estimée | Contenu | Nom du fichier |
|--------|--------------|---------|----------------|
| **Figure 28** | ~35-40 | 6 logos Data Science (pandas, NumPy, scikit-learn, XGBoost, matplotlib, seaborn) | `figure-28-data-science.png` |
| **Figure 31** | ~40-45 | 3 logos Backend (FastAPI, Pydantic, uvicorn) | `figure-31-backend.png` |
| **Figure 34** | ~45-50 | 3 logos Frontend (React, Recharts, Axios) | `figure-34-frontend.png` |
| **Figure 35** | ~50-55 | Logos DevOps/Optimization (OR-Tools, Docker, Git, pytest, PostgreSQL) | `figure-35-devops.png` |

## Spécifications techniques

- **Format:** PNG
- **Résolution:** Conserver la résolution originale du PDF (généralement 150-300 DPI)
- **Dimensions:** Conserver les proportions originales
- **Nommage:** `figure-[numéro]-[catégorie].png`
- **Emplacement:** `Chapitre3/images/logos/`

## Méthodes d'extraction

### Méthode 1: Adobe Acrobat (Recommandé)

1. Ouvrez le PDF `Optimisation intelligente de la planification de la production (3).pdf`
2. Naviguez vers la page contenant la figure souhaitée
3. Utilisez l'outil "Modifier le PDF" (Outils → Modifier le PDF)
4. Sélectionnez l'image de la figure
5. Clic droit → "Copier l'image" ou "Exporter l'image"
6. Enregistrez avec le nom approprié dans `Chapitre3/images/logos/`

**Avantages:** Qualité maximale, extraction précise

### Méthode 2: PDF-XChange Editor

1. Ouvrez le PDF avec PDF-XChange Editor
2. Naviguez vers la page contenant la figure
3. Clic droit sur l'image → "Exporter l'image"
4. Choisissez le format PNG
5. Enregistrez avec le nom approprié

**Avantages:** Gratuit, simple d'utilisation

### Méthode 3: Capture d'écran haute résolution

1. Ouvrez le PDF à 200-300% de zoom
2. Utilisez l'outil Capture Windows (Win + Shift + S)
3. Sélectionnez précisément la figure
4. Collez dans un éditeur d'images (Paint, GIMP, Photoshop)
5. Enregistrez en PNG avec le nom approprié

**Avantages:** Rapide, fonctionne toujours

### Méthode 4: Script Python avec PyMuPDF (Avancé)

```python
import fitz  # PyMuPDF

# Ouvrir le PDF
pdf_path = "Optimisation intelligente de la planification de la production (3).pdf"
doc = fitz.open(pdf_path)

# Extraire les images d'une page spécifique
page_num = 35  # Ajuster selon la page de la figure
page = doc[page_num]

# Extraire toutes les images de la page
images = page.get_images()

for img_index, img in enumerate(images):
    xref = img[0]
    base_image = doc.extract_image(xref)
    image_bytes = base_image["image"]
    
    # Sauvegarder l'image
    with open(f"figure-28-data-science.png", "wb") as f:
        f.write(image_bytes)

doc.close()
```

**Installation PyMuPDF:**
```bash
pip install PyMuPDF
```

**Avantages:** Automatisé, extraction en masse possible

### Méthode 5: Convertisseur en ligne

1. Allez sur https://www.ilovepdf.com/pdf_to_jpg ou https://smallpdf.com/pdf-to-jpg
2. Uploadez le PDF
3. Sélectionnez "Extraire images" ou convertissez les pages spécifiques
4. Téléchargez les images
5. Renommez selon la convention

**Avantages:** Pas d'installation nécessaire

## Instructions détaillées par figure

### Figure 28 - Data Science (6 logos)
1. Localisez la Figure 28 dans le PDF (cherchez "Figure 28" ou naviguez vers les pages 35-40)
2. Cette figure contient les logos: pandas, NumPy, scikit-learn, XGBoost, matplotlib, seaborn
3. Extrayez l'image complète avec la méthode de votre choix
4. Enregistrez sous: `Chapitre3/images/logos/figure-28-data-science.png`

### Figure 31 - Backend (3 logos)
1. Localisez la Figure 31 dans le PDF (pages 40-45 estimées)
2. Cette figure contient les logos: FastAPI, Pydantic, uvicorn
3. Extrayez l'image complète
4. Enregistrez sous: `Chapitre3/images/logos/figure-31-backend.png`

### Figure 34 - Frontend (3 logos)
1. Localisez la Figure 34 dans le PDF (pages 45-50 estimées)
2. Cette figure contient les logos: React, Recharts, Axios
3. Extrayez l'image complète
4. Enregistrez sous: `Chapitre3/images/logos/figure-34-frontend.png`

### Figure 35 - DevOps/Optimization (5+ logos)
1. Localisez la Figure 35 dans le PDF (pages 50-55 estimées)
2. Cette figure contient les logos: OR-Tools, Docker, Git, pytest, PostgreSQL
3. Extrayez l'image complète
4. Enregistrez sous: `Chapitre3/images/logos/figure-35-devops.png`

## Vérification de la qualité

Après extraction, vérifiez que:
- [ ] Les 4 fichiers sont présents dans `Chapitre3/images/logos/`
- [ ] Les noms de fichiers correspondent exactement
- [ ] Les images sont lisibles et de bonne qualité
- [ ] La résolution est suffisante (pas de pixellisation)
- [ ] Les fichiers ne sont pas corrompus

## Astuce: Trouver les figures rapidement

Utilisez la fonction de recherche du lecteur PDF (Ctrl+F) et cherchez:
- "Figure 28"
- "Figure 31"
- "Figure 34"
- "Figure 35"

Cela vous amènera directement à la page contenant la figure.

## Dépannage

### Problème: Je ne trouve pas la figure dans le PDF
**Solution:** 
- Utilisez Ctrl+F et cherchez "Figure 28", "Figure 31", etc.
- Parcourez le Chapitre 3 du PDF (généralement pages 30-60)
- Vérifiez la table des figures au début du document

### Problème: L'image extraite est de mauvaise qualité
**Solution:** 
- Augmentez le zoom du PDF avant la capture d'écran (200-300%)
- Utilisez Adobe Acrobat ou PDF-XChange pour une extraction directe
- Essayez la méthode PyMuPDF pour une extraction native

### Problème: L'image contient du texte en plus des logos
**Solution:** 
- Utilisez un éditeur d'images (GIMP, Photoshop, Paint) pour recadrer
- Sélectionnez uniquement la partie contenant les logos
- Conservez les légendes si elles font partie intégrante de la figure

### Problème: Le fichier est trop volumineux
**Solution:** 
- Utilisez un compresseur PNG en ligne (TinyPNG, Compressor.io)
- Réduisez légèrement la résolution si nécessaire (mais gardez > 150 DPI)

## Contact

Pour toute question concernant l'extraction des figures, consultez:
- Documentation du design: `.kiro/specs/chapitre3-logos-enrichissement/design.md`
- Plan d'implémentation: `.kiro/specs/chapitre3-logos-enrichissement/tasks.md`

## Checklist finale

- [ ] Figure 28 (Data Science) extraite → `figure-28-data-science.png`
- [ ] Figure 31 (Backend) extraite → `figure-31-backend.png`
- [ ] Figure 34 (Frontend) extraite → `figure-34-frontend.png`
- [ ] Figure 35 (DevOps) extraite → `figure-35-devops.png`
- [ ] Tous les fichiers sont dans `Chapitre3/images/logos/`
- [ ] Les noms de fichiers sont corrects
- [ ] La qualité des images est vérifiée
- [ ] Les images sont lisibles et non corrompues

**Total: 4 figures à extraire**

## Prochaines étapes

Une fois les figures extraites:
1. Vérifiez que les 4 fichiers PNG sont dans `Chapitre3/images/logos/`
2. Ouvrez le fichier `Chapitre3/chapitre3.tex`
3. Suivez les tâches dans `.kiro/specs/chapitre3-logos-enrichissement/tasks.md`
4. Commencez par la tâche 2.1 pour insérer la première figure

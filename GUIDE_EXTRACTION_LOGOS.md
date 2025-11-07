# Guide d'extraction des logos depuis le PDF source

## Objectif

Extraire les figures 28, 31, 34, et 35 du PDF source pour les utiliser comme logos dans le Chapitre 3.

**Fichier source:** `C:\Users\HP\OneDrive\Bureau\Mémoire\Optimisation intelligente de la planification de la productioion (3).pdf`

## Méthode 1: Extraction automatique avec Python (Recommandée)

### Installation de PyMuPDF

```powershell
pip install PyMuPDF
```

### Exécution du script

```powershell
python extract_pdf_pages_pymupdf.py
```

Le script va:
1. Ouvrir le PDF source
2. Extraire les pages 28, 31, 34, 35
3. Les convertir en images PNG haute résolution (300 DPI)
4. Les sauvegarder dans `Chapitre3/images/extracted_logos/`

## Méthode 2: Extraction manuelle (Sans installation)

### Étape 1: Ouvrir le PDF source

Ouvrez le fichier PDF avec Adobe Acrobat Reader, Foxit Reader, ou votre lecteur PDF préféré.

### Étape 2: Capturer les pages

Pour chaque page (28, 31, 34, 35):

1. **Naviguez vers la page**
2. **Prenez une capture d'écran:**
   - Windows: `Win + Shift + S` (Outil Capture d'écran)
   - Ou: Utilisez l'outil de capture intégré au lecteur PDF
3. **Sauvegardez l'image:**
   - Format: PNG
   - Nom: `page_28.png`, `page_31.png`, `page_34.png`, `page_35.png`
   - Dossier: `Chapitre3/images/extracted_logos/`

### Étape 3: Améliorer la qualité (optionnel)

Si les captures d'écran ont une résolution insuffisante:
1. Zoomez à 200-300% dans le PDF avant de capturer
2. Ou utilisez l'option "Exporter en image" de votre lecteur PDF

## Méthode 3: Export depuis Adobe Acrobat

Si vous avez Adobe Acrobat Pro:

1. Ouvrez le PDF
2. Allez dans **Fichier > Exporter vers > Image > PNG**
3. Sélectionnez les pages 28, 31, 34, 35
4. Choisissez la résolution: **300 DPI**
5. Exportez dans `Chapitre3/images/extracted_logos/`

## Méthode 4: Utilisation d'outils en ligne

Sites web pour extraire des pages PDF:

1. **iLovePDF** - https://www.ilovepdf.com/fr/extraire-pages-pdf
2. **Smallpdf** - https://smallpdf.com/fr/extraire-pages-pdf
3. **PDF24** - https://tools.pdf24.org/fr/extraire-pages

Étapes:
1. Uploadez le PDF
2. Sélectionnez les pages 28, 31, 34, 35
3. Téléchargez les pages extraites
4. Convertissez-les en PNG si nécessaire

## Correspondance des pages avec les logos

Après extraction, vous devrez identifier quel logo correspond à quelle technologie:

| Page | Contenu probable | Destination |
|------|------------------|-------------|
| 28 | Logos Data Science? | `data-science/` |
| 31 | Logos Backend/Frontend? | `backend/` ou `frontend/` |
| 34 | Logos Optimisation? | `optimization/` |
| 35 | Logos DevOps? | `devops/` |

**Note:** Vérifiez le contenu de chaque page pour identifier les logos exacts.

## Après extraction

### Étape 1: Vérifier les images

```powershell
cd Chapitre3\images\extracted_logos\
dir
```

Vous devriez voir:
- `page_28.png`
- `page_31.png`
- `page_34.png`
- `page_35.png`

### Étape 2: Découper les logos individuels (si nécessaire)

Si une page contient plusieurs logos, vous devrez les découper:

**Option A: Avec Paint (Windows)**
1. Ouvrez l'image dans Paint
2. Utilisez l'outil de sélection pour isoler chaque logo
3. Copiez et collez dans une nouvelle image
4. Sauvegardez avec le nom approprié

**Option B: Avec GIMP (gratuit)**
1. Ouvrez l'image dans GIMP
2. Utilisez l'outil Rectangle de sélection
3. Image > Découper selon la sélection
4. Fichier > Exporter sous > PNG

**Option C: Avec un script Python**
Je peux créer un script pour découper automatiquement si vous me donnez les coordonnées.

### Étape 3: Renommer et organiser

Copiez les logos dans les bons dossiers avec les bons noms:

```powershell
# Exemple (ajustez selon le contenu réel)
copy Chapitre3\images\extracted_logos\page_28.png Chapitre3\images\logos\data-science\pandas-logo.png
copy Chapitre3\images\extracted_logos\page_31.png Chapitre3\images\logos\backend\fastapi-logo.png
# etc.
```

### Étape 4: Recompiler le document

```powershell
pdflatex main.tex
```

Les logos devraient maintenant s'afficher dans le PDF!

## Dépannage

### Problème: PyMuPDF ne s'installe pas

**Solution 1:** Essayez avec pip:
```powershell
pip install --upgrade pip
pip install PyMuPDF
```

**Solution 2:** Utilisez la méthode manuelle (Méthode 2)

### Problème: Le PDF est protégé

**Solution:** Utilisez la méthode de capture d'écran (Méthode 2)

### Problème: La qualité est insuffisante

**Solution:** 
1. Augmentez le zoom avant la capture
2. Utilisez l'export natif du lecteur PDF
3. Augmentez le DPI dans le script Python (de 300 à 600)

### Problème: Les images sont trop grandes

**Solution:** Compressez-les avec:
```powershell
# Avec Python et Pillow
python -c "from PIL import Image; img = Image.open('input.png'); img.save('output.png', optimize=True, quality=85)"
```

## Script d'installation rapide

Si vous voulez installer PyMuPDF rapidement:

```powershell
# Installer PyMuPDF
pip install PyMuPDF

# Exécuter le script d'extraction
python extract_pdf_pages_pymupdf.py

# Vérifier les résultats
dir Chapitre3\images\extracted_logos\
```

## Alternative: Utiliser les logos officiels

Si l'extraction est trop complexe, vous pouvez toujours télécharger les logos officiels en suivant:
- `Chapitre3/images/logos/README.md`

Les logos officiels ont généralement:
- Meilleure qualité
- Fond transparent
- Format vectoriel (SVG)
- Taille optimale

## Besoin d'aide?

Si vous rencontrez des difficultés:
1. Vérifiez que le chemin du PDF est correct
2. Essayez la méthode manuelle (capture d'écran)
3. Consultez les logs d'erreur pour plus de détails

---

**Créé le:** 7 novembre 2025  
**Auteur:** Kiro AI Assistant

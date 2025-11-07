# Guide d'installation des packages LaTeX

Ce document explique comment installer MiKTeX et les packages nécessaires pour compiler le rapport.

## Méthode 1 : Installation automatique (Recommandée)

### Option A : Via PowerShell (en tant qu'administrateur)

1. Ouvrez PowerShell en tant qu'administrateur
2. Naviguez vers le répertoire du projet :
   ```powershell
   cd "C:\Users\HP\Downloads\rapport__2_"
   ```
3. Exécutez le script :
   ```powershell
   .\install_miktex_simple.ps1
   ```

### Option B : Installation complète des packages

```powershell
.\install_latex_packages.ps1
```

## Méthode 2 : Installation manuelle de MiKTeX

1. Téléchargez MiKTeX depuis : https://miktex.org/download
2. Installez MiKTeX (choisissez l'installation complète pour tous les utilisateurs)
3. Redémarrez votre terminal/PowerShell
4. Les packages seront installés automatiquement lors de la première compilation

## Méthode 3 : Via winget (Windows 10/11)

```powershell
winget install --id MiKTeX.MiKTeX
```

## Méthode 4 : Via Chocolatey (si installé)

```powershell
choco install miktex -y
```

## Compilation du document

Une fois MiKTeX installé, compilez le document avec :

```powershell
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Ou utilisez un éditeur LaTeX comme :
- **TeXstudio** (recommandé) : https://www.texstudio.org/
- **TeXmaker** : https://www.xm1math.net/texmaker/
- **Overleaf** (en ligne) : https://www.overleaf.com/

## Packages requis

Le document utilise les packages suivants (ils seront installés automatiquement par MiKTeX lors de la première compilation) :

- babel, babel-french
- fontenc, inputenc
- tabularx, longtable, array
- geometry, float
- tikz, pgf
- multirow, colortbl
- csquotes, textgreek
- xcolor, sectsty
- fancyhdr, enumitem
- url, hyperref
- graphicx, minitoc
- amsmath, amssymb, amsthm, mathrsfs
- lscape, tabulary, supertabular
- etoolbox, afterpage
- nomencl, setspace, adjustbox
- pdfpages, caption
- biblatex, biber

## Notes importantes

- **MiKTeX installera automatiquement les packages manquants** lors de la première compilation
- Si vous voyez des erreurs de packages manquants, MiKTeX vous demandera de les installer
- Assurez-vous d'avoir une connexion Internet pour télécharger les packages
- Après l'installation, redémarrez votre terminal pour que les commandes soient disponibles dans le PATH

## Vérification de l'installation

Vérifiez que LaTeX est installé :

```powershell
pdflatex --version
biber --version
```

Si ces commandes fonctionnent, l'installation est réussie !





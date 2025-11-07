# Script d'installation des packages LaTeX nécessaires pour le rapport
# Ce script installe MiKTeX et tous les packages requis

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Installation des packages LaTeX" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Liste des packages nécessaires
$packages = @(
    "babel",
    "babel-french",
    "fontenc",
    "inputenc",
    "tabularx",
    "longtable",
    "array",
    "geometry",
    "float",
    "tikz",
    "pgf",
    "multirow",
    "csquotes",
    "textgreek",
    "xcolor",
    "sectsty",
    "colortbl",
    "fancyhdr",
    "enumitem",
    "url",
    "hyperref",
    "graphicx",
    "minitoc",
    "amsthm",
    "amsmath",
    "amssymb",
    "mathrsfs",
    "lscape",
    "tabulary",
    "supertabular",
    "etoolbox",
    "afterpage",
    "nomencl",
    "setspace",
    "adjustbox",
    "pdfpages",
    "caption",
    "biblatex",
    "biber"
)

# Vérifier si MiKTeX est installé
$miktexPath = "C:\Program Files\MiKTeX\miktex\bin\x64\miktex.exe"
if (-not (Test-Path $miktexPath)) {
    Write-Host "MiKTeX n'est pas détecté dans le chemin standard." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Options d'installation:" -ForegroundColor Cyan
    Write-Host "1. Télécharger MiKTeX depuis: https://miktex.org/download" -ForegroundColor White
    Write-Host "2. Installer via Chocolatey (si installé): choco install miktex" -ForegroundColor White
    Write-Host "3. Installer via winget: winget install MiKTeX.MiKTeX" -ForegroundColor White
    Write-Host ""
    
    # Essayer winget
    $wingetAvailable = Get-Command winget -ErrorAction SilentlyContinue
    if ($wingetAvailable) {
        Write-Host "Tentative d'installation via winget..." -ForegroundColor Yellow
        winget install --id MiKTeX.MiKTeX --accept-source-agreements --accept-package-agreements
        Start-Sleep -Seconds 5
    }
    
    # Essayer chocolatey
    $chocoAvailable = Get-Command choco -ErrorAction SilentlyContinue
    if ($chocoAvailable) {
        Write-Host "Tentative d'installation via Chocolatey..." -ForegroundColor Yellow
        choco install miktex -y
        Start-Sleep -Seconds 5
    }
}

# Chercher miktex dans plusieurs emplacements
$miktexPaths = @(
    "C:\Program Files\MiKTeX\miktex\bin\x64\miktex.exe",
    "C:\Program Files\MiKTeX\miktex\bin\miktex.exe",
    "C:\Program Files (x86)\MiKTeX\miktex\bin\miktex.exe",
    "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\miktex.exe"
)

$miktexFound = $false
foreach ($path in $miktexPaths) {
    if (Test-Path $path) {
        $miktexPath = $path
        $miktexFound = $true
        Write-Host "MiKTeX trouvé: $path" -ForegroundColor Green
        break
    }
}

if (-not $miktexFound) {
    # Chercher dans le PATH
    $miktexInPath = Get-Command miktex -ErrorAction SilentlyContinue
    if ($miktexInPath) {
        $miktexPath = $miktexInPath.Source
        $miktexFound = $true
        Write-Host "MiKTeX trouvé dans PATH: $miktexPath" -ForegroundColor Green
    }
}

if (-not $miktexFound) {
    Write-Host ""
    Write-Host "ERREUR: MiKTeX n'a pas été trouvé." -ForegroundColor Red
    Write-Host "Veuillez installer MiKTeX manuellement depuis: https://miktex.org/download" -ForegroundColor Yellow
    Write-Host "Après l'installation, relancez ce script." -ForegroundColor Yellow
    exit 1
}

# Trouver le répertoire MiKTeX
$miktexDir = Split-Path (Split-Path $miktexPath)
$packageManagerPath = Join-Path $miktexDir "bin\x64\miktex-package-manager.exe"
if (-not (Test-Path $packageManagerPath)) {
    $packageManagerPath = Join-Path $miktexDir "bin\miktex-package-manager.exe"
}

# Ajouter MiKTeX au PATH pour cette session
$miktexBinPath = Join-Path $miktexDir "bin\x64"
if (Test-Path $miktexBinPath) {
    $env:PATH = "$miktexBinPath;$env:PATH"
} else {
    $miktexBinPath = Join-Path $miktexDir "bin"
    $env:PATH = "$miktexBinPath;$env:PATH"
}

Write-Host ""
Write-Host "Installation des packages LaTeX..." -ForegroundColor Cyan
Write-Host ""

# Utiliser miktex-package-manager pour installer les packages
foreach ($package in $packages) {
    Write-Host "Installation de $package..." -ForegroundColor Yellow -NoNewline
    try {
        # Utiliser miktex packages install
        $result = & "$miktexBinPath\miktex" packages install $package --auto-yes 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host " ✓" -ForegroundColor Green
        } else {
            Write-Host " ✗ (peut être déjà installé)" -ForegroundColor Yellow
        }
    } catch {
        Write-Host " ✗ (erreur)" -ForegroundColor Red
        Write-Host "   Erreur: $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Mise à jour du FNDB (File Name Database)..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

try {
    & "$miktexBinPath\miktex" fndb refresh 2>&1 | Out-Null
    Write-Host "FNDB mis à jour avec succès." -ForegroundColor Green
} catch {
    Write-Host "Attention: impossible de mettre à jour le FNDB." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Installation terminée!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Packages installés:" -ForegroundColor Cyan
$packages | ForEach-Object { Write-Host "  - $_" -ForegroundColor White }

Write-Host ""
Write-Host "Note: Si certains packages ne sont pas installés," -ForegroundColor Yellow
Write-Host "      MiKTeX les installera automatiquement lors de la première compilation." -ForegroundColor Yellow
Write-Host ""
Write-Host "Pour compiler le document, exécutez:" -ForegroundColor Cyan
Write-Host "  pdflatex main.tex" -ForegroundColor White
Write-Host "  biber main" -ForegroundColor White
Write-Host "  pdflatex main.tex" -ForegroundColor White
Write-Host "  pdflatex main.tex" -ForegroundColor White
Write-Host ""





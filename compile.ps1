# Script de compilation automatique du rapport LaTeX
# Ce script execute toutes les etapes necessaires pour compiler le document

# Configurer l'encodage UTF-8 pour la console
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 | Out-Null

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Compilation du rapport LaTeX" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Recharger le PATH
$env:PATH = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Chemin vers pdflatex et biber
$pdflatex = "C:\Users\HP\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
$biber = "C:\Users\HP\AppData\Local\Programs\MiKTeX\miktex\bin\x64\biber.exe"

# Verifier que les commandes existent
if (-not (Test-Path $pdflatex)) {
    Write-Host "ERREUR: pdflatex non trouve!" -ForegroundColor Red
    Write-Host "Veuillez installer MiKTeX ou verifier le chemin." -ForegroundColor Yellow
    exit 1
}

if (-not (Test-Path $biber)) {
    Write-Host "ERREUR: biber non trouve!" -ForegroundColor Red
    exit 1
}

Write-Host "Etape 1/4: Premiere compilation (pdflatex)..." -ForegroundColor Yellow
& $pdflatex -interaction=nonstopmode main.tex | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Avertissement: La premiere compilation peut avoir des erreurs de references (normal)" -ForegroundColor Yellow
}

Write-Host "Etape 2/4: Traitement de la bibliographie (biber)..." -ForegroundColor Yellow
& $biber main | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Avertissement: Des erreurs peuvent survenir si la bibliographie a des problemes" -ForegroundColor Yellow
}

Write-Host "Etape 3/4: Deuxieme compilation (pdflatex)..." -ForegroundColor Yellow
& $pdflatex -interaction=nonstopmode main.tex | Out-Null

Write-Host "Etape 4/4: Troisieme compilation finale (pdflatex)..." -ForegroundColor Yellow
& $pdflatex -interaction=nonstopmode main.tex | Out-Null

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Compilation terminee!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

if (Test-Path "main.pdf") {
    $pdfSize = (Get-Item "main.pdf").Length / 1MB
    Write-Host "PDF genere: main.pdf ($([math]::Round($pdfSize, 2)) MB)" -ForegroundColor Green
} else {
    Write-Host "ATTENTION: Le fichier main.pdf n'a pas ete genere!" -ForegroundColor Red
    Write-Host "Verifiez le fichier main.log pour les erreurs." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Note: MiKTeX installe automatiquement les packages manquants." -ForegroundColor Cyan
Write-Host "      La premiere compilation peut prendre plus de temps." -ForegroundColor Cyan




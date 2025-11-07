# Script simplifié pour installer MiKTeX et compiler le document
# Exécutez ce script en tant qu'administrateur

Write-Host "Installation de MiKTeX..." -ForegroundColor Cyan

# Vérifier si winget est disponible
$winget = Get-Command winget -ErrorAction SilentlyContinue
if ($winget) {
    Write-Host "Installation via winget..." -ForegroundColor Yellow
    winget install --id MiKTeX.MiKTeX --accept-source-agreements --accept-package-agreements --silent
} else {
    Write-Host "winget n'est pas disponible. Veuillez installer MiKTeX manuellement:" -ForegroundColor Yellow
    Write-Host "https://miktex.org/download" -ForegroundColor Cyan
    exit 1
}

Write-Host ""
Write-Host "MiKTeX installé. Les packages seront installés automatiquement lors de la première compilation." -ForegroundColor Green
Write-Host ""
Write-Host "Note: Redémarrez votre terminal après l'installation pour que les commandes soient disponibles." -ForegroundColor Yellow





# Script pour corriger l'encodage des fichiers LaTeX
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "Correction de l'encodage du fichier chapitre2.tex..." -ForegroundColor Cyan

# Lire le fichier avec l'encodage par defaut
$content = [System.IO.File]::ReadAllText("Chapitre2/chapitre2.tex", [System.Text.Encoding]::Default)

# Remplacer les caracteres mal encodes
$replacements = @{
    'Ã©' = 'é'
    'Ã¨' = 'è'
    'Ãª' = 'ê'
    'Ã ' = 'à'
    'Ã´' = 'ô'
    'Ã»' = 'û'
    'Ã§' = 'ç'
    'Ã¯' = 'ï'
    'Ã®' = 'î'
    'Ã¢' = 'â'
    'Ã‰' = 'É'
    'Ã€' = 'À'
    'Å"' = 'œ'
    'â€™' = "'"
    'â€"' = '—'
    'â€"' = '–'
}

foreach ($key in $replacements.Keys) {
    $content = $content -replace [regex]::Escape($key), $replacements[$key]
}

# Sauvegarder avec UTF-8
[System.IO.File]::WriteAllText("Chapitre2/chapitre2.tex", $content, [System.Text.Encoding]::UTF8)

Write-Host "Encodage corrige!" -ForegroundColor Green

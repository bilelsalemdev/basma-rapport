# Script pour corriger l'encodage des fichiers LaTeX
# Convertit les caractères mal encodés en UTF-8 correct

$files = Get-ChildItem -Path . -Filter *.tex -Recurse

foreach ($file in $files) {
    Write-Host "Traitement de: $($file.FullName)"
    
    # Lire le contenu avec l'encodage UTF-8
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    
    # Corrections des caractères mal encodés
    $content = $content -replace 'Ã ', 'à'
    $content = $content -replace 'Ã¢', 'â'
    $content = $content -replace 'Ã©', 'é'
    $content = $content -replace 'Ã¨', 'è'
    $content = $content -replace 'Ãª', 'ê'
    $content = $content -replace 'Ã«', 'ë'
    $content = $content -replace 'Ã®', 'î'
    $content = $content -replace 'Ã¯', 'ï'
    $content = $content -replace 'Ã´', 'ô'
    $content = $content -replace 'Ã¹', 'ù'
    $content = $content -replace 'Ã»', 'û'
    $content = $content -replace 'Ã§', 'ç'
    $content = $content -replace 'Ã‰', 'É'
    $content = $content -replace 'Ãˆ', 'È'
    $content = $content -replace 'ÃŠ', 'Ê'
    $content = $content -replace 'Ã€', 'À'
    $content = $content -replace 'Ã‚', 'Â'
    $content = $content -replace 'Ã‡', 'Ç'
    $content = $content -replace 'Ã"', 'Ô'
    $content = $content -replace 'Ã›', 'Û'
    $content = $content -replace 'Ã™', 'Ù'
    $content = $content -replace 'Ã', 'Î'
    $content = $content -replace 'Ã‹', 'Ë'
    
    # Corrections spécifiques pour les apostrophes et guillemets
    $content = $content -replace 'â€™', "'"
    $content = $content -replace 'â€œ', '"'
    $content = $content -replace 'â€', '"'
    $content = $content -replace 'â€"', '—'
    $content = $content -replace 'â€"', '–'
    $content = $content -replace 'â€¦', '...'
    
    # Corrections pour les caractères spéciaux de l'erreur
    $content = $content -replace 'Ã\x{0080}', 'à'
    $content = $content -replace 'Ã\x{0099}', "'"
    $content = $content -replace 'Ã\x{0089}', 'É'
    $content = $content -replace 'Ã\x{0093}', 'œ'
    $content = $content -replace 'Å"', 'œ'
    $content = $content -replace 'Å ', 'Œ'
    
    # Corrections pour les séquences problématiques identifiées
    $content = $content -replace 'lâ', "l'"
    $content = $content -replace 'dâ', "d'"
    $content = $content -replace 'sâ', "s'"
    $content = $content -replace 'câ', "c'"
    $content = $content -replace 'nâ', "n'"
    $content = $content -replace 'mâ', "m'"
    $content = $content -replace 'tâ', "t'"
    $content = $content -replace 'jâ', "j'"
    $content = $content -replace 'quâ', "qu'"
    $content = $content -replace 'jusquâ', "jusqu'"
    
    # Corrections pour les majuscules avec apostrophe
    $content = $content -replace 'Lâ', "L'"
    $content = $content -replace 'Dâ', "D'"
    $content = $content -replace 'Sâ', "S'"
    $content = $content -replace 'Câ', "C'"
    $content = $content -replace 'Nâ', "N'"
    
    # Corrections pour "Ê" qui devrait être "ê"
    $content = $content -replace 'enquÊte', 'enquête'
    $content = $content -replace 'Être', 'être'
    
    # Corrections pour "oÃ¹"
    $content = $content -replace 'oÃ¹', 'où'
    
    # Corrections pour les caractères de boîte Unicode
    $content = $content -replace '├', '|'
    $content = $content -replace '─', '-'
    $content = $content -replace '│', '|'
    $content = $content -replace '└', '+'
    $content = $content -replace '≥', '>='
    
    # Supprimer le BOM UTF-8 si présent
    $content = $content -replace '^\xEF\xBB\xBF', ''
    $content = $content -replace '^ï»¿', ''
    
    # Écrire le contenu corrigé
    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.UTF8Encoding]::new($false))
    
    Write-Host "Corrigé: $($file.FullName)" -ForegroundColor Green
}

Write-Host "`nTerminé! Tous les fichiers .tex ont été traités." -ForegroundColor Cyan

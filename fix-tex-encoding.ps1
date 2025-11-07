# Script to fix LaTeX file encoding issues
$ErrorActionPreference = "Stop"

$replacements = @{
    'lâ' = "l'"
    'dâ' = "d'"
    'sâ' = "s'"
    'câ' = "c'"
    'nâ' = "n'"
    'mâ' = "m'"
    'tâ' = "t'"
    'jâ' = "j'"
    'quâ' = "qu'"
    'jusquâ' = "jusqu'"
    'Lâ' = "L'"
    'Dâ' = "D'"
    'Sâ' = "S'"
    'Câ' = "C'"
    'Nâ' = "N'"
    'enquÊte' = 'enquete'
    'Être' = 'etre'
    'Å"' = 'oe'
    'Å ' = 'Oe'
    'â€™' = "'"
    'â€œ' = '"'
    'â€' = '"'
}

$files = Get-ChildItem -Path . -Filter *.tex -Recurse

foreach ($file in $files) {
    Write-Host "Processing: $($file.Name)"
    
    try {
        $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
        
        foreach ($key in $replacements.Keys) {
            $content = $content -replace [regex]::Escape($key), $replacements[$key]
        }
        
        # Remove BOM
        if ($content.StartsWith([char]0xFEFF)) {
            $content = $content.Substring(1)
        }
        
        $utf8NoBom = New-Object System.Text.UTF8Encoding $false
        [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
        
        Write-Host "Fixed: $($file.Name)" -ForegroundColor Green
    }
    catch {
        Write-Host "Error processing $($file.Name): $_" -ForegroundColor Red
    }
}

Write-Host "`nDone!" -ForegroundColor Cyan

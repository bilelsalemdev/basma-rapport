# Script pour pivoter le PDF dans le sens normal (portrait)
# Utilise PyPDF2 pour la rotation

$pythonScript = @"
import sys
try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("Installation de PyPDF2...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf(input_path, output_path, rotation=0):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        # Obtenir la rotation actuelle
        current_rotation = page.get('/Rotate', 0)
        print(f"Rotation actuelle de la page: {current_rotation} degrés")
        
        # Pivoter la page (0 = portrait normal)
        if rotation != 0:
            page.rotate(rotation)
        elif current_rotation != 0:
            # Remettre à 0 (portrait normal)
            page.rotate(-current_rotation)
        
        writer.add_page(page)
    
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"PDF pivoté sauvegardé: {output_path}")

if __name__ == "__main__":
    rotate_pdf("main.pdf", "main_rotated.pdf", 0)
"@

# Sauvegarder le script Python temporaire
$pythonScript | Out-File -FilePath "rotate_pdf_temp.py" -Encoding UTF8

# Exécuter le script Python
Write-Host "Rotation du PDF en cours..."
python rotate_pdf_temp.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "Rotation réussie!"
    Write-Host "Remplacement de main.pdf par la version pivotée..."
    
    # Sauvegarder l'original
    if (Test-Path "main.pdf") {
        Copy-Item "main.pdf" "main_backup.pdf" -Force
        Write-Host "Backup créé: main_backup.pdf"
    }
    
    # Remplacer par la version pivotée
    if (Test-Path "main_rotated.pdf") {
        Move-Item "main_rotated.pdf" "main.pdf" -Force
        Write-Host "main.pdf a été pivoté dans le sens normal (portrait)"
    }
    
    # Nettoyer
    Remove-Item "rotate_pdf_temp.py" -ErrorAction SilentlyContinue
} else {
    Write-Host "Erreur lors de la rotation du PDF" -ForegroundColor Red
}

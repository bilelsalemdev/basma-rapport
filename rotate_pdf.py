import sys
import os

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("Installation de PyPDF2...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf(input_path, output_path):
    print(f"Lecture de {input_path}...")
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"Nombre de pages: {total_pages}")
    
    for i, page in enumerate(reader.pages, 1):
        # Obtenir la rotation actuelle
        current_rotation = page.get('/Rotate', 0)
        if i == 1:
            print(f"Rotation actuelle des pages: {current_rotation} degrés")
        
        # Remettre à 0 (portrait normal) si nécessaire
        if current_rotation != 0:
            page.rotate(-current_rotation)
        
        writer.add_page(page)
        
        if i % 20 == 0:
            print(f"Traitement: {i}/{total_pages} pages...")
    
    print(f"Sauvegarde du PDF pivoté...")
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"✓ PDF pivoté sauvegardé: {output_path}")
    return True

if __name__ == "__main__":
    try:
        # Pivoter le PDF
        if rotate_pdf("main.pdf", "main_rotated.pdf"):
            # Créer un backup
            if os.path.exists("main.pdf"):
                import shutil
                shutil.copy2("main.pdf", "main_backup.pdf")
                print("✓ Backup créé: main_backup.pdf")
            
            # Remplacer par la version pivotée
            if os.path.exists("main_rotated.pdf"):
                os.replace("main_rotated.pdf", "main.pdf")
                print("✓ main.pdf a été pivoté dans le sens normal (portrait)")
        
    except Exception as e:
        print(f"Erreur: {e}")
        sys.exit(1)

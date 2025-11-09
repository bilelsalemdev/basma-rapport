import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def rotate_specific_page(input_path, output_path, page_number, rotation=90):
    """
    Pivote une page spécifique du PDF
    page_number: numéro de la page (commence à 1)
    rotation: angle de rotation (90 = paysage vers la droite)
    """
    print(f"Lecture de {input_path}...")
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"Nombre total de pages: {total_pages}")
    
    if page_number > total_pages or page_number < 1:
        print(f"Erreur: La page {page_number} n'existe pas!")
        return False
    
    for i, page in enumerate(reader.pages, 1):
        if i == page_number:
            # Pivoter cette page
            current_rotation = page.get('/Rotate', 0)
            print(f"Page {i}: Rotation actuelle = {current_rotation}°")
            print(f"Page {i}: Application d'une rotation de {rotation}°")
            page.rotate(rotation)
        
        writer.add_page(page)
    
    print(f"Sauvegarde du PDF modifié...")
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"✓ PDF modifié sauvegardé: {output_path}")
    return True

if __name__ == "__main__":
    try:
        # Pivoter la page 42 en paysage (90° vers la droite)
        if rotate_specific_page("main.pdf", "main_rotated.pdf", 42, 90):
            # Créer un backup
            if os.path.exists("main.pdf"):
                import shutil
                if not os.path.exists("main_backup_original.pdf"):
                    shutil.copy2("main.pdf", "main_backup_original.pdf")
                    print("✓ Backup de l'original créé: main_backup_original.pdf")
            
            # Remplacer par la version modifiée
            if os.path.exists("main_rotated.pdf"):
                os.replace("main_rotated.pdf", "main.pdf")
                print("✓ La page 42 de main.pdf est maintenant en orientation horizontale")
        
    except Exception as e:
        print(f"Erreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

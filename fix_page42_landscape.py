import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def fix_page_landscape(input_path, output_path, page_number):
    """
    Met la page en mode paysage avec le contenu dans le bon sens
    et ajusté aux dimensions horizontales
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
            print(f"\n=== Traitement de la page {i} ===")
            
            # Obtenir la rotation actuelle
            current_rotation = page.get('/Rotate', 0)
            print(f"Rotation actuelle: {current_rotation}°")
            
            # Obtenir les dimensions
            media_box = page.mediabox
            page_width = float(media_box.width)
            page_height = float(media_box.height)
            print(f"Dimensions: {page_width:.1f} x {page_height:.1f}")
            
            # Remettre à 0 d'abord si nécessaire
            if current_rotation != 0:
                page.rotate(-current_rotation)
                print(f"Remise à 0°")
            
            # Appliquer rotation de -90° pour paysage dans le bon sens
            # -90° = rotation antihoraire = contenu lisible en mode paysage
            page.rotate(-90)
            print(f"Application rotation: -90° (paysage, sens de lecture correct)")
            print(f"Le contenu est maintenant lisible horizontalement")
        
        writer.add_page(page)
    
    print(f"\nSauvegarde du PDF modifié...")
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"✓ PDF modifié sauvegardé: {output_path}")
    return True

if __name__ == "__main__":
    try:
        print("=== Mise en paysage de la page 42 (sens correct) ===\n")
        
        if fix_page_landscape("main.pdf", "main_rotated.pdf", 42):
            # Créer un backup
            if os.path.exists("main.pdf"):
                import shutil
                backup_name = "main_backup_landscape.pdf"
                shutil.copy2("main.pdf", backup_name)
                print(f"✓ Backup créé: {backup_name}")
            
            # Remplacer par la version modifiée
            if os.path.exists("main_rotated.pdf"):
                os.replace("main_rotated.pdf", "main.pdf")
                print(f"\n✓ La page 42 est maintenant:")
                print(f"  - En mode paysage (landscape)")
                print(f"  - Contenu lisible horizontalement")
                print(f"  - Ajusté aux dimensions horizontales de la page")
        
    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

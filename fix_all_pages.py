import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def fix_all_pages_except_42(input_path, output_path):
    """
    Remet toutes les pages en mode portrait normal (0°)
    SAUF la page 42 qui reste en mode paysage
    """
    print(f"Lecture de {input_path}...")
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"Nombre total de pages: {total_pages}\n")
    
    for i, page in enumerate(reader.pages, 1):
        # Obtenir la rotation actuelle
        current_rotation = page.get('/Rotate', 0)
        
        if i == 42:
            # Page 42 : la mettre en paysage (270° ou -90°)
            if current_rotation != 270:
                # Remettre à 0 d'abord
                if current_rotation != 0:
                    page.rotate(-current_rotation)
                # Puis mettre en paysage
                page.rotate(270)  # 270° = -90° = paysage lisible
                print(f"Page {i}: Mode PAYSAGE (270°)")
        else:
            # Toutes les autres pages : mode portrait normal (0°)
            if current_rotation != 0:
                page.rotate(-current_rotation)
                if i <= 5 or i >= total_pages - 2:  # Afficher quelques exemples
                    print(f"Page {i}: Remise en mode PORTRAIT (0°) - était à {current_rotation}°")
        
        writer.add_page(page)
        
        # Afficher progression
        if i % 50 == 0:
            print(f"Traitement: {i}/{total_pages} pages...")
    
    print(f"\nSauvegarde du PDF corrigé...")
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"✓ PDF corrigé sauvegardé: {output_path}")
    return True

if __name__ == "__main__":
    try:
        print("=== Correction de toutes les pages ===")
        print("Toutes les pages → Portrait (0°)")
        print("Page 42 uniquement → Paysage (270°)\n")
        
        if fix_all_pages_except_42("main.pdf", "main_fixed.pdf"):
            # Créer un backup
            if os.path.exists("main.pdf"):
                import shutil
                backup_name = "main_backup_final.pdf"
                shutil.copy2("main.pdf", backup_name)
                print(f"✓ Backup créé: {backup_name}")
            
            # Remplacer par la version corrigée
            if os.path.exists("main_fixed.pdf"):
                os.replace("main_fixed.pdf", "main.pdf")
                print(f"\n✓ Correction terminée:")
                print(f"  - Toutes les pages sont en mode portrait normal")
                print(f"  - La page 42 est en mode paysage")
        
    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

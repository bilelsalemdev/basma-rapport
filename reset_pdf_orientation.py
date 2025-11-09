import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def reset_all_pages_to_portrait(input_path, output_path):
    """
    Remet TOUTES les pages en mode portrait normal (0°)
    Aucune exception, toutes les pages seront en mode normal
    """
    print(f"Lecture de {input_path}...")
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"Nombre total de pages: {total_pages}\n")
    
    pages_modifiees = 0
    
    for i, page in enumerate(reader.pages, 1):
        # Obtenir la rotation actuelle
        current_rotation = page.get('/Rotate', 0)
        
        # Remettre TOUTES les pages à 0° (portrait normal)
        if current_rotation != 0:
            page.rotate(-current_rotation)
            pages_modifiees += 1
            if i <= 10 or i == 42 or i >= total_pages - 5:
                print(f"Page {i}: {current_rotation}° → 0° (portrait normal)")
        
        writer.add_page(page)
        
        # Afficher progression
        if i % 50 == 0:
            print(f"Traitement: {i}/{total_pages} pages...")
    
    print(f"\nSauvegarde du PDF corrigé...")
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"\n✓ PDF corrigé sauvegardé: {output_path}")
    print(f"✓ {pages_modifiees} pages ont été remises en mode portrait normal")
    return True

if __name__ == "__main__":
    try:
        print("=== Remise de TOUTES les pages en mode portrait normal ===\n")
        
        if reset_all_pages_to_portrait("main.pdf", "main_portrait.pdf"):
            # Créer un backup
            if os.path.exists("main.pdf"):
                import shutil
                backup_name = "main_backup_before_reset.pdf"
                if not os.path.exists(backup_name):
                    shutil.copy2("main.pdf", backup_name)
                    print(f"✓ Backup créé: {backup_name}")
            
            # Remplacer par la version corrigée
            if os.path.exists("main_portrait.pdf"):
                os.replace("main_portrait.pdf", "main.pdf")
                print(f"\n✓ TERMINÉ: Toutes les pages de main.pdf sont maintenant en mode portrait normal (0°)")
                print(f"✓ Le PDF ne devrait plus s'inverser")
        
    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

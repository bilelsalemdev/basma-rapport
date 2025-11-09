import sys
import os
from PyPDF2 import PdfReader, PdfWriter, Transformation

def scale_page_42(input_path, output_path, scale_factor=0.75):
    """
    Réduit la taille du contenu de la page 42 pour voir toutes les informations
    scale_factor: 0.75 = 75% de la taille (réduction de 25%)
    """
    print(f"Lecture de {input_path}...")
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"Nombre total de pages: {total_pages}\n")
    
    for i, page in enumerate(reader.pages, 1):
        if i == 42:
            print(f"=== Traitement de la page {i} ===")
            
            # Obtenir les dimensions
            media_box = page.mediabox
            page_width = float(media_box.width)
            page_height = float(media_box.height)
            print(f"Dimensions de la page: {page_width:.1f} x {page_height:.1f}")
            
            # Calculer le décalage pour centrer le contenu réduit
            # Après réduction, on centre le contenu
            tx = (page_width - page_width * scale_factor) / 2
            ty = (page_height - page_height * scale_factor) / 2
            
            # Appliquer la transformation: réduction + centrage
            op = Transformation().scale(sx=scale_factor, sy=scale_factor).translate(tx=tx, ty=ty)
            page.add_transformation(op)
            
            print(f"Réduction appliquée: {int(scale_factor * 100)}% de la taille originale")
            print(f"Réduction de {int((1 - scale_factor) * 100)}%")
            print(f"Contenu centré sur la page")
        
        writer.add_page(page)
    
    print(f"\nSauvegarde du PDF modifié...")
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"✓ PDF modifié sauvegardé: {output_path}")
    return True

if __name__ == "__main__":
    try:
        print("=== Réduction de la page 42 pour voir toutes les informations ===\n")
        
        # Réduire à 75% (vous pouvez ajuster: 0.7 = 70%, 0.8 = 80%, etc.)
        scale = 0.75
        
        if scale_page_42("main.pdf", "main_scaled.pdf", scale):
            # Créer un backup
            if os.path.exists("main.pdf"):
                import shutil
                backup_name = "main_backup_before_scale42.pdf"
                shutil.copy2("main.pdf", backup_name)
                print(f"✓ Backup créé: {backup_name}")
            
            # Remplacer par la version modifiée
            if os.path.exists("main_scaled.pdf"):
                os.replace("main_scaled.pdf", "main.pdf")
                print(f"\n✓ Page 42 modifiée:")
                print(f"  - Contenu réduit à {int(scale * 100)}%")
                print(f"  - Toutes les informations devraient être visibles")
                print(f"  - Contenu centré sur la page")
        
    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

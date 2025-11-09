import sys
import os
from PyPDF2 import PdfReader, PdfWriter, Transformation

def center_and_scale_page(input_path, output_path, page_number, scale_factor=1.3):
    """
    Centre et agrandit une page spécifique du PDF
    page_number: numéro de la page (commence à 1)
    scale_factor: facteur d'agrandissement (1.3 = 130% de la taille originale)
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
            
            # Obtenir les dimensions de la page
            media_box = page.mediabox
            page_width = float(media_box.width)
            page_height = float(media_box.height)
            print(f"Dimensions originales: {page_width:.1f} x {page_height:.1f}")
            
            # Pivoter d'abord en paysage (90°)
            page.rotate(90)
            print(f"Rotation: 90° (paysage)")
            
            # Après rotation, les dimensions sont inversées
            rotated_width = page_height
            rotated_height = page_width
            
            # Calculer le nouveau centre après mise à l'échelle
            # On centre le contenu agrandi sur la page
            tx = (rotated_width - rotated_width * scale_factor) / 2
            ty = (rotated_height - rotated_height * scale_factor) / 2
            
            # Créer la transformation: mise à l'échelle + centrage
            op = Transformation().scale(sx=scale_factor, sy=scale_factor).translate(tx=tx, ty=ty)
            page.add_transformation(op)
            
            print(f"Mise à l'échelle: {scale_factor}x (agrandissement de {int((scale_factor-1)*100)}%)")
            print(f"Centrage appliqué")
        
        writer.add_page(page)
    
    print(f"\nSauvegarde du PDF modifié...")
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"✓ PDF modifié sauvegardé: {output_path}")
    return True

if __name__ == "__main__":
    try:
        # Demander le facteur d'agrandissement
        print("=== Centrage et agrandissement de la page 42 ===\n")
        
        # Utiliser un facteur de 1.3 (30% plus grand) par défaut
        scale = 1.3
        
        if center_and_scale_page("main.pdf", "main_rotated.pdf", 42, scale):
            # Créer un backup
            if os.path.exists("main.pdf"):
                import shutil
                backup_name = "main_backup_before_scale.pdf"
                if not os.path.exists(backup_name):
                    shutil.copy2("main.pdf", backup_name)
                    print(f"✓ Backup créé: {backup_name}")
            
            # Remplacer par la version modifiée
            if os.path.exists("main_rotated.pdf"):
                os.replace("main_rotated.pdf", "main.pdf")
                print(f"\n✓ La page 42 est maintenant:")
                print(f"  - En orientation horizontale (paysage)")
                print(f"  - Agrandie de {int((scale-1)*100)}%")
                print(f"  - Centrée sur la page")
        
    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

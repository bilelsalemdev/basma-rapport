#!/usr/bin/env python3
"""
Script pour extraire des pages spécifiques d'un PDF et les convertir en images
"""
import sys

try:
    from pdf2image import convert_from_path
    print("✓ pdf2image est installé")
except ImportError:
    print("✗ pdf2image n'est pas installé")
    print("Installation: pip install pdf2image")
    sys.exit(1)

try:
    from PIL import Image
    print("✓ Pillow est installé")
except ImportError:
    print("✗ Pillow n'est pas installé")
    print("Installation: pip install Pillow")
    sys.exit(1)

# Configuration
pdf_path = r"C:\Users\HP\OneDrive\Bureau\Mémoire\Optimisation intelligente de la planification de la productioion (3).pdf"
pages_to_extract = [28, 31, 34, 35]  # Pages à extraire
output_dir = "Chapitre3/images/extracted_logos"

import os
os.makedirs(output_dir, exist_ok=True)

print(f"\n📄 Extraction des pages {pages_to_extract} depuis:")
print(f"   {pdf_path}")
print(f"\n📁 Dossier de sortie: {output_dir}")

try:
    # Extraire les pages spécifiques
    for page_num in pages_to_extract:
        print(f"\n🔄 Extraction de la page {page_num}...")
        
        # Convertir la page en image (DPI élevé pour qualité)
        images = convert_from_path(
            pdf_path,
            first_page=page_num,
            last_page=page_num,
            dpi=300  # Haute résolution pour impression
        )
        
        if images:
            image = images[0]
            output_path = os.path.join(output_dir, f"page_{page_num}.png")
            image.save(output_path, "PNG")
            print(f"   ✓ Sauvegardé: {output_path}")
            print(f"   📐 Dimensions: {image.size[0]}x{image.size[1]} pixels")
        else:
            print(f"   ✗ Erreur: Impossible d'extraire la page {page_num}")
    
    print("\n✅ Extraction terminée!")
    print(f"\n📊 Résumé:")
    print(f"   - Pages extraites: {len(pages_to_extract)}")
    print(f"   - Dossier: {output_dir}")
    
except FileNotFoundError:
    print(f"\n✗ Erreur: Le fichier PDF n'a pas été trouvé:")
    print(f"   {pdf_path}")
    print("\n💡 Vérifiez que le chemin est correct.")
    sys.exit(1)
    
except Exception as e:
    print(f"\n✗ Erreur lors de l'extraction: {e}")
    print(f"\n💡 Assurez-vous que:")
    print("   1. Le PDF n'est pas protégé par mot de passe")
    print("   2. Poppler est installé (requis pour pdf2image)")
    print("   3. Le chemin du PDF est correct")
    sys.exit(1)

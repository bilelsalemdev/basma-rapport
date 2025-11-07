#!/usr/bin/env python3
"""
Script pour extraire des pages spécifiques d'un PDF et les convertir en images
Utilise PyMuPDF (fitz) - plus simple que pdf2image
"""
import sys
import os

try:
    import fitz  # PyMuPDF
    print("✓ PyMuPDF est installé")
except ImportError:
    print("✗ PyMuPDF n'est pas installé")
    print("\n📦 Installation:")
    print("   pip install PyMuPDF")
    print("\nOu:")
    print("   pip install pymupdf")
    sys.exit(1)

# Configuration
pdf_path = r"C:\Users\HP\OneDrive\Bureau\Mémoire\Optimisation intelligente de la planification de la productioion (3).pdf"
pages_to_extract = [28, 31, 34, 35]  # Pages à extraire (numérotation 1-based)
output_dir = "Chapitre3/images/extracted_logos"

# Créer le dossier de sortie
os.makedirs(output_dir, exist_ok=True)

print(f"\n📄 Extraction des pages {pages_to_extract} depuis:")
print(f"   {pdf_path}")
print(f"\n📁 Dossier de sortie: {output_dir}")

try:
    # Ouvrir le PDF
    pdf_document = fitz.open(pdf_path)
    total_pages = pdf_document.page_count
    print(f"\n📖 PDF ouvert: {total_pages} pages au total")
    
    # Extraire chaque page
    for page_num in pages_to_extract:
        if page_num > total_pages:
            print(f"\n⚠️  Page {page_num} n'existe pas (PDF a {total_pages} pages)")
            continue
            
        print(f"\n🔄 Extraction de la page {page_num}...")
        
        # Obtenir la page (index 0-based, donc page_num - 1)
        page = pdf_document[page_num - 1]
        
        # Convertir en image avec haute résolution
        # zoom=2.0 donne environ 144 DPI, zoom=3.0 donne environ 216 DPI
        mat = fitz.Matrix(3.0, 3.0)  # Zoom 3x pour haute qualité
        pix = page.get_pixmap(matrix=mat)
        
        # Sauvegarder l'image
        output_path = os.path.join(output_dir, f"page_{page_num}.png")
        pix.save(output_path)
        
        print(f"   ✓ Sauvegardé: {output_path}")
        print(f"   📐 Dimensions: {pix.width}x{pix.height} pixels")
        print(f"   💾 Taille: {os.path.getsize(output_path) / 1024:.1f} KB")
    
    pdf_document.close()
    
    print("\n✅ Extraction terminée!")
    print(f"\n📊 Résumé:")
    print(f"   - Pages extraites: {len(pages_to_extract)}")
    print(f"   - Dossier: {output_dir}")
    print(f"\n💡 Prochaines étapes:")
    print("   1. Vérifiez les images extraites")
    print("   2. Découpez les logos individuels si nécessaire")
    print("   3. Copiez-les dans les dossiers appropriés")
    
except FileNotFoundError:
    print(f"\n✗ Erreur: Le fichier PDF n'a pas été trouvé:")
    print(f"   {pdf_path}")
    print("\n💡 Vérifiez que le chemin est correct.")
    sys.exit(1)
    
except Exception as e:
    print(f"\n✗ Erreur lors de l'extraction: {e}")
    print(f"\n💡 Assurez-vous que:")
    print("   1. Le PDF n'est pas protégé par mot de passe")
    print("   2. PyMuPDF est installé: pip install PyMuPDF")
    print("   3. Le chemin du PDF est correct")
    sys.exit(1)

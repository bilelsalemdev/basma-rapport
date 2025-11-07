#!/usr/bin/env python3
"""
Script optimisé pour extraire les figures 28, 31, 34 et 35 du PDF
et les placer directement dans Chapitre3/images/logos/ avec les bons noms
"""
import sys
import os

# Vérifier PyMuPDF
try:
    import fitz  # PyMuPDF
    print("✓ PyMuPDF est installé")
except ImportError:
    print("✗ PyMuPDF n'est pas installé")
    print("\n📦 Installation:")
    print("   pip install PyMuPDF")
    sys.exit(1)

# Configuration
PDF_PATH = r"C:\Users\HP\OneDrive\Bureau\Mémoire\Optimisation intelligente de la planification de la productioion (3).pdf"
OUTPUT_DIR = "Chapitre3/images/logos"

# Mapping: numéro de page → nom de fichier de sortie
# IMPORTANT: Ajustez les numéros de pages selon l'emplacement réel des figures dans votre PDF
FIGURES_TO_EXTRACT = {
    # Format: page_number: (output_filename, description)
    35: ("figure-28-data-science.png", "Figure 28 - Data Science (pandas, NumPy, scikit-learn, XGBoost, matplotlib, seaborn)"),
    40: ("figure-31-backend.png", "Figure 31 - Backend (FastAPI, Pydantic, uvicorn)"),
    45: ("figure-34-frontend.png", "Figure 34 - Frontend (React, Recharts, Axios)"),
    50: ("figure-35-devops.png", "Figure 35 - DevOps (Docker, Git, pytest, PostgreSQL, OR-Tools)")
}

def find_figure_page(pdf_doc, figure_number):
    """
    Recherche la page contenant une figure spécifique
    """
    search_text = f"Figure {figure_number}"
    for page_num in range(len(pdf_doc)):
        page = pdf_doc[page_num]
        text = page.get_text()
        if search_text in text:
            return page_num + 1  # Retourner numéro 1-based
    return None

def extract_figures():
    """
    Extrait les figures du PDF
    """
    # Créer le dossier de sortie
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("=" * 70)
    print("🎯 EXTRACTION DES FIGURES POUR CHAPITRE 3")
    print("=" * 70)
    print(f"\n📄 PDF source: {PDF_PATH}")
    print(f"📁 Dossier de sortie: {OUTPUT_DIR}")
    print(f"🔍 Figures à extraire: {len(FIGURES_TO_EXTRACT)}")
    
    try:
        # Ouvrir le PDF
        print(f"\n📖 Ouverture du PDF...")
        pdf_document = fitz.open(PDF_PATH)
        total_pages = pdf_document.page_count
        print(f"   ✓ PDF ouvert: {total_pages} pages au total")
        
        # Option 1: Recherche automatique des figures
        print(f"\n🔍 Recherche automatique des figures dans le PDF...")
        auto_found = {}
        for fig_num in [28, 31, 34, 35]:
            page_num = find_figure_page(pdf_document, fig_num)
            if page_num:
                auto_found[fig_num] = page_num
                print(f"   ✓ Figure {fig_num} trouvée à la page {page_num}")
            else:
                print(f"   ⚠️  Figure {fig_num} non trouvée automatiquement")
        
        # Demander confirmation ou utiliser les pages par défaut
        print(f"\n📋 Pages configurées par défaut:")
        for page_num, (filename, desc) in FIGURES_TO_EXTRACT.items():
            print(f"   Page {page_num}: {desc}")
        
        if auto_found:
            print(f"\n💡 Pages trouvées automatiquement:")
            for fig_num, page_num in auto_found.items():
                print(f"   Figure {fig_num} → Page {page_num}")
            
            use_auto = input(f"\n❓ Utiliser les pages trouvées automatiquement? (o/n, défaut=n): ").strip().lower()
            if use_auto == 'o':
                # Mettre à jour FIGURES_TO_EXTRACT avec les pages trouvées
                new_mapping = {}
                for fig_num, page_num in auto_found.items():
                    # Trouver le filename correspondant
                    for old_page, (filename, desc) in FIGURES_TO_EXTRACT.items():
                        if f"Figure {fig_num}" in desc:
                            new_mapping[page_num] = (filename, desc)
                            break
                FIGURES_TO_EXTRACT.clear()
                FIGURES_TO_EXTRACT.update(new_mapping)
        
        print(f"\n🚀 Début de l'extraction...")
        extracted_count = 0
        
        # Extraire chaque figure
        for page_num, (output_filename, description) in FIGURES_TO_EXTRACT.items():
            if page_num > total_pages:
                print(f"\n⚠️  Page {page_num} n'existe pas (PDF a {total_pages} pages)")
                print(f"   Ignoré: {description}")
                continue
            
            print(f"\n{'─' * 70}")
            print(f"🔄 Extraction: {description}")
            print(f"   Page source: {page_num}")
            print(f"   Fichier cible: {output_filename}")
            
            # Obtenir la page (index 0-based)
            page = pdf_document[page_num - 1]
            
            # Convertir en image avec haute résolution
            # zoom=2.5 donne environ 180 DPI (bon compromis qualité/taille)
            mat = fitz.Matrix(2.5, 2.5)
            pix = page.get_pixmap(matrix=mat)
            
            # Sauvegarder l'image
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            pix.save(output_path)
            
            file_size_kb = os.path.getsize(output_path) / 1024
            print(f"   ✓ Sauvegardé: {output_path}")
            print(f"   📐 Dimensions: {pix.width}x{pix.height} pixels")
            print(f"   💾 Taille: {file_size_kb:.1f} KB")
            
            extracted_count += 1
        
        pdf_document.close()
        
        # Résumé final
        print(f"\n{'=' * 70}")
        print(f"✅ EXTRACTION TERMINÉE!")
        print(f"{'=' * 70}")
        print(f"\n📊 Résumé:")
        print(f"   ✓ Figures extraites: {extracted_count}/{len(FIGURES_TO_EXTRACT)}")
        print(f"   📁 Dossier: {OUTPUT_DIR}")
        
        # Lister les fichiers créés
        print(f"\n📄 Fichiers créés:")
        for filename in sorted(os.listdir(OUTPUT_DIR)):
            if filename.startswith("figure-"):
                filepath = os.path.join(OUTPUT_DIR, filename)
                size_kb = os.path.getsize(filepath) / 1024
                print(f"   ✓ {filename} ({size_kb:.1f} KB)")
        
        print(f"\n🎯 Prochaines étapes:")
        print(f"   1. Vérifiez les images extraites dans {OUTPUT_DIR}")
        print(f"   2. Compilez le document LaTeX:")
        print(f"      cd rapport__2_")
        print(f"      pdflatex main.tex")
        print(f"   3. Les figures devraient maintenant s'afficher au lieu des placeholders")
        
        return True
        
    except FileNotFoundError:
        print(f"\n✗ ERREUR: Le fichier PDF n'a pas été trouvé:")
        print(f"   {PDF_PATH}")
        print(f"\n💡 Solutions:")
        print(f"   1. Vérifiez que le chemin est correct")
        print(f"   2. Modifiez la variable PDF_PATH dans ce script")
        return False
        
    except Exception as e:
        print(f"\n✗ ERREUR lors de l'extraction: {e}")
        print(f"\n💡 Vérifications:")
        print(f"   1. Le PDF n'est pas protégé par mot de passe")
        print(f"   2. PyMuPDF est installé: pip install PyMuPDF")
        print(f"   3. Le chemin du PDF est correct")
        print(f"   4. Vous avez les droits d'écriture dans {OUTPUT_DIR}")
        return False

def main():
    """
    Point d'entrée principal
    """
    print("\n" + "=" * 70)
    print("  EXTRACTEUR DE FIGURES - CHAPITRE 3")
    print("  Figures 28, 31, 34, 35")
    print("=" * 70)
    
    # Vérifier que le PDF existe
    if not os.path.exists(PDF_PATH):
        print(f"\n⚠️  ATTENTION: Le PDF n'existe pas à l'emplacement configuré:")
        print(f"   {PDF_PATH}")
        print(f"\n💡 Veuillez modifier la variable PDF_PATH dans ce script")
        
        # Proposer de chercher le PDF
        search = input(f"\n❓ Voulez-vous chercher le PDF? (o/n): ").strip().lower()
        if search == 'o':
            print(f"\n🔍 Recherche de fichiers PDF dans le répertoire courant...")
            for root, dirs, files in os.walk("."):
                for file in files:
                    if file.endswith(".pdf") and "production" in file.lower():
                        found_path = os.path.join(root, file)
                        print(f"   Trouvé: {found_path}")
        
        return False
    
    # Lancer l'extraction
    success = extract_figures()
    
    if success:
        print(f"\n✨ Succès! Les figures sont prêtes à être utilisées.")
    else:
        print(f"\n❌ L'extraction a échoué. Consultez les messages d'erreur ci-dessus.")
    
    return success

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n\n⚠️  Extraction interrompue par l'utilisateur")
        sys.exit(1)

#!/usr/bin/env python3
"""
Script to fix Chapter 2 tables and carte mentale image.
"""

import re
import shutil
from pathlib import Path

def backup_file(filepath):
    """Create backup"""
    backup_path = f"{filepath}.backup_ch2_fix"
    if not Path(backup_path).exists():
        shutil.copy2(filepath, backup_path)
        print(f"✓ Backup created: {backup_path}")

def fix_tables_and_image(filepath):
    """Fix the two tables and the carte mentale image"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modifications = []
    
    # Fix Divatex table - remove adjustbox and use fixed widths
    pattern1 = r'(\\caption\{Résumé du fonctionnement du logiciel Divatex\}\s*\\begin\{adjustbox\}\{max width=\\textwidth\}\s*\\begin\{tabular\}\{)\|l\|l\|(\}.*?\\end\{tabular\}\s*)\\end\{adjustbox\}'
    
    replacement1 = r'\1|p{3.5cm}|p{10.5cm}|\2'
    
    if re.search(pattern1, content, re.DOTALL):
        content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)
        modifications.append("Fixed Divatex table")
    
    # Fix G.Pro table - remove adjustbox and use fixed widths
    pattern2 = r'(\\caption\{Résumé du fonctionnement du logiciel G\.Pro\}\s*\\begin\{adjustbox\}\{max width=\\textwidth\}\s*\\begin\{tabular\}\{)\|l\|l\|(\}.*?\\end\{tabular\}\s*)\\end\{adjustbox\}'
    
    replacement2 = r'\1|p{3.5cm}|p{10.5cm}|\2'
    
    if re.search(pattern2, content, re.DOTALL):
        content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)
        modifications.append("Fixed G.Pro table")
    
    # Fix carte mentale image - make it landscape and full page
    pattern3 = r'(\\subsubsection\{Outil utilisé : Carte mentale\}.*?)(\\begin\{figure\}\[H\].*?\\includegraphics\[width=\\textwidth\]\{Chapitre2/images/23\.png\}.*?\\end\{figure\})'
    
    replacement3 = r'''\1\\begin{landscape}
\\begin{figure}[p]
\\centering
\\includegraphics[width=0.95\\linewidth,height=0.9\\textheight,keepaspectratio]{Chapitre2/images/23.png}
\\caption{Carte mentale}
\\label{form}
\\end{figure}
\\end{landscape}'''
    
    if re.search(pattern3, content, re.DOTALL):
        content = re.sub(pattern3, replacement3, content, flags=re.DOTALL)
        modifications.append("Fixed carte mentale image - now landscape full page")
    
    if modifications:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Applied {len(modifications)} fixes:")
        for mod in modifications:
            print(f"  - {mod}")
        return len(modifications)
    else:
        print("  No fixes applied")
        return 0

def main():
    print("=" * 70)
    print("Chapter 2 Tables and Image Fix")
    print("=" * 70)
    
    filepath = Path("basma-rapport/Chapitre2/chapitre2.tex")
    
    if not filepath.exists():
        print(f"Error: {filepath} not found")
        return
    
    print(f"\nProcessing: {filepath}\n")
    
    backup_file(filepath)
    count = fix_tables_and_image(filepath)
    
    print("\n" + "=" * 70)
    print(f"Summary: {count} fixes applied")
    print("=" * 70)
    print("\nChanges:")
    print("1. Divatex table: Removed adjustbox, using fixed widths (3.5cm + 10.5cm)")
    print("2. G.Pro table: Removed adjustbox, using fixed widths (3.5cm + 10.5cm)")
    print("3. Carte mentale: Now landscape mode, full page size")
    print("\nNext: Compile PDF to see results")

if __name__ == "__main__":
    main()

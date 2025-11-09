#!/usr/bin/env python3
"""
Remove adjustbox from Divatex and G.Pro tables to make text normal size.
"""

import re
import shutil
from pathlib import Path

def fix_tables():
    filepath = Path("basma-rapport/Chapitre2/chapitre2.tex")
    
    # Backup
    backup_path = f"{filepath}.backup_textsize"
    if not Path(backup_path).exists():
        shutil.copy2(filepath, backup_path)
        print(f"✓ Backup created: {backup_path}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix Divatex table - remove adjustbox, use fixed column widths
    pattern1 = r'(\\caption\{Résumé du fonctionnement du logiciel Divatex\}\s*)\\begin\{adjustbox\}\{width=0\.95\\textwidth\}\s*\\begin\{tabular\}\{\|l\|l\|\}'
    replacement1 = r'\1\\begin{tabular}{|p{3.5cm}|p{10.5cm}|}'
    content = re.sub(pattern1, replacement1, content)
    
    # Remove closing adjustbox for Divatex
    content = re.sub(
        r'(rapports de consommation \\\\[\s]*\\hline[\s]*\\end\{tabular\})[\s]*\\end\{adjustbox\}([\s]*\\end\{table\})',
        r'\1\2',
        content
    )
    
    # Fix G.Pro table - remove adjustbox, use fixed column widths
    pattern2 = r'(\\caption\{Résumé du fonctionnement du logiciel G\.Pro\}\s*)\\begin\{adjustbox\}\{width=0\.95\\textwidth\}\s*\\begin\{tabular\}\{\|l\|l\|\}'
    replacement2 = r'\1\\begin{tabular}{|p{3.5cm}|p{10.5cm}|}'
    content = re.sub(pattern2, replacement2, content)
    
    # Remove closing adjustbox for G.Pro
    content = re.sub(
        r'(mouvements post-coupe \\\\[\s]*\\hline[\s]*\\end\{tabular\})[\s]*\\end\{adjustbox\}([\s]*\\end\{table\})',
        r'\1\2',
        content
    )
    
    # Fix the special character Ãlément -> Élément
    content = content.replace('\\textbf{Ãlément}', '\\textbf{Élément}')
    
    # Fix "Mise a jour" -> "Mise à jour"
    content = content.replace('Mise a jour', 'Mise à jour')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Fixed both tables:")
    print("  - Removed adjustbox scaling")
    print("  - Using fixed column widths: 3.5cm + 10.5cm")
    print("  - Text is now normal size (not scaled down)")
    print("  - Fixed special characters (Élément, à)")

if __name__ == "__main__":
    fix_tables()

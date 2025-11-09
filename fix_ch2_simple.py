#!/usr/bin/env python3
"""
Simple fix for Chapter 2 - just change adjustbox to use width instead of max width,
and make the carte mentale image bigger.
"""

import re

def fix_chapter2():
    filepath = "basma-rapport/Chapitre2/chapitre2.tex"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix 1: Change adjustbox for Divatex table to use width=0.95\textwidth
    content = content.replace(
        '\\caption{Résumé du fonctionnement du logiciel Divatex}\n\\begin{adjustbox}{max width=\\textwidth}',
        '\\caption{Résumé du fonctionnement du logiciel Divatex}\n\\begin{adjustbox}{width=0.95\\textwidth}'
    )
    
    # Fix 2: Change adjustbox for G.Pro table to use width=0.95\textwidth  
    content = content.replace(
        '\\caption{Résumé du fonctionnement du logiciel G.Pro}\n\\begin{adjustbox}{max width=\\textwidth}',
        '\\caption{Résumé du fonctionnement du logiciel G.Pro}\n\\begin{adjustbox}{width=0.95\\textwidth}'
    )
    
    # Fix 3: Make carte mentale image bigger - rotate 90 degrees and use full height
    pattern = r'(\\includegraphics\[width=\\textwidth\]\{Chapitre2/images/23\.png\})'
    replacement = r'\\includegraphics[angle=90,width=\\textheight,keepaspectratio]{Chapitre2/images/23.png}'
    content = re.sub(pattern, replacement, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Fixed Chapter 2:")
    print("  - Divatex table: width=0.95\\textwidth (text will be larger)")
    print("  - G.Pro table: width=0.95\\textwidth (text will be larger)")
    print("  - Carte mentale: rotated 90°, using full page height")

if __name__ == "__main__":
    fix_chapter2()

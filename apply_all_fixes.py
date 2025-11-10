#!/usr/bin/env python3
"""
Master script to reapply all formatting fixes to the rapport.
This script applies all the fixes made during the session.
"""

import re
import shutil
from pathlib import Path
from datetime import datetime

def backup_files():
    """Create backups of all files before modification"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(f"basma-rapport/backups_{timestamp}")
    backup_dir.mkdir(exist_ok=True)
    
    files_to_backup = [
        "basma-rapport/main.tex",
        "basma-rapport/IntroductionGenerale/intro.tex",
        "basma-rapport/ConclusionGenerale/conclusion.tex",
        "basma-rapport/Chapitre1/chapitre1.tex",
        "basma-rapport/Chapitre2/chapitre2.tex",
        "basma-rapport/Chapitre3/chapitre3.tex",
        "basma-rapport/Chapitre6/chapitre6.tex",
    ]
    
    for filepath in files_to_backup:
        if Path(filepath).exists():
            shutil.copy2(filepath, backup_dir / Path(filepath).name)
    
    print(f"✓ Backups created in: {backup_dir}")
    return backup_dir

def fix_main_tex():
    """Fix main.tex - styledtitle command"""
    print("\n1. Fixing main.tex...")
    filepath = Path("basma-rapport/main.tex")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix styledtitle command
    old_pattern = r'\\begin\{minipage\}\[t\]\{0\.9\\linewidth\}'
    new_pattern = r'\\begin{minipage}[t]{0.93\\linewidth}'
    content = re.sub(old_pattern, new_pattern, content)
    
    # Add mbox to title
    content = re.sub(
        r'\{\\Huge \\textbf\{#1\}\}',
        r'{\\Huge \\textbf{\\mbox{#1}}}',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  ✓ Fixed styledtitle command")

def fix_introduction():
    """Fix Introduction - title and spacing"""
    print("\n2. Fixing Introduction...")
    filepath = Path("basma-rapport/IntroductionGenerale/intro.tex")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix title with non-breaking space
    content = content.replace(
        '\\styledtitle{INTRODUCTION GÉNÉRALE}',
        '\\styledtitle{INTRODUCTION~GÉNÉRALE}'
    )
    
    # Add spacing if not present
    if '\\begin{spacing}{1.5}' not in content:
        # Add after addcontentsline
        content = re.sub(
            r'(\\addcontentsline\{toc\}\{chapter\}\{INTRODUCTION GÉNÉRALE\}\s*\n)',
            r'\1\\begin{spacing}{1.5}\n',
            content
        )
        # Add end before last line
        if not content.strip().endswith('\\end{spacing}'):
            content = content.rstrip() + '\n\\end{spacing}\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  ✓ Fixed title and spacing")

def fix_conclusion():
    """Fix Conclusion - title and spacing"""
    print("\n3. Fixing Conclusion...")
    filepath = Path("basma-rapport/ConclusionGenerale/conclusion.tex")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix title with non-breaking space
    content = content.replace(
        '\\styledtitle{Conclusion générale}',
        '\\styledtitle{Conclusion~générale}'
    )
    
    # Add spacing if not present
    if '\\begin{spacing}{1.5}' not in content:
        content = re.sub(
            r'(\\rhead\{\\thepage\}\s*\n)',
            r'\1\\begin{spacing}{1.5}\n',
            content
        )
        if not content.strip().endswith('\\end{spacing}'):
            content = content.rstrip() + '\n\\end{spacing}\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  ✓ Fixed title and spacing")

def fix_chapter1_image():
    """Fix Chapter 1 - Process diagram image"""
    print("\n4. Fixing Chapter 1 image...")
    filepath = Path("basma-rapport/Chapitre1/chapitre1.tex")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix process diagram image
    content = re.sub(
        r'\\includegraphics\[width=0\.95\\textwidth\]\{Chapitre1/images/process-Page-4\.drawio\.png\}',
        r'\\includegraphics[width=0.95\\textwidth,height=0.85\\textheight,keepaspectratio]{Chapitre1/images/process-Page-4.drawio.png}',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  ✓ Fixed process diagram image")

def fix_chapter2_tables_and_images():
    """Fix Chapter 2 - Divatex/G.Pro tables and images"""
    print("\n5. Fixing Chapter 2 tables and images...")
    filepath = Path("basma-rapport/Chapitre2/chapitre2.tex")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix Divatex table - remove adjustbox
    content = re.sub(
        r'(\\caption\{Résumé du fonctionnement du logiciel Divatex\}\s*)\\begin\{adjustbox\}\{[^}]+\}\s*\\begin\{tabular\}\{\|l\|l\|\}',
        r'\1\\begin{tabular}{|p{3.5cm}|p{10.5cm}|}',
        content
    )
    content = re.sub(
        r'(rapports de consommation \\\\[\s]*\\hline[\s]*\\end\{tabular\})[\s]*\\end\{adjustbox\}',
        r'\1',
        content
    )
    
    # Fix G.Pro table - remove adjustbox
    content = re.sub(
        r'(\\caption\{Résumé du fonctionnement du logiciel G\.Pro\}\s*)\\begin\{adjustbox\}\{[^}]+\}\s*\\begin\{tabular\}\{\|l\|l\|\}',
        r'\1\\begin{tabular}{|p{3.5cm}|p{10.5cm}|}',
        content
    )
    content = re.sub(
        r'(mouvements post-coupe \\\\[\s]*\\hline[\s]*\\end\{tabular\})[\s]*\\end\{adjustbox\}',
        r'\1',
        content
    )
    
    # Fix special characters
    content = content.replace('\\textbf{Ãlément}', '\\textbf{Élément}')
    content = content.replace('Mise a jour', 'Mise à jour')
    
    # Fix Carte mentale image
    content = re.sub(
        r'\\includegraphics\[angle=90[^]]*\]\{Chapitre2/images/23\.png\}',
        r'\\includegraphics[angle=90,width=0.65\\textheight,keepaspectratio]{Chapitre2/images/23.png}',
        content
    )
    
    # Fix methodology images - make them full width stacked
    pattern = r'\\begin\{minipage\}\[b\]\{0\.45\\textwidth\}[\s\S]*?\\includegraphics\[width=\\textwidth\]\{Chapitre2/images/IMG_20250614_141256_509\.jpg\}[\s\S]*?\\end\{minipage\}[\s]*\\hfill[\s]*\\begin\{minipage\}\[b\]\{0\.50\\textwidth\}[\s\S]*?\\includegraphics\[width=\\textwidth\]\{Chapitre2/images/IMG_20250614_141303_456\.jpg\}[\s\S]*?\\end\{minipage\}'
    
    replacement = r'''\\includegraphics[width=0.85\\textwidth]{Chapitre2/images/IMG_20250614_141256_509.jpg}
  \\caption{Fiche d'enregistrement (modèle Rim)}
  \\label{chpp3}
\\end{figure}

\\begin{figure}[H]
  \\centering
  \\includegraphics[width=0.85\\textwidth]{Chapitre2/images/IMG_20250614_141303_456.jpg}
  \\caption{Fiche d'enregistrement (modèle Leotard 500g pink)}
  \\label{chp3}'''
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Fix PDF page to landscape
    content = re.sub(
        r'\\includepdf\[pages=1,scale=[^]]+\]',
        r'\\includepdf[pages=1,angle=90,scale=0.85,pagecommand=\\thispagestyle{plain}]',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  ✓ Fixed Divatex and G.Pro tables")
    print("  ✓ Fixed Carte mentale image")
    print("  ✓ Fixed methodology images")
    print("  ✓ Fixed PDF page to landscape")

def fix_chapter3_diagrams():
    """Fix Chapter 3 - TikZ diagrams"""
    print("\n6. Fixing Chapter 3 TikZ diagrams...")
    filepath = Path("basma-rapport/Chapitre3/chapitre3.tex")
    
    if not filepath.exists():
        print("  ⚠ Chapter 3 not found, skipping")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix backend diagram
    content = content.replace('node distance=1.5cm', 'node distance=2.0cm')
    content = content.replace('text width=8cm', 'text width=7cm')
    
    # Fix frontend diagram
    content = re.sub(
        r'node distance=1\.8cm',
        'node distance=3.0cm',
        content
    )
    content = re.sub(
        r'below left=2\.5cm and 2\.2cm',
        'below left=3.2cm and 2.8cm',
        content
    )
    content = re.sub(
        r'below=2\.5cm of app',
        'below=3.2cm of app',
        content
    )
    content = re.sub(
        r'below right=2\.5cm and 2\.2cm',
        'below right=3.2cm and 2.8cm',
        content
    )
    content = re.sub(
        r'below=5\.2cm of app',
        'below=6.8cm of app',
        content
    )
    
    # Fix DevOps diagram
    content = re.sub(
        r'below=4cm of annotation, xshift=-5cm',
        'below=4.5cm of annotation, xshift=-6cm',
        content
    )
    content = re.sub(
        r'below=4cm of annotation, xshift=-1\.7cm',
        'below=4.5cm of annotation, xshift=-2cm',
        content
    )
    content = re.sub(
        r'below=4cm of annotation, xshift=1\.7cm',
        'below=4.5cm of annotation, xshift=2cm',
        content
    )
    content = re.sub(
        r'below=4cm of annotation, xshift=5cm',
        'below=4.5cm of annotation, xshift=6cm',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  ✓ Fixed TikZ diagram spacing")

def fix_chapter6_diagram():
    """Fix Chapter 6 - Service architecture diagram"""
    print("\n7. Fixing Chapter 6 diagram...")
    filepath = Path("basma-rapport/Chapitre6/chapitre6.tex")
    
    if not filepath.exists():
        print("  ⚠ Chapter 6 not found, skipping")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix service architecture diagram
    content = re.sub(
        r'\\begin\{tikzpicture\}\[node distance=2cm',
        r'\\begin{tikzpicture}[node distance=2.5cm',
        content
    )
    content = re.sub(
        r'xshift=-2cm',
        'xshift=-2.5cm',
        content
    )
    content = re.sub(
        r'xshift=2cm',
        'xshift=2.5cm',
        content
    )
    content = re.sub(
        r'yshift=-1cm',
        'yshift=-1.5cm',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  ✓ Fixed service architecture diagram")

def wrap_all_tables():
    """Wrap all tables with adjustbox for proper sizing"""
    print("\n8. Wrapping all tables with adjustbox...")
    
    chapter_files = [
        "basma-rapport/Chapitre1/chapitre1.tex",
        "basma-rapport/Chapitre2/chapitre2.tex",
        "basma-rapport/Chapitre3/chapitre3.tex",
        "basma-rapport/Chapitre5/chapitre5.tex",
    ]
    
    total_wrapped = 0
    
    for filepath in chapter_files:
        if not Path(filepath).exists():
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find tabular environments not already wrapped
        pattern = r'(?<!\\begin\{adjustbox\}\{max width=\\textwidth\}\n)(\\begin\{tabular\}\{[^}]+\}(?:.*?)\\end\{tabular\})'
        
        def wrap_table(match):
            nonlocal total_wrapped
            tabular_block = match.group(1)
            
            # Check if it has fixed widths or many columns
            spec_match = re.search(r'\\begin\{tabular\}\{([^}]+)\}', tabular_block)
            if spec_match:
                spec = spec_match.group(1)
                has_fixed_width = 'p{' in spec
                col_count = spec.count('|') - 1
                
                if has_fixed_width or col_count >= 5:
                    total_wrapped += 1
                    return f'\\begin{{adjustbox}}{{max width=\\textwidth}}\n{tabular_block}\n\\end{{adjustbox}}'
            
            return match.group(0)
        
        new_content = re.sub(pattern, wrap_table, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
    
    print(f"  ✓ Wrapped {total_wrapped} tables")

def main():
    print("=" * 70)
    print("MASTER FIX SCRIPT - Reapplying All Formatting Fixes")
    print("=" * 70)
    
    # Create backups
    backup_dir = backup_files()
    
    try:
        # Apply all fixes
        fix_main_tex()
        fix_introduction()
        fix_conclusion()
        fix_chapter1_image()
        fix_chapter2_tables_and_images()
        fix_chapter3_diagrams()
        fix_chapter6_diagram()
        wrap_all_tables()
        
        print("\n" + "=" * 70)
        print("✓ ALL FIXES APPLIED SUCCESSFULLY!")
        print("=" * 70)
        print("\nSummary of fixes:")
        print("  1. ✓ Main.tex - styledtitle command")
        print("  2. ✓ Introduction - title and spacing")
        print("  3. ✓ Conclusion - title and spacing")
        print("  4. ✓ Chapter 1 - process diagram image")
        print("  5. ✓ Chapter 2 - Divatex/G.Pro tables, Carte mentale, methodology images")
        print("  6. ✓ Chapter 3 - TikZ diagram spacing")
        print("  7. ✓ Chapter 6 - service architecture diagram")
        print("  8. ✓ All tables wrapped with adjustbox")
        print(f"\nBackups saved in: {backup_dir}")
        print("\nNext step: Compile the PDF")
        print("  cd basma-rapport && pdflatex main.tex")
        
    except Exception as e:
        print(f"\n✗ Error occurred: {e}")
        print(f"You can restore from backups in: {backup_dir}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

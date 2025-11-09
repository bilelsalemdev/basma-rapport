#!/usr/bin/env python3
"""
Script to fix overlapping boxes in TikZ diagrams by adjusting node distances and positioning.
"""

import re
import shutil
from pathlib import Path

def backup_file(filepath):
    """Create a backup of the file"""
    backup_path = f"{filepath}.backup_tikz"
    if not Path(backup_path).exists():
        shutil.copy2(filepath, backup_path)
        print(f"✓ Backup created: {backup_path}")
    else:
        print(f"  Backup already exists")

def fix_frontend_diagram(content):
    """Fix the frontend diagram with overlapping boxes"""
    
    # Pattern to find the frontend diagram
    pattern = r'(\\begin\{tikzpicture\}\[.*?node distance=1\.8cm.*?\].*?% Application principale.*?)(node distance=2\.5cm and 2\.2cm)(.*?below=2\.5cm of app.*?)(below=5\.2cm of app)(.*?\\end\{tikzpicture\})'
    
    def replace_frontend(match):
        before = match.group(1)
        old_dist1 = match.group(2)
        middle = match.group(3)
        old_dist2 = match.group(4)
        after = match.group(5)
        
        # Increase spacing
        new_dist1 = "node distance=3.2cm and 2.8cm"
        new_dist2 = "below=6.5cm of app"
        
        return f"{before}{new_dist1}{middle}{new_dist2}{after}"
    
    new_content = re.sub(pattern, replace_frontend, content, flags=re.DOTALL)
    
    if new_content != content:
        return new_content, 1
    return content, 0

def fix_backend_diagram(content):
    """Fix the backend diagram spacing"""
    
    # Increase node distance for backend diagram
    pattern = r'(\\begin\{tikzpicture\}\[.*?node distance=1\.5cm.*?box/\.style=\{.*?text width=8cm)'
    
    def replace_backend(match):
        text = match.group(0)
        # Increase node distance
        text = text.replace("node distance=1.5cm", "node distance=2.0cm")
        # Reduce text width to prevent overflow
        text = text.replace("text width=8cm", "text width=7cm")
        return text
    
    new_content = re.sub(pattern, replace_backend, content, flags=re.DOTALL)
    
    if new_content != content:
        return new_content, 1
    return content, 0

def fix_devops_diagram(content):
    """Fix the DevOps diagram with overlapping classes"""
    
    # Pattern for DevOps diagram
    pattern = r'(node distance=2\.2cm.*?DevOpsInfrastructure.*?)(below=4cm of annotation, xshift=-5cm)(.*?)(below=4cm of annotation, xshift=-1\.7cm)(.*?)(below=4cm of annotation, xshift=1\.7cm)(.*?)(below=4cm of annotation, xshift=5cm)'
    
    def replace_devops(match):
        before = match.group(1)
        pos1 = match.group(2)
        mid1 = match.group(3)
        pos2 = match.group(4)
        mid2 = match.group(5)
        pos3 = match.group(6)
        mid3 = match.group(7)
        pos4 = match.group(8)
        
        # Increase spacing between boxes
        new_pos1 = "below=4.5cm of annotation, xshift=-6cm"
        new_pos2 = "below=4.5cm of annotation, xshift=-2cm"
        new_pos3 = "below=4.5cm of annotation, xshift=2cm"
        new_pos4 = "below=4.5cm of annotation, xshift=6cm"
        
        return f"{before}{new_pos1}{mid1}{new_pos2}{mid2}{new_pos3}{mid3}{new_pos4}"
    
    new_content = re.sub(pattern, replace_devops, content, flags=re.DOTALL)
    
    if new_content != content:
        return new_content, 1
    return content, 0

def fix_all_node_distances(content):
    """Increase all node distances that are too small"""
    modifications = 0
    
    # Find all node distance declarations that are < 2cm
    patterns = [
        (r'node distance=1\.5cm', 'node distance=2.2cm'),
        (r'node distance=1\.8cm', 'node distance=2.5cm'),
        (r'node distance=1\.2cm', 'node distance=2.0cm'),
        (r'node distance=0\.8cm', 'node distance=1.5cm'),
    ]
    
    for old_pattern, new_pattern in patterns:
        if re.search(old_pattern, content):
            content = re.sub(old_pattern, new_pattern, content)
            modifications += 1
    
    return content, modifications

def process_file(filepath):
    """Process a single LaTeX file"""
    print(f"\nProcessing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup first
    backup_file(filepath)
    
    original_content = content
    total_fixes = 0
    
    # Apply fixes
    content, fixes = fix_frontend_diagram(content)
    total_fixes += fixes
    if fixes:
        print(f"  ✓ Fixed frontend diagram spacing")
    
    content, fixes = fix_backend_diagram(content)
    total_fixes += fixes
    if fixes:
        print(f"  ✓ Fixed backend diagram spacing")
    
    content, fixes = fix_devops_diagram(content)
    total_fixes += fixes
    if fixes:
        print(f"  ✓ Fixed DevOps diagram spacing")
    
    content, fixes = fix_all_node_distances(content)
    total_fixes += fixes
    if fixes:
        print(f"  ✓ Increased {fixes} node distances")
    
    if total_fixes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Total: {total_fixes} fixes applied")
    else:
        print("  No fixes needed")
    
    return total_fixes

def main():
    print("=" * 70)
    print("TikZ Diagram Overlap Fix Tool")
    print("=" * 70)
    
    basma_dir = Path("basma-rapport")
    chapter_files = []
    
    # Find all chapter files with TikZ diagrams
    for chapter_dir in basma_dir.glob("Chapitre*"):
        if chapter_dir.is_dir():
            for tex_file in chapter_dir.glob("chapitre*.tex"):
                if "BACKUP" not in tex_file.name and "backup" not in tex_file.name and "_NEW" not in tex_file.name:
                    # Check if file contains tikzpicture
                    with open(tex_file, 'r', encoding='utf-8') as f:
                        if 'tikzpicture' in f.read():
                            chapter_files.append(tex_file)
    
    print(f"\nFound {len(chapter_files)} files with TikZ diagrams\n")
    
    total = 0
    for filepath in sorted(chapter_files):
        count = process_file(filepath)
        total += count
    
    print("\n" + "=" * 70)
    print(f"Summary: Applied {total} fixes to TikZ diagrams")
    print("=" * 70)
    print("\nChanges made:")
    print("- Increased node distances for better spacing")
    print("- Adjusted box positions to prevent overlaps")
    print("- Reduced text widths where needed")
    print("\nNext: Compile PDF to verify the fixes")

if __name__ == "__main__":
    main()

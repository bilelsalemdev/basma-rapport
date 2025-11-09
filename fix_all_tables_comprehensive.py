#!/usr/bin/env python3
"""
Comprehensive fix for ALL tables to prevent overflow.
Wraps every tabular environment with adjustbox.
"""

import re
import shutil
from pathlib import Path

def process_file(filepath):
    """Process a single LaTeX file and wrap ALL tables"""
    print(f"\nProcessing: {filepath}")
    
    # Create backup if it doesn't exist
    backup_path = f"{filepath}.backup_comprehensive"
    if not Path(backup_path).exists():
        shutil.copy2(filepath, backup_path)
        print(f"✓ Backup created: {backup_path}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modifications = 0
    
    # Pattern to find tabular environments NOT already wrapped in adjustbox
    # Look for \begin{tabular} that is NOT preceded by \begin{adjustbox}
    pattern = r'(?<!\\begin\{adjustbox\}\{max width=\\textwidth\}\n)(\\begin\{tabular\}\{[^}]+\}(?:.*?)\\end\{tabular\})'
    
    def wrap_table(match):
        nonlocal modifications
        tabular_block = match.group(1)
        
        # Check if already wrapped (double check)
        if '\\begin{adjustbox}' in match.group(0):
            return match.group(0)
        
        modifications += 1
        return f'\\begin{{adjustbox}}{{max width=\\textwidth}}\n{tabular_block}\n\\end{{adjustbox}}'
    
    # Apply wrapping
    new_content = re.sub(pattern, wrap_table, content, flags=re.DOTALL)
    
    if modifications > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Wrapped {modifications} tables")
    else:
        print("  No new tables to wrap")
    
    return modifications

def main():
    print("=" * 70)
    print("Comprehensive Table Wrapping - ALL Tables")
    print("=" * 70)
    
    basma_dir = Path("basma-rapport")
    chapter_files = []
    
    # Find all chapter files
    for chapter_dir in basma_dir.glob("Chapitre*"):
        if chapter_dir.is_dir():
            for tex_file in chapter_dir.glob("chapitre*.tex"):
                if "BACKUP" not in tex_file.name and "backup" not in tex_file.name and "_NEW" not in tex_file.name:
                    chapter_files.append(tex_file)
    
    # Also check intro and conclusion
    for section in ["IntroductionGenerale", "ConclusionGenerale"]:
        section_dir = basma_dir / section
        if section_dir.exists():
            for tex_file in section_dir.glob("*.tex"):
                if "backup" not in tex_file.name.lower():
                    chapter_files.append(tex_file)
    
    print(f"\nFound {len(chapter_files)} files to process\n")
    
    total = 0
    for filepath in sorted(chapter_files):
        count = process_file(filepath)
        total += count
    
    print("\n" + "=" * 70)
    print(f"Summary: Wrapped {total} additional tables")
    print("=" * 70)
    print("\nAll tables are now wrapped with adjustbox to prevent overflow.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script to fix table widths in LaTeX files to prevent overflow.
Converts fixed-width tabular environments to use relative widths.
"""

import re
import os
import shutil
from pathlib import Path

def backup_file(filepath):
    """Create a backup of the file before modification"""
    backup_path = f"{filepath}.backup_tables"
    shutil.copy2(filepath, backup_path)
    print(f"✓ Backup created: {backup_path}")

def adjust_table_widths(content):
    """
    Adjust table column widths to prevent overflow.
    Converts fixed widths (e.g., p{10cm}) to relative widths using tabularx.
    """
    modifications = []
    
    # Pattern to find tabular environments with fixed widths
    # Match: \begin{tabular}{|l|p{10cm}|} or similar
    tabular_pattern = r'\\begin\{tabular\}\{([^}]+)\}'
    
    def replace_tabular(match):
        spec = match.group(1)
        original_spec = spec
        
        # Check if it has fixed-width columns (p{...cm})
        if 'p{' in spec and 'cm}' in spec:
            # Replace p{Xcm} with X (for tabularx)
            # Keep alignment specifiers like |l|c|r|
            new_spec = re.sub(r'p\{[\d.]+cm\}', 'X', spec)
            
            # If we made changes, use tabularx instead
            if new_spec != original_spec:
                modifications.append(f"  - Changed: {original_spec} → {new_spec}")
                return f'\\begin{{tabularx}}{{\\textwidth}}{{{new_spec}}}'
        
        return match.group(0)
    
    # Replace tabular with tabularx where needed
    new_content = re.sub(tabular_pattern, replace_tabular, content)
    
    # Also need to replace \end{tabular} with \end{tabularx} for modified tables
    # This is tricky - we need to track which ones were changed
    # Simpler approach: replace all tabular with tabularx if content changed
    if new_content != content:
        # Count changes
        count = len(modifications)
        print(f"  Found {count} tables with fixed widths to adjust")
        
        # Now replace corresponding \end{tabular}
        # We need to be more careful here - only replace the ones we changed
        # For now, let's use a different approach
        pass
    
    return new_content, modifications

def adjust_table_widths_v2(content):
    """
    Better approach: Find complete table environments and adjust them.
    """
    modifications = []
    
    # Find all table/tabular blocks
    # Pattern: \begin{table}...\begin{tabular}{spec}...\end{tabular}...\end{table}
    
    def process_tabular_block(match):
        full_match = match.group(0)
        spec = match.group(1)
        table_content = match.group(2)
        
        original_spec = spec
        
        # Check if it has fixed-width columns that might overflow
        if 'p{' in spec:
            # Calculate total width
            widths = re.findall(r'p\{([\d.]+)cm\}', spec)
            total_width = sum(float(w) for w in widths)
            
            # If total width > 15cm (safe margin for A4 with 3cm margins)
            # A4 width = 21cm, margins = 6cm total, so usable = 15cm
            if total_width > 15:
                # Convert to tabularx with relative widths
                new_spec = re.sub(r'p\{[\d.]+cm\}', 'X', spec)
                modifications.append(f"  - Adjusted table: {original_spec} → {new_spec} (total width: {total_width}cm)")
                
                return f'\\begin{{tabularx}}{{\\textwidth}}{{{new_spec}}}\n{table_content}\\end{{tabularx}}'
        
        return full_match
    
    # Match tabular environments
    pattern = r'\\begin\{tabular\}\{([^}]+)\}(.*?)\\end\{tabular\}'
    new_content = re.sub(pattern, process_tabular_block, content, flags=re.DOTALL)
    
    return new_content, modifications

def process_file(filepath):
    """Process a single LaTeX file"""
    print(f"\nProcessing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Backup first
        backup_file(filepath)
        
        # Adjust table widths
        new_content, modifications = adjust_table_widths_v2(content)
        
        if modifications:
            # Write the modified content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Modified {len(modifications)} tables:")
            for mod in modifications:
                print(mod)
        else:
            print("  No tables needed adjustment")
            
        return len(modifications)
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return 0

def main():
    """Main function to process all chapter files"""
    print("=" * 60)
    print("LaTeX Table Width Adjustment Tool")
    print("=" * 60)
    
    # Find all chapter files
    basma_dir = Path("basma-rapport")
    chapter_files = []
    
    for chapter_dir in basma_dir.glob("Chapitre*"):
        if chapter_dir.is_dir():
            for tex_file in chapter_dir.glob("chapitre*.tex"):
                # Skip backup files
                if "BACKUP" not in tex_file.name and "backup" not in tex_file.name:
                    chapter_files.append(tex_file)
    
    print(f"\nFound {len(chapter_files)} chapter files to process")
    
    total_modifications = 0
    for filepath in sorted(chapter_files):
        mods = process_file(filepath)
        total_modifications += mods
    
    print("\n" + "=" * 60)
    print(f"Summary: Adjusted {total_modifications} tables across {len(chapter_files)} files")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review the changes in each file")
    print("2. Compile the PDF: cd basma-rapport && pdflatex main.tex")
    print("3. If issues occur, restore from .backup_tables files")

if __name__ == "__main__":
    main()

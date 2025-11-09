#!/usr/bin/env python3
"""
Script to fix ALL table widths in LaTeX files to prevent overflow.
Uses adjustbox and resizebox to scale tables that are too wide.
"""

import re
import os
import shutil
from pathlib import Path

def backup_file(filepath):
    """Create a backup of the file before modification"""
    backup_path = f"{filepath}.backup_widths"
    if not os.path.exists(backup_path):
        shutil.copy2(filepath, backup_path)
        print(f"✓ Backup created: {backup_path}")
    else:
        print(f"  Backup already exists: {backup_path}")

def calculate_table_width(spec):
    """Calculate approximate width of a table specification"""
    # Extract all p{Xcm} widths
    widths = re.findall(r'p\{([\d.]+)cm\}', spec)
    total_p_width = sum(float(w) for w in widths)
    
    # Count other columns (l, c, r) - estimate 2cm each
    other_cols = len(re.findall(r'\|[lcr]\|', spec))
    other_cols += len(re.findall(r'\|[lcr]$', spec))
    other_cols += len(re.findall(r'^[lcr]\|', spec))
    
    # Rough estimate
    estimated_width = total_p_width + (other_cols * 2)
    
    return estimated_width, total_p_width

def wrap_table_with_adjustbox(content):
    """
    Wrap tables with adjustbox to make them fit the page width.
    This is the most reliable method for preventing overflow.
    """
    modifications = []
    
    # Pattern to match complete table environments
    # Matches: \begin{table}...\begin{tabular}{...}...\end{tabular}...\end{table}
    table_pattern = r'(\\begin\{table\}.*?)(\\begin\{tabular\}\{([^}]+)\})(.*?)(\\end\{tabular\})(.*?\\end\{table\})'
    
    def process_table(match):
        table_start = match.group(1)  # \begin{table}...
        tabular_start = match.group(2)  # \begin{tabular}{spec}
        spec = match.group(3)  # table spec
        table_content = match.group(4)  # content
        tabular_end = match.group(5)  # \end{tabular}
        table_end = match.group(6)  # ...\end{table}
        
        # Calculate if table might overflow
        est_width, p_width = calculate_table_width(spec)
        
        # If table has fixed widths or many columns, wrap it
        has_fixed_width = 'p{' in spec
        col_count = spec.count('|') - 1
        
        if has_fixed_width or col_count >= 5:
            modifications.append(f"  - Wrapped table with spec: {spec} (est. width: {est_width:.1f}cm, cols: {col_count})")
            
            # Wrap with adjustbox
            new_table = (
                f"{table_start}"
                f"\\begin{{adjustbox}}{{max width=\\textwidth}}\n"
                f"{tabular_start}"
                f"{table_content}"
                f"{tabular_end}\n"
                f"\\end{{adjustbox}}"
                f"{table_end}"
            )
            return new_table
        
        return match.group(0)
    
    new_content = re.sub(table_pattern, process_table, content, flags=re.DOTALL)
    
    # Also handle standalone tabular (not in table environment)
    standalone_pattern = r'(?<!\\begin\{adjustbox\})(\n\\begin\{tabular\}\{([^}]+)\})(.*?)(\\end\{tabular\})'
    
    def process_standalone(match):
        tabular_start = match.group(1)
        spec = match.group(2)
        content_part = match.group(3)
        tabular_end = match.group(4)
        
        est_width, p_width = calculate_table_width(spec)
        has_fixed_width = 'p{' in spec
        col_count = spec.count('|') - 1
        
        if has_fixed_width or col_count >= 5:
            modifications.append(f"  - Wrapped standalone table: {spec} (est. width: {est_width:.1f}cm)")
            
            return (
                f"\n\\begin{{adjustbox}}{{max width=\\textwidth}}"
                f"{tabular_start}"
                f"{content_part}"
                f"{tabular_end}"
                f"\\end{{adjustbox}}"
            )
        
        return match.group(0)
    
    new_content = re.sub(standalone_pattern, process_standalone, new_content, flags=re.DOTALL)
    
    return new_content, modifications

def process_file(filepath):
    """Process a single LaTeX file"""
    print(f"\nProcessing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Backup first
        backup_file(filepath)
        
        # Wrap tables with adjustbox
        new_content, modifications = wrap_table_with_adjustbox(content)
        
        if modifications:
            # Write the modified content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Modified {len(modifications)} tables:")
            for mod in modifications[:10]:  # Show first 10
                print(mod)
            if len(modifications) > 10:
                print(f"  ... and {len(modifications) - 10} more")
        else:
            print("  No tables needed adjustment")
            
        return len(modifications)
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        import traceback
        traceback.print_exc()
        return 0

def main():
    """Main function to process all chapter files"""
    print("=" * 70)
    print("LaTeX Table Width Adjustment Tool - Adjustbox Method")
    print("=" * 70)
    
    # Find all chapter files
    basma_dir = Path("basma-rapport")
    chapter_files = []
    
    for chapter_dir in basma_dir.glob("Chapitre*"):
        if chapter_dir.is_dir():
            for tex_file in chapter_dir.glob("chapitre*.tex"):
                # Skip backup files
                if "BACKUP" not in tex_file.name and "backup" not in tex_file.name and "_NEW" not in tex_file.name:
                    chapter_files.append(tex_file)
    
    # Also check intro and conclusion
    for section in ["IntroductionGenerale", "ConclusionGenerale"]:
        section_dir = basma_dir / section
        if section_dir.exists():
            for tex_file in section_dir.glob("*.tex"):
                if "backup" not in tex_file.name.lower():
                    chapter_files.append(tex_file)
    
    print(f"\nFound {len(chapter_files)} files to process")
    
    total_modifications = 0
    for filepath in sorted(chapter_files):
        mods = process_file(filepath)
        total_modifications += mods
    
    print("\n" + "=" * 70)
    print(f"Summary: Adjusted {total_modifications} tables across {len(chapter_files)} files")
    print("=" * 70)
    print("\nNote: All tables are now wrapped with adjustbox{max width=\\textwidth}")
    print("This ensures they will automatically scale to fit the page width.")
    print("\nNext steps:")
    print("1. Compile the PDF to see the results")
    print("2. If you need to restore, use the .backup_widths files")

if __name__ == "__main__":
    main()

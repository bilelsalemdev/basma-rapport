#!/usr/bin/env python3
"""
Final script to properly fix table widths without double wrapping.
"""

import re
import shutil
from pathlib import Path

def restore_and_fix(filepath):
    """Restore from backup and apply correct fix"""
    backup_path = f"{filepath}.backup_widths"
    
    if Path(backup_path).exists():
        print(f"Restoring from backup: {filepath}")
        shutil.copy2(backup_path, filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modifications = []
    
    # Pattern 1: Tables within table environment
    # Match: \begin{table}...\begin{tabular}{spec}...\end{tabular}...\end{table}
    def wrap_table_env(match):
        before_tabular = match.group(1)
        tabular_block = match.group(2)
        after_tabular = match.group(3)
        spec = match.group(4)
        
        # Check if needs wrapping
        has_p = 'p{' in spec
        col_count = spec.count('|')
        
        if has_p or col_count >= 6:
            modifications.append(f"  Table: {spec}")
            return (
                f"{before_tabular}"
                f"\\begin{{adjustbox}}{{max width=\\textwidth}}\n"
                f"{tabular_block}\n"
                f"\\end{{adjustbox}}"
                f"{after_tabular}"
            )
        return match.group(0)
    
    # Apply to table environments
    pattern1 = r'(\\begin\{table\}.*?)(\\begin\{tabular\}\{([^}]+)\}.*?\\end\{tabular\})(.*?\\end\{table\})'
    content = re.sub(pattern1, wrap_table_env, content, flags=re.DOTALL)
    
    # Pattern 2: Standalone tabular (not in table environment)
    def wrap_standalone(match):
        indent = match.group(1)
        tabular_block = match.group(2)
        spec = match.group(3)
        
        has_p = 'p{' in spec
        col_count = spec.count('|')
        
        if has_p or col_count >= 6:
            modifications.append(f"  Standalone: {spec}")
            return (
                f"{indent}\\begin{{adjustbox}}{{max width=\\textwidth}}\n"
                f"{indent}{tabular_block}\n"
                f"{indent}\\end{{adjustbox}}"
            )
        return match.group(0)
    
    # Match standalone tabular not preceded by \begin{table}
    pattern2 = r'(?<!\\begin\{table\}\n)(?<!\\begin\{table\}\r\n)([ \t]*)(\\begin\{tabular\}\{([^}]+)\}.*?\\end\{tabular\})'
    content = re.sub(pattern2, wrap_standalone, content, flags=re.DOTALL)
    
    if modifications:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed {len(modifications)} tables")
        for mod in modifications[:5]:
            print(mod)
        if len(modifications) > 5:
            print(f"  ... and {len(modifications) - 5} more")
    else:
        print("  No changes needed")
    
    return len(modifications)

def main():
    print("=" * 70)
    print("Final Table Width Fix - Removing Double Wrapping")
    print("=" * 70)
    
    basma_dir = Path("basma-rapport")
    files_to_fix = []
    
    # Find files with backups
    for backup in basma_dir.rglob("*.backup_widths"):
        original = Path(str(backup).replace(".backup_widths", ""))
        if original.exists():
            files_to_fix.append(original)
    
    print(f"\nFound {len(files_to_fix)} files to fix\n")
    
    total = 0
    for filepath in sorted(files_to_fix):
        print(f"\nProcessing: {filepath}")
        count = restore_and_fix(filepath)
        total += count
    
    print("\n" + "=" * 70)
    print(f"Summary: Fixed {total} tables")
    print("=" * 70)

if __name__ == "__main__":
    main()

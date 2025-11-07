#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix encoding issues in LaTeX files"""

import os
import glob

# Mapping of incorrect characters to correct ones
replacements = {
    b'\xc3\xa2\xe2\x82\xac\xe2\x84\xa2': b"'",  # â€™ -> '
    b'l\xc3\xa2': b"l'",
    b'd\xc3\xa2': b"d'",
    b's\xc3\xa2': b"s'",
    b'c\xc3\xa2': b"c'",
    b'n\xc3\xa2': b"n'",
    b'm\xc3\xa2': b"m'",
    b't\xc3\xa2': b"t'",
    b'j\xc3\xa2': b"j'",
    b'qu\xc3\xa2': b"qu'",
    b'jusqu\xc3\xa2': b"jusqu'",
    b'L\xc3\xa2': b"L'",
    b'D\xc3\xa2': b"D'",
    b'S\xc3\xa2': b"S'",
    b'C\xc3\xa2': b"C'",
    b'N\xc3\xa2': b"N'",
    b'enqu\xc3\x8ate': b'enquete',
    b'\xc3\x8atre': b'etre',
    b'\xc3\x85\xc5\x93': b'oe',
    b'\xc3\x85 ': b'Oe',
    b'\xc3\x83\xc2\xa0': b'a',
    b'\xc3\x83\xc2\xa9': b'e',
    b'\xc3\x83\xc2\xa8': b'e',
    b'\xc3\x83\xc2\xaa': b'e',
    b'\xc3\x83\xc2\xae': b'i',
    b'\xc3\x83\xc2\xb4': b'o',
    b'\xc3\x83\xc2\xb9': b'u',
    b'\xc3\x83\xc2\xa7': b'c',
    b'o\xc3\x83\xc2\xb9': b'ou',
}

def fix_file(filepath):
    """Fix encoding in a single file"""
    print(f"Processing: {filepath}")
    
    try:
        with open(filepath, 'rb') as f:
            content = f.read()
        
        # Remove BOM if present
        if content.startswith(b'\xef\xbb\xbf'):
            content = content[3:]
        
        # Apply replacements
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        # Write back
        with open(filepath, 'wb') as f:
            f.write(content)
        
        print(f"  Fixed: {filepath}")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False

def main():
    """Main function"""
    tex_files = glob.glob('**/*.tex', recursive=True)
    
    fixed = 0
    errors = 0
    
    for filepath in tex_files:
        if fix_file(filepath):
            fixed += 1
        else:
            errors += 1
    
    print(f"\nDone! Fixed {fixed} files, {errors} errors")

if __name__ == '__main__':
    main()

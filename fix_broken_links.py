#!/usr/bin/env python3

import os
import re
import json

def load_broken_links():
    """Extract broken links from link checker output"""
    # Run check_links.py and parse output
    import subprocess
    
    try:
        result = subprocess.run(['python3', 'check_links.py'], 
                              capture_output=True, text=True, cwd='.')
        output = result.stdout
    except Exception as e:
        print(f"Error running link checker: {e}")
        return []
    
    # Parse the output to find broken links with fixes
    broken_links = []
    lines = output.split('\n')
    
    current_file = None
    current_text = None
    current_broken = None
    current_fix = None
    
    for line in lines:
        line = line.strip()
        if line.startswith('📄 '):
            current_file = line[2:].strip()
        elif line.startswith('Text: '):
            current_text = line[6:].strip("'\"")
        elif line.startswith('Broken: '):
            current_broken = line[8:].strip()
        elif line.startswith('Fix: '):
            current_fix = line[5:].strip()
            if current_fix != "No matching file found":
                broken_links.append({
                    'file': current_file,
                    'text': current_text,
                    'broken_url': current_broken,
                    'fix_url': current_fix
                })
    
    return broken_links

def manual_fixes():
    """Manual mapping for known fixes"""
    return {
        '/resources/Notes/': '/resources/notes/',
        '/activities/Set-associative_caching/': '/activities/set-associative-caching/',
        '/activities/Event_handlers_in_Java/': '/activities/event-handlers-in-java/', 
        '/activities/Computer_Architecture_Multilevel_Cache/': '/activities/computer-architecture-multilevel-cache/',
        '/activities/Constructor_Calls/': '/activities/constructor-calls/',
        '/activities/Matching_Types_Part_Three/': '/activities/matching-types-part-three/',
        '/activities/Passing_Arrays_PBV_PBR/': '/activities/passing-arrays-pbv-pbr/',
        '/activities/Parameterized_Student_Sort/': '/activities/parameterized-student-sort/',
        '/activities/Start_of_Class_Shout/': '/activities/start-of-class-shout/',
        '/resources/KLA_Background_Notes/': '/resources/kla-background-notes/',
        '/activities/Merge_Sort/': '/activities/merge-sort/',
        '/activities/Quadratic_Growth/': '/activities/quadratic-growth/',
    }

def fix_file_links(file_path, url_fixes):
    """Fix broken URLs in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = 0
        
        for broken_url, fix_url in url_fixes.items():
            # Fix Jekyll-style links: {{ "/broken/url/" | relative_url }}
            old_pattern = f'{{{{ "{broken_url}" | relative_url }}}}'
            new_pattern = f'{{{{ "{fix_url}" | relative_url }}}}'
            
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                changes += 1
                print(f"  Fixed: {broken_url} → {fix_url}")
        
        if changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
    
    return False

def main():
    print("🔧 Fixing broken links...\n")
    
    # Get all URL fixes (both automatic and manual)
    broken_links = load_broken_links()
    manual_url_fixes = manual_fixes()
    
    # Create comprehensive fix mapping
    all_fixes = {}
    
    # Add automatic fixes from link checker
    for link in broken_links:
        if link['fix_url']:
            all_fixes[link['broken_url']] = link['fix_url']
    
    # Add manual fixes
    all_fixes.update(manual_url_fixes)
    
    print(f"Found {len(all_fixes)} URL fixes to apply:")
    for broken, fixed in all_fixes.items():
        print(f"  {broken} → {fixed}")
    print()
    
    # Apply fixes to all markdown files
    import glob
    
    files_fixed = 0
    for pattern in ['*.md', '_*/*.md']:
        for file_path in glob.glob(pattern, recursive=True):
            if 'node_modules' in file_path or not file_path.endswith('.md'):
                continue
                
            print(f"Checking {file_path}...")
            if fix_file_links(file_path, all_fixes):
                files_fixed += 1
    
    print(f"\n✅ Fixed links in {files_fixed} files")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import os
import re
import glob

def filename_to_jekyll_url(filename):
    """Convert filename to Jekyll URL format"""
    # Remove extension and convert to lowercase with dashes
    name = filename.replace('.md', '')
    name = name.lower().replace('_', '-')
    return name

def create_comprehensive_url_mapping():
    """Create mapping from original-style URLs to correct Jekyll URLs"""
    url_mapping = {}
    
    # Activities
    for file_path in glob.glob('_activities/*.md'):
        filename = os.path.basename(file_path)
        original_name = filename.replace('.md', '')
        jekyll_name = filename_to_jekyll_url(filename)
        
        # Map both ways broken links might appear
        url_mapping[f'/activities/{original_name}/'] = f'/activities/{jekyll_name}/'
        
    # Workshops  
    for file_path in glob.glob('_workshops/*.md'):
        filename = os.path.basename(file_path)
        original_name = filename.replace('.md', '')
        jekyll_name = filename_to_jekyll_url(filename)
        
        url_mapping[f'/workshops/{original_name}/'] = f'/workshops/{jekyll_name}/'
        
    # Resources
    for file_path in glob.glob('_resources/*.md'):
        filename = os.path.basename(file_path)
        original_name = filename.replace('.md', '')  
        jekyll_name = filename_to_jekyll_url(filename)
        
        url_mapping[f'/resources/{original_name}/'] = f'/resources/{jekyll_name}/'
    
    return url_mapping

def fix_all_links():
    """Fix all broken links in all markdown files"""
    url_mapping = create_comprehensive_url_mapping()
    
    print(f"Created URL mapping for {len(url_mapping)} potential broken links")
    print("Sample mappings:")
    for i, (broken, fixed) in enumerate(url_mapping.items()):
        if i < 5:
            print(f"  {broken} → {fixed}")
    print("...\n")
    
    files_fixed = 0
    
    for pattern in ['*.md', '_*/*.md']:
        for file_path in glob.glob(pattern, recursive=True):
            if 'node_modules' in file_path or not file_path.endswith('.md'):
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                changes_made = []
                
                for broken_url, fix_url in url_mapping.items():
                    # Fix Jekyll-style links: {{ "/broken/url/" | relative_url }}
                    old_pattern = f'{{{{ "{broken_url}" | relative_url }}}}'
                    new_pattern = f'{{{{ "{fix_url}" | relative_url }}}}'
                    
                    if old_pattern in content:
                        content = content.replace(old_pattern, new_pattern)
                        changes_made.append(f"{broken_url} → {fix_url}")
                
                if changes_made:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"📄 Fixed {file_path}:")
                    for change in changes_made:
                        print(f"  {change}")
                    files_fixed += 1
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    print(f"\n✅ Fixed links in {files_fixed} files")

if __name__ == "__main__":
    fix_all_links()
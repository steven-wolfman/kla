#!/usr/bin/env python3

import os
import re
import glob

def fix_markdown_links(content):
    """Fix hardcoded absolute URLs in markdown links"""
    
    # Fix markdown links like [text](/activities/page/) 
    content = re.sub(
        r'\[([^\]]*)\]\((/activities/[^)]*)\)',
        r'[\1]({{ "\2" | relative_url }})',
        content
    )
    
    # Fix markdown links like [text](/workshops/page/)
    content = re.sub(
        r'\[([^\]]*)\]\((/workshops/[^)]*)\)',
        r'[\1]({{ "\2" | relative_url }})',
        content
    )
    
    # Fix markdown links like [text](/resources/page/)
    content = re.sub(
        r'\[([^\]]*)\]\((/resources/[^)]*)\)',
        r'[\1]({{ "\2" | relative_url }})',
        content
    )
    
    return content

def main():
    # Find all markdown files
    markdown_files = []
    for pattern in ['**/*.md', '_*/**/*.md']:
        markdown_files.extend(glob.glob(pattern, recursive=True))
    
    print(f"Found {len(markdown_files)} markdown files")
    
    files_changed = 0
    
    for file_path in markdown_files:
        # Skip certain files
        if 'node_modules' in file_path or '.git' in file_path:
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            fixed_content = fix_markdown_links(original_content)
            
            if original_content != fixed_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"Fixed links in: {file_path}")
                files_changed += 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    print(f"\nFixed links in {files_changed} files")

if __name__ == "__main__":
    main()
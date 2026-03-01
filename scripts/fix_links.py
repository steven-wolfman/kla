#!/usr/bin/env python3
"""
Link Cleanup Script for Converted Markdown Files

Fixes common link formatting issues from QWiki conversion.
"""

import os
import re
import glob

def fix_broken_links(content):
    """Fix various broken link patterns."""
    
    # Fix ![Name](Name.md) patterns that should just be names
    content = re.sub(r'!\[([^\]]+)\]\([^\)]+\.md\)', r'\1', content)
    
    # Fix broken HTML link remnants
    content = re.sub(r'<html><a href="[^"]*">([^<]*)<\*a>', r'\1', content)
    content = re.sub(r'<\*html>', '', content)
    
    # Fix malformed URLs with * instead of /
    content = re.sub(r'http:\*\*([^*]+)\*', r'http://\1/', content)
    content = re.sub(r'http:\*([^*]+)\*', r'http://\1/', content)
    
    # Fix broken attachment links
    content = re.sub(r'data\*[^*]+\*([^"]*\.(ppt|pdf|jpg|png))([^"]*)?">', 
                     r'/assets/attachments/\1>', content)
    
    # Fix CamelCase links that became malformed
    content = re.sub(r'\[([A-Z][a-z]+)\s+([A-Z][a-z]+)\]\([^)]*\.md\)', r'[\1 \2](\1_\2.md)', content)
    
    # Remove broken markdown in link text
    content = re.sub(r'\[([^\]]*)\*([^\]]*)\]', r'[\1\2]', content)
    
    return content

def fix_collection_links(content):
    """Fix links to point to correct collection paths."""
    
    # Common activity names - these should link to /activities/
    activity_pattern = r'\[([^\]]+)\]\(([A-Z][A-Za-z0-9_]+)\.md\)'
    
    def replace_activity_link(match):
        text = match.group(1) 
        target = match.group(2)
        
        # Check if this is likely a workshop or resource
        if any(keyword in target.lower() for keyword in ['sigcse_', 'kla_template', 'kla_heuristics', 'design_pattern', 'background_', 'qwiki']):
            if 'sigcse_' in target.lower():
                return f'[{text}](/workshops/{target}/)'
            else:
                return f'[{text}](/resources/{target}/)'
        else:
            return f'[{text}](/activities/{target}/)'
            
    content = re.sub(activity_pattern, replace_activity_link, content)
    
    return content

def process_markdown_file(file_path):
    """Process a single markdown file for link cleanup."""
    print(f"Processing {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
        
    original_content = content
    content = fix_broken_links(content)
    content = fix_collection_links(content)
    
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Updated links in {file_path}")
            return True
        except Exception as e:
            print(f"Error writing {file_path}: {e}")
            return False
    else:
        print(f"  No link fixes needed in {file_path}")
        return True

def main():
    """Main function to process all markdown files."""
    
    # Process all markdown files in collections
    markdown_files = (glob.glob("_activities/*.md") + 
                     glob.glob("_workshops/*.md") + 
                     glob.glob("_resources/*.md") +
                     glob.glob("*.md"))
    
    print(f"Processing {len(markdown_files)} markdown files for link cleanup...")
    print("-" * 50)
    
    processed = 0
    errors = 0
    
    for file_path in sorted(markdown_files):
        if process_markdown_file(file_path):
            processed += 1
        else:
            errors += 1
            
    print("-" * 50)
    print(f"Link cleanup complete!")
    print(f"  Processed: {processed} files")
    print(f"  Errors: {errors} files")

if __name__ == "__main__":
    main()
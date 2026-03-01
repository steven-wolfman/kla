#!/usr/bin/env python3
"""
QWikiWiki to Markdown Converter

This script converts QWikiWiki syntax to standard Markdown syntax.
"""

import os
import re
import glob
from pathlib import Path

def convert_formatting(text):
    """Convert QWiki formatting to Markdown."""
    # Bold: *text* -> **text**
    text = re.sub(r'\*([^*]+)\*', r'**\1**', text)
    
    # Italic: /text/ -> *text*
    text = re.sub(r'/([^/]+)/', r'*\1*', text)
    
    # Code: #text# -> `text`
    text = re.sub(r'#([^#]+)#', r'`\1`', text)
    
    return text

def convert_lists(text):
    """Convert QWiki list syntax to Markdown."""
    lines = text.split('\n')
    converted_lines = []
    
    for line in lines:
        # Handle different list types
        if re.match(r'^[\s]*[-.*!?]\s+', line):
            # Convert to unordered list
            indent = len(line) - len(line.lstrip())
            content = re.sub(r'^[\s]*[-.*!?]\s+', '', line)
            converted_lines.append(' ' * indent + '- ' + content)
        elif re.match(r'^[\s]*\d+\.\s+', line):
            # Numbered lists are already valid markdown
            converted_lines.append(line)
        else:
            converted_lines.append(line)
            
    return '\n'.join(converted_lines)

def convert_links(text, file_stem):
    """Convert QWiki links to Markdown."""
    # Convert explicit links: _Page_Name_ -> [Page Name](Page_Name.md)
    def replace_explicit_link(match):
        page_name = match.group(1)
        display_name = page_name.replace('_', ' ')
        return f'[{display_name}]({page_name}.md)'
    
    text = re.sub(r'_([A-Za-z][A-Za-z0-9_]*)_', replace_explicit_link, text)
    
    # Convert CamelCase links (but be careful not to convert existing markdown)
    def replace_camelcase_link(match):
        page_name = match.group(0)
        # Skip if it's already in a markdown link
        return f'[{page_name}]({page_name}.md)'
    
    # Look for CamelCase words that aren't already in links
    text = re.sub(r'(?<!\[)(?<!\()(?<!\.md)(\b[A-Z][a-z]+[A-Z][A-Za-z]*\b)(?!\])', replace_camelcase_link, text)
    
    return text

def convert_headings(text):
    """Convert QWiki heading syntax to Markdown."""
    lines = text.split('\n')
    converted_lines = []
    
    for line in lines:
        stripped = line.strip()
        # If line is just capitalized words, make it a heading
        if (stripped and 
            not line.startswith(' ') and 
            not line.startswith('-') and
            not line.startswith('.') and
            not line.startswith('!') and
            not line.startswith('?') and
            not line.startswith('#') and
            not '<' in stripped and
            re.match(r'^[A-Z][A-Za-z\s]*[A-Za-z]$', stripped)):
            # Make it a heading
            converted_lines.append(f'## {stripped}')
        else:
            converted_lines.append(line)
            
    return '\n'.join(converted_lines)

def clean_urls(text):
    """Clean up URL formatting."""
    # Fix broken HTML in links
    text = re.sub(r'<b>([^<]*)<b>', r'<b>\1</b>', text)
    return text

def add_frontmatter(content, file_stem, collection_type):
    """Add Jekyll frontmatter to the content."""
    title = file_stem.replace('_', ' ')
    
    frontmatter = f"""---
title: "{title}"
layout: {collection_type}
---

"""
    
    return frontmatter + content

def determine_collection_type(file_stem):
    """Determine which Jekyll collection a file belongs to."""
    
    # Workshop materials
    if any(x in file_stem.lower() for x in ['sigcse_', 'workshop']):
        return 'workshop'
    
    # Resources and meta materials
    resource_keywords = [
        'kla_template', 'kla_heuristics', 'kla_building_blocks', 'kla_background_notes',
        'background_and_philosophy', 'design_pattern', 'qwikisyntax', 'qwikiwiki',
        'home', 'links', 'papers', 'notes', 'props', 'isotlpaper',
        'curriculum_paradigms', 'new_paradigms', 'articulating_cs0', 'cs0_learning_goals'
    ]
    
    if any(keyword in file_stem.lower() for keyword in resource_keywords):
        return 'resource'
    
    # Everything else is an activity
    return 'activity'

def convert_qwiki_file(file_path):
    """Convert a single QWiki file to Markdown."""
    file_stem = Path(file_path).stem
    print(f"Converting {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
        
    # Apply conversions
    content = convert_formatting(content)
    content = convert_lists(content)
    content = convert_links(content, file_stem)
    content = convert_headings(content)
    content = clean_urls(content)
    
    # Determine collection type and add frontmatter
    collection_type = determine_collection_type(file_stem)
    content = add_frontmatter(content, file_stem, collection_type)
    
    return content, collection_type

def main():
    """Main conversion function."""
    data_dir = "data"
    
    # Find all QWiki files
    qwiki_files = glob.glob(os.path.join(data_dir, "*.qwiki"))
    
    if not qwiki_files:
        print(f"No .qwiki files found in {data_dir}/")
        return
        
    print(f"Converting {len(qwiki_files)} QWiki files to Markdown...")
    print("-" * 50)
    
    converted = 0
    errors = 0
    collections = {'activity': 0, 'workshop': 0, 'resource': 0}
    
    for file_path in sorted(qwiki_files):
        result = convert_qwiki_file(file_path)
        if result:
            content, collection_type = result
            file_stem = Path(file_path).stem
            
            # Determine output path
            if collection_type == 'activity':
                output_dir = '_activities'
            elif collection_type == 'workshop':
                output_dir = '_workshops' 
            elif collection_type == 'resource':
                output_dir = '_resources'
            output_path = os.path.join(output_dir, f"{file_stem}.md")
            
            # Write converted file
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  -> {output_path}")
                converted += 1
                collections[collection_type] += 1
            except Exception as e:
                print(f"Error writing {output_path}: {e}")
                errors += 1
        else:
            errors += 1
            
    print("-" * 50)
    print(f"Conversion complete!")
    print(f"  Converted: {converted} files")
    print(f"  Activities: {collections['activity']}")
    print(f"  Workshops: {collections['workshop']}")  
    print(f"  Resources: {collections['resource']}")
    print(f"  Errors: {errors} files")

if __name__ == "__main__":
    main()
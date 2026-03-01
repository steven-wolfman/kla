#!/usr/bin/env python3

import os
import re
import glob
from pathlib import Path

def get_jekyll_url(file_path):
    """Convert file path to Jekyll URL structure"""
    file_path = Path(file_path)
    
    if file_path.match('_activities/*.md'):
        name = file_path.stem.lower().replace('_', '-')
        return f'/activities/{name}/'
    elif file_path.match('_workshops/*.md'):
        name = file_path.stem.lower().replace('_', '-')
        return f'/workshops/{name}/'
    elif file_path.match('_resources/*.md'):
        name = file_path.stem.lower().replace('_', '-')
        return f'/resources/{name}/'
    elif file_path.name in ['index.md', 'activities.md', 'resources.md']:
        if file_path.stem == 'index':
            return '/'
        else:
            return f'/{file_path.stem}/'
    
    return None

def find_all_files():
    """Find all content files and map their Jekyll URLs"""
    url_map = {}
    
    for pattern in ['_activities/*.md', '_workshops/*.md', '_resources/*.md', '*.md']:
        for file_path in glob.glob(pattern):
            if os.path.basename(file_path).startswith('.'):
                continue
            jekyll_url = get_jekyll_url(file_path)
            if jekyll_url:
                url_map[jekyll_url] = file_path
                # Also add version without trailing slash
                if jekyll_url.endswith('/') and jekyll_url != '/':
                    url_map[jekyll_url[:-1]] = file_path
    
    return url_map

def extract_links(content):
    """Extract all markdown links from content"""
    # Match [text]({{ "/path/" | relative_url }}) and [text](/path/)
    pattern = r'\[([^\]]*)\]\(\{\{\s*"([^"]*)"\s*\|\s*relative_url\s*\}\}\)|' \
              r'\[([^\]]*)\]\(([^)]*)\)'
    
    links = []
    for match in re.finditer(pattern, content):
        if match.group(2):  # Jekyll link
            links.append((match.group(1), match.group(2), match.span()))
        elif match.group(4) and not match.group(4).startswith('http'):  # Regular relative link
            links.append((match.group(3), match.group(4), match.span()))
    
    return links

def check_links():
    """Check all links in markdown files"""
    url_map = find_all_files()
    
    print("Available Jekyll URLs:")
    for url in sorted(url_map.keys()):
        print(f"  {url}")
    print()
    
    broken_links = []
    
    for pattern in ['*.md', '_*/*.md']:
        for file_path in glob.glob(pattern, recursive=True):
            if not file_path.endswith('.md') or 'node_modules' in file_path:
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                links = extract_links(content)
                
                for text, url, span in links:
                    if url.startswith('/activities/') or url.startswith('/workshops/') or url.startswith('/resources/'):
                        if url not in url_map:
                            # Try to find a case-insensitive match
                            candidate = None
                            for valid_url in url_map.keys():
                                if valid_url.lower() == url.lower():
                                    candidate = valid_url
                                    break
                            
                            broken_links.append({
                                'file': file_path,
                                'text': text,
                                'broken_url': url,
                                'suggested_fix': candidate,
                                'span': span
                            })
                            
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    
    return broken_links

def main():
    print("🔍 Checking all internal links...\n")
    
    broken_links = check_links()
    
    if not broken_links:
        print("✅ All internal links are working!")
        return
    
    print(f"❌ Found {len(broken_links)} broken links:\n")
    
    for link in broken_links:
        print(f"📄 {link['file']}")
        print(f"   Text: '{link['text']}'")
        print(f"   Broken: {link['broken_url']}")
        if link['suggested_fix']:
            print(f"   Fix: {link['suggested_fix']}")
        else:
            print(f"   Fix: No matching file found")
        print()

if __name__ == "__main__":
    main()
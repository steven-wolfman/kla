#!/usr/bin/env python3
"""
Spam Detection and Cleanup Script for QWikiWiki Files

This script identifies and removes likely spam content from QWiki files 
while generating diff files for manual review.
"""

import os
import re
import glob
import difflib
from pathlib import Path

# Spam detection patterns
SPAM_PATTERNS = {
    'commercial_urls': [
        r'harms-software\.com',
        r'primetimeclothing\.com',
        r'beyondnice\.com',
        r'salon.*software',
        r'wholesale.*clothing',
        r'hot.*tub.*covers'
    ],
    'promotional_keywords': [
        r'\bsalon\b.*\bsoftware\b',
        r'\bwholesale\b.*\bclothing\b', 
        r'\bcheap\b.*\bwholesale\b',
        r'\bhot\b.*\btub\b.*\bcovers\b',
        r'\bmillennium\b.*\bsalon\b',
        r'\bbeauty\b.*\bsalons?\b',
        r'\bfactory\b.*\bdirect\b',
        r'\baward[\-\s]winning\b'
    ],
    'commercial_markers': [
        r'<a\s+href=["\']http://[^"\']*\.com[^"\']*["\'][^>]*>.*?</a>',
        r'designed for beauty salons',
        r'for sale\b',
        r'software\..*salon',
        r'covers?\s+for\s+sale'
    ]
}

# Educational terms that should NOT be flagged as spam
EDUCATIONAL_WHITELIST = [
    r'\bcomputer\s+science\b',
    r'\balgorithm\b',
    r'\bdata\s+structure\b',
    r'\bkinesthetic\b',
    r'\blearning\b',
    r'\beducation\b',
    r'\bstudent\b',
    r'\bteaching\b',
    r'\bsigcse\b',
    r'\buniversity\b',
    r'\bprofessor\b',
    r'\bclass\b',
    r'\bcourse\b'
]

def is_educational_content(text):
    """Check if text contains educational terms that should be preserved."""
    text_lower = text.lower()
    for pattern in EDUCATIONAL_WHITELIST:
        if re.search(pattern, text_lower, re.IGNORECASE):
            return True
    return False

def detect_spam_lines(content):
    """
    Detect likely spam lines in content.
    Returns list of (line_number, line_content, spam_type) tuples.
    """
    spam_lines = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Skip if line contains educational content
        if is_educational_content(line):
            continue
            
        # Check each spam pattern category
        for category, patterns in SPAM_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    spam_lines.append((i + 1, line, f"{category}: {pattern}"))
                    break
                    
    return spam_lines

def clean_spam_from_content(content):
    """
    Remove spam lines from content.
    Returns (cleaned_content, removed_lines) tuple.
    """
    lines = content.split('\n')
    spam_lines = detect_spam_lines(content)
    spam_line_numbers = {line_num for line_num, _, _ in spam_lines}
    
    cleaned_lines = []
    removed_lines = []
    
    for i, line in enumerate(lines):
        if (i + 1) in spam_line_numbers:
            removed_lines.append((i + 1, line))
        else:
            cleaned_lines.append(line)
            
    return '\n'.join(cleaned_lines), removed_lines

def process_qwiki_file(file_path, output_dir):
    """
    Process a single QWiki file for spam removal.
    Creates diff file in output_dir for review.
    """
    print(f"Processing {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            original_content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
        
    # Detect spam
    spam_lines = detect_spam_lines(original_content)
    if not spam_lines:
        print(f"  No spam detected in {file_path}")
        return True
        
    # Clean content
    cleaned_content, removed_lines = clean_spam_from_content(original_content)
    
    # Generate diff
    file_name = Path(file_path).stem
    diff_file = os.path.join(output_dir, f"{file_name}_cleanup.diff")
    
    original_lines = original_content.splitlines(keepends=True)
    cleaned_lines = cleaned_content.splitlines(keepends=True)
    
    diff = list(difflib.unified_diff(
        original_lines,
        cleaned_lines,
        fromfile=f"original/{file_name}.qwiki",
        tofile=f"cleaned/{file_name}.qwiki",
        lineterm=''
    ))
    
    if diff:
        with open(diff_file, 'w', encoding='utf-8') as f:
            f.writelines(diff)
        
        print(f"  Found {len(spam_lines)} spam lines:")
        for line_num, line, reason in spam_lines[:3]:  # Show first 3
            print(f"    Line {line_num}: {line[:60]}... ({reason})")
        if len(spam_lines) > 3:
            print(f"    ... and {len(spam_lines) - 3} more")
        print(f"  Diff saved to: {diff_file}")
        
        # Write cleaned content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
            
        return True
    else:
        print(f"  No changes needed for {file_path}")
        return True

def main():
    """Main execution function."""
    data_dir = "data"
    cleanup_dir = "cleanup-review"
    
    # Create cleanup review directory
    os.makedirs(cleanup_dir, exist_ok=True)
    
    # Find all QWiki files
    qwiki_files = glob.glob(os.path.join(data_dir, "*.qwiki"))
    
    if not qwiki_files:
        print(f"No .qwiki files found in {data_dir}/")
        return
        
    print(f"Found {len(qwiki_files)} QWiki files to process")
    print(f"Cleanup diffs will be saved to {cleanup_dir}/")
    print("-" * 50)
    
    processed = 0
    errors = 0
    
    for file_path in sorted(qwiki_files):
        if process_qwiki_file(file_path, cleanup_dir):
            processed += 1
        else:
            errors += 1
            
    print("-" * 50)
    print(f"Processing complete!")
    print(f"  Processed: {processed} files")
    print(f"  Errors: {errors} files")
    print(f"\nReview cleanup diffs in {cleanup_dir}/ before proceeding.")

if __name__ == "__main__":
    main()
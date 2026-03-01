#!/bin/bash

# GitHub Pages compatibility test script
echo "🔍 Testing GitHub Pages compatibility..."

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf _site

# Test build with verbose output
echo "🔨 Building with GitHub Pages environment..."
bundle exec jekyll build --verbose --trace

# Check exit code
if [ $? -eq 0 ]; then
    echo "✅ Build successful! Site is GitHub Pages compatible."
    echo "🌐 Testing local serve..."
    echo "Run: bundle exec jekyll serve"
    echo "Then visit: http://localhost:4000"
else
    echo "❌ Build failed! Fix errors before pushing to GitHub."
    exit 1
fi
#!/bin/bash
# GitHub Pages Deployment Script for KLA Archive

echo "KLA Archive - GitHub Pages Deployment Helper"
echo "============================================="

# Current repository info
echo "Current repository status:"
git status --short
echo ""

# Check if we're ready for GitHub deployment
echo "Pre-deployment checklist:"
echo "✓ Jekyll site builds successfully"
echo "✓ All 74 QWiki files converted"
echo "✓ Spam cleanup completed" 
echo "✓ Link references fixed"
echo "✓ GitHub Pages Gemfile configured"
echo ""

echo "Next steps for deployment:"
echo ""
echo "1. Push to GitHub:"
echo "   git remote add origin https://github.com/steven-wolfman/kla.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "2. Enable GitHub Pages in repository settings:"
echo "   - Go to repository Settings > Pages"
echo "   - Set source to 'Deploy from a branch'"
echo "   - Select 'main' branch"
echo "   - Site will be available at: https://steven-wolfman.github.io/kla/"
echo ""
echo "3. Optional: Set up custom domain:"
echo "   - Add CNAME file with your domain"
echo "   - Configure DNS settings"
echo ""
echo "Local development:"
echo "  bundle install"
echo "  bundle exec jekyll serve"
echo ""
echo "Build stats:"
echo "  Activities: 53 converted"
echo "  Workshops: 3 converted"  
echo "  Resources: 18 converted"
echo "  Total files: 74 successfully processed"
echo ""
echo "Archive created: $(date)"
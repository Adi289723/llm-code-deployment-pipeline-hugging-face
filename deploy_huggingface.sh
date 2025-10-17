#!/bin/bash

echo "🤗 Deploying to Hugging Face Spaces"
echo "=================================="

# Check if git is configured
if ! git config user.name &> /dev/null; then
    echo "❌ Git user.name not set. Please run: git config --global user.name 'Your Name'"
    exit 1
fi

if ! git config user.email &> /dev/null; then
    echo "❌ Git user.email not set. Please run: git config --global user.email 'your@email.com'"
    exit 1
fi

# Check environment file
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "Please create .env with your environment variables"
    exit 1
fi

echo "✅ Prerequisites check passed"

# Initialize git repository if not exists
if [ ! -d .git ]; then
    git init
    echo "📁 Initialized git repository"
fi

# Add all files
git add .
git commit -m "Deploy to Hugging Face Spaces"

echo "🚀 Files prepared for Hugging Face deployment"
echo ""
echo "Next steps:"
echo "1. Create a new Space on https://huggingface.co/spaces"
echo "2. Choose 'Docker' as the SDK" 
echo "3. Clone the Space repository locally"
echo "4. Copy all files from this directory to the Space repository"
echo "5. Push to the Space repository"
echo "6. Set environment variables in Space settings:"
echo "   - SECRET_KEY"
echo "   - GITHUB_TOKEN"  
echo "   - GITHUB_USERNAME"
echo "   - AIPIPE_TOKEN"
echo ""
echo "Your app will be available at: https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME"

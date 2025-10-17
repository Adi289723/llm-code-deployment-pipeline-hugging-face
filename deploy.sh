#!/bin/bash
# Deployment script for LLM Code Deployment project

echo "🚀 LLM Code Deployment - Automated Deployment Script"
echo "=================================================="

if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "❌ Virtual environment not activated!"
    echo "Please run: source venv/bin/activate (or venv\\Scripts\\activate on Windows)"
    exit 1
fi

if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "Please copy .env.template to .env and configure your variables"
    exit 1
fi

command -v vercel >/dev/null 2>&1 || { 
    echo "❌ Vercel CLI not installed!"
    echo "Please run: npm install -g vercel"
    exit 1
}

echo "✅ Environment checks passed"

pip install -r requirements.txt

echo "🧪 Running local tests..."
python test_api.py

if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Please fix issues before deploying."
    exit 1
fi

echo "✅ Tests passed"

echo "🚀 Deploying to Vercel..."
vercel --prod

if [ $? -eq 0 ]; then
    echo "✅ Deployment successful!"
    echo "🎉 Your API is now live!"
    echo ""
    echo "Next steps:"
    echo "1. Copy your Vercel URL"
    echo "2. Test the deployed API"
    echo "3. Submit to the Google Form with your API endpoint and secret"
else
    echo "❌ Deployment failed!"
    echo "Please check the error messages above and try again."
fi

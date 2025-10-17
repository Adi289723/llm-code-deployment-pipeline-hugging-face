---
title: LLM Code Deployment API
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# LLM Code Deployment API

An automated system that receives application briefs, generates code using LLMs, deploys to GitHub repository, enables GitHub Pages, and reports back to evaluation endpoints.

## Features

- **API Endpoint**: Accepts JSON POST requests with application briefs
- **LLM Integration**: Uses OpenAI GPT-4 via AIPipe to generate application code  
- **GitHub Automation**: Creates repositories, pushes code, enables Pages
- **Evaluation Callback**: Reports deployment details to evaluation URLs

## Environment Variables Required

- `SECRET_KEY`: Your authentication secret
- `GITHUB_TOKEN`: GitHub Personal Access Token
- `GITHUB_USERNAME`: Your GitHub username  
- `AIPIPE_TOKEN`: AIPipe token for OpenAI access

## API Endpoints

- `GET /` - Health check
- `POST /api/deploy` - Deploy new application
- `POST /api/update` - Update existing application (Round 2)

Check the repository for full documentation and usage examples.

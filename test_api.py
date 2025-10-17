#!/usr/bin/env python3
"""
Test script for the LLM Code Deployment API
"""

import requests
import json
import os
import uuid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Test configuration
BASE_URL = "http://127.0.0.1:5000"  # Change to your deployed URL when testing live
SECRET_KEY = os.getenv('SECRET_KEY')
nonce = str(uuid.uuid4())

def test_health_check():
    """Test the health check endpoint"""
    print("Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_deploy_app():
    """Test the app deployment endpoint"""
    print("\nTesting app deployment...")
    
    test_data = {
        "email": "21f3002781@ds.study.iitm.ac.in",
        "secret": SECRET_KEY,
        "task": "test-captcha-solver-123",
        "round": 1,
        "nonce": nonce,
        "brief": "Create a simple captcha solver that displays an image and allows text input for the solution.",
        "checks": [
            "Page displays captcha image",
            "Page has input field for solution",
            "Page has submit button"
        ],
        "evaluation_url": "https://httpbin.org/post",  # Test endpoint
        "attachments": []
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/deploy",
            headers={'Content-Type': 'application/json'},
            json=test_data,
            timeout=60
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
        
    except Exception as e:
        print(f"Deployment test failed: {e}")
        return False

def test_invalid_secret():
    """Test with invalid secret"""
    
    print("\nTesting Secret Authentication with Invalid Secret...")
    test_data = {
        "email": "21f3002781@ds.study.iitm.ac.in",
        "secret": SECRET_KEY + "invalid",
        "task": "test-hello-html",
        "round": 1,
        "nonce": nonce,
        "brief": "Create a simple page that shows Hello and a button.",
        "evaluation_url": "https://httpbin.org/post",
        "attachments": [],
        "checks":["Page has a button", "Shows Hello"]
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/deploy",
            headers={'Content-Type': 'application/json'},
            json=test_data
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 401
        
    except Exception as e:
        print(f"Invalid secret test failed: {e}")
        return False

if __name__ == "__main__":
    print("LLM Code Deployment API Test Suite")
    print("=" * 50)
    
    # Run tests
    health_ok = test_health_check()
    deploy_ok = test_deploy_app()  # Uncomment when ready to test deployment
    secret_ok = test_invalid_secret()
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print(f"Health Check: {'✅ PASS' if health_ok else '❌ FAIL'}")
    print(f"Deployment: {'✅ PASS' if deploy_ok else '❌ FAIL'}")
    print(f"Invalid Secret Test: {'✅ PASS' if secret_ok else '❌ FAIL'}")
    
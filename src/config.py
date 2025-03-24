"""
Configuration file for the HR Policy Chatbot
"""
import os

# Get the absolute path to the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Project Root Directory: {PROJECT_ROOT}")

# API Keys
GEMINI_API_KEY = ""

# Model Configuration
MODEL_CONFIG = {
    "model_name": "gemini-2.0-flash",
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,
}

# Login Credentials
CREDENTIALS = {
    "username": "amana",
    "password": "password123"
}

# System Prompt
SYSTEM_PROMPT = """I'm an HR Policy Chatbot developed by final year students of BBD ITM as their final year project. 
I can help you with information about company HR policies and answer your questions about company benefits, 
work culture, and policies."""

# Image Paths
LOGO_DIR = os.path.join(PROJECT_ROOT, "src", "logos")
print(f"Logo Directory: {LOGO_DIR}")
print(f"Logo Directory exists: {os.path.exists(LOGO_DIR)}")

# Function to find logo file regardless of case
def find_logo_file(company_name):
    """Find the logo file for a company, ignoring case and handling spaces."""
    if not os.path.exists(LOGO_DIR):
        return None
        
    company_name = company_name.lower().replace(" ", "")
    for filename in os.listdir(LOGO_DIR):
        if filename.lower().replace(" ", "") == f"{company_name}.png":
            return os.path.join(LOGO_DIR, filename)
    return None

BBD_LOGO_LOGIN = find_logo_file("bbdlogo") or os.path.join(LOGO_DIR, "bbdlogo.png")
BBD_LOGO_CHAT = find_logo_file("bbdlogochat") or os.path.join(LOGO_DIR, "bbdlogochat.png")

print(f"BBD Login Logo path: {BBD_LOGO_LOGIN}")
print(f"BBD Login Logo exists: {os.path.exists(BBD_LOGO_LOGIN)}")
print(f"BBD Chat Logo path: {BBD_LOGO_CHAT}")
print(f"BBD Chat Logo exists: {os.path.exists(BBD_LOGO_CHAT)}")

# Company Logos (using absolute paths)
COMPANY_LOGOS = {}
COMPANIES = [
    "Genpact", "HCL Tech", "TCS", "Infosys", "Wipro",
    "Accenture", "Cognizant", "Capgemini", "Tech Mahindra", "IBM"
]

for company in COMPANIES:
    logo_path = find_logo_file(company)
    if logo_path:
        COMPANY_LOGOS[company] = logo_path
        print(f"{company} Logo path: {logo_path}")
        print(f"{company} Logo exists: {os.path.exists(logo_path)}")
    else:
        print(f"Warning: Could not find logo for {company}")

# Project Information
CONTRIBUTORS = {
    "students": [
        "Amana Shariq Khan",
        "Chandan Yadav",
        "Aditya Raj Tiwari"
    ],
    "faculty_advisor": "Dr. Anurag Tiwari"
}

# UI Configuration
UI_CONFIG = {
    "theme": {
        "primary_hue": "blue",
        "neutral_hue": "slate",
    },
    "chat_height": 400,
    "input_lines": 2,
    "styles": {
        "header_logo": """
            display: block;
            margin: 0 auto;
            max-width: 200px;
            height: auto;
            margin-bottom: 2rem;
        """,
        "chat_logo": """
            position: absolute;
            top: 20px;
            right: 20px;
            width: 100px;
            height: auto;
        """,
        "container": """
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            text-align: center;
        """,
        "title": """
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #2563eb;
        """,
        "subtitle": """
            font-size: 1.2rem;
            color: #64748b;
            margin-bottom: 2rem;
        """,
        "contributors": """
            margin-top: 3rem;
            padding: 1rem;
            background: #f8fafc;
            border-radius: 8px;
        """,
        "login_form": """
            max-width: 400px;
            margin: 0 auto;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        """
    }
} 
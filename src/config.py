"""
Configuration file for the HR Policy Chatbot
"""
import os

# Hardcoded project root and logo directory
PROJECT_ROOT = "/libpostal/boot/HR-Chatbot"
LOGO_DIR = os.path.join(PROJECT_ROOT, "src", "logos")
print(f"Logo Directory: {LOGO_DIR}")
print(f"Logo Directory exists: {os.path.exists(LOGO_DIR)}")

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
SYSTEM_PROMPT = """You are an HR Policy Chatbot developed by final year students of BBD ITM as their final year project. 
You can help you with information about company HR policies and answer your questions about company benefits, 
work culture, and policies. Only answer questions related to the company you are from. Your are developed by Amana Shariq Khan, Chandan Yadav, Aditya Raj Tiwari and faculty advisor Dr. Anurag Tiwari.
Don't answer any irrelevant question, Only provide answer to query nothing else"""

# Hardcoded logo paths
BBD_LOGO_LOGIN = os.path.join(LOGO_DIR, "bbdlogo.png")
BBD_LOGO_CHAT = os.path.join(LOGO_DIR, "bbdlogochat.png")

# Company Logos with hardcoded paths
COMPANY_LOGOS = {
    "Genpact": os.path.join(LOGO_DIR, "genpact.png"),
    "HCL Tech": os.path.join(LOGO_DIR, "hcltech.png"),
    "TCS": os.path.join(LOGO_DIR, "tcs.png"),
    "Infosys": os.path.join(LOGO_DIR, "infosys.png"),
    "Wipro": os.path.join(LOGO_DIR, "wipro.png"),
    "Accenture": os.path.join(LOGO_DIR, "accenture.png"),
    "Cognizant": os.path.join(LOGO_DIR, "cognizant.png"),
    "Capgemini": os.path.join(LOGO_DIR, "capgemini.png"),
    "Tech Mahindra": os.path.join(LOGO_DIR, "techmahindra.png"),
    "IBM": os.path.join(LOGO_DIR, "ibm.png")
}

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
# HR Policy Chatbot

A simple chatbot that provides information about HR policies for different companies. Currently supports multiple companies including Genpact, HCL Tech, TCS, Infosys, Wipro, Accenture, Cognizant, Capgemini, Tech Mahindra, and IBM.

## Project Structure
```
.
├── src/
│   ├── hr_chatbot.py    # Main application file
│   ├── hr_policies.py   # Company HR policy data
│   ├── config.py        # Configuration settings
│   └── logos/          # Company logos directory
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Setup and Running

1. Set up your Gemini API key in `src/config.py`:
```python
GEMINI_API_KEY = 'your-api-key-here'
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the chatbot:
```bash
python src/hr_chatbot.py
```

## Features
- Secure login system
- Company selection via dropdown menu
- Interactive chat interface with image support
- Modern UI with company logos
- Information about company HR policies including:
  - Leave policies
  - Work hours
  - Benefits
  - Company information

## Contributors
- Amana Shariq Khan
- Chandan Yadav
- Aditya Raj Tiwari

Faculty Advisor: Dr. Anurag Tiwari

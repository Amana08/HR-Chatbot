"""
HR Policy Chatbot - Main Application
"""
import os
import gradio as gr
import google.generativeai as genai
from PIL import Image
from hr_policies import get_company_names, get_company_context
from config import (
    GEMINI_API_KEY, MODEL_CONFIG, CREDENTIALS, SYSTEM_PROMPT,
    COMPANY_LOGOS, CONTRIBUTORS, UI_CONFIG, BBD_LOGO_LOGIN, BBD_LOGO_CHAT
)

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name=MODEL_CONFIG["model_name"],
    generation_config={
        "temperature": MODEL_CONFIG["temperature"],
        "top_p": MODEL_CONFIG["top_p"],
        "top_k": MODEL_CONFIG["top_k"],
        "max_output_tokens": MODEL_CONFIG["max_output_tokens"],
    }
)

def get_hr_response(company_name: str, user_query: str, image_file: str = None) -> str:
    """Get response from the HR chatbot based on company context and user query."""
    if not company_name:
        return "Please select a company first."

    try:
        context = get_company_context(company_name)
        prompt = f"""{SYSTEM_PROMPT}

        I'm currently helping with {company_name}'s HR policies.
        
        Company Information and Policies:
        {context}
        
        User Question: {user_query}"""

        if image_file:
            try:
                image = Image.open(image_file)
                response = model.generate_content([prompt, image])
            except Exception as e:
                return f"Error processing image: {str(e)}"
        else:
            response = model.generate_content(prompt)
            
        return response.text
    except Exception as e:
        return f"Error processing your request: {str(e)}"

css = """
    #bbd-logo-login {
        display: block;
        margin: 0 auto;
        max-width: 200px;
        height: auto;
        margin-bottom: 2rem;
    }
    #bbd-logo-chat {
        position: absolute;
        top: 20px;
        right: 20px;
        width: 100px;
        height: auto;
    }
    .login-form {
        max-width: 400px;
        margin: 0 auto;
        padding: 2rem;
        background: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    }
    .contributors {
        margin-top: 3rem;
        padding: 1rem;
        background: #f8fafc;
        border-radius: 8px;
    }
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
        text-align: center;
    }
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: #2563eb;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #64748b;
        margin-bottom: 2rem;
    }
"""

def create_login_page():
    """Create the login page interface."""
    with gr.Blocks(theme=gr.themes.Soft(**UI_CONFIG["theme"])) as login_page:
        with gr.Column():
            # BBD Logo
            gr.Image(
                value=BBD_LOGO_LOGIN,
                show_label=False,
                container=False,
                elem_id="bbd-logo-login"
            )
            
            # Title and Subtitle
            gr.Markdown(
                """
                <div class="container">
                    <h1 class="title">HR Policy Chatbot</h1>
                    <p class="subtitle">Final Year Project - BBD ITM</p>
                </div>
                """
            )
            
            # Login Form
            with gr.Group(elem_classes="login-form"):
                gr.Markdown("### Login")
                username = gr.Textbox(
                    label="Username",
                    placeholder="Enter username",
                    container=True
                )
                password = gr.Textbox(
                    label="Password",
                    type="password",
                    placeholder="Enter password",
                    container=True
                )
                login_button = gr.Button("Login", variant="primary")
                error_message = gr.Markdown(visible=False)
            
            # Contributors Section
            with gr.Group(elem_classes="contributors"):
                gr.Markdown("### Contributors")
                for student in CONTRIBUTORS["students"]:
                    gr.Markdown(f"- {student}")
                gr.Markdown("\n### Faculty Advisor")
                gr.Markdown(f"- {CONTRIBUTORS['faculty_advisor']}")
            
        return login_page, username, password, login_button, error_message

def create_chat_interface():
    """Create the main chat interface."""
    with gr.Blocks(theme=gr.themes.Soft(**UI_CONFIG["theme"])) as chat_interface:
        # Chat Logo
        gr.Image(
            value=BBD_LOGO_CHAT,
            show_label=False,
            container=False,
            elem_id="bbd-logo-chat"
        )
        
        gr.Markdown(
            """
            <div class="container">
                <h1 class="title">HR Policy Chatbot</h1>
                <p class="subtitle">Your AI Assistant for Company HR Policies</p>
            </div>
            """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                company_dropdown = gr.Dropdown(
                    choices=get_company_names(),
                    label="Select Company",
                    info="Choose the company you want to learn about",
                    container=True
                )
                company_logo = gr.Image(
                    label="Company Logo",
                    interactive=False,
                    show_label=False,
                    container=False
                )
                
                def update_logo(company):
                    return COMPANY_LOGOS.get(company, None) if company else None
                company_dropdown.change(fn=update_logo, inputs=company_dropdown, outputs=company_logo)
                
                image_input = gr.Image(
                    label="Upload Image (Optional)",
                    type="filepath",
                    sources="upload",
                    container=True
                )
            
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(
                    label="Conversation",
                    height=UI_CONFIG["chat_height"],
                    show_label=False,
                    bubble_full_width=False,
                    container=True
                )
                
                with gr.Row():
                    user_input = gr.Textbox(
                        label="Your Question",
                        placeholder="Ask about leave policy, work hours, benefits, etc.",
                        lines=UI_CONFIG["input_lines"],
                        container=True
                    )
                    submit_btn = gr.Button("Ask", variant="primary")
                
                clear_btn = gr.Button("Clear Conversation", variant="secondary")
                
                def chat_response(company, question, image, history):
                    history = history or []
                    response = get_hr_response(company, question, image)
                    history.append((question, response))
                    return history, ""
                
                submit_btn.click(
                    fn=chat_response,
                    inputs=[company_dropdown, user_input, image_input, chatbot],
                    outputs=[chatbot, user_input]
                )
                
                clear_btn.click(
                    fn=lambda: ([], None),
                    outputs=[chatbot, user_input]
                )
                
        return chat_interface

def verify_credentials(username: str, password: str) -> bool:
    """Verify login credentials."""
    return username == CREDENTIALS["username"] and password == CREDENTIALS["password"]

def create_app():
    """Create the complete application with login and chat interfaces."""
    login_interface, username_input, password_input, login_button, login_error = create_login_page()
    chat_interface = create_chat_interface()

    with gr.Blocks(theme=gr.themes.Soft(**UI_CONFIG["theme"]), css=css) as app:
        login_block = gr.Group(visible=True)
        chat_block = gr.Group(visible=False)
        
        with login_block:
            login_interface.render()
        
        with chat_block:
            chat_interface.render()
        
        def handle_login(username, password):
            if verify_credentials(username, password):
                return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=True, value="Invalid credentials. Please try again.")
        
        login_button.click(
            fn=handle_login,
            inputs=[username_input, password_input],
            outputs=[login_block, chat_block, login_error]
        )
        
        return app

if __name__ == "__main__":
    app = create_app()
    app.launch(share=True, server_name="0.0.0.0", server_port=8811)
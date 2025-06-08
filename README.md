# Intuitive Frontend
This README provides details on the user interface for the Intuitive Soul Chatbot, including setup, configuration, and file descriptions for the Streamlit app.

## Installation
1. Clone the repo
```bash
git clone https://github.com/intuitivechatbot/UI.git
```
2. Navigate to the UI folder
```bash
cd UI
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
## Configuration
No additional environment variables are required for the UI beyond those configured for the API backend. Ensure that the backend service URL is reachable and update it in streamlit_app.py if needed

## Project Structure
```txt
UI/
├── Procfile
├── requirements.txt
├── runtime.txt
└── streamlit_app.py
```
## File Descriptions

1. Procfile
- Purpose: Defines the startup command for Render (and other Procfile-based platforms) to launch the Streamlit app.
- Content: 
```bash
web: streamlit run streamlit_app.py --server.port=$PORT 
```
2. requirments.txt
- Purpose: Lists Python packages required by the Streamlit UI.
- Key Entries:
```txt
streamlit
requests
```
3. runtime.txt 
- Purpose: Specifies the Python runtime version for deployment platforms.
4. streamlit_app.py
- Purpose: Implements the Streamlit-based chat interface that interacts with the backend API.
- Key Sections:
Page Setup:
```python
st.set_page_config(page_title="Intuitive Soul Chatbot", page_icon="")
```
Session State Initialization:
```python
if "messages" not in st.session_state:
    st.session_state.messages = []
if "role" not in st.session_state:
    st.session_state.role = "You are the CEO of Intuitive Soul"
```
User Input & API Call:
Captures user questions via `st.chat_input`.
Sends a POST request to the backend API (/ask) with JSON payload containing input and role.

Error Handling:
Handles non-200 HTTP responses and network exceptions, displaying informative messages in the chat.

Chat History Rendering:
```python
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
```

## Usage
1. Ensure the backend API is deployed and accessible (e.g., https://api.example.com/ask).

2. In the streamlit_app.py, update the URL passed to requests.post() if it differs from the default.

3. Start the Streamlit UI locally:
```bash
streamlit run streamlit_app.py
```
4. In production on Render, the Procfile’s web: command will launch the UI. Navigate to your service URL to interact with the chat UI.


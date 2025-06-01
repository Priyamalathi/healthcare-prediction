import streamlit as st
import google.generativeai as genai

# --- Config API ---
genai.configure(api_key="AIzaSyClwCo8aIpV8gieeDQ5HsjiASODhGkxt-0")  # Replace with your actual API key

# --- Generation configuration ---
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# --- Initialize the model ---
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "Want to create a Medical chatbot. User can ask questions related to their disease "
        "like suggest medicines, precautions and so on. If I speak in Tulu, the reply must be in Tulu."
    ),
)

# --- Set up Streamlit ---
st.set_page_config(page_title="💊 Medical Chatbot", layout="wide")
st.title("💊 Medical Chatbot")
st.markdown("Ask any health-related questions. If you speak in Tulu, the bot will reply in Tulu.")

# --- Session state for chat history ---
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": ["Hi, I have a cold, give suggestions."]
        },
        {
            "role": "model",
            "parts": ["""I am an AI and cannot give medical advice. A cold is usually caused by a virus and will typically clear up on its own within 7–10 days. However, to alleviate symptoms, try the following:

- 💧 **Hydration:** Drink fluids like water or tea  
- 😴 **Rest:** Help your body recover  
- 💊 **OTC Meds:** Try paracetamol or ibuprofen for fever  
- 🌬️ **Humidifier:** Helps with nasal congestion  
- 🧂 **Salt gargle:** For sore throat  
- 🚫 **Avoid irritants:** Like smoke and dust

> ⚠️ **Consult a doctor if symptoms persist or worsen.**
"""]
        }
    ])
    st.session_state.messages = []

# --- Chat form ---
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You", placeholder="Describe your symptoms or ask a health question...", label_visibility="collapsed")
    submitted = st.form_submit_button("Send")

# --- Handle input and display ---
if submitted and user_input:
    st.session_state.messages.append(("user", user_input))
    response = st.session_state.chat.send_message(user_input)
    st.session_state.messages.append(("bot", response.text))

# --- Display chat messages ---
for role, msg in st.session_state.messages:
    col1, col2 = st.columns([1, 5]) if role == "user" else st.columns([5, 1])
    with col1 if role == "user" else col2:
        if role == "user":
            st.markdown(f"🧑‍💬 **You:**\n\n{msg}", unsafe_allow_html=True)
        else:
            st.markdown(f"🤖 **Bot:**\n\n{msg}", unsafe_allow_html=True)

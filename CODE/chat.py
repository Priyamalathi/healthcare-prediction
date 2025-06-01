# Required package:
# pip install google-generativeai

import google.generativeai as genai

# Configure API
genai.configure(api_key="AIzaSyClwCo8aIpV8gieeDQ5HsjiASODhGkxt-0")  # Replace with your API key

# Generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model with system instruction
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "Want to create a Medical chatbot. User can ask questions related to their disease "
        "like suggest medicines, precautions and so on. If I speak in Tulu, the reply must be in Tulu."
    ),
)

# Start the chat session
chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["Hi, I have a cold, give suggestions."]
    },
    {
        "role": "model",
        "parts": ["""I am an AI and cannot give medical advice. A cold is usually caused by a virus and will typically clear up on its own within 7–10 days. However, to alleviate symptoms, try the following:

* **Rest:** Help your body recover.
* **Hydration:** Drink fluids like water, clear broths, or herbal teas.
* **OTC medications:** For fever or aches, use acetaminophen or ibuprofen. For congestion, try decongestants or saline sprays. Read instructions carefully.
* **Humidifier:** Keeps air moist to ease breathing.
* **Saltwater gargle:** Soothes sore throat.
* **Avoid irritants:** Smoke and dust may worsen symptoms.

**See a doctor if:**
* Symptoms last more than 1–2 weeks
* You have a high fever (>101°F / 38.3°C)
* Breathing difficulty or chest pain
* Green/yellow mucus persists

Always consult a healthcare professional for personalized advice."""]
    }
])

# Chat loop
def chat_loop():
    print("Medical Chatbot (type 'exit' to stop)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            print("Bot: Goodbye! Take care.")
            break
        response = chat.send_message(user_input)
        print("Bot:", response.text)

if __name__ == "__main__":
    chat_loop()

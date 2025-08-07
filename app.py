import streamlit as st
import openai
import random

st.set_page_config(page_title="AI Quote Generator", layout="centered")
st.title("🎭 Emotion-based AI Quote Generator")

# Select emotion
emotion = st.selectbox("Choose your emotion:", ["Happy", "Sad", "Motivated", "Heartbroken", "Excited"])

# Mode selector (demo vs OpenAI)
mode = st.radio("Choose mode:", ["Demo Version (Free)", "AI-Powered Version (OpenAI)"])

# Predefined quotes for demo
demo_quotes = {
    "Happy": [
        "Happiness is not by chance, but by choice.",
        "Smile – it’s the key to happiness."
    ],
    "Sad": [
        "Tears come from the heart, not the brain.",
        "Sometimes it's okay to not be okay."
    ],
    "Motivated": [
        "Push yourself, because no one else is going to do it for you.",
        "Dream big. Work hard. Stay focused."
    ],
    "Heartbroken": [
        "It hurts because it mattered.",
        "Sometimes goodbye is a second chance."
    ],
    "Excited": [
        "Great things are coming – stay excited!",
        "Let your excitement light up the world!"
    ]
}

# Generate quote
if st.button("Generate Quote"):
    if mode == "Demo Version (Free)":
        quote = random.choice(demo_quotes[emotion])
        st.success(quote)

    else:
        try:
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            prompt = f"Generate a short, original quote that reflects the emotion: {emotion.lower()}."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            quote = response.choices[0].message.content.strip()
            st.success(quote)
        except Exception as e:
            st.error("OpenAI API error or quota exceeded. Try demo mode instead.")

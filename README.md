# 🎭 Emotion-based AI Quote Generator

An AI-powered web app that generates short, original quotes based on the user's selected emotion.  
This project uses **Streamlit** for the frontend and **OpenAI's GPT model** to generate meaningful quotes that resonate with specific moods like **happiness**, **sadness**, **motivation**, **heartbreak**, or **excitement**.

---

## ✨ Features

- 🎨 Emotion selection (Happy, Sad, Motivated, Heartbroken, Excited)
- 🤖 AI-generated original quotes using GPT-3.5
- ⚡ Simple, interactive, and user-friendly interface
- 🧪 **Demo version available (no API key required)**
- 📦 Built using **Streamlit** and **Python**

---

## 🚀 How to Run Locally

### 1. Clone the repository

git clone https://github.com/anjaliupmanyu01/ai-quote-generator.git
cd ai-quote-generator

2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate  # For Windows

3. Install dependencies

pip install -r requirements.txt

4. Add your OpenAI API key (for real quote generation)
Create a file called .streamlit/secrets.toml and add the following:


OPENAI_API_KEY = "your-api-key-here"
🔑 Don’t have an API key? You can get one from OpenAI.
Or simply try the free demo mode (see below).

5. Run the app

streamlit run app.py


🌐 Live Demo
Try the 👉 Free Demo Version
(Optional: if deployed on HuggingFace, Streamlit Cloud, or any mock version)

🛠️ Tech Stack
Python

Streamlit

OpenAI GPT-3.5 (ChatCompletion API)

📂 Project Structure

ai-quote-generator/
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml


📄 License
This project is licensed under the MIT License – feel free to use and modify for personal or professional use.

🙋‍♀️ Author
Made with ❤️ by Anjali Upmanyu

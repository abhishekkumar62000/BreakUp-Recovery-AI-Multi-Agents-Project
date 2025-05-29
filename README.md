https://github.com/user-attachments/assets/adc1b1e1-9948-4d28-950b-9e3144f9d9ae

![App look page](https://github.com/user-attachments/assets/77a76e8f-90ce-4f3e-9aeb-092667703ef0)
![thumnail](https://github.com/user-attachments/assets/9b8b8943-e294-4583-b19e-8af84a1b0b67)


---

# 💔 BreakUp Recovery AI – Multi-Agent Emotional Support App

A feature-rich, emotionally intelligent AI-powered platform to help users heal from breakups through text, image, and audio-based interactions with specialized AI agents. Built using **Streamlit**, **Google Gemini**, and **Agno framework**, the app delivers personalized recovery plans and real-time support.

---

## 🌟 Core Purpose

This app is designed to assist users through the emotional turbulence of breakups by offering AI-driven empathy, actionable feedback, and self-care tools in a structured, supportive environment.

---

## 🧠 Key Features

### 🤖 Multi-Agent AI Team

* **Therapist Agent**: Offers support, validation, and image-based emotion analysis.
* **Closure Agent**: Helps craft unsent messages and closure rituals.
* **Routine Planner Agent**: Suggests 7-day recovery plans and wellness routines.
* **Brutal Honesty Agent**: Gives direct feedback using web-based factual insights (via DuckDuckGo).

### 💬 User Input & Uploads

* **Text Input**: Breakup story or feelings.
* **Image Upload**: Upload chat screenshots for emotion/context detection.
* **Audio Upload**: Upload voice recordings for tone and sentiment analysis.

### 📊 Interactive Tools

* **Mood Tracker**: Daily mood logs with visual chart (line graph).
* **Affirmations**: Positive rotating affirmations.
* **Self-Care Checklist**: Tasks with checkboxes, songs, and actions.
* **Journal**: User entries with Therapist reflections.
* **Anonymous Community Chat**: Supportive message board.

### 🧩 Personalized Recovery Plan

* On “Get Recovery Plan 💝”, all agents are initialized using the **Gemini API key**.
* Inputs are analyzed and feedback is provided by each agent.

### 🎧 Audio Call Analysis

* Placeholder for transcription (MP3, WAV, M4A supported).
* AI agents analyze and generate empowering replies.
* User can rate analysis usefulness.

### 📞 Real-Time AI Call (via Vipe API)

* Start voice conversations with AI agent.
* Shareable call link generation.

### 💾 Session Management

* All data (API keys, journal, chat, mood logs) managed via `st.session_state`.

---

## 🛠️ Tech Stack

| Component          | Technology                            |
| ------------------ | ------------------------------------- |
| Frontend/UI        | Streamlit                             |
| Agents & AI Logic  | Agno + Google Gemini 2.0 Flash Vision |
| Image Processing   | PIL (via Agno)                        |
| Audio Handling     | Upload + Transcription (placeholder)  |
| Web Search         | DuckDuckGo API                        |
| Voice API          | Vipe                                  |
| State Management   | `st.session_state`                    |
| Data Visualization | Pandas / Matplotlib                   |

---

## 🔒 Security & Privacy

* No data is permanently stored.
* All inputs (journal, mood, chat) are session-based.
* API keys are stored securely in session state.

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/abhishekkumar62000/BreakUp-Recovery-AI-Multi-Agents-Project.git
cd breakup-recovery-ai
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
📁 breakup-recovery-ai/
│
├── app.py                      # Main Streamlit app
├── agents/
│   ├── therapist.py
│   ├── closure.py
│   ├── planner.py
│   └── brutal_honesty.py
│
├── utils/
│   ├── mood_tracker.py
│   ├── audio_handler.py
│   └── image_analysis.py
│
├── requirements.txt
└── README.md
```

---

## 🔮 Extensibility

* Easily plug in more agents with unique functions.
* Add real-time transcription or more community tools.
* Modular design promotes clean code and scalability.

---

## 🧘 Summary

**BreakUp Recovery AI** is more than an app — it’s a healing companion. Whether you want empathy, structure, or tough love, the AI agent team is here to guide you toward a better emotional state using state-of-the-art AI.

---

## 🙏 Special Thanks

* [Gemini API](https://ai.google.dev/)
* [Agno Framework](https://github.com/jina-ai/agno)
* [DuckDuckGo API](https://duckduckgo.com/)
* [Vipe Voice API](https://vipe.ai/)
* [Streamlit](https://streamlit.io)

---

## ✨ License

MIT License. Feel free to fork, customize, and improve!

---


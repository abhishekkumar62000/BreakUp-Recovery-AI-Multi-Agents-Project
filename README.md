https://github.com/user-attachments/assets/adc1b1e1-9948-4d28-950b-9e3144f9d9ae

![App look page](https://github.com/user-attachments/assets/77a76e8f-90ce-4f3e-9aeb-092667703ef0)
![thumnail](https://github.com/user-attachments/assets/9b8b8943-e294-4583-b19e-8af84a1b0b67)

App Try it YourSelf🚨:-- https://breakup-recovery-ai.streamlit.app/
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


4. Optionally, export the diagram from [https://mermaid.live](https://mermaid.live) as a PNG/SVG and upload it to your repo `/assets/` folder.

---

## ❤️ **Made with Passion by Abhishek Yadav & Open-Source Contributors!** 🚀✨


<h1 align="center">© LICENSE <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Telegram-Animated-Emojis/main/Symbols/Check%20Box%20With%20Check.webp" alt="Check Box With Check" width="25" height="25" /></h1>

<table align="center">
  <tr>
     <td>
       <p align="center"> <img src="https://github.com/malivinayak/malivinayak/blob/main/LICENSE-Logo/MIT.png?raw=true" width="80%"></img>
    </td>
    <td> 
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg"/> <br> 
This project is licensed under <a href="./LICENSE">MIT</a>. <img width=2300/>
    </td>
  </tr>
</table>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">




 <hr>

<div align="center">
<a href="#"><img src="assets/githubgif.gif" width="150"></a>
	
### **Thanks for checking out my GitHub Profile!**  

 ## 💌 Sponser

  [![BuyMeACoffee](https://img.buymeacoffee.com/button-api/?text=Buymeacoffee&emoji=&slug=codingstella&button_colour=FFDD00&font_colour=000000&font_family=Comic&outline_colour=000000&coffee_colour=ffffff)](https://www.buymeacoffee.com/abhishekkumar62000)

## 👨‍💻 Developer Information  
**Created by:** **Abhishek Kumar**  
**📧 Email:** [abhiydv23096@gmail.com](mailto:abhiydv23096@gmail.com)  
**🔗 LinkedIn:** [Abhishek Kumar](https://www.linkedin.com/in/abhishek-kumar-70a69829a/)  
**🐙 GitHub Profile:** [@abhishekkumar62000](https://github.com/abhishekkumar62000)

<p align="center">
  <img src="https://github.com/user-attachments/assets/6283838c-8640-4f22-87d4-6d4bfcbbb093" width="120" style="border-radius: 50%;">
</p>
</div>  


`Don't forget to give A star to this repository ⭐`


`👍🏻 All Set! 💌`

</div>

---

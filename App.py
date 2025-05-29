from agno.agent import Agent
from agno.models.google import Gemini
from agno.media import Image as AgnoImage
from agno.tools.duckduckgo import DuckDuckGoTools 
import streamlit as st 
from typing import List, Optional
import logging
from pathlib import Path
import tempfile
import os
import datetime
import random
import pandas as pd
import requests

# Configure logging for errors only
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def initialize_agents(api_key: str) -> tuple[Agent, Agent, Agent, Agent]:
    try:
        model = Gemini(id="gemini-2.0-flash-exp", api_key=api_key)
        
        therapist_agent = Agent(
            model=model,
            name="Therapist Agent",
            instructions=[
                "You are an empathetic therapist that:",
                "1. Listens with empathy and validates feelings",
                "2. Uses gentle humor to lighten the mood",
                "3. Shares relatable breakup experiences",
                "4. Offers comforting words and encouragement",
                "5. Analyzes both text and image inputs for emotional context",
                "Be supportive and understanding in your responses"
            ],
            markdown=True
        )

        closure_agent = Agent(
            model=model,
            name="Closure Agent",
            instructions=[
                "You are a closure specialist that:",
                "1. Creates emotional messages for unsent feelings",
                "2. Helps express raw, honest emotions",
                "3. Formats messages clearly with headers",
                "4. Ensures tone is heartfelt and authentic",
                "Focus on emotional release and closure"
            ],
            markdown=True
        )

        routine_planner_agent = Agent(
            model=model,
            name="Routine Planner Agent",
            instructions=[
                "You are a recovery routine planner that:",
                "1. Designs 7-day recovery challenges",
                "2. Includes fun activities and self-care tasks",
                "3. Suggests social media detox strategies",
                "4. Creates empowering playlists",
                "Focus on practical recovery steps"
            ],
            markdown=True
        )

        brutal_honesty_agent = Agent(
            model=model,
            name="Brutal Honesty Agent",
            tools=[DuckDuckGoTools()],
            instructions=[
                "You are a direct feedback specialist that:",
                "1. Gives raw, objective feedback about breakups",
                "2. Explains relationship failures clearly",
                "3. Uses blunt, factual language",
                "4. Provides reasons to move forward",
                "Focus on honest insights without sugar-coating"
            ],
            markdown=True
        )
        
        return therapist_agent, closure_agent, routine_planner_agent, brutal_honesty_agent
    except Exception as e:
        st.error(f"Error initializing agents: {str(e)}")
        return None, None, None, None

# Set page config and UI elements
st.set_page_config(
    page_title="💔 Breakup Recovery Squad",
    page_icon="💔",
    layout="wide"
)



# Sidebar for API key input
with st.sidebar:
    st.header("🔑 API Configuration")

    if "api_key_input" not in st.session_state:
        st.session_state.api_key_input = ""
        
    api_key = st.text_input(
        "Enter your Gemini API Key",
        value=st.session_state.api_key_input,
        type="password",
        help="Get your API key from Google AI Studio",
        key="api_key_widget"  
    )

    if api_key != st.session_state.api_key_input:
        st.session_state.api_key_input = api_key
    
    if api_key:
        st.success("API Key provided! ✅")
    else:
        st.warning("Please enter your API key to proceed")
        st.markdown("""
        To get your API key:
        1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
        2. Enable the Generative Language API in your [Google Cloud Console](https://console.developers.google.com/apis/api/generativelanguage.googleapis.com)
        """)

# --- Mood Tracker & Progress Visualization ---
def mood_tracker():
    st.subheader("📈 Mood Tracker")
    if "mood_data" not in st.session_state:
        st.session_state.mood_data = []
    today = datetime.date.today()
    mood_options = ["😭 Very Sad", "😢 Sad", "😐 Neutral", "🙂 Okay", "😃 Good"]
    mood = st.radio("How do you feel today?", mood_options, key=f"mood_{today}")
    if st.button("Save Mood", key="save_mood"):
        st.session_state.mood_data.append({"date": today, "mood": mood})
        st.success("Mood saved!")
    if st.session_state.mood_data:
        df = pd.DataFrame(st.session_state.mood_data)
        st.line_chart(df.groupby("date").mood.apply(lambda x: mood_options.index(x.iloc[-1])).reset_index(name="Mood Index").set_index("date"))

# --- Personal Journal with AI Reflection ---
def personal_journal(therapist_agent):
    st.subheader("📓 Personal Journal")
    if "journal_entries" not in st.session_state:
        st.session_state.journal_entries = []
    journal_text = st.text_area("Write about your day or feelings:", height=100, key="journal_text")
    if st.button("Save Journal", key="save_journal"):
        entry = {"date": datetime.date.today(), "text": journal_text}
        st.session_state.journal_entries.append(entry)
        st.success("Journal entry saved!")
        # AI Reflection
        with st.spinner("AI reflecting on your journal..."):
            ai_response = therapist_agent.run(message=f"Reflect on this journal entry and offer gentle encouragement:\n{journal_text}")
            st.markdown(f"**AI Reflection:** {ai_response.content}")
    if st.session_state.journal_entries:
        st.markdown("#### Previous Entries")
        for entry in reversed(st.session_state.journal_entries):
            st.markdown(f"**{entry['date']}**: {entry['text']}")

# --- Daily Affirmations ---
AFFIRMATIONS = [
    "You are stronger than you think.",
    "Every day is a new beginning.",
    "You deserve happiness and peace.",
    "Let go of what no longer serves you.",
    "Your feelings are valid.",
    "Healing is not linear, and that's okay."
]
def daily_affirmation():
    st.subheader("🌞 Daily Affirmation")
    today = datetime.date.today()
    idx = today.toordinal() % len(AFFIRMATIONS)
    st.info(AFFIRMATIONS[idx])

# --- Self-Care Checklist ---
SELF_CARE_TASKS = [
    "Drink a glass of water",
    "Go for a short walk",
    "Listen to your favorite song",
    "Write down 3 things you're grateful for",
    "Do a 5-minute meditation",
    "Call or text a friend"
]
def self_care_checklist():
    st.subheader("🧘 Self-Care Checklist")
    if "self_care" not in st.session_state:
        st.session_state.self_care = {task: False for task in SELF_CARE_TASKS}
    for task in SELF_CARE_TASKS:
        st.session_state.self_care[task] = st.checkbox(task, value=st.session_state.self_care[task], key=f"sc_{task}")
        if task == "Listen to your favorite song" and st.session_state.self_care[task]:
            song_url = st.text_input("Paste a YouTube/Spotify link to your favorite song:", key="fav_song_url")
            if song_url:
                if "youtube.com" in song_url or "youtu.be" in song_url:
                    st.video(song_url)
                elif "spotify.com" in song_url:
                    st.markdown(f"[Open in Spotify]({song_url})")
                else:
                    st.markdown(f"[Open your song]({song_url})")
        if task == "Call or text a friend" and st.session_state.self_care[task]:
            phone_number = st.text_input("Enter your friend's phone number:", key="friend_phone")
            message = st.text_area("Message to send (optional):", key="friend_message")
            if phone_number:
                st.markdown(f"[📞 Call your friend](tel:{phone_number})")
                st.markdown(f"[💬 Send SMS](sms:{phone_number}?body={message})")
    if all(st.session_state.self_care.values()):
        st.success("Great job! You completed all self-care tasks today.")

# --- Anonymous Community Support Chat (Simple) ---
def community_chat():
    st.subheader("💬 Community Support (Anonymous)")
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []
    chat_input = st.text_input("Share your thoughts or support others (anonymous):", key="chat_input")
    if st.button("Send", key="send_chat"):
        if chat_input.strip():
            st.session_state.chat_messages.append({"time": datetime.datetime.now().strftime("%H:%M"), "msg": chat_input})
    for msg in reversed(st.session_state.chat_messages[-20:]):
        st.markdown(f"**[{msg['time']}]** {msg['msg']}")

# --- MAIN APP LAYOUT ---

# Main content
st.title("💔 BreakUp Recovery Squad Multi Agents🤖")
st.markdown("""
    ### Your AI-powered breakup recovery team is here to help!
    Share your feelings and chat screenshots, and we'll help you navigate through this tough time.
""")

# --- New Interactive Features Section ---
with st.expander("✨ Interactive Recovery Tools (Click to expand)"):
    mood_tracker()
    daily_affirmation()
    self_care_checklist()
    if "therapist_agent" in st.session_state and st.session_state["therapist_agent"]:
        personal_journal(st.session_state["therapist_agent"])
    else:
        st.info("Journal AI reflection will be available after you enter your API key and generate a recovery plan.")
    community_chat()

# Input section
col1, col2 = st.columns(2)

with col1:
    st.subheader("Share Your Feelings")
    user_input = st.text_area(
        "How are you feeling? What happened?",
        height=150,
        placeholder="Tell us your story..."
    )
    
with col2:
    st.subheader("Upload Chat Screenshots")
    uploaded_files = st.file_uploader(
        "Upload screenshots of your chats (optional)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="screenshots"
    )
    if uploaded_files:
        for file in uploaded_files:
            st.image(file, caption=file.name, use_container_width=True)

# --- New: Upload Audio Call Recording ---
st.subheader("🎙️ Upload Your Couple Call Recording")
audio_file = st.file_uploader(
    "Upload an audio recording of your call with your lover/ex (mp3, wav, m4a)",
    type=["mp3", "wav", "m4a"],
    key="audio_call"
)
if audio_file:
    st.audio(audio_file, format="audio/wav")
    st.info("Your audio will be analyzed for emotional tone, key moments, and recovery advice.")

# Process button and API key check
if st.button("Get Recovery Plan 💝", type="primary"):
    if not st.session_state.api_key_input:
        st.warning("Please enter your API key in the sidebar first!")
    else:
        therapist_agent, closure_agent, routine_planner_agent, brutal_honesty_agent = initialize_agents(st.session_state.api_key_input)
        
        if all([therapist_agent, closure_agent, routine_planner_agent, brutal_honesty_agent]):
            st.session_state["therapist_agent"] = therapist_agent
            st.session_state["closure_agent"] = closure_agent
            st.session_state["routine_planner_agent"] = routine_planner_agent
            st.session_state["brutal_honesty_agent"] = brutal_honesty_agent
            if user_input or uploaded_files or audio_file:
                try:
                    st.header("Your Personalized Recovery Plan")
                    
                    def process_images(files):
                        processed_images = []
                        for file in files:
                            try:
                                temp_dir = tempfile.gettempdir()
                                temp_path = os.path.join(temp_dir, f"temp_{file.name}")
                                
                                with open(temp_path, "wb") as f:
                                    f.write(file.getvalue())
                                
                                agno_image = AgnoImage(filepath=Path(temp_path))
                                processed_images.append(agno_image)
                                
                            except Exception as e:
                                logger.error(f"Error processing image {file.name}: {str(e)}")
                                continue
                        return processed_images
                    
                    all_images = process_images(uploaded_files) if uploaded_files else []
                    
                    # Therapist Analysis
                    with st.spinner("🤗 Getting empathetic support..."):
                        therapist_prompt = f"""
                        Analyze the emotional state and provide empathetic support based on:
                        User's message: {user_input}
                        
                        Please provide a compassionate response with:
                        1. Validation of feelings
                        2. Gentle words of comfort
                        3. Relatable experiences
                        4. Words of encouragement
                        """
                        
                        response = therapist_agent.run(
                            message=therapist_prompt,
                            images=all_images
                        )
                        
                        st.subheader("🤗 Emotional Support")
                        st.markdown(response.content)
                    
                    # Closure Messages
                    with st.spinner("✍️ Crafting closure messages..."):
                        closure_prompt = f"""
                        Help create emotional closure based on:
                        User's feelings: {user_input}
                        
                        Please provide:
                        1. Template for unsent messages
                        2. Emotional release exercises
                        3. Closure rituals
                        4. Moving forward strategies
                        """
                        
                        response = closure_agent.run(
                            message=closure_prompt,
                            images=all_images
                        )
                        
                        st.subheader("✍️ Finding Closure")
                        st.markdown(response.content)
                    
                    # Recovery Plan
                    with st.spinner("📅 Creating your recovery plan..."):
                        routine_prompt = f"""
                        Design a 7-day recovery plan based on:
                        Current state: {user_input}
                        
                        Include:
                        1. Daily activities and challenges
                        2. Self-care routines
                        3. Social media guidelines
                        4. Mood-lifting music suggestions
                        """
                        
                        response = routine_planner_agent.run(
                            message=routine_prompt,
                            images=all_images
                        )
                        
                        st.subheader("📅 Your Recovery Plan")
                        st.markdown(response.content)
                    
                    # Honest Feedback
                    with st.spinner("💪 Getting honest perspective..."):
                        honesty_prompt = f"""
                        Provide honest, constructive feedback about:
                        Situation: {user_input}
                        
                        Include:
                        1. Objective analysis
                        2. Growth opportunities
                        3. Future outlook
                        4. Actionable steps
                        """
                        
                        response = brutal_honesty_agent.run(
                            message=honesty_prompt,
                            images=all_images
                        )
                        
                        st.subheader("💪 Honest Perspective")
                        st.markdown(response.content)
                            
                    # --- New: Audio Transcription and Analysis ---
                    audio_transcript = ""
                    if audio_file:
                        with st.spinner("Transcribing your call..."):
                            # Placeholder: Replace with actual transcription logic
                            audio_bytes = audio_file.read()
                            # Example: Use a transcription API or library here
                            # audio_transcript = transcribe_audio(audio_bytes)
                            audio_transcript = "[Transcription of your call goes here...]"
                            st.markdown("**Transcript of your call:**")
                            st.code(audio_transcript)
                    
                    # --- Deep Analysis of Couple Call ---
                    if audio_transcript:
                        st.markdown("## 🔎 Deep Analysis of Your Couple Call")
                        st.info("Below, each AI agent will analyze your call and give you unique insights and advice based on the conversation.")

                        # Therapist Agent: Emotional Support
                        with st.spinner("🤗 Therapist analyzing your call..."):
                            therapist_call_prompt = f"""
                            Analyze this couple call transcript for emotional tone, emotional needs, and provide empathetic support.
                            Give:
                            1. Validation of feelings
                            2. Gentle words of comfort
                            3. Relatable experiences
                            4. Words of encouragement

                            Transcript:
                            {audio_transcript}
                            """
                            therapist_response = therapist_agent.run(message=therapist_call_prompt)
                            st.subheader("🤗 Therapist's Emotional Support")
                            st.markdown(therapist_response.content)

                        # Closure Agent: Closure & Letting Go
                        with st.spinner("✍️ Closure specialist analyzing your call..."):
                            closure_call_prompt = f"""
                            Based on this couple call transcript, help the user find closure.
                            Provide:
                            1. Template for unsent messages
                            2. Emotional release exercises
                            3. Closure rituals
                            4. Moving forward strategies

                            Transcript:
                            {audio_transcript}
                            """
                            closure_response = closure_agent.run(message=closure_call_prompt)
                            st.subheader("✍️ Closure & Letting Go")
                            st.markdown(closure_response.content)

                        # Routine Planner Agent: Recovery Plan
                        with st.spinner("📅 Routine planner analyzing your call..."):
                            routine_call_prompt = f"""
                            Based on this couple call transcript, design a 7-day recovery plan.
                            Include:
                            1. Daily activities and challenges
                            2. Self-care routines
                            3. Social media guidelines
                            4. Mood-lifting music suggestions

                            Transcript:
                            {audio_transcript}
                            """
                            routine_response = routine_planner_agent.run(message=routine_call_prompt)
                            st.subheader("📅 Recovery Plan Based on Your Call")
                            st.markdown(routine_response.content)

                        # Brutal Honesty Agent: Honest Feedback
                        with st.spinner("💪 Brutal honesty agent analyzing your call..."):
                            honesty_call_prompt = f"""
                            Give honest, constructive feedback about this couple call transcript.
                            Include:
                            1. Objective analysis
                            2. Growth opportunities
                            3. Future outlook
                            4. Actionable steps

                            Transcript:
                            {audio_transcript}
                            """
                            honesty_response = brutal_honesty_agent.run(message=honesty_call_prompt)
                            st.subheader("💪 Honest Perspective on Your Call")
                            st.markdown(honesty_response.content)

                        # --- Unique: Best Comeback/Empowering Response Generator ---
                        with st.expander("💬 Need a Powerful Comeback or Response? (Click to generate)"):
                            if "comeback_response" not in st.session_state:
                                st.session_state.comeback_response = ""
                            if st.button("Generate Best Response for Your Lover/Ex"):
                                comeback_prompt = f"""
                                Based on this couple call transcript, generate a short, empowering, and respectful response the user can give to their lover/ex in future conversations.
                                Make it supportive, confident, and focused on self-worth and growth.

                                Transcript:
                                {audio_transcript}
                                """
                                comeback_response = brutal_honesty_agent.run(message=comeback_prompt)
                                st.session_state.comeback_response = comeback_response.content
                            if st.session_state.comeback_response:
                                st.success("Here's your empowering response:")
                                st.markdown(f"> {st.session_state.comeback_response}")

                        # --- User Feedback on Advice ---
                        st.markdown("#### 🙋 How helpful was this analysis?")
                        if "call_analysis_feedback" not in st.session_state:
                            st.session_state.call_analysis_feedback = None
                        feedback = st.radio(
                            "Rate the advice you received:",
                            ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
                            key="call_analysis_feedback_radio"
                        )
                        if st.button("Submit Feedback", key="submit_call_feedback"):
                            st.session_state.call_analysis_feedback = feedback
                        if st.session_state.call_analysis_feedback:
                            st.success("Thank you for your feedback! 💖")

                except Exception as e:
                    logger.error(f"Error during analysis: {str(e)}")
                    st.error("An error occurred during analysis. Please check the logs for details.")
            else:
                st.warning("Please share your feelings, upload screenshots, or add a call recording to get help.")
        else:
            st.error("Failed to initialize agents. Please check your API key.")

# After successful agent initialization, save to session for journal AI reflection
if (
    "therapist_agent" in locals() and
    "closure_agent" in locals() and
    "routine_planner_agent" in locals() and
    "brutal_honesty_agent" in locals()
):
    if all([therapist_agent, closure_agent, routine_planner_agent, brutal_honesty_agent]):
        st.session_state["therapist_agent"] = therapist_agent

# --- New: Real-Time Voice Call with AI Agent (Vipe) ---
VIPE_API_KEY = "36428d52-ea15-4532-ba75-de2308b6b7e1"
VIPE_API_URL = "https://api.vipe.ai/v1/call/start"  # Replace with actual endpoint if different

def start_vipe_call():
    st.subheader("📞 Real-Time Voice Call with AI Agent (Vipe)")
    st.markdown("Start a real-time voice conversation with your AI agent using Vipe.")
    if st.button("Start Voice Call"):
        with st.spinner("Connecting to Vipe..."):
            try:
                # Example payload, adjust as per Vipe API docs
                payload = {
                    "api_key": VIPE_API_KEY,
                    "agent_name": "Breakup Recovery AI",
                    "user_id": "streamlit_user",  # You can use session info or user email if available
                }
                response = requests.post(VIPE_API_URL, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    call_url = data.get("call_url")
                    if call_url:
                        st.success("Your call is ready! Click below to join:")
                        st.markdown(f"[🔗 Join Voice Call]({call_url})", unsafe_allow_html=True)
                        st.info("Share this link with your lover if you want them to join the call.")
                    else:
                        st.error("Failed to get call link from Vipe.")
                else:
                    st.error(f"Vipe API error: {response.text}")
            except Exception as e:
                st.error(f"Error connecting to Vipe: {str(e)}")

start_vipe_call()

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Made with ❤️ by the Breakup Recovery Squad Multi Agent</p>
        <p>Share your recovery journey with #BreakupRecoverySquad</p>
    </div>
""", unsafe_allow_html=True)

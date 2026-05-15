"""
Riddle Game - Utility Functions
Contains helper functions for styling, animations, and UI components.
"""

import streamlit as st
import json

# Custom CSS for dark mode gaming UI
CUSTOM_CSS = """
<style>
    /* Main styling */
    body {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: #eaeaea;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    
    /* Riddle card styling */
    .riddle-card {
        background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
        border: 2px solid #e94560;
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(233, 69, 96, 0.2);
        transition: all 0.3s ease;
    }
    
    .riddle-card:hover {
        box-shadow: 0 12px 40px rgba(233, 69, 96, 0.4);
        transform: translateY(-5px);
    }
    
    /* Level indicator */
    .level-indicator {
        background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(233, 69, 96, 0.3);
    }
    
    /* Progress bar styling */
    .progress-container {
        margin: 20px 0;
    }
    
    .progress-bar {
        background: #0f3460;
        border-radius: 10px;
        height: 30px;
        overflow: hidden;
        border: 2px solid #e94560;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #e94560 0%, #ff6b6b 100%);
        height: 100%;
        border-radius: 8px;
        transition: width 0.5s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 12px;
    }
    
    /* Input styling */
    .stTextInput input {
        background-color: #0f3460 !important;
        border: 2px solid #e94560 !important;
        color: #eaeaea !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 16px !important;
    }
    
    .stTextInput input:focus {
        border: 2px solid #ff6b6b !important;
        box-shadow: 0 0 10px rgba(233, 69, 96, 0.5) !important;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 30px !important;
        font-weight: bold !important;
        font-size: 16px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(233, 69, 96, 0.3) !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(233, 69, 96, 0.4) !important;
    }
    
    /* Success message */
    .success-message {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #27ae60;
        margin: 20px 0;
        animation: slideIn 0.5s ease;
    }
    
    /* Error/Hint message */
    .hint-message {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #e67e22;
        margin: 20px 0;
    }
    
    /* Incorrect message */
    .incorrect-message {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #c0392b;
        margin: 20px 0;
    }
    
    /* Winner celebration */
    .winner-container {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        border: 3px solid #27ae60;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(46, 204, 113, 0.3);
        animation: pulse 1s infinite;
    }
    
    .winner-title {
        font-size: 48px;
        font-weight: bold;
        color: white;
        margin: 20px 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .winner-emoji {
        font-size: 72px;
        animation: bounce 1s infinite;
    }
    
    /* Animations */
    @keyframes slideIn {
        from {
            transform: translateX(-100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes bounce {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            box-shadow: 0 10px 40px rgba(46, 204, 113, 0.3);
        }
        50% {
            box-shadow: 0 10px 60px rgba(46, 204, 113, 0.6);
        }
    }
    
    @keyframes confetti {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(500px) rotate(360deg);
            opacity: 0;
        }
    }
    
    /* Score display */
    .score-display {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        padding: 15px 25px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 18px;
        text-align: center;
        margin: 20px 0;
    }
    
    /* Hint section */
    .hint-section {
        background: rgba(243, 156, 18, 0.1);
        border-left: 4px solid #f39c12;
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
    }
</style>
"""

def inject_custom_css():
    """Inject custom CSS into Streamlit app."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def get_confetti_animation():
    """Generate confetti animation JSON for Lottie."""
    return {
        "v": "5.6.10",
        "fr": 24,
        "ip": 0,
        "op": 120,
        "w": 600,
        "h": 600,
        "nm": "Confetti",
        "ddd": 0,
        "assets": [],
        "layers": [
            {
                "ddd": 0,
                "ind": 1,
                "ty": 4,
                "nm": "Confetti Layer",
                "sr": 1,
                "ks": {
                    "o": {"a": 0, "k": 100},
                    "r": {"a": 0, "k": 0},
                    "p": {"a": 0, "k": [300, 300, 0]},
                    "a": {"a": 0, "k": [0, 0, 0]},
                    "s": {"a": 0, "k": [100, 100, 100]}
                },
                "ao": 0,
                "shapes": []
            }
        ]
    }

def display_level_indicator(current_level, total_levels):
    """
    Display level indicator with progress.
    
    Args:
        current_level (int): Current level number
        total_levels (int): Total number of levels
    """
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            f"""
            <div class="level-indicator">
                🎮 LEVEL {current_level} / {total_levels}
            </div>
            """,
            unsafe_allow_html=True
        )

def display_progress_bar(current_level, total_levels):
    """
    Display progress bar.
    
    Args:
        current_level (int): Current level (1-10)
        total_levels (int): Total levels
    """
    progress = (current_level - 1) / total_levels * 100
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown(
            f"""
            <div class="progress-container">
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {progress}%">
                        {current_level - 1}/{total_levels}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

def display_riddle_card(riddle_text, difficulty):
    """
    Display riddle in a styled card.
    
    Args:
        riddle_text (str): The riddle question
        difficulty (str): Difficulty level
    """
    st.markdown(
        f"""
        <div class="riddle-card">
            <h2 style="color: #eaeaea; margin-top: 0;">🧩 Riddle</h2>
            <h3 style="color: #ff6b6b; font-size: 24px; line-height: 1.6;">
                {riddle_text}
            </h3>
            <p style="color: #b0b0b0; font-size: 14px; margin-top: 15px;">
                Difficulty: <span style="color: #f39c12; font-weight: bold;">{difficulty}</span>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def display_success_message(message="Correct! 🎉"):
    """Display success message with animation."""
    st.markdown(
        f"""
        <div class="success-message">
            <h3 style="margin: 0; color: white;">✅ {message}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()

def display_hint_message(hint):
    """Display hint message."""
    st.markdown(
        f"""
        <div class="hint-message">
            <h4 style="margin-top: 0; color: white;">💡 Hint:</h4>
            <p style="margin-bottom: 0; color: white; font-size: 16px;">{hint}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def display_incorrect_message():
    """Display incorrect answer message."""
    st.markdown(
        f"""
        <div class="incorrect-message">
            <h3 style="margin: 0; color: white;">❌ Incorrect Answer</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

def display_score(score, total):
    """
    Display current score.
    
    Args:
        score (int): Current score
        total (int): Total possible score
    """
    st.markdown(
        f"""
        <div class="score-display">
            ⭐ Score: {score} / {total}
        </div>
        """,
        unsafe_allow_html=True
    )

def display_winner_screen(total_levels, score):
    """
    Display winner celebration screen.
    
    Args:
        total_levels (int): Total levels completed
        score (int): Final score
    """
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            f"""
            <div class="winner-container">
                <div class="winner-emoji" style="animation: bounce 1s infinite;">🎉</div>
                <div class="winner-title">CONGRATULATIONS!</div>
                <h2 style="color: white; margin: 20px 0;">You are the Winner! 🏆</h2>
                <h3 style="color: white; margin: 20px 0;">Levels Completed: {total_levels}</h3>
                <h3 style="color: white; margin: 20px 0;">Final Score: {score}/{total_levels} 🌟</h3>
                <p style="color: white; font-size: 18px; margin-top: 30px;">
                    Amazing performance! You've mastered all {total_levels} riddles! 
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.balloons()

def get_difficulty_color(difficulty):
    """
    Get color for difficulty level.
    
    Args:
        difficulty (str): Difficulty level
    
    Returns:
        str: Hex color code
    """
    colors = {
        "Easy": "#2ecc71",
        "Medium": "#f39c12",
        "Hard": "#e74c3c"
    }
    return colors.get(difficulty, "#eaeaea")

def initialize_session_state():
    """Initialize session state variables."""
    if "current_level" not in st.session_state:
        st.session_state.current_level = 1
    
    if "score" not in st.session_state:
        st.session_state.score = 0
    
    if "hint_shown" not in st.session_state:
        st.session_state.hint_shown = False
    
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    
    if "game_won" not in st.session_state:
        st.session_state.game_won = False
    
    if "user_answer" not in st.session_state:
        st.session_state.user_answer = ""

def reset_game():
    """Reset game to initial state."""
    st.session_state.current_level = 1
    st.session_state.score = 0
    st.session_state.hint_shown = False
    st.session_state.attempts = 0
    st.session_state.game_won = False
    st.session_state.user_answer = ""

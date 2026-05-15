"""
Riddle Game - Main Application
A modern, interactive riddle-based game built with Streamlit.

Author: Your Name
Date: 2024
Version: 1.0.0
"""

import streamlit as st
import os
from dotenv import load_dotenv
from riddles import get_riddle, check_answer, get_total_levels, get_difficulty
from utils import (
    inject_custom_css, initialize_session_state, reset_game,
    display_level_indicator, display_progress_bar, display_riddle_card,
    display_success_message, display_hint_message, display_incorrect_message,
    display_score, display_winner_screen
)

# Load environment variables
load_dotenv()

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="🎮 Riddle Game",
    page_icon="🧩",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ============================================================================
# SESSION STATE & INITIALIZATION
# ============================================================================

initialize_session_state()
inject_custom_css()

# ============================================================================
# SECURITY FUNCTIONS
# ============================================================================

def get_api_key():
    """
    Safely retrieve API key from environment or Streamlit secrets.
    
    Returns:
        str: API key or None if not configured
    """
    # Try Streamlit secrets first (preferred for deployment)
    try:
        if hasattr(st, 'secrets') and 'api_key' in st.secrets:
            return st.secrets['api_key']
    except Exception:
        pass
    
    # Fall back to .env file (local development)
    api_key = os.getenv('API_KEY')
    return api_key if api_key else None

def validate_security():
    """
    Validate security and prevent abuse.
    
    Returns:
        bool: True if security checks pass
    """
    # You can add security checks here
    # For example: rate limiting, input validation, etc.
    return True

# ============================================================================
# MAIN GAME LOGIC
# ============================================================================

def main():
    """Main application logic."""
    
    # Header
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            "<h1 style='text-align: center; color: #e94560; margin-bottom: 30px;'>🧩 RIDDLE GAME 🧩</h1>",
            unsafe_allow_html=True
        )
    
    # Check if game is won
    if st.session_state.game_won:
        display_winner_screen(get_total_levels(), st.session_state.score)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🔄 Play Again", key="play_again_btn", use_container_width=True):
                reset_game()
                st.rerun()
        return
    
    # Display level indicator and progress bar
    display_level_indicator(st.session_state.current_level, get_total_levels())
    display_progress_bar(st.session_state.current_level, get_total_levels())
    display_score(st.session_state.score, get_total_levels())
    
    # Get current riddle
    current_riddle = get_riddle(st.session_state.current_level)
    
    if current_riddle:
        # Display riddle
        display_riddle_card(
            current_riddle["question"],
            get_difficulty(st.session_state.current_level)
        )
        
        # Input section
        st.markdown("<h3 style='color: #eaeaea; margin-top: 30px;'>Your Answer:</h3>", unsafe_allow_html=True)
        user_input = st.text_input(
            label="Enter your answer",
            key=f"answer_input_{st.session_state.current_level}",
            placeholder="Type your answer here...",
            label_visibility="collapsed"
        )
        
        # Button layout
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            hint_btn = st.button("💡 Get Hint", key="hint_btn", use_container_width=True)
        
        with col2:
            submit_btn = st.button("✅ Submit Answer", key="submit_btn", use_container_width=True)
        
        with col3:
            restart_btn = st.button("🔄 Restart Game", key="restart_btn", use_container_width=True)
        
        # Handle restart button
        if restart_btn:
            reset_game()
            st.rerun()
        
        # Handle hint button
        if hint_btn:
            st.session_state.hint_shown = True
        
        # Display hint if requested
        if st.session_state.hint_shown:
            display_hint_message(current_riddle["hint"])
            st.markdown(
                "<p style='text-align: center; color: #b0b0b0; margin-top: 20px; font-size: 14px;'>"
                "💪 Don't give up! You can solve this riddle.</p>",
                unsafe_allow_html=True
            )
        
        # Handle submit button
        if submit_btn:
            if user_input.strip() == "":
                st.warning("⚠️ Please enter an answer before submitting!")
            else:
                st.session_state.attempts += 1
                
                # Check if answer is correct
                if check_answer(user_input, current_riddle["answer"]):
                    # Correct answer
                    display_success_message(
                        f"Correct! Moving to Level {st.session_state.current_level + 1}..."
                    )
                    
                    # Update score and level
                    st.session_state.score += 1
                    
                    # Check if this was the last level
                    if st.session_state.current_level == get_total_levels():
                        st.session_state.game_won = True
                    else:
                        st.session_state.current_level += 1
                        st.session_state.hint_shown = False
                    
                    # Rerun to show next level
                    import time
                    time.sleep(2)
                    st.rerun()
                
                else:
                    # Incorrect answer
                    display_incorrect_message()
                    st.markdown(
                        "<p style='color: #eaeaea; font-size: 16px; text-align: center; margin-top: 15px;'>"
                        "Try again! You can do this. 💪</p>",
                        unsafe_allow_html=True
                    )
        
        # Display helpful tips
        st.markdown("<hr style='border-color: #0f3460; margin: 40px 0;'>", unsafe_allow_html=True)
        
        with st.expander("📚 How to Play"):
            st.markdown("""
            - **Read** the riddle carefully.
            - **Think** about what the answer could be.
            - **Use** the hint if you get stuck.
            - **Submit** your answer when ready.
            - **Progress** through all 10 levels to win!
            
            **Tips:**
            - Answers are case-insensitive.
            - Extra spaces are ignored.
            - Think creatively and outside the box!
            """)
    
    else:
        st.error("Error loading riddle. Please restart the game.")

# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == "__main__":
    # Validate security
    if not validate_security():
        st.error("Security validation failed. Please refresh the page.")
        st.stop()
    
    # Run main application
    main()
    
    # Footer
    st.markdown("<hr style='border-color: #0f3460; margin-top: 50px;'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            "<p style='text-align: center; color: #999; font-size: 12px;'>"
            "🎮 Riddle Game v1.0 | Made with ❤️ using Streamlit</p>",
            unsafe_allow_html=True
        )

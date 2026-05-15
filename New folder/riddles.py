"""
Riddle Game - Riddle Database
Contains all 10 riddles with varying difficulty levels.
"""

RIDDLES = [
    {
        "level": 1,
        "question": "I have a face and two hands, but no arms or legs. What am I?",
        "answer": "clock",
        "hint": "Think about something you find on a wall in your home.",
        "difficulty": "Easy"
    },
    {
        "level": 2,
        "question": "What has keys but no locks, space but no room, and you can enter but can't go inside?",
        "answer": "keyboard",
        "hint": "Think about computer equipment.",
        "difficulty": "Easy"
    },
    {
        "level": 3,
        "question": "The more you take, the more you leave behind. What am I?",
        "answer": "footsteps",
        "hint": "Think about walking on a beach.",
        "difficulty": "Easy"
    },
    {
        "level": 4,
        "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "answer": "echo",
        "hint": "You hear this in mountains or canyons.",
        "difficulty": "Medium"
    },
    {
        "level": 5,
        "question": "What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?",
        "answer": "river",
        "hint": "Think about nature and water bodies.",
        "difficulty": "Medium"
    },
    {
        "level": 6,
        "question": "What gets wet while drying?",
        "answer": "towel",
        "hint": "You use this after a shower.",
        "difficulty": "Medium"
    },
    {
        "level": 7,
        "question": "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
        "answer": "fire",
        "hint": "Think about elements and combustion.",
        "difficulty": "Medium"
    },
    {
        "level": 8,
        "question": "What has a head and a tail but no body?",
        "answer": "coin",
        "hint": "You flip this to make decisions.",
        "difficulty": "Hard"
    },
    {
        "level": 9,
        "question": "The more of this there is, the less you see. What is it?",
        "answer": "darkness",
        "hint": "Think about light and vision.",
        "difficulty": "Hard"
    },
    {
        "level": 10,
        "question": "What occurs once in a minute, twice in a moment, and never in one hundred years?",
        "answer": "the letter m",
        "hint": "Look at the words carefully - it's about letters, not events.",
        "difficulty": "Hard"
    }
]

def get_riddle(level):
    """
    Get a riddle by level number.
    
    Args:
        level (int): Level number (1-10)
    
    Returns:
        dict: Riddle data or None if level doesn't exist
    """
    for riddle in RIDDLES:
        if riddle["level"] == level:
            return riddle
    return None

def check_answer(user_answer, correct_answer):
    """
    Check if the user's answer is correct (case-insensitive, strips whitespace).
    
    Args:
        user_answer (str): User's submitted answer
        correct_answer (str): Correct answer from riddle
    
    Returns:
        bool: True if answers match, False otherwise
    """
    return user_answer.strip().lower() == correct_answer.strip().lower()

def get_difficulty(level):
    """
    Get difficulty level for a given level number.
    
    Args:
        level (int): Level number
    
    Returns:
        str: Difficulty level (Easy, Medium, Hard)
    """
    if level <= 3:
        return "Easy"
    elif level <= 7:
        return "Medium"
    else:
        return "Hard"

def get_total_levels():
    """Get total number of riddle levels."""
    return len(RIDDLES)

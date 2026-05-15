# 🎮 Riddle Game

A modern, interactive riddle-based game built with **Python** and **Streamlit**. Test your problem-solving skills across 10 increasingly challenging levels!

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Locally](#running-locally)
- [Gameplay](#gameplay)
- [Deployment Guide](#deployment-guide)
- [Security Best Practices](#security-best-practices)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

---

## ✨ Features

### 🎯 Gameplay
- **10 Unique Levels** with progressive difficulty
- **3 Difficulty Tiers**: Easy (Levels 1-3), Medium (Levels 4-7), Hard (Levels 8-10)
- **Smart Hint System**: Get helpful hints without losing progress
- **Unlimited Attempts**: Try as many times as needed
- **Real-time Score Tracking**: Monitor your progress

### 🎨 Modern UI/UX
- **Dark Mode Gaming Interface** with vibrant colors
- **Progress Bar** showing level completion
- **Smooth Animations** and visual feedback
- **Interactive Riddle Cards** with difficulty indicators
- **Responsive Design** that works on all devices
- **Success/Error Messages** with engaging animations
- **Victory Screen** with celebration effects

### 🛡️ Security
- **Secure API Key Management** via `.env` file or Streamlit Secrets
- **Input Validation** to prevent injection attacks
- **Case-Insensitive Answers** for better UX
- **Modular Architecture** for maintainability

### 📦 Developer-Friendly
- **Modular Code Structure** with separate files
- **Clean Code** with comprehensive comments
- **Reusable Functions** for easy customization
- **Environment Variable Management**
- **Error Handling** throughout the application

---

## 📁 Project Structure

```
riddlegameproj/
│
├── app.py                    # Main Streamlit application
├── riddles.py               # Riddle database & logic
├── utils.py                 # UI components & utilities
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .env                     # (Create this) Environment variables
├── README.md               # This file
└── assets/                 # (Optional) Images, sounds, etc.
```

### File Descriptions

#### 📄 `app.py`
Main application file containing:
- Page configuration
- Session state management
- Game logic and flow control
- Security validation
- Main UI rendering

#### 🧩 `riddles.py`
Riddle database with:
- All 10 riddle questions
- Correct answers
- Helpful hints
- Difficulty classifications
- Answer checking functions

#### 🎨 `utils.py`
Utility functions including:
- Custom CSS styling
- UI component rendering
- Session state initialization
- Game state management
- Animation handling

#### 📦 `requirements.txt`
Python package dependencies:
- `streamlit`: Web framework
- `python-dotenv`: Environment variable management
- `streamlit-lottie`: Animation support

---

## 🚀 Installation

### Prerequisites
- **Python 3.8+** installed
- **pip** package manager
- **Git** (optional, for cloning)

### Step 1: Clone or Download Project

```bash
# Option 1: Clone the repository
git clone <repository-url>
cd riddlegameproj

# Option 2: Download as ZIP and extract
# Then navigate to the folder in terminal
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installation:
```bash
pip list
```

---

## ⚙️ Configuration

### Setting Up Environment Variables

#### Option 1: Using `.env` File (Local Development)

1. **Create `.env` file** in the project root:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env`** and add your configuration:
   ```
   API_KEY=your_actual_api_key_here
   STREAMLIT_LOGGER_LEVEL=warning
   ```

3. The application automatically loads these variables from `.env`

#### Option 2: Using Streamlit Secrets (Cloud Deployment)

1. **In Streamlit Cloud**, navigate to App Settings
2. **Go to "Secrets"** section
3. **Add your secrets** in the format:
   ```
   api_key = "your_actual_api_key_here"
   ```

4. The `app.py` automatically checks Streamlit secrets first

### API Key Management

- **⚠️ Never** commit `.env` file to version control
- **Always** use `.gitignore` to exclude `.env`:
  ```
  echo ".env" >> .gitignore
  ```
- **Never** hardcode API keys in source code
- **Use** environment variables or Streamlit Secrets

---

## 🎮 Running Locally

### Start the Application

```bash
# Activate virtual environment first (if using one)
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Run the app
streamlit run app.py
```

### Expected Output

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### Access the Game

- **Open** http://localhost:8501 in your web browser
- **Start** playing immediately
- **Press** `Ctrl+C` in terminal to stop the server

---

## 🎯 Gameplay

### Game Flow

1. **Level 1** displays the first riddle
2. **Read** the riddle carefully
3. **Type** your answer in the input field
4. **Click** "Get Hint" if you need help (optional)
5. **Click** "Submit Answer" to check your response
6. **Correct**: Progress to the next level ✅
7. **Incorrect**: Try again up to 10 times 🔄
8. **Level 10**: Complete all riddles to win! 🏆

### Features

- **Hints**: Get helpful clues without losing progress
- **Progress Bar**: Visual indicator of completion (0-100%)
- **Score Tracking**: Points awarded for each correct answer
- **Difficulty**: Clear indication of riddle difficulty
- **Attempt Counter**: See how many tries you've made
- **Restart Button**: Start a new game anytime

### Tips for Players

- ✨ Think creatively and outside the box
- 💡 Use hints strategically
- ⏰ Take your time—no time limits
- 🧠 Riddles often have wordplay and double meanings
- 🎯 Focus on key words in the question

---

## 📤 Deployment Guide

### Option 1: Deploy to Streamlit Cloud (Recommended)

#### Prerequisites
- GitHub account
- Streamlit Cloud account (free)
- Push code to GitHub

#### Steps

1. **Push Code to GitHub**
   ```bash
   git remote add origin <your-repo-url>
   git add .
   git commit -m "Initial commit: Riddle Game"
   git push -u origin main
   ```

2. **Go to** [Streamlit Cloud](https://streamlit.io/cloud)

3. **Click** "New App"

4. **Select**:
   - Your GitHub repository
   - Main branch
   - `app.py` as the main file

5. **Click** "Deploy"

6. **Configure Secrets**:
   - Go to App Settings → Secrets
   - Paste your secrets in TOML format:
     ```
     api_key = "your_api_key_here"
     ```

7. **Save** and your app is live! 🎉

#### Public URL
Your app will be available at:
```
https://riddle-game-<username>.streamlit.app
```

---

### Option 2: Deploy to Heroku

#### Prerequisites
- Heroku account (free)
- Heroku CLI installed

#### Steps

1. **Create Heroku App**
   ```bash
   heroku create your-riddle-game
   ```

2. **Add Buildpack**
   ```bash
   heroku buildpacks:add heroku/python
   ```

3. **Create Procfile**
   ```bash
   echo "web: streamlit run app.py" > Procfile
   ```

4. **Create `runtime.txt`**
   ```bash
   echo "python-3.11.0" > runtime.txt
   ```

5. **Set Secrets**
   ```bash
   heroku config:set API_KEY=your_api_key_here
   ```

6. **Deploy**
   ```bash
   git push heroku main
   ```

7. **View Logs**
   ```bash
   heroku logs --tail
   ```

---

### Option 3: Deploy to AWS

#### Using AWS App Runner

1. **Push code to GitHub**
2. **Connect GitHub** to AWS App Runner
3. **Configure environment variables** in App Runner console
4. **Deploy** and get your public URL

[AWS App Runner Docs](https://docs.aws.amazon.com/apprunner/)

---

### Option 4: Deploy with Docker

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py"]
   ```

2. **Build Image**
   ```bash
   docker build -t riddle-game .
   ```

3. **Run Container**
   ```bash
   docker run -p 8501:8501 riddle-game
   ```

4. **Push to Registry** (Docker Hub, ECR, etc.)
   ```bash
   docker tag riddle-game:latest username/riddle-game:latest
   docker push username/riddle-game:latest
   ```

---

## 🛡️ Security Best Practices

### API Key Security

✅ **DO:**
- Store keys in `.env` file (local)
- Use Streamlit Secrets (production)
- Rotate keys regularly
- Use separate keys for each environment

❌ **DON'T:**
- Commit `.env` to version control
- Hardcode keys in source code
- Log or print API keys
- Share keys publicly

### Input Validation

The app includes:
- Case-insensitive answer checking
- Whitespace trimming
- Empty input validation
- Injection attempt prevention

### Additional Security Measures

1. **Environment Variables**: Separate config from code
2. **Error Handling**: Catch exceptions gracefully
3. **Logging**: Log errors securely without exposing keys
4. **Rate Limiting**: Can be added via Streamlit middleware

---

## 🐛 Troubleshooting

### Common Issues

#### 1. "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
pip install -r requirements.txt
```

#### 2. "Port 8501 is already in use"

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

#### 3. ".env file not found"

**Solution:**
```bash
# The app still works without .env—just won't have API_KEY
# To add it:
cp .env.example .env
# Edit .env with your values
```

#### 4. "App stuck showing 'Running...'"

**Solution:**
- Refresh browser (Ctrl+Shift+R)
- Restart Streamlit: Press `Ctrl+C` and run again
- Clear browser cache

#### 5. "API key not working in production"

**Solution:**
- Check if `.env` is in `.gitignore`
- Use **Streamlit Secrets** instead of `.env`
- Verify API_KEY in Streamlit Cloud dashboard
- Check API key format and expiration

#### 6. "Game state resets unexpectedly"

**Solution:**
- Ensure session_state is initialized
- Check for page reruns
- Clear browser cache/cookies

---

## 🔧 Customization

### Adding More Riddles

Edit `riddles.py`:
```python
{
    "level": 11,
    "question": "Your riddle here?",
    "answer": "answer",
    "hint": "Your hint here.",
    "difficulty": "Hard"
}
```

### Changing Colors

Edit `utils.py` and modify the CSS:
```css
.riddle-card {
    background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
    border: 2px solid #YOUR_BORDER_COLOR;
}
```

### Adding Animations

Streamlit includes built-in animations:
```python
st.balloons()  # Balloons
st.snow()      # Snow
st.success()   # Success message
st.error()     # Error message
```

---

## 📊 Performance Tips

1. **Optimize Images**: Compress if adding custom assets
2. **Cache Data**: Use `@st.cache_data` for static content
3. **Minimize Reloads**: Structure logic to avoid unnecessary reruns
4. **Clean CSS**: Keep styles optimized

---

## 📝 License

This project is provided as-is for educational and personal use.

---

## 🤝 Contributing

To improve this game:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 💬 Support

### Getting Help

- **Local Issues**: Check Troubleshooting section
- **Streamlit Docs**: https://docs.streamlit.io
- **Stack Overflow**: Tag questions with `streamlit`
- **Community Forum**: https://discuss.streamlit.io

---

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Python Official Docs](https://docs.python.org/3/)
- [Git & GitHub Guide](https://guides.github.com)
- [Environment Variables](https://en.wikipedia.org/wiki/Environment_variable)

---

## 📈 Roadmap

Future enhancements:
- [ ] Leaderboard system
- [ ] Multiplayer mode
- [ ] Custom difficulty settings
- [ ] User authentication
- [ ] Database integration
- [ ] Sound effects
- [ ] Mobile app version
- [ ] Admin dashboard

---

## 🎉 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- Inspired by classic riddle games
- Community feedback and suggestions

---

## 📧 Contact

For questions or suggestions, feel free to reach out!

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Active ✅

---

**Happy Riddling! 🧩🎮**

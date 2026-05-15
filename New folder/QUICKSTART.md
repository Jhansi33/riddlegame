# 🎮 Quick Start Guide

Get the Riddle Game running in 5 minutes!

## ⚡ Super Quick Start

### 1️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the App

```bash
streamlit run app.py
```

### 3️⃣ Play!

- Opens automatically at http://localhost:8501
- Start playing immediately
- No configuration needed!

---

## 🔑 Adding an API Key (Optional)

### Method 1: Using `.env` File (Local)

```bash
# Copy the template
cp .env.example .env

# Edit .env and add your key
# API_KEY=your_key_here
```

### Method 2: Using Streamlit Secrets (Production)

1. In Streamlit Cloud dashboard
2. Go to **Settings** → **Secrets**
3. Paste:
   ```
   api_key = "your_key_here"
   ```
4. Save and redeploy

---

## 🎯 First Game Steps

1. **Read** the riddle carefully
2. **Type** your answer
3. **Click** "Submit Answer"
4. **Get Hint** if stuck (optional)
5. **Submit** again to try
6. **Progress** to next level when correct
7. **Win** by completing all 10 levels!

---

## 🚀 Deploy in Minutes

### Streamlit Cloud (Free & Easy)

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Click "New App"
4. Select your repo and `app.py`
5. Deploy!

**URL**: `https://riddle-game-<username>.streamlit.app`

---

## 📚 More Help

- Full README: See `README.md`
- Deployment: See `DEPLOYMENT_GUIDE.md`
- Issues? Check the README Troubleshooting section

---

## ✅ What's Included

- ✅ 10 unique riddles (Easy → Hard)
- ✅ Beautiful dark UI with animations
- ✅ Progress tracking & scoring
- ✅ Hint system
- ✅ Victory celebration screen
- ✅ Secure API key management
- ✅ Mobile responsive
- ✅ Production-ready code

---

## 🎉 You're Ready!

Start playing now:

```bash
streamlit run app.py
```

**Enjoy the game! 🧩**

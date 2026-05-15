# 📦 Installation & Setup Guide

Complete step-by-step guide for setting up the Riddle Game on any system.

## Table of Contents

- [System Requirements](#system-requirements)
- [Installation Methods](#installation-methods)
- [Detailed Setup](#detailed-setup)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## 🖥️ System Requirements

### Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 7+, macOS 10.9+, Linux (any) |
| **Python** | 3.8 or higher |
| **RAM** | 2 GB |
| **Disk Space** | 500 MB |
| **Internet** | Required for deployment |

### Recommended

| Component | Recommendation |
|-----------|------------------|
| **Python** | 3.10 or higher |
| **RAM** | 4 GB+ |
| **Disk Space** | 1 GB+ |
| **Browser** | Chrome, Firefox, Safari, Edge (latest) |

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

Should show version 3.8+. If not, download from https://www.python.org

---

## 💾 Installation Methods

### Method 1: Standard Installation (Recommended)

**Prerequisites:**
- Python 3.8+
- pip (usually comes with Python)
- Terminal/Command Prompt

**Time:** ~5 minutes

#### Step 1: Download Project

**Option A: Using Git**
```bash
git clone https://github.com/YOUR_USERNAME/riddle-game.git
cd riddle-game
```

**Option B: Download ZIP**
1. Go to GitHub repository
2. Click **Code** → **Download ZIP**
3. Extract ZIP file
4. Open terminal in extracted folder

#### Step 2: Create Virtual Environment

**Why?** Isolates project dependencies from system Python.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, your terminal should show:
```
(venv) $ 
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Wait for installation to complete. You should see:
```
Successfully installed streamlit-... python-dotenv-... streamlit-lottie-...
```

#### Step 4: Create Environment File

```bash
cp .env.example .env
```

Or manually create `.env`:
```
API_KEY=your_api_key_here
STREAMLIT_LOGGER_LEVEL=warning
```

#### Step 5: Run the App

```bash
streamlit run app.py
```

**Expected Output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501

  For better performance, install the Watchdog module:
  $ pip install watchdog
```

#### Step 6: Play!

Open http://localhost:8501 in your browser and start playing!

---

### Method 2: Docker Installation

**Prerequisites:**
- Docker installed
- ~5 minutes

#### Step 1: Build Docker Image

```bash
docker build -t riddle-game:latest .
```

#### Step 2: Run Container

```bash
docker run -p 8501:8501 \
  -e API_KEY=your_api_key_here \
  riddle-game:latest
```

#### Step 3: Access App

Open http://localhost:8501

---

### Method 3: Using Anaconda

**For Anaconda/Miniconda users:**

```bash
# Create conda environment
conda create -n riddle-game python=3.11

# Activate environment
conda activate riddle-game

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 🔧 Detailed Setup

### Detailed Step-by-Step (Windows)

#### 1. Verify Python Installation

**Open Command Prompt:**
```
Windows Key → Type "cmd" → Press Enter
```

**Check Python:**
```cmd
python --version
```

**If "python is not recognized":**
1. Download Python from https://www.python.org
2. Run installer
3. **IMPORTANT**: Check "Add Python to PATH"
4. Click "Install Now"
5. Restart Command Prompt, try again

#### 2. Navigate to Project Folder

```cmd
# Navigate to your project
cd C:\Users\YourName\OneDrive\Desktop\riddlegameproj

# Verify files
dir
# Should show: app.py, riddles.py, utils.py, requirements.txt, etc.
```

#### 3. Create Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate
```

**Verify activation** (should show `(venv)` at start of prompt):
```
(venv) C:\...\riddlegameproj>
```

#### 4. Upgrade pip (Optional but Recommended)

```cmd
python -m pip install --upgrade pip
```

#### 5. Install Dependencies

```cmd
pip install -r requirements.txt
```

**Expected output:**
```
Collecting streamlit==1.28.1
  Downloading streamlit-1.28.1-py2.py3-none-any.whl
  ...
Successfully installed streamlit-1.28.1 python-dotenv-1.0.0 streamlit-lottie-0.0.5
```

#### 6. Create .env File

**Using Notepad:**
1. Right-click empty space in folder
2. New → Text Document
3. Name it `.env`
4. Edit with Notepad
5. Paste:
```
API_KEY=your_api_key_here
STREAMLIT_LOGGER_LEVEL=warning
```
6. Save

#### 7. Run Application

```cmd
streamlit run app.py
```

#### 8. Access App

Browser opens automatically to http://localhost:8501

---

### Detailed Step-by-Step (macOS)

#### 1. Verify Python Installation

**Open Terminal:**
```
Cmd + Space → Type "terminal" → Press Enter
```

**Check Python:**
```bash
python3 --version
```

**If not installed:**
```bash
# Using Homebrew
brew install python3

# Or download from https://www.python.org
```

#### 2. Navigate to Project

```bash
cd ~/Desktop/riddlegameproj
ls  # List files to verify
```

#### 3. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Verify:
```bash
(venv) $  # Should show at start of prompt
```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 5. Create .env File

```bash
cp .env.example .env

# Edit .env
nano .env
# Or use your preferred editor
```

#### 6. Run Application

```bash
streamlit run app.py
```

#### 7. Access App

Browser opens automatically to http://localhost:8501

---

### Detailed Step-by-Step (Linux)

#### 1. Verify Python

```bash
python3 --version
```

#### 2. Install pip (if needed)

```bash
sudo apt-get update
sudo apt-get install python3-pip
```

#### 3. Navigate to Project

```bash
cd ~/riddlegameproj
```

#### 4. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 6. Create .env File

```bash
cp .env.example .env
nano .env  # Edit as needed
```

#### 7. Run Application

```bash
streamlit run app.py
```

#### 8. Access App

Open http://localhost:8501 in browser

---

## ✅ Verification

### Verify Installation

Create a test script `verify.py`:

```python
import sys
print(f"Python: {sys.version}")

try:
    import streamlit
    print(f"✓ Streamlit {streamlit.__version__}")
except ImportError:
    print("✗ Streamlit not installed")

try:
    import dotenv
    print(f"✓ python-dotenv installed")
except ImportError:
    print("✗ python-dotenv not installed")

try:
    import streamlit_lottie
    print(f"✓ streamlit-lottie installed")
except ImportError:
    print("✗ streamlit-lottie not installed")

print("\nAll dependencies installed! Ready to play! 🎮")
```

Run it:
```bash
python verify.py
```

Expected output:
```
Python: 3....
✓ Streamlit 1.28.1
✓ python-dotenv installed
✓ streamlit-lottie installed

All dependencies installed! Ready to play! 🎮
```

---

## 🐛 Troubleshooting

### Issue: "Python is not recognized"

**Windows:**
1. Reinstall Python from https://www.python.org
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Restart computer
4. Try again: `python --version`

**macOS/Linux:**
```bash
which python3
# Should show path like /usr/bin/python3
```

### Issue: "Permission denied" when running commands

**Solution:**
```bash
# Windows: Open Command Prompt as Administrator
# 1. Press Windows Key
# 2. Type "cmd"
# 3. Right-click → "Run as administrator"

# macOS/Linux: Use sudo (may be needed for installation)
sudo pip install -r requirements.txt
```

### Issue: "No module named streamlit"

```bash
# Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Reinstall
pip install -r requirements.txt
```

### Issue: "Port 8501 is already in use"

```bash
# Use different port
streamlit run app.py --server.port 8502

# Or kill process using port 8501:
# Windows:
netstat -ano | findstr :8501
taskkill /PID <numbers> /F

# macOS/Linux:
lsof -i :8501
kill -9 <PID>
```

### Issue: ".env file not found" error

**Solution:**
```bash
# Create .env file manually
cp .env.example .env

# Verify it's created
ls -la .env

# Add your API key
```

App works fine without .env—this is optional.

### Issue: "requirements.txt not found"

**Solution:**
Verify you're in correct folder:
```bash
ls  # Should show: app.py, requirements.txt, riddles.py, etc.

# If not in right folder:
cd /path/to/riddlegameproj
```

### Issue: Virtual environment won't activate

**Windows:**
```bash
# PowerShell issue? Try Command Prompt instead
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
# Try different shell
source venv/bin/activate.csh  # For csh
# or just try again with bash
```

### Issue: "ModuleNotFoundError" when running app

```bash
# Verify virtual environment is activated
# Should see (venv) at start of prompt

# If not:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Then reinstall:
pip install -r requirements.txt
```

---

## 📞 Getting Help

If installation fails:

1. **Check Python version**: `python --version` (should be 3.8+)
2. **Verify pip**: `pip --version`
3. **Check internet connection**: Required for downloading packages
4. **Try troubleshooting above**
5. **Check the README.md** Troubleshooting section
6. **Check Streamlit docs**: https://docs.streamlit.io

---

## ✨ Success Indicators

Installation is successful when:

✅ `pip install -r requirements.txt` completes without errors  
✅ `streamlit run app.py` starts without errors  
✅ Browser opens to http://localhost:8501  
✅ Game loads and displays first riddle  
✅ You can submit answers and progress through levels  

---

## 🎉 You're All Set!

Congratulations! Your Riddle Game is installed and ready to play.

**Quick commands to remember:**

```bash
# Activate virtual environment
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Start the game
streamlit run app.py

# Deactivate virtual environment (when done)
deactivate
```

**Enjoy the game! 🧩🎮**

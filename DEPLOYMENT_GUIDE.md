# 🚀 Complete Deployment Guide for Riddle Game

This guide covers deploying the Riddle Game to various platforms with step-by-step instructions.

## Table of Contents

1. [Streamlit Cloud (Recommended)](#streamlit-cloud-recommended)
2. [Heroku](#heroku)
3. [AWS](#aws)
4. [Google Cloud](#google-cloud)
5. [DigitalOcean](#digitalocean)
6. [Docker](#docker-deployment)
7. [Troubleshooting](#troubleshooting)
8. [Post-Deployment](#post-deployment)

---

## 🌟 Streamlit Cloud (Recommended)

**Why Streamlit Cloud?**
- ✅ Easiest setup (5 minutes)
- ✅ Free tier available
- ✅ Built for Streamlit apps
- ✅ Automatic deployments from GitHub
- ✅ Built-in secrets management
- ✅ No server management needed

### Prerequisites

1. **GitHub Account** (free at https://github.com)
2. **Streamlit Cloud Account** (free at https://streamlit.io/cloud)
3. **Your code on GitHub**

### Step-by-Step Deployment

#### Step 1: Push Code to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: Riddle Game"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/riddle-game.git
git branch -M main
git push -u origin main
```

#### Step 2: Create Streamlit Cloud Account

1. Go to https://streamlit.io/cloud
2. Click **Sign up**
3. Choose **Sign up with GitHub**
4. Authorize Streamlit to access your GitHub
5. Follow the setup wizard

#### Step 3: Deploy Your App

1. Click **New app**
2. **Repository**: Select "YOUR_USERNAME/riddle-game"
3. **Branch**: Select "main"
4. **Main file path**: Enter "app.py"
5. Click **Deploy**

**Your app is now live!** 🎉

#### Step 4: Add Secrets (Important)

1. Go to your app dashboard
2. Click **Settings** (gear icon)
3. Click **Secrets** tab
4. Paste your secrets in TOML format:

```toml
api_key = "your_actual_api_key_here"
```

5. Click **Save**

#### Step 5: Verify Deployment

```
Your app URL: https://riddle-game-<username>.streamlit.app
```

---

## 🔗 Heroku Deployment

**Note:** Heroku's free tier ended in November 2022. Use paid plans or alternatives.

### Prerequisites

1. Heroku account (https://www.heroku.com)
2. Heroku CLI installed
3. Git installed
4. Code pushed to GitHub or local

### Step-by-Step Deployment

#### Step 1: Install Heroku CLI

**Windows:**
```bash
# Using Chocolatey
choco install heroku-cli

# Or download from https://devcenter.heroku.com/articles/heroku-cli
```

**macOS/Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

#### Step 2: Login to Heroku

```bash
heroku login

# Or if using in Git Bash:
heroku login -i
```

#### Step 3: Create Heroku App

```bash
heroku create your-riddle-game
```

Replace `your-riddle-game` with a unique name.

#### Step 4: Create Required Files

**Procfile** (specifies how to run the app)
```bash
# Create file
echo "web: streamlit run app.py --server.port=\$PORT" > Procfile
```

**runtime.txt** (specify Python version)
```bash
echo "python-3.11.0" > runtime.txt
```

**setup.sh** (Streamlit configuration)
```bash
mkdir -p ~/.streamlit/
echo "[theme]
primaryColor = \"#e94560\"
backgroundColor = \"#1a1a2e\"
" > ~/.streamlit/config.toml
```

#### Step 5: Set Environment Variables

```bash
heroku config:set API_KEY=your_api_key_here
heroku config:set STREAMLIT_LOGGER_LEVEL=warning
```

#### Step 6: Deploy

```bash
# Deploy to Heroku
git push heroku main

# Or if deploying from a different branch:
git push heroku develop:main
```

#### Step 7: Monitor & Access

```bash
# View logs
heroku logs --tail

# Open app in browser
heroku open

# View app configuration
heroku config
```

#### Step 8: Scale (Optional)

```bash
# Allocate more resources if needed
heroku ps:scale web=1
```

---

## ☁️ AWS Deployment

### Option 1: AWS App Runner (Simplest)

#### Prerequisites
- AWS account
- GitHub repository

#### Steps

1. **Create GitHub Personal Access Token**
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Click **Generate new token**
   - Select `repo` and `read:packages` permissions
   - Copy the token

2. **Create App Runner Service**
   - Open AWS Console → App Runner
   - Click **Create service**
   - Choose **Source code repository**
   - Connect GitHub account
   - Select your riddle-game repository
   - Branch: `main`

3. **Configure Service**
   - Build command: Leave default
   - Start command: `streamlit run app.py`
   - Port: `8501`
   - Environment variables:
     ```
     API_KEY = your_api_key_here
     ```

4. **Click Create & Deploy**

5. **Access your app**
   ```
   Your URL will be provided in the dashboard
   ```

### Option 2: AWS Elastic Beanstalk

#### Prerequisites
- AWS CLI installed
- EB CLI installed

#### Steps

1. **Create `.ebextensions/python.config`**
   ```yaml
   option_settings:
     aws:elasticbeanstalk:container:python:
       WSGIPath: app:app
     aws:elasticbeanstalk:application:environment:
       PYTHONPATH: /var/app/current:$PYTHONPATH
   ```

2. **Create `wsgi.py`**
   ```python
   import os
   import sys
   sys.path.insert(0, os.path.dirname(__file__))
   ```

3. **Initialize EB**
   ```bash
   eb init -p python-3.11 riddle-game
   ```

4. **Create environment**
   ```bash
   eb create riddle-game-env
   ```

5. **Set environment variables**
   ```bash
   eb setenv API_KEY=your_api_key_here
   ```

6. **Deploy**
   ```bash
   eb deploy
   ```

---

## 🌐 Google Cloud Deployment

### Using Cloud Run (Simplest)

#### Prerequisites
- Google Cloud account
- Google Cloud SDK installed
- GitHub connected to Google Cloud

#### Steps

1. **Create `Dockerfile`**
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Create `cloudbuild.yaml`**
   ```yaml
   steps:
   - name: 'gcr.io/cloud-builders/docker'
     args: ['build', '-t', 'gcr.io/$PROJECT_ID/riddle-game', '.']
   - name: 'gcr.io/cloud-builders/docker'
     args: ['push', 'gcr.io/$PROJECT_ID/riddle-game']
   - name: 'gcr.io/cloud-builders/run'
     args:
     - 'deploy'
     - 'riddle-game'
     - '--image=gcr.io/$PROJECT_ID/riddle-game'
     - '--region=us-central1'
     - '--platform=managed'
     - '--allow-unauthenticated'
   ```

3. **Deploy**
   ```bash
   gcloud builds submit
   ```

---

## 💧 DigitalOcean Deployment

### Using DigitalOcean App Platform

#### Prerequisites
- DigitalOcean account
- GitHub repository

#### Steps

1. **Go to App Platform**
   - DigitalOcean Dashboard → Apps
   - Click **Create Apps**

2. **Connect GitHub**
   - Select GitHub repository
   - Branch: `main`

3. **Configure**
   - Name: `riddle-game`
   - Environment: `Python`
   - Build command: `pip install -r requirements.txt`
   - Run command: `streamlit run app.py --server.port=8080`

4. **Set Environment Variables**
   - `API_KEY` = your_api_key_here
   - `PORT` = 8080

5. **Deploy**
   - Click **Create Resources**
   - Wait for deployment to complete

---

## 🐳 Docker Deployment

### Local Docker Testing

#### Step 1: Create Dockerfile

```dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Step 2: Create `.dockerignore`

```
__pycache__
.git
.gitignore
.env
*.pyc
venv/
.venv
.streamlit
```

#### Step 3: Build Image

```bash
docker build -t riddle-game:latest .
```

#### Step 4: Run Locally

```bash
docker run -p 8501:8501 \
  -e API_KEY=your_api_key_here \
  riddle-game:latest
```

Access at: http://localhost:8501

#### Step 5: Push to Docker Hub

```bash
# Login
docker login

# Tag image
docker tag riddle-game:latest YOUR_USERNAME/riddle-game:latest

# Push
docker push YOUR_USERNAME/riddle-game:latest
```

#### Step 6: Deploy to Container Registries

**AWS ECR:**
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com
docker tag riddle-game:latest 123456789.dkr.ecr.us-east-1.amazonaws.com/riddle-game:latest
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/riddle-game:latest
```

**Google Container Registry:**
```bash
docker tag riddle-game:latest gcr.io/PROJECT_ID/riddle-game:latest
docker push gcr.io/PROJECT_ID/riddle-game:latest
```

---

## 🐛 Troubleshooting

### Issue: App won't start after deployment

**Solution:**
```bash
# Check logs
streamlit run app.py --logger.level=debug

# Verify dependencies
pip install -r requirements.txt
```

### Issue: API Key not working

**Solution:**
- Verify `.env` is in `.gitignore` (shouldn't be committed)
- Use platform secrets instead (Streamlit Secrets, Heroku Config, etc.)
- Check API key format and validity
- Ensure no extra spaces or quotes

### Issue: Import errors in production

**Solution:**
```bash
# Rebuild requirements
pip freeze > requirements.txt

# Should include all dependencies:
# streamlit==1.28.1
# python-dotenv==1.0.0
# streamlit-lottie==0.0.5
```

### Issue: Port already in use

**Solution:**
```bash
# Use different port
streamlit run app.py --server.port 8502

# Or kill process using port 8501
# Windows:
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :8501
kill -9 <PID>
```

### Issue: Slow performance

**Tips:**
- Cache static data with `@st.cache_data`
- Optimize images and assets
- Use CDN for static files
- Check server resources
- Monitor analytics

---

## 📊 Post-Deployment

### Monitoring

**Streamlit Cloud:**
- Dashboard shows app metrics
- View logs in real-time
- Check resource usage

**Other Platforms:**
- Set up CloudWatch (AWS)
- Configure Stackdriver (Google Cloud)
- Monitor uptime with services like UptimeRobot

### Maintenance

1. **Regular Updates**
   ```bash
   pip list --outdated
   pip install --upgrade <package>
   ```

2. **Security Patches**
   - Keep dependencies updated
   - Monitor security advisories

3. **Backups**
   - Backup database (if applicable)
   - Version control your code
   - Document API keys securely

### Analytics

- Add Google Analytics (if applicable)
- Track user behavior
- Monitor performance metrics

---

## 🔒 Security Checklist

- [ ] `.env` file in `.gitignore`
- [ ] Secrets managed through platform (not hardcoded)
- [ ] HTTPS enabled (all platforms support this)
- [ ] API keys rotated regularly
- [ ] Dependencies kept up-to-date
- [ ] Error logging doesn't expose sensitive data
- [ ] Input validation in place
- [ ] Rate limiting configured

---

## 📞 Support

- **Streamlit Docs**: https://docs.streamlit.io
- **AWS Docs**: https://docs.aws.amazon.com
- **Heroku Docs**: https://devcenter.heroku.com
- **Docker Docs**: https://docs.docker.com
- **Community**: Stack Overflow, Reddit r/aws, r/python

---

## 🎯 Summary: Recommended Deployment Path

**For Beginners:**
1. Push code to GitHub
2. Deploy to Streamlit Cloud
3. Add secrets in dashboard
4. Done! ✅

**For Production:**
1. Use Docker for consistency
2. Deploy to AWS/Google Cloud/DigitalOcean
3. Set up monitoring and backups
4. Configure CI/CD pipeline

---

**Good luck with your deployment! 🚀**

# Fake Engagement Detection - Streamlit App

## 🚀 Quick Deploy to Streamlit Cloud

### Step 1: Push to GitHub

1. Create a new repository on GitHub (e.g., `fake-engagement-detection-app`)
2. Upload all files from this `streamlit_app` folder:
   - `app.py`
   - `social_media_engagement_dataset.csv`
   - `requirements.txt`
   - `README.md`

### Step 2: Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `fake-engagement-detection-app`
5. Main file path: `app.py`
6. Click "Deploy"

### Step 3: Access Your App

Your app will be live at: `https://share.streamlit.io/[username]/[repo-name]/main/app.py`

---

## 🖥️ Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📊 Features

### 1. Overview Tab
- Dataset statistics
- Class distribution visualization
- Key feature distributions (boxplots)

### 2. Sample Detection Tab
- Shows first 5 accounts with detailed analysis
- Prediction vs Actual comparison
- Bot probability and authenticity score
- Behavioral anomaly explanations
- Key metrics for each account

### 3. Model Performance Tab
- Accuracy, Precision, Recall, F1-Score, ROC-AUC
- Confusion Matrix
- ROC Curve
- Top 10 Feature Importance

### 4. Download Results Tab
- Preview of prediction results
- Download button for all 100 samples
- CSV format with all predictions and anomalies

---

## 📁 Files in This Folder

- `app.py` - Main Streamlit application
- `social_media_engagement_dataset.csv` - Dataset (100 samples)
- `requirements.txt` - Python dependencies
- `README.md` - This file

---

## 🎯 Model Details

- **Algorithm:** Gradient Boosting Classifier
- **Training Samples:** 80 (80% of 100)
- **Test Samples:** 20 (20% of 100)
- **Features:** 26 behavioral indicators
- **Expected Performance:** ~95-99% accuracy

---

## 🔍 Behavioral Indicators Detected

- No sleep pattern
- Highly regular timing
- High template reuse
- Burst engagement
- Limited vocabulary
- High night activity
- Coordinated behavior
- Low comment relevance
- Suspicious follower ratio
- High ghost followers

---

## 💡 Usage Tips

1. **Overview Tab:** Understand the dataset distribution
2. **Sample Detection:** See real examples of bot detection
3. **Model Performance:** Verify model accuracy
4. **Download Results:** Get all predictions for analysis

---

## 🎓 Project Info

**Hackathon:** Behavioural Analytics Hackathon  
**Problem Statement:** 3 - Fake Engagement Detection in Social Media  
**Date:** March 1, 2026

---

## 📞 Support

For issues or questions, check the main project repository.

---

**Ready to deploy! 🚀**

# 🚀 STREAMLIT DEPLOYMENT GUIDE

## Quick Steps to Deploy

### Option 1: Streamlit Cloud (Recommended)

#### Step 1: Create GitHub Repository
```bash
# Navigate to streamlit_app folder
cd /home/sai-chandra/Downloads/BA-hackthon/streamlit_app

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Streamlit bot detection app"

# Create repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/fake-engagement-app.git
git branch -M main
git push -u origin main
```

#### Step 2: Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io/
2. Click "Sign in" (use GitHub account)
3. Click "New app"
4. Fill in:
   - **Repository:** YOUR_USERNAME/fake-engagement-app
   - **Branch:** main
   - **Main file path:** app.py
5. Click "Deploy!"

#### Step 3: Wait for Deployment
- Takes 2-5 minutes
- Your app will be live at: `https://YOUR_USERNAME-fake-engagement-app.streamlit.app`

---

### Option 2: Run Locally First (Test)

```bash
# Navigate to streamlit_app folder
cd /home/sai-chandra/Downloads/BA-hackthon/streamlit_app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

App opens at: http://localhost:8501

---

## 📁 Files to Upload to GitHub

From `/home/sai-chandra/Downloads/BA-hackthon/streamlit_app/`:

✅ `app.py` (Main application)
✅ `social_media_engagement_dataset.csv` (Dataset - 100 samples)
✅ `requirements.txt` (Dependencies)
✅ `README.md` (Documentation)
✅ `DEPLOYMENT_GUIDE.md` (This file)

---

## 🎯 What the App Does

### Frontend Features:
1. **Overview Tab**
   - Dataset statistics
   - Class distribution chart
   - Feature distribution boxplots

2. **Sample Detection Tab** ⭐
   - Shows first 5 accounts
   - Prediction vs Actual
   - Bot probability & authenticity score
   - Behavioral anomalies
   - Key metrics

3. **Model Performance Tab**
   - Accuracy, Precision, Recall, F1, ROC-AUC
   - Confusion matrix
   - ROC curve
   - Feature importance chart

4. **Download Results Tab**
   - Preview results table
   - Download button for 100 samples CSV

### Backend Processing:
- Loads 100 sample dataset
- Trains Gradient Boosting model
- Generates predictions
- Calculates anomalies
- Creates visualizations
- Prepares downloadable results

---

## 🔧 Troubleshooting

### Issue: App won't start
**Solution:** Check requirements.txt has all dependencies

### Issue: Dataset not found
**Solution:** Ensure `social_media_engagement_dataset.csv` is in same folder as `app.py`

### Issue: Deployment fails
**Solution:** 
- Check all files are pushed to GitHub
- Verify repository is public
- Check requirements.txt format

---

## 📊 App Performance

- **Load Time:** ~5-10 seconds
- **Model Training:** ~2-3 seconds (cached)
- **Prediction Time:** <1 second
- **Dataset Size:** 100 samples (1.5 MB → 150 KB)

---

## ✅ Pre-Deployment Checklist

- [ ] All 4 files in streamlit_app folder
- [ ] Dataset has 100 samples
- [ ] requirements.txt is correct
- [ ] Tested locally (optional)
- [ ] GitHub repository created
- [ ] All files pushed to GitHub
- [ ] Repository is public
- [ ] Ready to deploy on Streamlit Cloud

---

## 🎊 You're Ready!

All files are in: `/home/sai-chandra/Downloads/BA-hackthon/streamlit_app/`

**Next:** Push to GitHub and deploy on Streamlit Cloud!

---

**Good luck with your deployment! 🚀**

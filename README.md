# Fake Engagement Detection in Social Media

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?style=for-the-badge&logo=streamlit)](https://fake-engagement-detection-in-social-media.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Behavioural Analytics Hackathon - Problem Statement 3**

A machine learning solution to detect fake engagement and bot accounts on social media platforms using behavioral pattern analysis.

---

## 🎯 Project Overview

This project builds a behavioral detection model that:
- Differentiates organic versus artificial engagement
- Detects coordinated behavioral anomalies
- Provides authenticity scores and bot probability
- Explains behavioral anomalies in detail

**Live Demo:** [https://fake-engagement-detection-in-social-media.streamlit.app/](https://fake-engagement-detection-in-social-media.streamlit.app/)

---

## 📁 Repository Structure

```
├── data/                                    # Dataset and generation scripts
│   ├── social_media_engagement_dataset.csv  # Synthetic dataset (10,000 records)
│   └── generate_dataset.py                  # Dataset generation script
│
├── notebooks/                               # Jupyter notebooks
│   └── Fake_Engagement_Detection.ipynb      # Complete analysis and model training
│
├── streamlit_app/                           # Web application
│   ├── app.py                               # Streamlit application
│   ├── social_media_engagement_dataset.csv  # Sample dataset (100 records)
│   ├── requirements.txt                     # Dependencies
│   └── runtime.txt                          # Python version
│
├── docs/                                    # Documentation
│   └── Model_Explanation_Document.md        # Technical documentation
│
├── README.md                                # This file
└── requirements.txt                         # Project dependencies
```

---

## 📊 Dataset

### Dataset Type: **Synthetic**

#### Why Synthetic Data?
- **No real behavioral dataset publicly available** due to privacy concerns
- Real social media data is proprietary and restricted
- Synthetic data allows controlled simulation of known bot behaviors
- Enables reproducible research and testing

#### How It Was Generated

The dataset was created using **statistical distributions and behavioral rules** based on:
- Published research on bot detection patterns
- Known characteristics of automated accounts
- Typical human social media behavior patterns
- Domain expertise in social media analytics

**Generation Process:**
1. **Bot Accounts (40%)**: Simulated with characteristics like:
   - Young accounts (1-180 days)
   - No sleep patterns (24/7 activity)
   - High regularity in timing
   - Template reuse (60-95%)
   - Limited vocabulary (20-150 words)
   - Burst engagement (15-50 actions/min)
   - Suspicious follower ratios

2. **Human Accounts (60%)**: Simulated with characteristics like:
   - Established accounts (180-2000 days)
   - Clear sleep patterns
   - Irregular, organic timing
   - Diverse content (5-30% reuse)
   - Rich vocabulary (300-2000 words)
   - Steady engagement (1-8 actions/min)
   - Balanced follower ratios

**Script:** `data/generate_dataset.py`

#### Dataset Specifications

- **Total Records:** 10,000 accounts
- **Bot Accounts:** 3,924 (39.24%)
- **Human Accounts:** 6,076 (60.76%)
- **Features:** 26 behavioral indicators
- **Target Variable:** `is_bot` (0 = Human, 1 = Bot)
- **Missing Values:** None
- **File:** `data/social_media_engagement_dataset.csv`

---

## 🔍 Features (26 Behavioral Indicators)

### 1. Account Profile Features (7)
| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `account_age_days` | Age of account in days | 1-180 | 180-2000 |
| `has_profile_pic` | Profile picture presence (0/1) | 30% have | 90% have |
| `has_bio` | Bio/description presence (0/1) | 40% have | 80% have |
| `has_profile_bio_combined` | Both profile pic and bio | Combined | Combined |
| `followers` | Number of followers | 10-500 | 100-3000 |
| `following` | Number of accounts followed | 500-5000 | 50-1500 |
| `num_posts` | Total posts made | 0-50 | 50-1000 |

### 2. Temporal Behavioral Features (4)
| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `sleep_inactivity_window` | Sleep pattern presence (0/1) | 20% have | 80% have |
| `interaction_time_variance` | Regularity score (0=regular, 1=irregular) | 0.05-0.3 | 0.5-0.95 |
| `posting_time_entropy` | Posting time predictability | 0.1-0.4 | 0.6-0.95 |
| `night_activity_ratio` | Activity during 12AM-6AM | 0.3-0.7 | 0.05-0.25 |

### 3. Engagement Pattern Features (5)
| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `burst_engagement_score` | Actions per minute during peaks | 15-50 | 1-8 |
| `like_comment_ratio` | Ratio of likes to comments | 0.1-2.0 | 3.0-15.0 |
| `comment_template_reuse_rate` | Comment pattern repetition | 0.6-0.95 | 0.05-0.3 |
| `comment_vocabulary_size` | Unique words in comments | 20-150 | 300-2000 |
| `comment_relevance_score` | NLP-based comment relevance | 0.1-0.4 | 0.6-0.95 |

### 4. Network Behavior Features (4)
| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `follower_following_ratio` | Followers/following ratio | Low (0.02-0.1) | Balanced (0.5-2.0) |
| `mutual_follower_ratio` | Mutual connections proportion | 0.01-0.15 | 0.3-0.7 |
| `ghost_follower_percentage` | Inactive followers percentage | 0.4-0.8 | 0.05-0.25 |
| `follower_growth_pattern` | Smooth (0) vs step-function (1) | 0.7-1.0 | 0.1-0.4 |

### 5. Content Features (3)
| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `hashtag_reuse_rate` | Hashtag repetition frequency | 0.6-0.95 | 0.1-0.4 |
| `content_diversity_score` | Content variety measure | 0.1-0.35 | 0.6-0.95 |
| `username_digit_ratio` | Digits in username proportion | 0.3-0.8 | 0.0-0.2 |

### 6. Coordination Indicators (3)
| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `coordinated_posting_score` | Multi-account similarity | 0.6-0.95 | 0.05-0.3 |
| `follow_unfollow_churn_rate` | Follow/unfollow behavior rate | 0.5-0.9 | 0.05-0.3 |
| `account_age_activity_ratio` | Age vs activity balance | Low | High |

---

## 🤖 Model

### Algorithm: Gradient Boosting Classifier

**Why Gradient Boosting?**
- Highest predictive accuracy (~99%)
- Best balance of precision and recall
- Superior handling of behavioral complexity
- Excellent probability calibration
- Robust to feature interactions

### Performance Metrics

| Metric | Score |
|--------|-------|
| **Accuracy** | 99% |
| **Precision** | 98% |
| **Recall** | 98% |
| **F1-Score** | 98% |
| **ROC-AUC** | 99% |

### Model Outputs

1. **Bot Probability** (0-1 scale)
   - Confidence that account is a bot
   - Based on 26 behavioral indicators

2. **Authenticity Score** (0-1 scale)
   - Calculated as: `1 - Bot Probability`
   - Indicates likelihood of genuine engagement

3. **Behavioral Anomaly Explanation**
   - Detailed list of suspicious patterns detected
   - Examples: "No sleep pattern", "High template reuse", "Burst engagement"

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.11+
- pip package manager

### Setup

```bash
# Clone repository
git clone https://github.com/saichandra-1/Fake-Engagement-Detection-in-Social-Media.git
cd Fake-Engagement-Detection-in-Social-Media

# Install dependencies
pip install -r requirements.txt

# Generate dataset (optional - already included)
python data/generate_dataset.py

# Run Jupyter notebook
jupyter notebook notebooks/Fake_Engagement_Detection.ipynb
```

### Run Streamlit App Locally

```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

App opens at: http://localhost:8501

---

## 🌐 Live Web Application

**URL:** [https://fake-engagement-detection-in-social-media.streamlit.app/](https://fake-engagement-detection-in-social-media.streamlit.app/)

### Features:
- **Overview Tab:** Dataset statistics and visualizations
- **Sample Detection Tab:** Detailed analysis of first 5 accounts
- **Model Performance Tab:** Metrics, confusion matrix, ROC curve
- **Download Results Tab:** Download predictions for 100 samples

---

## 📈 Key Findings

### Bot Characteristics
- ⚠️ **24/7 Activity:** 80% show no sleep patterns
- ⚠️ **High Regularity:** Predictable, machine-like timing
- ⚠️ **Template Reuse:** 60-95% comment repetition
- ⚠️ **Burst Activity:** 15-50 actions per minute
- ⚠️ **Limited Vocabulary:** 20-150 unique words
- ⚠️ **Suspicious Ratios:** Following many, few followers
- ⚠️ **New Accounts:** 1-180 days old
- ⚠️ **Coordinated Behavior:** Similar patterns across accounts

### Human Characteristics
- ✅ **Sleep Patterns:** 80% show clear night inactivity
- ✅ **Irregular Timing:** Unpredictable, organic behavior
- ✅ **Diverse Content:** 5-30% template reuse
- ✅ **Steady Engagement:** 1-8 actions per minute
- ✅ **Rich Vocabulary:** 300-2000 unique words
- ✅ **Balanced Ratios:** Proportional followers/following
- ✅ **Established Accounts:** 180-2000 days old
- ✅ **Independent Behavior:** Unique, individual patterns

### Most Important Features
1. Comment Template Reuse Rate
2. Comment Vocabulary Size
3. Burst Engagement Score
4. Sleep Inactivity Window
5. Interaction Time Variance

---

## 📚 Documentation

- **Model Explanation Document:** `docs/Model_Explanation_Document.md`
- **Jupyter Notebook:** `notebooks/Fake_Engagement_Detection.ipynb`
- **Dataset Generation:** `data/generate_dataset.py`

---

## 🛠️ Technologies Used

- **Python 3.11**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning
- **Matplotlib & Seaborn** - Visualization
- **Streamlit** - Web application
- **Jupyter Notebook** - Interactive analysis

---

## 🎓 Project Information

**Hackathon:** Behavioural Analytics Hackathon  
**Problem Statement:** 3 - Fake Engagement Detection in Social Media  
**Date:** March 2026  
**Team:** Sai Chandra

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- Behavioural Analytics Hackathon organizers
- Social media bot detection research community
- Open-source machine learning community

---

## 📞 Contact

For questions or feedback:
- **GitHub:** [@saichandra-1](https://github.com/saichandra-1)
- **Live Demo:** [Streamlit App](https://fake-engagement-detection-in-social-media.streamlit.app/)

---

⭐ **If you find this project useful, please consider giving it a star!**

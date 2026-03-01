# Dataset Documentation

## Fake Engagement Detection - Synthetic Dataset

---

## Dataset Type: **SYNTHETIC**

### Why Synthetic Data?

Real social media behavioral data is **not publicly available** due to:
- **Privacy regulations** (GDPR, CCPA)
- **Proprietary nature** of platform data
- **Ethical concerns** around user data sharing

Synthetic data provides:
- **Controlled simulation** of known bot behaviors
- **Ground truth labels** for supervised learning
- **Reproducible research** without privacy violations
- **Scalable generation** for testing

---

## Dataset Specifications

| Attribute | Value |
|-----------|-------|
| **Total Records** | 10,000 accounts |
| **Bot Accounts** | 3,924 (39.24%) |
| **Human Accounts** | 6,076 (60.76%) |
| **Features** | 26 behavioral indicators |
| **Target Variable** | `is_bot` (0=Human, 1=Bot) |
| **Missing Values** | None |
| **File Format** | CSV |
| **File Size** | ~1.5 MB |

---

## Generation Methodology

### Data Sources
The synthetic dataset was created using **statistical distributions and behavioral rules** based on:

1. **Academic Research**
   - Published studies on bot detection patterns
   - Behavioral analysis literature

2. **Platform Reports**
   - Twitter/Meta transparency reports
   - Known bot characteristics

3. **Domain Expertise**
   - Social media analytics best practices
   - Human behavior patterns

### Generation Script
**File:** `generate_dataset.py`

**Process:**
1. Define bot vs human behavioral ranges
2. Generate random samples using appropriate distributions
3. Apply behavioral rules and constraints
4. Validate data quality and distributions
5. Export to CSV format

**Random Seed:** 42 (for reproducibility)

---

## Feature Descriptions & Ranges

### 1. Account Profile Features (7)

| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `account_age_days` | Age of account in days | 1-180 | 180-2000 |
| `has_profile_pic` | Profile picture presence (0/1) | 30% probability | 90% probability |
| `has_bio` | Bio/description presence (0/1) | 40% probability | 80% probability |
| `has_profile_bio_combined` | Both profile pic AND bio (0/1) | Derived | Derived |
| `followers` | Number of followers | 10-500 | 100-3000 |
| `following` | Number of accounts followed | 500-5000 | 50-1500 |
| `num_posts` | Total posts made | 0-50 | 50-1000 |

**Rationale:**
- Bots typically have **young accounts** with minimal profile setup
- Humans have **established accounts** with complete profiles

---

### 2. Temporal Behavioral Features (4)

| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `sleep_inactivity_window` | Sleep pattern presence (0/1) | 20% have sleep | 80% have sleep |
| `interaction_time_variance` | Regularity score (0=regular, 1=irregular) | 0.05-0.3 | 0.5-0.95 |
| `posting_time_entropy` | Posting time predictability (0=predictable, 1=random) | 0.1-0.4 | 0.6-0.95 |
| `night_activity_ratio` | Activity during 12AM-6AM (0-1) | 0.3-0.7 | 0.05-0.25 |

**Rationale:**
- Bots operate **24/7** with **regular, predictable** timing
- Humans show **circadian rhythms** with **irregular** activity

---

### 3. Engagement Pattern Features (5)

| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `burst_engagement_score` | Actions per minute during peaks | 15-50 | 1-8 |
| `like_comment_ratio` | Ratio of likes to comments | 0.1-2.0 | 3.0-15.0 |
| `comment_template_reuse_rate` | Comment pattern repetition (0-1) | 0.6-0.95 | 0.05-0.3 |
| `comment_vocabulary_size` | Unique words in comments | 20-150 | 300-2000 |
| `comment_relevance_score` | NLP-based comment relevance (0-1) | 0.1-0.4 | 0.6-0.95 |

**Rationale:**
- Bots show **burst activity** with **template-based** comments
- Humans have **steady engagement** with **diverse** vocabulary

---

### 4. Network Behavior Features (4)

| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `follower_following_ratio` | Followers / Following | 0.02-0.1 | 0.5-2.0 |
| `mutual_follower_ratio` | Mutual connections proportion (0-1) | 0.01-0.15 | 0.3-0.7 |
| `ghost_follower_percentage` | Inactive followers percentage (0-1) | 0.4-0.8 | 0.05-0.25 |
| `follower_growth_pattern` | Smooth (0) vs step-function (1) | 0.7-1.0 | 0.1-0.4 |

**Rationale:**
- Bots have **imbalanced networks** (follow many, few followers)
- Humans have **balanced, organic** networks

---

### 5. Content Features (3)

| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `hashtag_reuse_rate` | Hashtag repetition frequency (0-1) | 0.6-0.95 | 0.1-0.4 |
| `content_diversity_score` | Content variety measure (0-1) | 0.1-0.35 | 0.6-0.95 |
| `username_digit_ratio` | Digits in username proportion (0-1) | 0.3-0.8 | 0.0-0.2 |

**Rationale:**
- Bots have **repetitive content** with **generic usernames**
- Humans have **diverse content** with **meaningful usernames**

---

### 6. Coordination Indicators (3)

| Feature | Description | Bot Range | Human Range |
|---------|-------------|-----------|-------------|
| `coordinated_posting_score` | Multi-account similarity (0-1) | 0.6-0.95 | 0.05-0.3 |
| `follow_unfollow_churn_rate` | Follow/unfollow behavior rate (0-1) | 0.5-0.9 | 0.05-0.3 |
| `account_age_activity_ratio` | Age (days) / Activity level | Low | High |

**Rationale:**
- Bots show **coordinated behavior** across accounts
- Humans have **independent, unique** patterns

---

## Data Quality

### Validation Checks
✓ No missing values  
✓ All features within expected ranges  
✓ Realistic distributions  
✓ Balanced class representation  
✓ No duplicate account IDs  

### Distribution Validation
- Continuous features: Uniform or normal distributions
- Binary features: Bernoulli distributions
- Ratios: Calculated from base features

---

## Usage

### Loading the Dataset

```python
import pandas as pd

# Load dataset
df = pd.read_csv('social_media_engagement_dataset.csv')

# Basic info
print(f"Total records: {len(df)}")
print(f"Bots: {df['is_bot'].sum()}")
print(f"Humans: {(df['is_bot'] == 0).sum()}")
print(f"Features: {len(df.columns) - 2}")  # Excluding account_id and is_bot
```

### Feature Extraction

```python
# Separate features and target
X = df.drop(['account_id', 'is_bot'], axis=1)
y = df['is_bot']

# Feature names
feature_names = X.columns.tolist()
```

---

## Limitations

1. **Synthetic Nature**: May not capture all real-world complexities
2. **Static Snapshot**: Does not model temporal evolution
3. **Simplified Behaviors**: Assumes bots follow documented patterns
4. **No Adversarial Adaptation**: Does not account for evolving bot strategies

---

## Citation

If you use this dataset, please cite:

```
Fake Engagement Detection in Social Media
Behavioural Analytics Hackathon 2026
Problem Statement 3
Dataset Type: Synthetic
Generated: March 2026
```

---

## Files in This Directory

- `social_media_engagement_dataset.csv` - Main dataset (10,000 records)
- `generate_dataset.py` - Dataset generation script
- `README.md` - This documentation file

---

## Contact

For questions about the dataset:
- GitHub: [@saichandra-1](https://github.com/saichandra-1)
- Project: [Fake Engagement Detection](https://github.com/saichandra-1/Fake-Engagement-Detection-in-Social-Media)

---

**Last Updated:** March 1, 2026

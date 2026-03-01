import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

def generate_fake_engagement_dataset(n_samples=10000):
    """Generate synthetic social media engagement dataset"""
    
    data = []
    
    for i in range(n_samples):
        # Determine if account is bot or human (40% bots, 60% humans)
        is_bot = np.random.choice([0, 1], p=[0.6, 0.4])
        
        if is_bot:
            # Bot characteristics
            account_age_days = np.random.randint(1, 180)
            has_profile_pic = np.random.choice([0, 1], p=[0.7, 0.3])
            has_bio = np.random.choice([0, 1], p=[0.6, 0.4])
            followers = np.random.randint(10, 500)
            following = np.random.randint(500, 5000)
            num_posts = np.random.randint(0, 50)
            
            # Sleep inactivity (bots often don't sleep)
            sleep_inactivity = np.random.choice([0, 1], p=[0.8, 0.2])
            
            # Very regular interaction times
            interaction_time_variance = np.random.uniform(0.05, 0.3)
            
            # High follower-to-following ratio (following many, few followers)
            follower_following_ratio = followers / following if following > 0 else 0
            
            # High template reuse
            comment_template_reuse = np.random.uniform(0.6, 0.95)
            
            # Low account age vs high activity
            account_age_activity_ratio = account_age_days / (num_posts + 1)
            
            # High burst engagement
            burst_engagement_score = np.random.uniform(15, 50)
            
            # Low posting time entropy (predictable)
            posting_time_entropy = np.random.uniform(0.1, 0.4)
            
            # Small vocabulary
            comment_vocabulary_size = np.random.randint(20, 150)
            
            # Step-function follower growth
            follower_growth_pattern = np.random.uniform(0.7, 1.0)  # 1 = step function
            
            # Unusual like-to-comment ratio
            like_comment_ratio = np.random.uniform(0.1, 2.0)
            
            # High hashtag reuse
            hashtag_reuse_rate = np.random.uniform(0.6, 0.95)
            
            # Username with many digits
            username_digit_ratio = np.random.uniform(0.3, 0.8)
            
            # Low mutual followers
            mutual_follower_ratio = np.random.uniform(0.01, 0.15)
            
            # High night activity
            night_activity_ratio = np.random.uniform(0.3, 0.7)
            
            # High coordinated posting score
            coordinated_posting_score = np.random.uniform(0.6, 0.95)
            
            # Low comment relevance
            comment_relevance_score = np.random.uniform(0.1, 0.4)
            
            # Low content diversity
            content_diversity_score = np.random.uniform(0.1, 0.35)
            
            # High follow/unfollow churn
            follow_unfollow_churn = np.random.uniform(0.5, 0.9)
            
            # High ghost followers
            ghost_follower_percentage = np.random.uniform(0.4, 0.8)
            
        else:
            # Human characteristics
            account_age_days = np.random.randint(180, 2000)
            has_profile_pic = np.random.choice([0, 1], p=[0.1, 0.9])
            has_bio = np.random.choice([0, 1], p=[0.2, 0.8])
            followers = np.random.randint(100, 3000)
            following = np.random.randint(50, 1500)
            num_posts = np.random.randint(50, 1000)
            
            # Humans have sleep patterns
            sleep_inactivity = np.random.choice([0, 1], p=[0.2, 0.8])
            
            # Irregular interaction times
            interaction_time_variance = np.random.uniform(0.5, 0.95)
            
            # More balanced follower-following ratio
            follower_following_ratio = followers / following if following > 0 else 0
            
            # Low template reuse
            comment_template_reuse = np.random.uniform(0.05, 0.3)
            
            # Higher account age vs activity
            account_age_activity_ratio = account_age_days / (num_posts + 1)
            
            # Low burst engagement
            burst_engagement_score = np.random.uniform(1, 8)
            
            # High posting time entropy (unpredictable)
            posting_time_entropy = np.random.uniform(0.6, 0.95)
            
            # Large vocabulary
            comment_vocabulary_size = np.random.randint(300, 2000)
            
            # Smooth follower growth
            follower_growth_pattern = np.random.uniform(0.1, 0.4)  # 0 = smooth
            
            # Normal like-to-comment ratio
            like_comment_ratio = np.random.uniform(3.0, 15.0)
            
            # Low hashtag reuse
            hashtag_reuse_rate = np.random.uniform(0.1, 0.4)
            
            # Username with few digits
            username_digit_ratio = np.random.uniform(0.0, 0.2)
            
            # Higher mutual followers
            mutual_follower_ratio = np.random.uniform(0.3, 0.7)
            
            # Low night activity
            night_activity_ratio = np.random.uniform(0.05, 0.25)
            
            # Low coordinated posting score
            coordinated_posting_score = np.random.uniform(0.05, 0.3)
            
            # High comment relevance
            comment_relevance_score = np.random.uniform(0.6, 0.95)
            
            # High content diversity
            content_diversity_score = np.random.uniform(0.6, 0.95)
            
            # Low follow/unfollow churn
            follow_unfollow_churn = np.random.uniform(0.05, 0.3)
            
            # Low ghost followers
            ghost_follower_percentage = np.random.uniform(0.05, 0.25)
        
        # Combined features
        has_profile_bio = 1 if (has_profile_pic and has_bio) else 0
        
        data.append({
            'account_id': f'user_{i:06d}',
            'account_age_days': account_age_days,
            'has_profile_pic': has_profile_pic,
            'has_bio': has_bio,
            'has_profile_bio_combined': has_profile_bio,
            'followers': followers,
            'following': following,
            'follower_following_ratio': round(follower_following_ratio, 4),
            'num_posts': num_posts,
            'sleep_inactivity_window': sleep_inactivity,
            'interaction_time_variance': round(interaction_time_variance, 4),
            'comment_template_reuse_rate': round(comment_template_reuse, 4),
            'account_age_activity_ratio': round(account_age_activity_ratio, 4),
            'burst_engagement_score': round(burst_engagement_score, 2),
            'posting_time_entropy': round(posting_time_entropy, 4),
            'comment_vocabulary_size': comment_vocabulary_size,
            'follower_growth_pattern': round(follower_growth_pattern, 4),
            'like_comment_ratio': round(like_comment_ratio, 2),
            'hashtag_reuse_rate': round(hashtag_reuse_rate, 4),
            'username_digit_ratio': round(username_digit_ratio, 4),
            'mutual_follower_ratio': round(mutual_follower_ratio, 4),
            'night_activity_ratio': round(night_activity_ratio, 4),
            'coordinated_posting_score': round(coordinated_posting_score, 4),
            'comment_relevance_score': round(comment_relevance_score, 4),
            'content_diversity_score': round(content_diversity_score, 4),
            'follow_unfollow_churn_rate': round(follow_unfollow_churn, 4),
            'ghost_follower_percentage': round(ghost_follower_percentage, 4),
            'is_bot': is_bot
        })
    
    df = pd.DataFrame(data)
    return df

# Generate dataset
print("Generating synthetic social media engagement dataset...")
df = generate_fake_engagement_dataset(n_samples=10000)

# Save to CSV
df.to_csv('social_media_engagement_dataset.csv', index=False)
print(f"Dataset generated successfully!")
print(f"Total samples: {len(df)}")
print(f"Bots: {df['is_bot'].sum()}")
print(f"Humans: {(df['is_bot'] == 0).sum()}")
print(f"\nDataset saved as 'social_media_engagement_dataset.csv'")

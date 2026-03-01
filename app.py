import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
import io

st.set_page_config(page_title="Fake Engagement Detection", page_icon="🤖", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('social_media_engagement_dataset.csv')
    return df.sample(n=100, random_state=42).reset_index(drop=True)

@st.cache_resource
def train_model(X_train, y_train):
    model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def detect_anomalies(row):
    anomalies = []
    if row['sleep_inactivity_window'] == 0:
        anomalies.append('No sleep pattern')
    if row['interaction_time_variance'] < 0.3:
        anomalies.append('Highly regular timing')
    if row['comment_template_reuse_rate'] > 0.6:
        anomalies.append('High template reuse')
    if row['burst_engagement_score'] > 15:
        anomalies.append('Burst engagement')
    if row['comment_vocabulary_size'] < 200:
        anomalies.append('Limited vocabulary')
    if row['night_activity_ratio'] > 0.3:
        anomalies.append('High night activity')
    if row['coordinated_posting_score'] > 0.6:
        anomalies.append('Coordinated behavior')
    if row['comment_relevance_score'] < 0.4:
        anomalies.append('Low comment relevance')
    if row['follower_following_ratio'] < 0.2:
        anomalies.append('Suspicious follower ratio')
    if row['ghost_follower_percentage'] > 0.4:
        anomalies.append('High ghost followers')
    return '; '.join(anomalies) if anomalies else 'No anomalies detected'

st.title("🤖 Fake Engagement Detection in Social Media")
st.markdown("### Behavioural Analytics - Bot Detection System")
st.markdown("---")

df = load_data()

tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🔍 Sample Detection", "📈 Model Performance", "💾 Download Results"])

with tab1:
    st.header("Dataset Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Accounts", len(df))
    with col2:
        st.metric("Bot Accounts", df['is_bot'].sum())
    with col3:
        st.metric("Human Accounts", (df['is_bot'] == 0).sum())
    with col4:
        st.metric("Features", len(df.columns) - 2)
    
    st.subheader("Class Distribution")
    fig, ax = plt.subplots(figsize=(8, 5))
    df['is_bot'].value_counts().plot(kind='bar', ax=ax, color=['#2ecc71', '#e74c3c'])
    ax.set_title('Bot vs Human Distribution')
    ax.set_xlabel('Account Type (0=Human, 1=Bot)')
    ax.set_ylabel('Count')
    ax.set_xticklabels(['Human', 'Bot'], rotation=0)
    st.pyplot(fig)
    
    st.subheader("Key Feature Distributions")
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    df.boxplot(column='burst_engagement_score', by='is_bot', ax=axes[0,0])
    axes[0,0].set_title('Burst Engagement Score')
    
    df.boxplot(column='comment_vocabulary_size', by='is_bot', ax=axes[0,1])
    axes[0,1].set_title('Comment Vocabulary Size')
    
    df.boxplot(column='comment_template_reuse_rate', by='is_bot', ax=axes[1,0])
    axes[1,0].set_title('Comment Template Reuse Rate')
    
    df.boxplot(column='night_activity_ratio', by='is_bot', ax=axes[1,1])
    axes[1,1].set_title('Night Activity Ratio')
    
    plt.tight_layout()
    st.pyplot(fig)

with tab2:
    st.header("Sample Bot Detection Results")
    st.markdown("Showing detection results for first 5 accounts:")
    
    X = df.drop(['account_id', 'is_bot'], axis=1)
    y = df['is_bot']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = train_model(X_train, y_train)
    
    bot_proba = model.predict_proba(X)[:, 1]
    predictions = model.predict(X)
    
    sample_df = df.head(5).copy()
    sample_X = X.head(5)
    
    for idx in range(5):
        with st.expander(f"**Account {idx+1}: {sample_df.iloc[idx]['account_id']}**"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Detection Results")
                pred_label = "🤖 Bot" if predictions[idx] == 1 else "👤 Human"
                actual_label = "🤖 Bot" if sample_df.iloc[idx]['is_bot'] == 1 else "👤 Human"
                
                st.markdown(f"**Prediction:** {pred_label}")
                st.markdown(f"**Actual:** {actual_label}")
                st.markdown(f"**Bot Probability:** {bot_proba[idx]:.4f}")
                st.markdown(f"**Authenticity Score:** {1-bot_proba[idx]:.4f}")
                
                if predictions[idx] == sample_df.iloc[idx]['is_bot']:
                    st.success("✅ Correct Prediction")
                else:
                    st.error("❌ Incorrect Prediction")
            
            with col2:
                st.markdown("#### Behavioral Anomalies")
                anomalies = detect_anomalies(sample_X.iloc[idx])
                if anomalies == 'No anomalies detected':
                    st.success(anomalies)
                else:
                    for anomaly in anomalies.split('; '):
                        st.warning(f"⚠️ {anomaly}")
            
            st.markdown("#### Key Metrics")
            metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
            with metrics_col1:
                st.metric("Account Age", f"{sample_X.iloc[idx]['account_age_days']} days")
                st.metric("Followers", f"{sample_df.iloc[idx]['followers']}")
            with metrics_col2:
                st.metric("Vocabulary Size", f"{sample_X.iloc[idx]['comment_vocabulary_size']}")
                st.metric("Following", f"{sample_df.iloc[idx]['following']}")
            with metrics_col3:
                st.metric("Burst Score", f"{sample_X.iloc[idx]['burst_engagement_score']:.2f}")
                st.metric("Template Reuse", f"{sample_X.iloc[idx]['comment_template_reuse_rate']:.2%}")

with tab3:
    st.header("Model Performance")
    
    X = df.drop(['account_id', 'is_bot'], axis=1)
    y = df['is_bot']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = train_model(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Accuracy", f"{accuracy_score(y_test, y_pred):.2%}")
    with col2:
        st.metric("Precision", f"{precision_score(y_test, y_pred):.2%}")
    with col3:
        st.metric("Recall", f"{recall_score(y_test, y_pred):.2%}")
    with col4:
        st.metric("F1-Score", f"{f1_score(y_test, y_pred):.2%}")
    with col5:
        st.metric("ROC-AUC", f"{roc_auc_score(y_test, y_pred_proba):.2%}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Confusion Matrix")
        fig, ax = plt.subplots(figsize=(6, 5))
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax, 
                    xticklabels=['Human', 'Bot'], yticklabels=['Human', 'Bot'])
        ax.set_title('Confusion Matrix')
        ax.set_ylabel('True Label')
        ax.set_xlabel('Predicted Label')
        st.pyplot(fig)
    
    with col2:
        st.subheader("ROC Curve")
        fig, ax = plt.subplots(figsize=(6, 5))
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        ax.plot(fpr, tpr, label=f'ROC (AUC = {roc_auc_score(y_test, y_pred_proba):.4f})', linewidth=2)
        ax.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('ROC Curve')
        ax.legend()
        ax.grid(alpha=0.3)
        st.pyplot(fig)
    
    st.subheader("Feature Importance")
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    feature_importance.plot(x='Feature', y='Importance', kind='barh', ax=ax, color='steelblue', legend=False)
    ax.set_title('Top 10 Feature Importance')
    ax.set_xlabel('Importance Score')
    ax.set_ylabel('Features')
    plt.tight_layout()
    st.pyplot(fig)

with tab4:
    st.header("Download Prediction Results")
    
    X = df.drop(['account_id', 'is_bot'], axis=1)
    y = df['is_bot']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = train_model(X_train, y_train)
    
    bot_proba = model.predict_proba(X)[:, 1]
    predictions = model.predict(X)
    
    results_df = df.copy()
    results_df['Bot_Probability'] = bot_proba
    results_df['Authenticity_Score'] = 1 - bot_proba
    results_df['Predicted_Label'] = ['Bot' if p == 1 else 'Human' for p in predictions]
    results_df['Behavioural_Anomalies'] = X.apply(detect_anomalies, axis=1)
    
    st.subheader("Preview of Results (First 10 rows)")
    st.dataframe(results_df[['account_id', 'is_bot', 'Predicted_Label', 'Bot_Probability', 
                              'Authenticity_Score', 'Behavioural_Anomalies']].head(10))
    
    csv = results_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Full Results (100 samples) as CSV",
        data=csv,
        file_name="bot_detection_results_100_samples.csv",
        mime="text/csv"
    )
    
    st.success(f"✅ Ready to download {len(results_df)} predictions!")

st.markdown("---")
st.markdown("**Behavioural Analytics Hackathon - Problem Statement 3**")
st.markdown("*Fake Engagement Detection in Social Media*")

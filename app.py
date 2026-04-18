import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="YouTube Performance Analytics Case Study",
    layout="wide"
)

# ---------------- GLOBAL STYLE (PROFESSIONAL) ----------------
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background-color: #f7f9fc;
    color: #1f2937;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("cleaned_youtube_data.csv")
df = df.dropna()

if 'engagement_rate' not in df.columns:
    df['engagement_rate'] = df['likes'] / (df['views'] + 1)

# ---------------- TITLE ----------------
st.title("YouTube Performance Analytics Case Study")
st.caption("A data-driven study of engagement patterns, audience behavior, and content performance on YouTube")

# ---------------- CATEGORY MAP ----------------
category_map = {
    1: "Film & Animation",
    2: "Autos & Vehicles",
    10: "Music",
    15: "Pets & Animals",
    17: "Sports",
    19: "Travel & Events",
    20: "Gaming",
    22: "People & Blogs",
    23: "Comedy",
    24: "Entertainment",
    25: "News & Politics",
    26: "How-to & Style",
    27: "Education",
    28: "Science & Technology"
}

# ---------------- FILTERS ----------------
st.sidebar.header("Filters")

country = st.sidebar.selectbox("Country", df['publish_country'].unique())
filtered_df = df[df['publish_country'] == country]

category = st.sidebar.selectbox("Category", filtered_df['category_id'].unique())
filtered_df = filtered_df[filtered_df['category_id'] == category]

sample_df = filtered_df.sample(min(2000, len(filtered_df)))

# =========================================================
# KEY CONCEPTS
# =========================================================
st.subheader("Key Concepts")

corr = filtered_df['views'].corr(filtered_df['likes'])
avg_eng = filtered_df['engagement_rate'].mean()

st.markdown(f"""
### Correlation (Views vs Likes)
Value: **{corr:.3f}**

This measures the relationship between video reach (views) and audience response (likes).

- Higher values indicate stronger alignment between visibility and engagement.
- Lower values indicate weak or inconsistent relationship.

---

### Engagement Rate
Average: **{avg_eng:.4f}**

This represents interaction per view.

Example:
- 0.03 ≈ 3 interactions per 100 views
""")

st.markdown("---")

# =========================================================
# VIEWS VS LIKES
# =========================================================
st.subheader("Views vs Likes Analysis")

fig, ax = plt.subplots()
ax.scatter(sample_df['views'], sample_df['likes'], alpha=0.25, s=10)
ax.set_xlabel("Views")
ax.set_ylabel("Likes")
st.pyplot(fig)

hi = sample_df.loc[sample_df['likes'].idxmax()]
lo = sample_df.loc[sample_df['likes'].idxmin()]

mean_likes = sample_df['likes'].mean()

outlier_idx = (sample_df['likes'] - mean_likes).abs().idxmax()
outlier_point = sample_df.loc[outlier_idx]

diff = outlier_point['likes'] - mean_likes
pct = (diff / mean_likes * 100) if mean_likes != 0 else 0

outlier_type = "HIGH-LYING OUTLIER" if diff > 0 else "LOW-LYING OUTLIER"

st.markdown(f"""
### Distribution Insights

Highest point:
- ({hi['views']:,}, {hi['likes']:,})

Lowest point:
- ({lo['views']:,}, {lo['likes']:,})

Outlier point:
- ({outlier_point['views']:,}, {outlier_point['likes']:,})

---

### Outlier Analysis

Average likes: {mean_likes:,.0f}  
Difference: {diff:+,.0f} likes  
Percentage deviation: {pct:.2f}%

Classification: **{outlier_type}**

Interpretation:
This point significantly deviates from normal dataset behavior, indicating unusual engagement relative to typical videos.
""")

# =========================================================
# CATEGORY PERFORMANCE
# =========================================================
st.subheader("Category Performance Analysis")

cat_data = filtered_df.groupby('category_id')['views'].mean()

fig, ax = plt.subplots()
cat_data.plot(kind='bar', ax=ax)
st.pyplot(fig)

overall_avg = df['views'].mean()
selected_avg = filtered_df['views'].mean()

st.markdown(f"""
### Category-Level Insights

Overall platform average views: {overall_avg:,.0f}  
Selected category average views: {selected_avg:,.0f}

This highlights how the selected content category performs relative to overall platform behavior within the chosen country.
""")

# =========================================================
# ENGAGEMENT RATE
# =========================================================
st.subheader("Engagement Rate Analysis")

fig, ax = plt.subplots()
ax.scatter(sample_df['views'], sample_df['engagement_rate'], alpha=0.25, s=10)
st.pyplot(fig)

hi_eng = sample_df.loc[sample_df['engagement_rate'].idxmax()]
lo_eng = sample_df.loc[sample_df['engagement_rate'].idxmin()]

st.markdown(f"""
### Engagement Distribution

Highest engagement:
- ({hi_eng['views']:,}, {hi_eng['engagement_rate']:.4f})

Lowest engagement:
- ({lo_eng['views']:,}, {lo_eng['engagement_rate']:.4f})

This reflects how actively users interact with content across different videos.
""")

# =========================================================
# DIAGNOSTIC INSIGHT
# =========================================================
st.subheader("Diagnostic Insight")

top_channel = filtered_df.groupby('channel_title')['views'].sum().idxmax()
best_video = filtered_df.sort_values(by='engagement_rate', ascending=False).iloc[0]

st.markdown(f"""
Top channel: **{top_channel}**  
Most engaging video: **{best_video['title']}**
""")

# =========================================================
# SUMMARY
# =========================================================
st.subheader("Summary of Findings")

avg_views = filtered_df['views'].mean()
avg_likes = filtered_df['likes'].mean()

st.markdown(f"""
### Performance Overview

- Average Views: {avg_views:,.0f}
- Average Likes: {avg_likes:,.0f}
- Correlation (Views vs Likes): {corr:.2f}
- Engagement Rate: {avg_eng:.4f}

### Key Observations

- Engagement is strongly influenced by content type and audience behavior.
- Views alone do not guarantee high engagement.
- Outliers indicate exceptional or underperforming content patterns.

### Conclusion

Within this dataset segment, content performance is primarily driven by engagement quality rather than raw visibility.
""")
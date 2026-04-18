import pandas as pd

# Load dataset
df = pd.read_csv("youtube.csv")

# Drop unnecessary columns
df = df.drop(columns=[
    'index',
    'video_id',
    'tags',
    'comments_disabled',
    'ratings_disabled',
    'video_error_or_removed'
], errors='ignore')

# Convert dates
df['publish_date'] = pd.to_datetime(df['publish_date'], errors='coerce')
df['trending_date'] = pd.to_datetime(df['trending_date'], errors='coerce')

# Remove missing values
df = df.dropna()

# Create new feature: Engagement Rate
df['engagement_rate'] = (df['likes'] + df['comment_count']) / df['views']

# Save cleaned data
df.to_csv("cleaned_youtube_data.csv", index=False)

print("✅ Data cleaned successfully!")
print(df.head())
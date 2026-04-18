YouTube Performance Analytics Case Study
Live link to the site of the analysis provided - https://dhruvaravikeerthi-youtube-performance-analytics-case-app-o0s0uj.streamlit.app/
Overview
This project is a data science case study that analyzes global YouTube trending video data to understand patterns in content performance. The study focuses on exploring how views, likes, engagement rate, and content categories influence video success across different countries.
The goal is to move beyond simple visualization and develop meaningful statistical and behavioral insights from real-world data.

Objective
The main objectives of this study are:
Analyze the relationship between views and likes using correlation
Measure audience engagement through engagement rate
Identify outliers in video performance data
Compare performance across different content categories
Understand country-wise differences in audience behavior
Dataset Information

Source: Kaggle – YouTube Trending Videos Dataset (The Devastator)

File Used: cleaned_youtube_data.csv

Key Features:
views
likes
category_id
publish_country
channel_title
engagement_rate
published_day_of_week

Methodology
 Correlation Analysis:
This measures how strongly views and likes are related.
A high correlation means videos with more views tend to receive more likes.
A low correlation indicates inconsistent engagement behavior.
 Engagement Rate:
Engagement rate is calculated as:
Engagement Rate = Likes / Views
This metric shows how actively users interact with a video relative to its reach.
Example interpretation:
0.03 means approximately 3 interactions per 100 views
Outlier Detection
Outliers are data points that significantly deviate from normal dataset behavior.
They can represent:
Extremely high-performing (viral) videos
Unusually low-performing videos
Outliers help identify exceptional content behavior that does not follow normal trends.
Category Performance Analysis
This analysis compares average video performance across YouTube content categories such as music, entertainment, sports, education, and others.
It helps identify which types of content generally perform better in terms of audience reach.

Key Findings
Views and likes show a strong positive correlation in most cases
Engagement rate is relatively low, indicating passive viewing behavior
A small number of videos act as strong outliers in the dataset
Content category significantly influences video performance
Audience behavior varies across countries and categories
Diagnostic Insights

The analysis identifies:
Top performing channels based on total views
Most engaging videos based on engagement rate
Distribution patterns across categories and countries
These insights help explain why certain videos perform significantly better than others.

Tools and Technologies:
Python
Pandas
NumPy
Matplotlib
Streamlit

Project Structure
YouTube Performance Analytics Case Study
│
├── app.py
├── clean_data.py
├── youtube.csv
├── cleaned_youtube_data.csv
└── README.md

Future Improvements
Time-series trend analysis for video performance over time
Predictive modeling for forecasting views and engagement
Clustering videos based on performance similarity
Deeper country-wise comparative analysis
Deployment as a full interactive analytics web application

What I Learned:

Through this project, I developed a stronger understanding of:
Data cleaning and preprocessing using pandas
Statistical analysis including correlation and distributions
Interpreting engagement metrics beyond raw numbers
Detecting and explaining outliers in datasets
Building interactive dashboards using Streamlit
Translating data patterns into meaningful insights

Conclusion
This case study demonstrates how data science can be used to understand real-world content performance on digital platforms. The focus is on interpreting engagement behavior, identifying meaningful patterns, and deriving insights that go beyond visualization.
The results highlight that engagement quality and content type play a more significant role in performance than raw view counts alone.

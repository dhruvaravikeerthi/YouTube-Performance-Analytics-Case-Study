## YouTube Performance Analytics Case Study

## Live link to the site of the analysis provided - 
https://dhruvaravikeerthi-youtube-performance-analytics-case-app-o0s0uj.streamlit.app/

## Overview
This project is a data science study that looks at YouTube trending video data from around the world. It tries to find patterns in how videos do. The study checks how views likes, engagement rate and video categories affect a videos success in countries.
The goal is to do more than just look at charts and find real insights from actual data.

## Objective

The main goals of this study are:
* Analyze how views and likes are related
* Measure how engaged the audience is
* Find videos that do well or poorly
* Compare how well different types of videos do
* Understand how audiences behave differently in various countries

## Dataset Information
Source: Kaggle – YouTube Trending Videos Dataset (The Devastator)
File Used: cleaned_youtube_data.csv
Key Features:
* views
* likes
* category_id
* publish_country
* channel_title
* engagement_rate
* published_day_of_week

## Methodology

### Correlation Analysis
This measures how strongly views and likes are connected. A high correlation means videos with views tend to get many likes. A low correlation means likes and views do not always go up and down together.

### Engagement Rate
Engagement rate is calculated as: Engagement Rate = Likes / Views. This shows how often users interact with a video compared to how many people see it.
 Example: 0.03 means about 3 interactions per 100 views

### Outlier Detection
Outliers are data points that're very different from the rest. They can be:
* Popular videos
* Videos that do poorly
* Outliers help find cases that do not follow normal patterns.

### Category Performance Analysis
This compares how well videos do across YouTube categories like music, entertainment, sports, education and others. It helps find which types of content usually do better.

## Key Findings
* Views and likes are strongly connected in cases
* Engagement rate is relatively low showing people often watch passively
* A few videos are outliers in the dataset
* The category of a video significantly affects how well it does
* Audience behavior varies across countries and categories

## Diagnostic Insights

The analysis finds:
* channels based on total views
* Engaging videos based on engagement rate
* How videos are distributed across categories and countries
* These insights help explain why some videos do better than others.

## Tools and Technologies
* Python
* Pandas
* NumPy
* Matplotlib
* Streamlit

## Future Improvements
* Time-series trend analysis for video performance over time
* Predictive modeling for forecasting views and engagement
* Clustering videos based on performance similarity
* Deeper country-wise comparative analysis
* Deployment as a full interactive analytics web application

## What I Learned
Through this project I gained an understanding of:
* Data cleaning and preprocessing using pandas
* Statistical analysis including correlation and distributions
* Interpreting engagement metrics beyond numbers
* Explaining outliers in datasets
* Building dashboards using Streamlit
* Translating data patterns into insights

# This case study shows how data science can be used to understand real-world content performance on digital platforms. The focus is on interpreting engagement behavior finding patterns and deriving insights that go beyond visualization.

The results highlight that engagement quality and content type play a significant role, in performance than just view counts.

## Author
Dhruva Ravi Keerthi

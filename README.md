# Vendor_Performance_DA
This project focuses on analyzing vendor sales performance using exploratory data analysis, statistical methods, and visualization techniques to uncover patterns and opportunities for strategic business improvement.

🔧 Tools & Technologies Used
Python (Pandas, NumPy) – Data cleaning, aggregation, and statistical summarization

Matplotlib & Seaborn – Visualizations and custom plots for trends and outliers

Scipy Stats – Confidence intervals, t-tests, and hypothesis testing

Jupyter Notebook – Interactive, step-by-step analysis and business storytelling

SQLite – Lightweight relational database for structured querying and joining datasets

📈 Key Insights
✅ 1. Top vs. Low Performing Vendors (Confidence Interval Analysis)

Used t-distribution-based confidence intervals to compare profit margins of top and low-performing vendors

Top Vendors: Showed higher average profit margins with narrower intervals, suggesting stable and efficient performance

Low Vendors: Had wider intervals and lower means, indicating inconsistency or possible pricing inefficiencies

✅ 2. Promotional Opportunity: Low Sales, High Margin Brands

Applied quantile-based segmentation to flag brands in the bottom 15% of sales but top 15% in profit margin

Identified high-margin but low-volume brands as strategic targets for marketing or pricing promotions

These brands can potentially boost overall revenue without compromising profitability

✅ 3. Visualizations & Plots

📌 Histogram with Confidence Intervals: Compared sales margin distributions of vendors using KDE curves + shaded CI

📌 Scatter Plot: Visualized all brands vs. target brands using sales and profit margin; highlighted opportunity zones

📌 Threshold Lines: Added sales and margin cutoffs using 15th and 85th percentiles for business clarity

✅ 4. Database Integration with SQLite

Structured .csv data was loaded and queried using SQLite for backend analysis

Performed SQL joins on vendor, sales, and product tables before passing cleaned data to Python

Helped in modularizing data sources, reducing memory usage, and improving overall data management

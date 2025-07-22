# Vendor_Performance_DA
This project focuses on analyzing vendor sales performance using exploratory data analysis, statistical methods, and visualization techniques to uncover patterns and opportunities for business improvement.

🔧 Tools & Technologies Used

Python (Pandas, NumPy) – Data cleaning, aggregation, statistical analysis

Matplotlib & Seaborn – Data visualizations and plots

Scipy Stats – Confidence intervals and hypothesis testing

Jupyter Notebook – Interactive analysis and visual storytelling



---

📈 Key Insights

✅ 1. Top vs. Low Performing Vendors (Confidence Interval Analysis)

Using t-distribution-based confidence intervals, we compared Top Vendors and Low Vendors on profit margins.

Top Vendors showed a higher mean profit margin with narrower confidence intervals, indicating consistent performance.

Low Vendors had lower mean margins and wider intervals, showing more variability and potential issues in pricing or strategy.


✅ 2. Promotional Opportunity: Low Sales, High Margin Brands

We identified brands with low total sales (bottom 15%) but high profit margins (top 15%) using scatter plots:

These brands are high-margin but underperforming in volume.

They are perfect candidates for marketing campaigns or pricing adjustments to drive growth without sacrificing profitability.


✅ 3. Visualizations & Plots

Histogram with Confidence Intervals: Compared distributions of Top vs. Low vendors using KDE and CI bands.

Scatter Plot: Highlighted target brands for strategic focus using sales vs. profit margin mapping.

Threshold Lines: Added quantile-based cutoffs to clearly differentiate target groups.

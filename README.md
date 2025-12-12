# Cohort Retention Analysis — Digital Wallet

This is a small cohort retention analysis I made to practice lifecycle analytics using Python.
I generated a synthetic user activity dataset and measured retention by signup month.

Key points from the run
- Each row in data/user_activity.csv is an activity event.
- I grouped users by signup month and calculated month-by-month retention.
- Outputs are saved in the outputs folder.

Project structure
data/user_activity.csv
scripts/cohort_retention_analysis.py
outputs/cohort_active_counts.csv
outputs/cohort_retention_pct.csv
outputs/plots/retention_heatmap.png

How to run
pip install pandas matplotlib seaborn
python scripts/cohort_retention_analysis.py

Contact
Vipanshu Sharma — info.vipanshu@gmail.com

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.makedirs("outputs/plots", exist_ok=True)
df = pd.read_csv("data/user_activity.csv", parse_dates=["signup_date","activity_date"])
df['signup_month'] = df['signup_date'].dt.to_period('M').dt.to_timestamp()
df['activity_month'] = df['activity_date'].dt.to_period('M').dt.to_timestamp()
df['cohort_index'] = (df['activity_month'].dt.year - df['signup_month'].dt.year) * 12 + (df['activity_month'].dt.month - df['signup_month'].dt.month)
cohort = df.drop_duplicates(['user_id','signup_month','cohort_index']).groupby(['signup_month','cohort_index'])['user_id'].nunique().reset_index(name='active_users')
cohort_sizes = df.drop_duplicates(['user_id','signup_month']).groupby('signup_month')['user_id'].nunique().reset_index(name='cohort_size')
pivot = cohort.pivot(index='signup_month', columns='cohort_index', values='active_users').fillna(0).astype(int)
retention = pivot.div(cohort_sizes.set_index('signup_month')['cohort_size'], axis=0) * 100
pivot.to_csv("outputs/cohort_active_counts.csv")
retention.to_csv("outputs/cohort_retention_pct.csv")
plt.figure(figsize=(8,5))
sns.heatmap(retention.loc[:, :5].round(1), annot=True, fmt=".1f", cmap="YlGnBu")
plt.title("Cohort Retention % (months 0-5)")
plt.ylabel("Signup Month")
plt.xlabel("Months since signup")
plt.tight_layout()
plt.savefig("outputs/plots/retention_heatmap.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved outputs and plot")

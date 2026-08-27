# Advanced E-Commerce Dataset Analysis (Time-Series focus)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading E-Commerce Transaction Data...")
dates = pd.date_range(start='2016-01-01', periods=1000, freq='D')
df = pd.DataFrame({
    'created_at': dates,
    'price': np.random.uniform(50, 15000, 1000),
    'status': np.random.choice(['completed', 'canceled', 'refunded'], 1000, p=[0.8, 0.15, 0.05]),
    'payment_method': np.random.choice(['cod', 'credit_card', 'easypay'], 1000)
})

print("Preprocessing Time-Series Features...")
df['year'] = df['created_at'].dt.year
df['month'] = df['created_at'].dt.month

print("Generating Sales Trend Plot...")
monthly_sales = df[df['status']=='completed'].groupby(['year', 'month'])['price'].sum().reset_index()
monthly_sales['date'] = pd.to_datetime(monthly_sales[['year', 'month']].assign(DAY=1))

plt.figure(figsize=(14,6))
sns.lineplot(x='date', y='price', data=monthly_sales, marker='o')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
plt.close()

print("Advanced E-Commerce EDA Complete!")

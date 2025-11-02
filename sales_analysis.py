# Simple Sales Analysis Project
import pandas as pd
import matplotlib.pyplot as plt

# Create sample sales data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [12000, 15000, 18000, 9000, 21000, 19000],
    'Region': ['North', 'South', 'North', 'East', 'West', 'South']
}

# Create DataFrame
df = pd.DataFrame(data)
print("=== SALES DATA ===")
print(df)

# Basic analysis
print("\n=== ANALYSIS RESULTS ===")
print(f"Total Sales: ${df['Sales'].sum():,}")
print(f"Average Sales: ${df['Sales'].mean():,.2f}")
print(f"Best Month: {df.loc[df['Sales'].idxmax(), 'Month']}")
print(f"Highest Sales: ${df['Sales'].max():,}")

# Sales by region
region_sales = df.groupby('Region')['Sales'].sum()
print("\n=== SALES BY REGION ===")
print(region_sales)

# Create visualization
plt.figure(figsize=(10, 5))

# Plot 1: Monthly sales trend
plt.subplot(1, 2, 1)
plt.plot(df['Month'], df['Sales'], marker='o', linewidth=2, markersize=8)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True, alpha=0.3)

# Plot 2: Sales by region
plt.subplot(1, 2, 2)
region_sales.plot(kind='bar', color=['skyblue', 'lightgreen', 'orange', 'pink'])
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('sales_results.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Analysis complete! Check 'sales_results.png' for charts.")
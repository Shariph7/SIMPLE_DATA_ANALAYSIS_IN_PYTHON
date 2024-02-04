# Importing Neccessary Modules! for simple data analaysis.
import pandas as pd
import matplotlib.pyplot as plt

# Reading CSV FILES USING read_csv functions.
Data = pd.read_csv('Details.csv')
print(Data.head()) # Gives Informations of first 5 rows of the Csv files.
# print(Data.tail()) # Gives Informations of last 5 rows of the CSV files.

# Analayzing the Amounts and the Profits.
total_amounts = Data.groupby('Category')['Amount'].sum().sort_values(ascending=False)
total_profits = Data.groupby('Category')['Profit'].sum().sort_values(ascending=False)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Total Sales By Category
total_amounts.plot(kind='bar',ax=axes[0],color='blue')
axes[0].set_title('AMOUNT')
axes[0].set_xlabel('Category')
axes[0].set_ylabel('Total Amounts')

# Total Profit by Category
total_profits.plot(kind='bar',ax=axes[1],color='purple')
axes[1].set_title('Total Profits')
axes[1].set_xlabel("Cateogry")
axes[1].set_ylabel('Total Profits')

plt.tight_layout()
plt.show()


# Quantity Sold by Category
total_quantity_category = Data.groupby('Category')['Quantity'].sum().sort_values(ascending=False)

# Average Profit Margin by Category
Data['Profit Margin'] = (Data['Profit'] / Data['Amount']) * 100
average_profit_margin_category = Data.groupby('Category')['Profit Margin'].mean().sort_values(ascending=False)

# Payment Mode Analysis
payment_mode_counts = Data['PaymentMode'].value_counts()

# Sub-Category Analysis
total_sales_subcategory = Data.groupby('Sub-Category')['Amount'].sum().sort_values(ascending=False)
total_profit_subcategory = Data.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)

# Plotting
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(18, 12))

# Quantity Sold by Category
total_quantity_category.plot(kind='bar', ax=axes[0, 0], color='lightcoral')
axes[0, 0].set_title('Quantity Sold by Category')
axes[0, 0].set_xlabel('Category')
axes[0, 0].set_ylabel('Total Quantity Sold')

# Average Profit Margin by Category
average_profit_margin_category.plot(kind='bar', ax=axes[0, 1], color='salmon')
axes[0, 1].set_title('Average Profit Margin by Category')
axes[0, 1].set_xlabel('Category')
axes[0, 1].set_ylabel('Average Profit Margin (%)')

# Payment Mode Analysis
payment_mode_counts.plot(kind='bar', ax=axes[1, 0], color='skyblue')
axes[1, 0].set_title('Payment Mode Analysis')
axes[1, 0].set_xlabel('Payment Mode')
axes[1, 0].set_ylabel('Count')

# Sub-Category Analysis
total_sales_subcategory.plot(kind='bar', ax=axes[1, 1], color='lightgreen')
total_profit_subcategory.plot(kind='line', ax=axes[1, 1], color='darkgreen', secondary_y=True)
axes[1, 1].set_title('Total Sales and Profit by Sub-Category')
axes[1, 1].set_xlabel('Sub-Category')
axes[1, 1].set_ylabel('Total Sales')
axes[1, 1].right_ax.set_ylabel('Total Profit')

plt.tight_layout()
plt.show()

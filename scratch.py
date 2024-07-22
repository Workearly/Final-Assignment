import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
df = pd.read_csv(r"C:\Users\venic\Desktop\DIMITRIS\years16to19.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Find the most popular item per zipcode
popular_items = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum().reset_index()
most_popular_items = popular_items.loc[popular_items.groupby('zip_code')['bottles_sold'].idxmax()]

# Calculate the percentage of sales per store
total_sales = df['sale_dollars'].sum()
sales_per_store = df.groupby('store_number')['sale_dollars'].sum().reset_index()
sales_per_store['percentage_of_sales'] = (sales_per_store['sale_dollars'] / total_sales) * 100

# Print results
print("Most popular items per zipcode:\n", most_popular_items)
print("\nPercentage of sales per store:\n", sales_per_store)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Bar plot of the most popular items per zipcode
plt.figure(figsize=(12, 6))
bar_plot = sns.barplot(data=most_popular_items, x='zip_code', y='bottles_sold', hue='zip_code', dodge=False, palette='viridis', legend=False)
# Adding title and labels
bar_plot.set_title('Most Popular Items per Zipcode (2016-2019)', fontsize=16)
bar_plot.set_xlabel('Zipcode', fontsize=14)
bar_plot.set_ylabel('Bottles Sold', fontsize=14)
# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
# Display the plot
plt.show()


# Calculate explode values
explode_values = [0.1 if value > 10 else 0 for value in sales_per_store['percentage_of_sales']]
# Pie chart of sales per store
plt.figure(figsize=(10, 10))
pie_chart = sales_per_store.set_index('store_number')['percentage_of_sales'].plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('viridis', len(sales_per_store)),
    explode=explode_values,
    legend=True
)
# Adding title
plt.title('Percentage of Sales per Store (2016-2019)', fontsize=16)
# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
# Display the legend outside the pie chart
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
# Remove y-axis label for cleaner look
plt.ylabel('')
# Display the plot
plt.show()
import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.image('https://cdn4.vectorstock.com/i/1000x1000/65/83/bicycle-stores-exterior-or-bike-shops-interior-vector-16226583.jpg')
st.title('DATA ANALYISIS')
st.header('BIKE STORE')
st.subheader('import Data')
st.code('pd.DataFrame(df)')

df=pd.read_csv("Bike store.csv")
st.write("## Bike Store DataFrame")
st.dataframe(df)
st.write("## DataFrame Shape")
st.write(f"Number of rows: {df.shape[0]}")
st.write(f"Number of columns: {df.shape[1]}")
st.write("## DataFrame Information")
st.write(df.info())
mean_age = df['Customer_Age'].mean()
st.write("## Mean Customer Age")
st.write(f"Mean: {mean_age}")
st.write("## Customer Age Density Plot")
# Create a figure and axis using seaborn
# Plot horizontal boxplot without seaborn
st.write("## Customer Age Boxplot")

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 4))

# Plot the boxplot
boxplot = ax.boxplot(df['Customer_Age'], vert=False, patch_artist=True, widths=0.7, boxprops=dict(facecolor='lightcoral'))

# Customize the plot if needed
ax.set_xlabel('Customer Age')

# Show the plot
st.pyplot(fig)
fig, ax = plt.subplots(figsize=(14, 6))

# Plot the density
df['Customer_Age'].plot(kind='density', label="", ax=ax)

# Add mean and median lines
mean_age = df['Customer_Age'].mean()
median_age = df['Customer_Age'].median()
ax.axvline(mean_age, color='orange', linestyle='dashed', linewidth=2, label=f'Mean ({mean_age})')
ax.axvline(median_age, color='green', linestyle='dashed', linewidth=2, label=f'Median ({median_age})')

# Show legend and plot
ax.legend()
st.pyplot(fig)
st.write("## Mean Order Quantity")
mean_order_quantity = df['Order_Quantity'].mean()
st.write(f"The mean order quantity is: {mean_order_quantity}")
st.write("## Order Quantity Histogram")
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the histogram
df['Order_Quantity'].plot(kind='hist', color='brown', ax=ax)
plt.title('Order Quantity', fontsize=20, color='blue')

# Show the plot using Streamlit
st.pyplot(fig)
st.write("## Order Quantity Boxplot")

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the boxplot
boxplot = ax.boxplot(df['Order_Quantity'], vert=False, patch_artist=True, widths=0.4, boxprops=dict(facecolor='purple'))

# Customize the plot if needed
plt.title('Order Quantity', fontsize=20, color='blue')

# Show the plot using Streamlit
st.pyplot(fig)
st.write("## Bike Store DataFrame")
st.dataframe(df)

# Calculate the sum of 'Order_Quantity' grouped by 'Year'
sales_year = df.groupby('Year')['Order_Quantity'].sum()

# Display the result
st.write("## Sales per Year")
st.write(sales_year)
sales_age_group = df.groupby('Age_Group')['Order_Quantity'].sum()

# Plot pie chart for sales per age group using Streamlit
st.write("## Sales per Age Group Pie Chart")

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the pie chart
sales_age_group.plot(kind="pie", label="", colors=("olive", "orange", "pink", "salmon", "gray"),
                     autopct='%1.1f%%', startangle=90, explode=[0.1, 0, 0, 0], ax=ax)
plt.title('Sales per Age Group', fontsize=20, color='green')
st.pyplot(fig)
sales_per_customer_age = df.groupby('Customer_Age')['Order_Quantity'].sum().reset_index()

# Create a Streamlit app
st.title('Sales per Customer Age')

# Plot the line chart using matplotlib within Streamlit
fig, ax = plt.subplots()
ax.plot(sales_per_customer_age['Customer_Age'], sales_per_customer_age['Order_Quantity'], marker='o', linestyle='-')
ax.set_xlabel('Customer Age')
ax.set_ylabel('Total Order Quantity')
ax.set_title('Sales per Customer Age', fontsize=20, color='green')

sales_month = df.groupby('Month')['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Sales per Month')

# Plot the bar chart using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(sales_month.index, sales_month.values, color='green')  # Use index and values to extract data
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales', fontsize=12)
ax.set_title('Sales per Month', fontsize=25, color='sienna')

# Display the plot in the Streamlit app
st.pyplot(fig)
st.slider('data')
sales_per_country = df.groupby('Country')['Order_Quantity'].sum().reset_index()

# Create a Streamlit app
st.title('Sales per Country')

# Plot the bar chart using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(sales_per_country['Country'], sales_per_country['Order_Quantity'], color='skyblue')
ax.set_xlabel('Country', fontsize=16)
ax.set_ylabel('Sales', fontsize=16)
ax.set_title('Sales per Country', fontsize=25, color='purple')

# Display the plot in the Streamlit app
st.pyplot(fig)
st.title('Product Category Analysis')
result_series = df.groupby("Product_Category")['Order_Quantity'].sum()

# Create a Streamlit app
result_series = df.groupby("Product_Category")['Order_Quantity'].sum()

# Convert the result to a list
result_list = result_series.tolist()

# Create a Streamlit app
st.title('Product Category Analysis')

# Display the result list
st.write(f'Total Order Quantity per Product Category: {result_list}')

# Plot the pie chart using matplotlib within Streamlit
fig_pie, ax_pie = plt.subplots(figsize=(8, 8))
df.groupby("Product_Category")['Order_Quantity'].sum().plot(
    kind="pie", autopct='%1.1f%%', explode=[0.1, 0, 0], colors=("olive", "orange", "pink"), ax=ax_pie
)
ax_pie.set_title('Distribution of Products in Categories', fontsize=20, color='green')

# Display the pie chart in the Streamlit app
st.pyplot(fig_pie)
product_sales = df.groupby("Product")['Order_Quantity'].sum()
top_10_products = product_sales.nlargest(10)

# Create a Streamlit app
st.title('Top 10 Products by Sales')

# Plot the bar chart using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(top_10_products.index, top_10_products.values, color='purple')
ax.set_xlabel('Product', fontsize=16)
ax.set_ylabel('Total Order Quantity', fontsize=16)
ax.set_title('Top 10 Products by Sales', fontsize=25, color='purple')
plt.xticks(rotation='vertical')  # Rotate x-axis labels vertically

# Display the plot in the Streamlit app
st.pyplot(fig)

# Assuming df is a DataFrame with 'Unit_Cost' and 'Unit_Price' columns

# Create a Streamlit app
st.title('Relationship between Unit Cost and Unit Price')

# Plot the scatter plot using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['Unit_Cost'], df['Unit_Price'], color='purple', marker='o')
ax.set_xlabel('Unit Cost')
ax.set_ylabel('Unit Price')
ax.set_title('Relationship between Unit Cost and Unit Price')

# Display the plot in the Streamlit app
st.pyplot(fig)
# Determine and display the correlation type
st.title('Correlation Analysis')

# Calculate the correlation coefficient
correlation_coefficient = df['Unit_Cost'].corr(df['Unit_Price'])
st.write(f'Correlation Coefficient: {correlation_coefficient}')
if correlation_coefficient > 0:
    st.write('Positive Correlation: As Unit_Price increases, Unit_Cost tends to increase.')
elif correlation_coefficient < 0:
    st.write('Negative Correlation: As Unit_Price increases, Unit_Cost tends to decrease.')
else:
    st.write('No Correlation: There is no clear trend between Unit_Price and Unit_Cost.')
    st.title('Relationship between Order Quantity and Profit')

# Plot the scatter plot using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['Order_Quantity'], df['Profit'], color='green', marker='o')
ax.set_xlabel('Order Quantity', fontsize=14)
ax.set_ylabel('Profit', fontsize=14)
ax.set_title('Relationship between Order Quantity and Profit')

# Display the plot in the Streamlit app
st.pyplot(fig)
st.title('Correlation Analysis')

# Calculate the correlation coefficient
correlation_coefficient = df['Order_Quantity'].corr(df['Profit'])

# Display the correlation coefficient
st.write(f'Correlation Coefficient: {correlation_coefficient}')

# Plot a scatter plot with regression line
fig, ax = plt.subplots(figsize=(10, 6))
sns.regplot(x='Order_Quantity', y='Profit', data=df, color='green', marker='o', ax=ax)
ax.set_xlabel('Order Quantity', fontsize=14)
ax.set_ylabel('Profit', fontsize=14)
ax.set_title('Relationship between Order Quantity and Profit')

# Display the plot in the Streamlit app
st.pyplot(fig)

# Determine and display the correlation type
if correlation_coefficient > 0:
    st.write('Positive Correlation: As Order Quantity increases, Profit tends to increase.')
elif correlation_coefficient < 0:
    st.write('Negative Correlation: As Order Quantity increases, Profit tends to decrease.')
else:
    st.write('No Correlation: There is no clear trend between Order Quantity and Profit.')
st.title('Profit Distribution by Country')

# Plot the boxplot using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(14, 8))
df.boxplot(column='Profit', by='Country', ax=ax)
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('Profit', fontsize=14)
ax.set_title('Profit Distribution by Country')

# Rotate x-axis labels vertically
plt.xticks(rotation='vertical')

# Display the plot in the Streamlit app
st.pyplot(fig)   
st.title('Customer Age Distribution by Country')

# Plot the boxplot using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(14, 8))
df.boxplot(column='Customer_Age', by='Country', ax=ax)
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('Customer Age', fontsize=14)
ax.set_title('Customer Age Distribution by Country')

# Rotate x-axis labels vertically
plt.xticks(rotation='vertical')

# Display the plot in the Streamlit app
st.pyplot(fig)
df['Calculated_Date'] = df[['Year', 'Month', 'Day']].apply(lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)

# Display the DataFrame and the new column in the Streamlit app
st.title('Calculated Date Example')
st.write('Original DataFrame:')
st.write(df)

st.write('\nDataFrame with Calculated_Date:')
st.write(df[['Year', 'Month', 'Day', 'Calculated_Date']])
df['Calculated_Date'] = df[['Year', 'Month', 'Day']].apply(lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)

# Convert 'Calculated_Date' to datetime format
df['Calculated_Date'] = pd.to_datetime(df['Calculated_Date'])

# Display the DataFrame with the datetime column in the Streamlit app
st.title('Calculated Date Example with Datetime')
st.write('Original DataFrame:')
st.write(df[['Year', 'Month', 'Day']])

st.write('\nDataFrame with Calculated_Date as Datetime:')
st.write(df[['Year', 'Month', 'Day', 'Calculated_Date']])
sales_year = df.groupby('Year')['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Sales per Year')

# Plot the sales per year using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(10, 6))
sales_year.plot(ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Total Order Quantity')
ax.set_title('Sales per Year')

# Display the plot in the Streamlit app
st.pyplot(fig)
Revenue_rate=df['Revenue']=df['Revenue']+50
Revenue_rate
filtered_country = df[df['Country'] == 'France']

# Calculate the total 'Order_Quantity' for France
total_order_quantity_france = filtered_country['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Order Quantity for France')

# Display the total order quantity for France
st.write(f'Total Order Quantity for France: {total_order_quantity_france}')
filtered_country = df[df['Country'] == 'Canada']

# Calculate the total 'Order_Quantity' for Canada
total_order_quantity_canada = filtered_country['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Order Quantity for Canada')
target_country = 'France'

filtered_country = df[df['Country'] == target_country]

# Group by 'State' and calculate total 'Order_Quantity' for each state
data = filtered_country.groupby('State')['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Order Quantity (state in France)')

# Display the grouped data by state
st.bar_chart(data, use_container_width=True)

# Additional information
st.write(f'Total Order Quantity for {target_country}: {filtered_country["Order_Quantity"].sum()}')
product_order_quantity = df.groupby('Product')['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Total Order Quantity per Product')

# Display the grouped data in the Streamlit app
st.write('Grouped Data:')
sub_category_order_quantity = df.groupby('Sub_Category')['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Sales per Sub-Category')

# Plot the bar chart using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(10, 6))
sub_category_order_quantity.plot(kind='bar', ax=ax, label='', title='Sales per Sub-Category', color='teal')
ax.set_xlabel('Sub-Category')
ax.set_ylabel('Total Order Quantity')

# Display the plot in the Streamlit app
st.pyplot(fig)
target_product = 'Bikes'

# Filter the DataFrame for the target product category
filtered_product_category = df[df['Product_Category'] == target_product]

# Group by 'Sub_Category' and calculate total 'Order_Quantity' for each sub-category
sub_category_order_quantity = filtered_product_category.groupby('Sub_Category')['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Sales per Bike Sub-Categories')

# Plot the pie chart using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(8, 8))
sub_category_order_quantity.plot(kind='pie', colors=('violet', 'teal', 'magenta'),
                                  label='', title=f'Sales per {target_product} Sub-Categories',
                                  autopct='%1.1f%%', explode=[0, 0.1, 0], ax=ax)

# Display the plot in the Streamlit app
st.pyplot(fig)
# Group by 'Customer_Gender' and calculate total 'Order_Quantity' for each gender
sales_per_gender = df.groupby('Customer_Gender')['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Sales per Gender')

# Display the grouped data in the Streamlit app
st.write('Sales per Gender:')
st.write(sales_per_gender)
filtered_sales = df.loc[(df['Revenue'] > 500) & (df['Customer_Gender'] == 'M')].shape[0]

# Create a Streamlit app
st.title('Filtered Sales')

# Display the number of filtered sales in the Streamlit app
st.write(f'Number of Sales where Revenue > 500 and Customer Gender is Male: {filtered_sales}')
top_5_products = df.groupby('Product')['Revenue'].sum().nlargest(5)

# Create a Streamlit app
st.title('Top 5 Products by Revenue')

# Display the top 5 products and their total revenue in the Streamlit app
st.write('Top 5 Products:')
st.write(top_5_products)
top_category_by_revenue = df.groupby('Product_Category')['Revenue'].sum().nlargest(1)

# Create a Streamlit app
st.title('Top Product Category by Revenue')

# Display the top product category and its total revenue in the Streamlit app
st.write('Top Product Category:')
st.write(top_category_by_revenue)
high_revenue_orders = df[df['Revenue'] > 10000]

# Calculate the mean 'Order_Quantity' for these high-revenue orders
mean_order_quantity = high_revenue_orders['Order_Quantity'].mean()

# Create a Streamlit app
st.title('Mean Order Quantity for High-Revenue Orders')

# Display the mean 'Order_Quantity' in the Streamlit app
st.write(f'Mean Order Quantity for High-Revenue Orders: {mean_order_quantity:.2f}')
# Filter the DataFrame for orders with revenue less than $1000
low_revenue_orders = df[df['Revenue'] < 1000]

# Calculate the mean 'Order_Quantity' for these low-revenue orders
mean_order_quantity = low_revenue_orders['Order_Quantity'].mean()

# Create a Streamlit app
st.title('Mean Order Quantity for Low-Revenue Orders')

# Display the mean 'Order_Quantity' in the Streamlit app
st.write(f'Mean Order Quantity for Low-Revenue Orders: {mean_order_quantity:.2f}')
# Filter the DataFrame for orders with dates between May 1, 2016, and June 1, 2016
selected_date_orders = df[(df['Date'] >= '2016-05-01') & (df['Date'] < '2016-06-01')]

# Calculate the sum of 'Order_Quantity' for these selected date orders
total_order_quantity = selected_date_orders['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Total Order Quantity for Selected Date Range')

# Display the total 'Order_Quantity' in the Streamlit app
st.write(f'Total Order Quantity for selected date range: {total_order_quantity}')
# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter the DataFrame for orders with dates between May 1, 2016, and August 1, 2016
selected_date_orders = df[(df['Date'] > '2016-05-01') & (df['Date'] < '2016-08-01')]

# Calculate the sum of 'Order_Quantity' for these selected date orders
total_order_quantity = selected_date_orders['Order_Quantity'].sum()

# Create a Streamlit app
st.title('Total Order Quantity for Selected Date Range')

# Display the total 'Order_Quantity' in the Streamlit app
st.write(f'Total Order Quantity for selected date range: {total_order_quantity}')
month_per_profit = df.groupby('Month')['Profit'].sum()

# Create a Streamlit app
st.title('Total Profit per Month')

# Display the total 'Profit' for each month in the Streamlit app
st.write('Total Profit per Month:')
st.write(month_per_profit)
st.title('Boxplot of Profit by Month')

# Plot the boxplot using matplotlib within Streamlit
fig, ax = plt.subplots(figsize=(10, 6))
df.boxplot(by='Month', column='Profit', ax=ax)
plt.xticks(rotation='vertical')

# Display the plot in the Streamlit app
st.pyplot(fig)
# Set the target country and tax rate
target_country = 'United States'
tax_rate = 0.072

# Create a Streamlit app
st.title('Calculate Unit_Price_with_tax')

# Calculate 'Unit_Price_with_tax' based on the specified conditions
df['Unit_Price_with_tax'] = df.apply(
    lambda row: row['Unit_Price'] * (1 + tax_rate) if row['Country'] == target_country else row['Unit_Price'],
    axis=1
)

# Display the DataFrame with the new 'Unit_Price_with_tax' column in the Streamlit app
st.write(df)

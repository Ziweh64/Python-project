import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
df = pd.read_csv('AirPassengers.csv')

# Display basic information about the dataset
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

#Data Cleaning
print("\nMissing Values in each column:")
print(df.isnull().sum())  # Checking for missing values

# Dropping missing values (if any)
df_cleaned = df.dropna()

# Checking for duplicates
print("\nChecking for duplicates:")
print(df_cleaned.duplicated().sum())  # No duplicates

# Removing any duplicates (if any)
df_cleaned = df_cleaned.drop_duplicates()

# Checking data types
print("\nData Types of each column:")
print(df_cleaned.dtypes)

#Convert the 'Month' column to datetime
df_cleaned['Month'] = pd.to_datetime(df_cleaned['Month'])

# Create a new column for 'Year'
df_cleaned['Year'] = df_cleaned['Month'].dt.year

# Visualizing the trend over time (line plot with styling)
plt.figure(figsize=(12, 6))
plt.plot(df_cleaned['Month'], df_cleaned['#Passengers'], marker='o', color='teal', linestyle='-', linewidth=2, markersize=5, label='Passengers')
plt.title('Number of Passengers Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Passengers', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(loc='upper left', fontsize=12)
plt.tight_layout()
plt.show()

# Visualizing total passengers per year (styled bar plot)
passengers_per_year = df_cleaned.groupby('Year')['#Passengers'].sum()

plt.figure(figsize=(10, 6))
sns.barplot(x=passengers_per_year.index, y=passengers_per_year.values, palette='Blues_d')
plt.title('Total Passengers per Year', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Passengers', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# Moving average (12 months) with improved styling
df_cleaned['Moving_Avg'] = df_cleaned['#Passengers'].rolling(window=12).mean()

plt.figure(figsize=(12, 6))
plt.plot(df_cleaned['Month'], df_cleaned['#Passengers'], label='Monthly Passengers', alpha=0.7, color='skyblue', linewidth=2)
plt.plot(df_cleaned['Month'], df_cleaned['Moving_Avg'], label='12-Month Moving Average', color='red', linestyle='--', linewidth=3)
plt.title('Monthly Passengers with 12-Month Moving Average', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Passengers', fontsize=12)
plt.xticks(rotation=45)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# Reporting findings
print("\n### Findings Summary ###")
print("- The dataset contains monthly data on airline passengers between 1949 and 1960.")
print("- No missing values or duplicates were found in the dataset after cleaning.")
print("- The number of passengers steadily increased over the years, indicating growth in air travel.")
print("- The 12-month moving average shows trends while smoothing out seasonal fluctuations.")


import pandas as pd

# Load the dataset (replace 'path_to_file.csv' with your actual file path)
unemployment_data = pd.read_csv('Unemployment in India.csv')

# Display the first few rows of the dataset
print(unemployment_data.head())
# Check the structure of the dataset
print(unemployment_data.info())

# Check for missing values
print(unemployment_data.isnull().sum())

# Get descriptive statistics
print(unemployment_data.describe())
# Example: Drop rows with missing values
unemployment_data.dropna(inplace=True)

# Convert date column to datetime format if necessary
unemployment_data['Date'] = pd.to_datetime(unemployment_data['Date'])

# Check the cleaned data
print(unemployment_data.info())
import matplotlib.pyplot as plt

# Plotting the unemployment rate over time
plt.figure(figsize=(12, 6))
plt.plot(unemployment_data['Date'], unemployment_data['Unemployment_Rate'], marker='o')
plt.title('Unemployment Rate Over Time During Covid-19')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
# Example: Group by age or gender if such columns exist
if 'Age_Group' in unemployment_data.columns:
    demographic_analysis = unemployment_data.groupby('Age_Group')['Unemployment_Rate'].mean()
    demographic_analysis.plot(kind='bar')
    plt.title('Average Unemployment Rate by Age Group')
    plt.ylabel('Unemployment Rate (%)')
    plt.show()
    # Correlation matrix
    correlation_matrix = unemployment_data.corr()
    print(correlation_matrix)

    # Visualize the correlation matrix
    import seaborn as sns

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
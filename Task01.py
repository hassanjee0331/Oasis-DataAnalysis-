import pandas as pd


# Load the dataset
url = "B:\python\oasisinfobyte\pythonProject1/iris.csv"  # Update this path
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data = pd.read_csv(url, header=None, names=column_names)

# Display the first few rows of the dataset
print(iris_data.head())


from sklearn.preprocessing import LabelEncoder

# Encode the species labels
label_encoder = LabelEncoder()
iris_data['species'] = label_encoder.fit_transform(iris_data['species'])

print("Original labels:", iris_data)
print("Encoded labels:",iris_data)

from sklearn.model_selection import train_test_split

# Features and labels
X = iris_data.drop('species', axis=1)
y = iris_data['species']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_test)
print(X_train)
print(y_test)
print(y_train)


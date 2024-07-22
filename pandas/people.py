import pandas as pd

# Read data from CSV file
df = pd.read_csv('peopledata.csv')

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print("Average age: ",average_age)
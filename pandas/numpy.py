import numpy as np
import pandas as pd

# Load data from CSV into a pandas DataFrame
df = pd.read_csv('peopledata.csv')

# Convert DataFrame to numpy array
data = df.to_numpy()

# Display the numpy array
print("Numpy Array:")
print(data)

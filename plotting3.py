import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
crime_data = pd.read_csv('visakhapatnam_crime_data.csv')

# Count the frequency of each crime type
crime_counts = crime_data['Crime_Type'].value_counts()

# Create a bar chart
plt.figure(figsize=(10, 6))
crime_counts.plot(kind='bar', color='skyblue')
plt.title('Frequency of Crime Types')
plt.xlabel('Crime Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

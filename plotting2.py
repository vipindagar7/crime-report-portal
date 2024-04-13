import folium
import pandas as pd

# Load the CSV file into a DataFrame
crime_data = pd.read_csv('visakhapatnam_crime_data.csv')

# Create a map centered at Visakhapatnam
visakhapatnam_map = folium.Map(location=[17.6868, 83.2185], zoom_start=12)

# Define marker colors for each crime type
crime_colors = {
    'Violent crimes': 'red',
    'Property crimes': 'blue',
    'Financial Crimes': 'green',
    'Drug-Related': 'orange',
    'Cyber crimes': 'purple',
    'Domestic Violence': 'pink',
    'Human Trafficking': 'black'
}

# Add markers for each crime incident
for index, row in crime_data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Crime_Type'],
        icon=folium.Icon(color=crime_colors.get(row['Crime_Type'], 'gray'), icon='info-sign')
    ).add_to(visakhapatnam_map)

# Save the map to an HTML file
visakhapatnam_map.save('visakhapatnam_crime_map.html')

print("Map created successfully!")

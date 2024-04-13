from django.shortcuts import render , HttpResponse
from nbconvert import HTMLExporter
import nbformat
from io import BytesIO


# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def support(request):
    
    return render(request, 'support.html')



import pandas as pd
from sklearn.cluster import KMeans
import folium



def chart(request):
    # Load your crime data (replace 'your_data.csv' with your actual file)
    crime_data = pd.read_csv('crime.csv')
    crime_data = crime_data.dropna()
    # Select relevant features for clustering (e.g., latitude, longitude, and primary type)
    X = crime_data[['Latitude', 'Longitude']]

    # Add one-hot encoding for the 'Primary Type' column
    X = pd.concat([X, pd.get_dummies(crime_data['Primary Type'], prefix='Type')], axis=1)

    # Train the K-means model with the optimal number of clusters
    k = 2  # Replace with your chosen number of clusters
    kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)

    # Add cluster labels to the original DataFrame
    crime_data['Cluster'] = kmeans.labels_

    # Create a folium map centered around the average latitude and longitude
    map_center = [crime_data['Latitude'].mean(), crime_data['Longitude'].mean()]
    crime_map = folium.Map(location=map_center, zoom_start=12)

    # Add markers for each crime incident with cluster color
    for index, row in crime_data.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,
            color='red' if row['Cluster'] == 0 else 'blue',  # Adjust colors based on your clusters
            fill=True,
            fill_color='red' if row['Cluster'] == 0 else 'blue',
            fill_opacity=0.6
        ).add_to(crime_map)

    # Save the map as an HTML file or display it
    chart = crime_map.save('templates/crime_map.html')
    return render(request, 'crime_map.html')
    # Alternatively, you can display the map in a Jupyter Notebook using:
    # crime_map
    
    
def charts(request):
    
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
    visakhapatnam_map.save('templates/visakhapatnam_crime_map.html')
    return render(request, 'visakhapatnam_crime_map.html')

    
    
def bar_chart(request):
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

    # Save plot image in memory
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    
    return HttpResponse(buffer.getvalue(), content_type='image/png')
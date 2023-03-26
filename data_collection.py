# STAGE 1
# SCRAPE AND STORE DATA

# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape
url = 'https://www.naturabuy.fr/Munitions-Balles-22LR-cat-884.html'

# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the offers on the page
offers = soup.find_all('div', class_='BlocVente')

# Create an empty list to store the data
data = []

# Loop through each offer and extract the desired information
for offer in offers:
    # Extract the item name
    item_name = offer.find('a', class_='TitreVente').text.strip()
    
    # Extract the quantity of bullets
    quantity = offer.find('span', class_='Qte').text.strip()
    
    # Extract the price
    price = offer.find('div', class_='Prix').text.strip()
    
    # Extract the delivery price
    delivery_price = offer.find('div', class_='Livraison').text.strip()
    
    # Append the data for this offer to the list
    data.append([item_name, quantity, price, delivery_price])

# Create a pandas DataFrame from the list of data
df = pd.DataFrame(data, columns=['Item Name', 'Quantity', 'Price', 'Delivery Price'])

# Write the DataFrame to a CSV file
df.to_csv('ammo_prices.csv', index=False)

# Print a message to indicate that the data has been saved
print("Data has been saved to 'ammo_prices.csv'")
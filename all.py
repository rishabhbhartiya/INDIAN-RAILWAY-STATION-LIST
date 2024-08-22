import requests
import pandas as pd
from bs4 import BeautifulSoup

# Initialize a list to store the extracted data
data = []

for i in range(1,359):
    url = 'https://etrain.info/list/STATIONS?page='+str(i)

    # Send a GET request to fetch the page content
    response = requests.get(url)
    print(f"Page{i} is has {response}")
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table with class 'nocps fullw bx0s rnd5 rel'
    table = soup.find('table', {'class': 'nocps fullw bx0s rnd5 rel'})

    # Loop through all the rows in the table body
    for row in table.find_all('tr'):
        # Initialize a list to store the columns of the current row
        cols = []
    
        # Loop through all the columns in the current row
        for cell in row.find_all('td'):
            # Get the text content of the cell and strip any extra whitespace
            cols.append(cell.get_text(strip=True))
    
        # Append the extracted columns to the data list
        data.append(cols)

dataset = pd.DataFrame(data)
dataset.to_csv("INDIAN RAILWAY STATION.csv")
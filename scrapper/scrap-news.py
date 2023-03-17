import requests
from bs4 import BeautifulSoup

# Fetch the BBC News homepage
url = "https://www.bbc.com/news"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the top news headlines and links
    headlines = soup.find_all('a', class_='gs-c-promo-heading')
    
    # Print the headlines and links
    for headline in headlines:
        print(f"{headline.text}: {headline['href']}")
else:
    print("Error fetching the webpage. Status code:", response.status_code)

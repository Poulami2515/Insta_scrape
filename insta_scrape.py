import requests
from bs4 import BeautifulSoup

# Define the URL of the Instagram profile to be scraped
url = "https://www.instagram.com/snigyban18/"

# Make a request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the information we want to scrape
    title = soup.find("title").get_text()
    description = soup.find("meta", attrs={"name": "description"})["content"]

    # Print the information
    print("Title:", title)
    print("Description:", description)
else:
    # If the request was not successful, print an error message
    print("Failed to retrieve data from", url)

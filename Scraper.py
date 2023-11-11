import requests
from bs4 import BeautifulSoup
import webbrowser

# Prompt user for URL
url = input("Enter the URL: ").strip()

# Add "https://" if not present
if not url.startswith(("http://", "https://")):
    url = "https://" + url

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links on the page
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Create an HTML file and write the links to it
    with open('links.html', 'w', encoding='utf-8') as file:
        file.write('<html><body>\n')
        for link in links:
            file.write(f'<a href="{link}">{link}</a><br>\n')
        file.write('</body></html>')

    print(f"Links saved to 'links.html'")

    # Open the HTML file in the default web browser
    webbrowser.open('links.html')
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

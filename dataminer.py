import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes(url, output_file):
    """Scrapes quotes from the website and saves them to a CSV file.

    Args:
        url (str): The URL of the website to scrape.
        output_file (str): The name of the CSV file to save the data to.
    """
    try:
        # Fetch the HTML content of the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        html_content = response.content
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract data from the website
    data = []
    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        
        data.append({
            "quote": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    # Check if data was extracted
    if not data:
        print("No data found on the page.")
        return

    # Create a Pandas DataFrame from the extracted data
    df = pd.DataFrame(data)

    # Save the data to a CSV file
    df.to_csv(output_file, index=False)
    print(f"Data successfully saved to {output_file}")

# Example usage
scrape_quotes("http://quotes.toscrape.com/", "quotes.csv")

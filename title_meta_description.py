import csv
import requests
from bs4 import BeautifulSoup

def extract_title_and_meta(url):
    try:
        # Send an HTTP GET request to the URL and get the response
        response = requests.get(url)
        
        # Parse the response content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the title and meta description from the HTML
        title = soup.title.string.strip() if soup.title else "N/A"
        meta_tag = soup.find("meta", attrs={"name": "description"})
        meta_description = meta_tag["content"].strip() if meta_tag else "N/A"
        
        return title, meta_description
    except Exception as e:
        # If any error occurs during the extraction, handle it and return "N/A" values
        print(f"Error occurred while processing {url}: {e}")
        return "N/A", "N/A"

def main():
    # Initialize the input and output file names
    input_file = "input.csv"
    output_file = "custom_extraction.csv"
    
    try:
        # Create a CSV file to store the extracted data
        with open(output_file, mode='w', newline='', encoding='utf-8') as output_csv:
            csv_writer = csv.writer(output_csv)
            csv_writer.writerow(['URL', 'Title', 'Meta Description'])
            
            # Read the URLs from the input file
            with open(input_file, mode='r', encoding='utf-8') as input_csv:
                csv_reader = csv.reader(input_csv)
                next(csv_reader)  # Skip the header row
                
                for row in csv_reader:
                    url = row[0].strip()
                    
                    # Extract title and meta description for each URL
                    title, meta_description = extract_title_and_meta(url)
                    
                    # Write the results to the output CSV file
                    csv_writer.writerow([url, title, meta_description])
                    
            print("Extraction complete. Results saved to custom_extraction.csv.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

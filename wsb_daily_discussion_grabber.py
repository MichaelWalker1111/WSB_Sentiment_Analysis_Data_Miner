import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
# Initialize the WebDriver
driver = webdriver.Chrome()

# Load the webpage containing the HTML data
driver.get("https://www.reddit.com/r/wallstreetbets/search/?q=%22Daily+Discussion%22&type=link&cId=245787e1-43ae-4d83-aa4e-853c5ad7ec7e&iId=c188a37c-1ee0-4ce8-bbff-923c342ef7a4&t=month")

# Find all <a> tags with data-testid="post-title"
post_links = driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="post-title"]')

# Limit the number of links to 30
post_links = post_links[:30]

# Get the href values for each link
href_values = [link.get_attribute("href") for link in post_links]
pattern = r"(?:january|february|march|april|may|june|july|august|september|october|november|december)_(\d{1,2})_(\d{4})"

real_href_values = []

for index, href_value in enumerate(href_values, start=1):
    match = re.search(pattern, href_value, re.IGNORECASE)
    if match:
        real_href_values.append(href_value)

    print(f"Link {index}: {href_value}")

with open("../../AppData/Roaming/JetBrains/PyCharm2023.3/scratches/daily_discussion_links.csv", "w", newline="", encoding="utf-8") as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write header row
    writer.writerow(["Date", "Link"])




    # Define a regular expression pattern to match the date format


    # Search for the pattern in the text


    # Extract data from each comment element and write to CSV
    for href_value in real_href_values:

        # Extract comment author
        text = str(href_value)
        # Extract date (assuming it's available in the comment element)
        match = re.search(pattern, href_value, re.IGNORECASE)

        if match:
            date_str = match.group(0)
            #date_str = date_str.replace("_", " ").title()


        # Write the extracted data to CSV
        writer.writerow([date_str, href_value])
# Close the WebDriver
driver.quit()

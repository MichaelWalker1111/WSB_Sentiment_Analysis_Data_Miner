import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Set up Selenium WebDriver (make sure to have the appropriate driver installed and in your PATH)
driver = webdriver.Chrome()  # You can change this to whichever WebDriver you prefer (Chrome, Firefox, etc.)

# Load the webpage
driver.get("https://www.reddit.com/r/wallstreetbets/comments/1b23eip/")

# Wait for the page to fully render (adjust the sleep time as needed)
time.sleep(5)  # Adjust this sleep time based on the page loading time
for i in range(50):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        driver.implicitly_wait(5)
        view_more_button = driver.find_element(By.XPATH, '//*[@id="comment-tree"]/faceplate-partial/div[1]/button')
        # Click the button if it's found
        view_more_button.click()

    except:
        pass

# Adjust this sleep time as needed
time.sleep(3)
# Extract the HTML after dynamic content has loaded
html = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the comment elements
comment_elements = soup.find_all("shreddit-comment")

# Open a CSV file in write mode
with open("../../AppData/Roaming/JetBrains/PyCharm2023.3/scratches/real_reddit_comments_max_comments.csv", "w", newline="", encoding="utf-8") as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write header row
    writer.writerow(["Author", "Comment", "Date"])

    # Extract data from each comment element and write to CSV
    for comment in comment_elements:
        # Extract comment text
        comment_text = comment.find("div", class_="md").text.strip()

        # Extract comment author
        comment_author = comment["author"]

        # Extract date (assuming it's available in the comment element)
        comment_date = comment.find("time")["datetime"]

        # Write the extracted data to CSV
        writer.writerow([comment_author, comment_text, comment_date])

# Prompt to keep the browser open
#input("Press Enter to close the browser and exit...")

# Close the Selenium WebDriver
driver.quit()

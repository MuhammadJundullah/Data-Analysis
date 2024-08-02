from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://kampusmerdeka.kemdikbud.go.id/program/magang/browse/")

    # Scroll the page to load dynamic content
    previous_height = page.evaluate("document.body.scrollHeight")
    while True:
        time.sleep(random.uniform(1, 20))  # Wait for the content to load
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == previous_height:
            break
        previous_height = new_height

    # Get the page content
    content = page.content()
    browser.close()

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    intern_positions = soup.find_all('p', class_='text-0-0-56 sans-0-0-70 heading-5-0-0-77 pad-0-0-812 ellipsis-0-0-817')
    intern_mitra = soup.find_all('p', class_='text-0-0-56 sans-0-0-70 tiny-0-0-72 ellipsis-0-0-59 pad-0-0-812')
    intern_lokasi = soup.find_all('span', class_='text-0-0-56 sans-0-0-70')
    intern_durasi = soup.find_all('span', class_='text-0-0-56 sans-0-0-70 tiny-0-0-72')

    # Collect data into lists
    allPositions = [position.text.strip() for position in intern_positions]
    allMitra = [mitra.text.strip() for mitra in intern_mitra]
    allLokasi = [lokasi.text.strip() for lokasi in intern_lokasi]
    allDurasi = [durasi.text.strip() for durasi in intern_durasi]

    # Ensure all lists have the same length by truncating longer lists
    min_length = min(len(allPositions), len(allMitra), len(allLokasi), len(allDurasi))
    allPositions = allPositions[:min_length]
    allMitra = allMitra[:min_length]
    allLokasi = allLokasi[:min_length]
    allDurasi = allDurasi[:min_length]

    # Save data to DataFrame
    df = pd.DataFrame({
        "Position": allPositions,
        "Mitra": allMitra,
        "Lokasi": allLokasi,
        "Durasi": allDurasi
    })

    df.to_excel('/Users/admin/Documents/Data Magang Mandiri.xlsx', index=False)
    print("Success")

# Main function to run Playwright script
with sync_playwright() as playwright:
    run(playwright)

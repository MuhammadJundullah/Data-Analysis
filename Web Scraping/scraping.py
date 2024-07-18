from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://kampusmerdeka.kemdikbud.go.id/program/magang/browse/')
    
    # Scroll down to load dynamic content and ensure the left side is visible
    for _ in range(5):
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(5000)

    content = page.content()
    browser.close()

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    intern_positions = soup.find_all('span', class_='text-0-0-56 sans-0-0-70')

    # Collect data into a list
    data = []
    for position in intern_positions:
        data.append(position.text)

    # Save data to Excel
    df = pd.DataFrame(data, columns=["Position"])
    df.to_excel('/Users/admin/Documents/Data Lokasi.xlsx', index=False)
    print("Success")

with sync_playwright() as playwright:
    run(playwright)

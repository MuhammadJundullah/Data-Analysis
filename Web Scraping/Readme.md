Berikut adalah deskripsi yang bisa kamu gunakan untuk GitHub repository proyek web scraping tersebut:

---

## Web Scraping Internship Positions from Kampus Merdeka

This project is a web scraping script designed to extract internship positions from the **Kampus Merdeka** website. The script uses **Playwright** and **BeautifulSoup** to navigate the dynamically loaded content and collect relevant data. The data is then saved into an **Excel** file for further analysis and use.

### Features

- **Dynamic Content Handling**: The script scrolls through the page to load all dynamic content.
- **Data Extraction**: Extracts positions, mitra (partners), locations, and duration of internships.
- **Data Storage**: Saves the extracted data into an Excel file for easy access and manipulation.

### Requirements

- Python 3.7 or higher
- **Playwright**: For navigating the website and handling dynamic content.
- **BeautifulSoup**: For parsing HTML content.
- **Pandas**: For data manipulation and saving to Excel.
- **openpyxl**: For writing the Excel file.

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/internship-scraping.git
    cd internship-scraping
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Playwright browsers**:
    ```bash
    playwright install
    ```

### Usage

Run the script to scrape internship positions and save them to an Excel file:
```bash
python scraping.py
```

### Script Details

The script performs the following steps:

1. **Initialize Playwright**:
    ```python
    from playwright.sync_api import sync_playwright
    ```

2. **Navigate to the website**:
    ```python
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://kampusmerdeka.kemdikbud.go.id/program/magang/browse/")
    ```

3. **Scroll through the page to load dynamic content**:
    ```python
    previous_height = page.evaluate("document.body.scrollHeight")
    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(random.uniform(1, 2))
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == previous_height:
            break
        previous_height = new_height
    ```

4. **Extract data using BeautifulSoup**:
    ```python
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    intern_positions = soup.find_all('p', class_='text-0-0-56 sans-0-0-70 heading-5-0-0-77 pad-0-0-812 ellipsis-0-0-817')
    intern_mitra = soup.find_all('p', class_='text-0-0-56 sans-0-0-70 tiny-0-0-72 ellipsis-0-0-59 pad-0-0-812')
    intern_lokasi = soup.find_all('span', class_='text-0-0-56 sans-0-0-70')
    intern_durasi = soup.find_all('span', class_='text-0-0-56 sans-0-0-70 tiny-0-0-72')
    ```

5. **Store data in lists and ensure equal lengths**:
    ```python
    allPositions = [position.text.strip() for position in intern_positions]
    allMitra = [mitra.text.strip() for mitra in intern_mitra]
    allLokasi = [lokasi.text.strip() for lokasi in intern_lokasi]
    allDurasi = [durasi.text.strip() for durasi in intern_durasi]

    min_length = min(len(allPositions), len(allMitra), len(allLokasi), len(allDurasi))
    allPositions = allPositions[:min_length]
    allMitra = allMitra[:min_length]
    allLokasi = allLokasi[:min_length]
    allDurasi = allDurasi[:min_length]
    ```

6. **Save data to an Excel file**:
    ```python
    import pandas as pd
    df = pd.DataFrame({
        "Position": allPositions,
        "Mitra": allMitra,
        "Lokasi": allLokasi,
        "Durasi": allDurasi
    })
    
    df.to_excel('/Users/admin/Documents/Data Magang Mandiri.xlsx', index=False)
    print("Success")
    ```

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

You can adjust the content as needed and ensure that your repository contains the necessary files like `requirements.txt` and `LICENSE`.

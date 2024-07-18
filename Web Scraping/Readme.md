# Internship Position Scraper

This project is a web scraping tool designed to extract internship positions from the [Kampus Merdeka](https://kampusmerdeka.kemdikbud.go.id/program/magang/browse/) website. The script uses Playwright and BeautifulSoup to load dynamic content and scrape the desired data, which is then saved to an Excel file.

## Features

- Loads dynamic content by scrolling the page.
- Scrapes internship positions and saves them to an Excel file.
- Uses Playwright for browser automation.
- Parses HTML content with BeautifulSoup.
- Saves data to Excel using pandas.

## Requirements

- Python 3.7+
- Playwright
- BeautifulSoup4
- pandas
- openpyxl

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/internship-scraper.git
    cd internship-scraper
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Install Playwright browsers:

    ```sh
    playwright install
    ```

## Usage

1. Run the scraping script:

    ```sh
    python scraping.py
    ```

2. The script will navigate to the Kampus Merdeka website, load the dynamic content by scrolling, and extract the internship positions. The results will be saved to an Excel file named `intern_positions.xlsx`.

## Example Output

The output Excel file will have a single column "Position" with the extracted internship positions.

## File Structure

- `scraping.py`: The main script for scraping the internship positions.
- `requirements.txt`: List of Python packages required to run the script.
- `README.md`: Documentation for the project.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact me at [your-email@example.com](mailto:your-email@example.com).


# Google Scholar Crawler

This enhanced Google Scholar crawler retrieves publication information, including abstracts, and saves the results to a CSV file.  It builds upon the original `gscrawler` and incorporates significant improvements for robustness, error handling, and proxy support.

## Features

* Crawls Google Scholar based on a provided keyword.
* Saves results in a well-formed CSV file, handling commas and quotes within the data.
* Leverage paid services ScraperAPI to avoid rate limiting and improve reliability.
* Robust error handling to manage connection issues, missing data, and other unexpected situations.
* Handles multiple authors correctly.
* Customizable output filenames.

## Requirements

* Python 3.6+
* `scholarly` package

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/bigwisu/google_scholar_crawler
   ```
2. Navigate to the project directory:
   ```bash
   cd google_scholar_crawler
   ```
3. Create virtual env
   ```bash
   python3.6 -m venv env
   ```
4. Enter virtual env
   ```bash
   source env/bin/activate
   ```
5. Install the required packages:
   ```bash
   pip install scholarly
   ```

## Usage

1. **Configure Proxy Settings:**

   Edit `gscrawler.py`:
   Enter your ScraperAPI key as the value of variable `SCRAPER_API_KEY`

2. **Config keywords:**

   Edit `crawl.py`:
   Populate queries with your keywords

   ```python
   queries = [
        "('Generative AI' OR GenAI OR 'Gen AI') AND healthcare",
        "('Generative AI' OR GenAI OR 'Gen AI') AND business",
        # Add more keywords here...
    ]
   ```
3. **Crawl:**

   ```bash
   python3.6 crawl.py
   ```

4. **Output:**
   Multiple files named generative-ai-nnn.csv

## Contributing

Contributions are welcome!  Please open an issue or submit a pull request.

## License

Apache License 2.0

## Author

Wisu Suntoyo

## Acknowledgments

* Byunghyun Ban (for the original `gscrawler` code)
* The `scholarly` library developers
* Gemini code assist
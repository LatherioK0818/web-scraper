# LAB - Class 17: Citation Scraper for Wikipedia

## Project Overview

In the realm of academic and professional research, the integrity of information sourced from Wikipedia is often scrutinized due to the platform's open-edit nature. Recognizing this, our project, developed by [Your Name/Group Name], aims to enhance the reliability of Wikipedia as a reference tool. We have crafted a sophisticated Python-based solution designed to meticulously scan Wikipedia articles, identifying and reporting segments that necessitate additional citations. This tool is pivotal for researchers, scholars, and the curious mind aiming to validate the authenticity of information presented in Wikipedia articles.

## Technical Setup

### Dependencies

Our application is built with Python 3.x, leveraging the `requests` library for HTTP requests and `BeautifulSoup` from `bs4` for HTML parsing. These dependencies are crucial for navigating and parsing the content of Wikipedia pages to identify "citation needed" tags and their corresponding content.

### Installation and Execution

To utilize our scraper, follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Install the necessary Python packages:
   ```bash
   pip install requests beautifulsoup4
   ```
3. To execute the script, navigate to the project directory and run:
   ```bash
   python scraper.py
   ```

This initiates our scraping process, targeting the specified Wikipedia article URL embedded within the script.

## Functionality and Usage

Our application encompasses several key functionalities:

- **Citation Count:** Determines the total number of "citation needed" instances within an article.
- **Citation Report:** Generates a detailed report of text snippets lacking citations.
- **Section-wise Citation Report:** Organizes citation needs by article section for a structured overview.
- **Link Citation Scan:** Examines internal Wikipedia links for citation completeness.

These capabilities are encapsulated within a user-friendly script, `scraper.py`, which automates the extraction and reporting process.

## Testing Framework

While our project is currently in its initial stages without a formal testing suite, we advocate for the implementation of tests using frameworks like `unittest` or `pytest`. Future development will include comprehensive test cases to ensure accuracy and reliability.

## Contributions and Acknowledgements

Contributions to enhance functionality or improve the codebase are highly welcomed. Interested parties are encouraged to fork the repository, commit modifications, and submit pull requests for review.

I extend my gratitude to colleagues Ekow, Steph, and the invaluable assistance provided by ChatGPT, which together have been instrumental in the realization of this project.

## Closing Remarks

This project underscores our commitment to enhancing the utility of Wikipedia as a credible reference source. By providing tools to easily identify and rectify unsupported claims, we contribute to the collective endeavor of ensuring information reliability and accuracy across this vast knowledge platform.

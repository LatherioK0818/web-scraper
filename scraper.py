#scraper.py
from page_scraper import (get_citations_needed_count, get_citations_needed_report,
                                 get_citations_needed_by_section, scan_citations_in_links, save_to_file)

def main():
    url = 'https://en.wikipedia.org/wiki/List_of_air_operations_during_the_Battle_of_Europe'

    # Perform the citation scan for links
    links_report = scan_citations_in_links(url)
    save_to_file(links_report, 'citations_in_links.json', 'json')

    # Get citations needed by section
    sections_report = get_citations_needed_by_section(url)
    save_to_file(sections_report, 'citations_needed_by_section.json', 'json')

if __name__ == "__main__":
    main()
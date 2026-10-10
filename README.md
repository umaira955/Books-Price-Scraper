# Books Price Scraper

## Description
Python project to scrape books data from the website “Books to Scrape” and save them into a CSV file.

## Features
- Scraping book titles
- Scraping book prices and their availability
- Scraping book links and ratings
- Scraping data from 50 pages
- Saving the scraped data into a CSV file

## Technologies
- Python
- Requests
- BeautifulSoup
- CSV

## Requirements
Installing the necessary libraries using the command below:

```bash
pip install -r requirements.txt
```

## Usage
To execute the application, run the command below:

```bash
python main.py
```

Scraped books data will be stored in the file `Book.csv`

## Output
The CSV file contains the following columns:
- Title
- Price
- Availability
- Links
- Rating

## Website
[Books to Scrape](https://books.toscrape.com/)
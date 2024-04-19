# Amazon Reviews Scraper

## Overview

The Amazon Reviews Scraper is a Python script built with Scrapy, allows users to extract review data from Amazon product pages for further analysis. It retrieves information such as the total number of ratings, the overall rating of the product, and individual reviews' ratings.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Install the required dependencies by running:
  ```
  pip install scrapy
  ```

### Usage

1. Prepare a CSV file containing a list of ASINs (Amazon Standard Identification Numbers) in a single column.
2. Run the script by executing:
   ```
   ASIN_scrapping_script.py
   ```

The script will start scraping Amazon product review data for each ASIN listed in the CSV file and store the results in a CSV file named `amazon_reviews.csv`.

## Example

Suppose you have a CSV file `ASIN_Bewertungen.csv` with ASINs:

```
B01M8L5Z3Y
B07RG9D51N
B0825P1G8K
```

After running the script, the `amazon_reviews.csv` file will contain review data for each ASIN:

| asin      | total_ratings | global_stars | datetime            |
|-----------|---------------|--------------|---------------------|
| B01M8L5Z3Y| 354           | 4.5          | 2024-03-19 08:30:00 |
| B07RG9D51N| 220           | 4.3          | 2024-03-19 08:31:00 |
| B0825P1G8K| 150           | 4.2          | 2024-03-19 08:32:00 |




# IndiaCode Scraper

## Overview

This project is a web scraper designed to extract data from [India Code](https://www.indiacode.nic.in/), specifically targeting information related to Acts. The scraped data includes various details such as "Act ID," "Act Number," "Enactment Date," "Act Year," "Short Title," "Ministry," "Department," "Type," "Location," "Act PDF," "Rule PDF," "Regulation PDF," "Notification PDF," "Circular PDF," "Order PDF," "Statutes PDF," "Ordinance PDF," and a "Link" associated with each entry.

## Getting Started

### Prerequisites

Before running the scraper, ensure you have the required dependencies installed. You can install them using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Usage

After installing the dependencies, you can run the scraper using the following command:

```bash
streamlit run new.py
```

This will launch a Streamlit web application allowing you to interact with the scraper.

## Features

- **Scraping:** The scraper extracts data from the [India Code](https://www.indiacode.nic.in/) website, focusing on Acts.

- **Data Columns:** The extracted data includes columns such as "Act ID," "Act Number," "Enactment Date," "Act Year," "Short Title," "Ministry," "Department," "Type," "Location," "Act PDF," "Rule PDF," "Regulation PDF," "Notification PDF," "Circular PDF," "Order PDF," "Statutes PDF," "Ordinance PDF," and a "Link."

- **Streamlit Web App:** The project includes a Streamlit web application providing a user-friendly interface to run the scraper and view the extracted data.


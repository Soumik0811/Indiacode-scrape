from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import csv
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service
import streamlit as st
import pandas as pd
import os
def extract(url):
# Initialize an empty list to store scraped data
    data_list = []
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome(ChromeDriverManager().install()) 
    driver.get(url)  
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    
     # Find the table with class 'table itemDisplayTable'
        table = soup.find('table', class_='table itemDisplayTable')
    
        if table:
            scraped = {}
        # Extracting data from table rows
            rows = table.find_all('tr')
            for row in rows:
                    label = row.find('td', class_='metadataFieldLabel').text.strip()
                    value = row.find('td', class_='metadataFieldValue').text.strip()
                    scraped[label] = value
        
            print(scraped)  # This will print the scraped data as a dictionary
        else:
            print("Table not found on the page.")
    else:
        print("Failed to fetch the page.")
    
     # Initialize Chrome WebDriver
     # Navigate to the URL
    time.sleep(3)  # Let the page load

    # Find the product ID
    act_pdf=[]
    product= driver.find_element(By.CSS_SELECTOR, ".container")
    elems = product.find_elements(By.TAG_NAME,"a")
    for j in elems:
       elem= j.get_attribute("href")
       if elem and elem.endswith(".pdf"):
           act_pdf.append(elem)
    # Ordinance
    ordi_links=[]
    try:
        ordi = driver.find_element(By.ID, "myTableOrdinance")
        a_tag7 = ordi.find_elements(By.TAG_NAME, "a")
        if a_tag7:
            for i in a_tag7:
                ordi_pdf = i.get_attribute("href")
                ordi_links.append(ordi_pdf)
        else:
            ordi_links.append('NA')
    except NoSuchElementException:
        ordi_links.append('NA') 

    # Circular
    circ_links=[]
    try:
        circ = driver.find_element(By.ID, "myTableCircular")
        a_tag5 = circ.find_elements(By.TAG_NAME, "a")
        if a_tag5:
            for i in a_tag5:
                circ_pdf = i.get_attribute("href")
                circ_links.append(circ_pdf)
        else:
            circ_links.append('NA')
    except NoSuchElementException:
        circ_links.append('NA')

    # Orders
    order_links=[]
    try:
        order = driver.find_element(By.ID, "myTableOrders")
        a_tag4 = order.find_elements(By.TAG_NAME, "a")
        if a_tag4:
            for i in a_tag4:
                order_pdf = i.get_attribute("href")
                order_links.append(order_pdf)
        else:
            order_links.append('NA')
    except NoSuchElementException:
        order_links.append('NA')

    # Regulations
    regu_links=[]
    try:
        regu = driver.find_element(By.ID, "myTableRegulation")
        a_tag3 = regu.find_elements(By.TAG_NAME, "a")
        if a_tag3:
            for i in a_tag3:
                regu_pdf = i.get_attribute("href")
                regu_links.append(regu_pdf)
        else:
            regu_links.append('NA')
    except NoSuchElementException:
        regu_links.append('NA')

    #Statutes
    stat_links=[]
    try:
        stat = driver.find_element(By.ID, "myTableStatutes")
        a_tag6 = stat.find_elements(By.TAG_NAME, "a")
        if a_tag6:
            for i in a_tag6:
                stat_pdf = i.get_attribute("href")
                stat_links.append(stat_pdf)
        else:
            stat_links.append('NA')
    except NoSuchElementException:
        stat_links.append('NA')

    #Notifications
    noti_links=[]
    try:
        noti = driver.find_element(By.ID, "myTableNotifications")
        a_tag2 = noti.find_elements(By.TAG_NAME, "a")
        if a_tag2:
            for i in a_tag2:
                noti_pdf = i.get_attribute("href")
                noti_links.append(noti_pdf)
        else:
            noti_links.append('NA')
    except NoSuchElementException:
        noti_links.append('NA')

    # Rules
    list_links=[]    
    try:
        rule = driver.find_element(By.ID, "myTableRules")
        a_tag = rule.find_elements(By.TAG_NAME, "a")
        if a_tag:
            for i in a_tag:
                rule_pdf = i.get_attribute("href")
                list_links.append(rule_pdf)
        else:
            list_links.append('NA')
    except NoSuchElementException:
        list_links.append('NA')

    
    scraped_data = list(scraped.items())
    # print(data_dict)
    print("act pdf:", act_pdf)
    print("Rule PDF", list_links)
    print("Regulation PDF", regu_links)
    print("Notification PDF", noti_links)
    print("Circular PDF", circ_links)
    print("Order PDF", order_links)
    print("Statutes PDF", stat_links)
    print("Ordinance PDF", ordi_links)
    # Close the web driver
    driver.quit()

    # Create a dictionary for the scraped data
    data = {
        "Act Details": scraped_data,
        "Act PDF": act_pdf,
        "Rule PDF": list_links,
        "Regulation PDF": regu_links,
        "Notification PDF": noti_links,
        "Circular PDF": circ_links,
        "Order PDF": order_links,
        "Statutes PDF": stat_links,
        "Ordinance PDF": ordi_links,
        "Act ID": scraped_data[0][1] if len(scraped_data) > 0 else "",
        "Act Number": scraped_data[1][1] if len(scraped_data) > 1 else "",
        "Enactment Date": scraped_data[2][1] if len(scraped_data) > 2 else "",
        "Act Year": scraped_data[3][1] if len(scraped_data) > 3 else "",
        "Short Title": scraped_data[4][1] if len(scraped_data) > 4 else "",
        "Ministry": scraped_data[5][1] if len(scraped_data) > 5 else "",
        "Department": scraped_data[6][1] if len(scraped_data) > 6 else "",
        "Type": scraped_data[7][1] if len(scraped_data) > 7 else "",
        "Location": scraped_data[8][1] if len(scraped_data) > 8 else "",
        "Link": url
    }
    return data

    
def main():
    st.title("Web Scraping with Streamlit")

    # Input box for entering URLs
    url_input = st.text_area("Enter URLs (one per line)", "")
    urls = url_input.split('\n')

    if st.button("Scrape Data"):
        new=[]
        all_data = []
        for i, url in enumerate(urls):
            if url.strip() != "":
                st.write(f"Scraping data from URL {i + 1}: {url}")
                data = extract(url)
                all_data.append(data) 

        if all_data:
            headers = ["Act Details", "Act ID", "Act Number", "Enactment Date", "Act Year", "Short Title", "Ministry", "Department", "Type", "Location", "Act PDF", "Rule PDF", "Regulation PDF", "Notification PDF", "Circular PDF", "Order PDF", "Statutes PDF", "Ordinance PDF", "Link"]
            csv_filename = "new_scraped.csv"
            downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
            csv_file_path = os.path.join(downloads_dir, csv_filename)

            # Check if the CSV file exists to write the header
            file_exists = os.path.isfile(csv_file_path)
            if not file_exists:
                with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=headers)
                    writer.writeheader()

            # Append data to the CSV file
            with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writerows(all_data)  # Write data rows

            st.success("Data scraped successfully!")

            # Read the file content
            with open(csv_file_path, "rb") as file:
                csv_file_content = file.read()

            # Download button
            st.download_button(
                label="Download new_scraped.csv",
                data=csv_file_content,
                file_name="new_scraped.csv",
                mime="text/csv",
            )

if __name__ == "__main__":
    main()


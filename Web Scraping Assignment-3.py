#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests beautifulsoup4 pandas


# In[ ]:


# Importing necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to search products on Amazon
def search_amazon_products(product_name):
    base_url = "https://www.amazon.in/s?k="
    search_url = base_url + product_name

    # Sending an HTTP request to the URL
    response = requests.get(search_url)

    # Parsing the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup

# Function to scrape details from Amazon search results
def scrape_amazon_details(soup):
    product_details = []

    # Finding all the products listed on the page
    products = soup.find_all('div', {'data-asin': True})

    for product in products:
        details = {
            'Brand Name': product.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}),
            'Name of the Product': product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}),
            'Price': product.find('span', {'class': 'a-offscreen'}),
            'Return/Exchange': product.find('div', {'class': 'a-row a-size-base a-color-secondary'}),
            'Expected Delivery': product.find('span', {'class': 'a-text-bold'}),
            'Availability': product.find('div', {'class': 'a-row a-size-base a-color-secondary'})
        }

        # Adding product URL
        details['Product URL'] = 'https://www.amazon.in' + product.find('a', {'class': 'a-link-normal'})['href']

        # Handling missing details
        for key, value in details.items():
            if value is not None:
                details[key] = value.text.strip()
            else:
                details[key] = '-'

        product_details.append(details)

    return product_details

# Function to save data to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f'Data saved to {filename}')

# User input for product search
product_to_search = input("Enter the product to search on Amazon: ")

# Searching for products on Amazon
amazon_soup = search_amazon_products(product_to_search)

# Scraping details from the first 3 pages of search results
all_product_details = []
for page_num in range(3):
    # Adding page number to the URL
    page_url = f'https://www.amazon.in/s?k={product_to_search}&page={page_num + 1}'
    page_soup = search_amazon_products(page_url)
    product_details = scrape_amazon_details(page_soup)
    all_product_details.extend(product_details)

# Saving data to CSV
save_to_csv(all_product_details, 'amazon_product_details.csv')


# In[ ]:


# Load the CSV file
df = pd.read_csv('amazon_product_details.csv')

# Display the dataframe
print(df)


# In[ ]:





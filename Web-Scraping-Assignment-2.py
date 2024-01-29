#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install requests beautifulsoup4 pandas')


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[15]:


# Function to scrape job data based on job title and location
def scrape_job_data(job_title, location, num_jobs=10):
    # Base URL
    base_url = "https://www.shine.com/"
    
    # URL for the search results page
    search_url = f"{base_url}job-search/{job_title}-jobs-in-{location}"
    
    # Send a GET request to the search results page
    response = requests.get(search_url)
    
        
        # Extract job details
        job_details = []
        for job in soup.find_all('div', class_='search_listing'):
            title = job.find('h3', class_='job_title').text.strip()
            company = job.find('span', class_='company_name').text.strip()
            location = job.find('li', class_='location').text.strip()
            experience = job.find('li', class_='experience').text.strip()
            
            job_details.append({
                'Title': title,
                'Company': company,
                'Location': location,
                'Experience': experience
            })
        
        return job_details
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Q1: Scrape data for Data Analyst jobs in Bangalore
data_analyst_jobs = scrape_job_data("Data Analyst", "Bangalore", num_jobs=10)

# Create a dataframe for Data Analyst jobs
data_analyst_df = pd.DataFrame(data_analyst_jobs)

# Display the Data Analyst jobs dataframe
data_analyst_df


# In[14]:


# Function to scrape job data based on job title and location
def scrape_job_data(job_title, location, num_jobs=10):
    # Base URL
    base_url = "https://www.shine.com/"
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract job details
        job_details = []
        for job in soup.find_all('div', class_='search_listing'):
            
            job_details.append({
                'Title': title,
                'Company': company,
                'Location': location
            })
            
            # Break the loop if required number of jobs is reached
            if len(job_details) == num_jobs:
                break
        
        return job_details
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Q2: Scrape data for Data Scientist jobs in Bangalore
data_scientist_jobs = scrape_job_data("Data Scientist", "Bangalore", num_jobs=10)

# Create a dataframe for Data Scientist jobs
data_scientist_df = pd.DataFrame(data_scientist_jobs)

# Display the Data Scientist jobs dataframe
data_scientist_df


# In[13]:


# Function to scrape job data based on filters (location and salary)
def scrape_filtered_job_data(job_title, location_filter, salary_filter, num_jobs=10):
    # Base URL
    base_url = "https://www.shine.com/"
    
    # URL for the search results page
    search_url = f"{base_url}job-search/{job_title}-jobs"
    
    # Send a GET request to the search results page
    response = requests.get(search_url)
    
        # Apply filters
        location_checkbox = soup.find('input', {'data-value': location_filter})
        salary_checkbox = soup.find('input', {'data-value': salary_filter})
        
        # Check the location and salary checkboxes
        if location_checkbox:
            location_checkbox['checked'] = 'checked'
        if salary_checkbox:
            salary_checkbox['checked'] = 'checked'
        
        # Click the search button after applying filters
        search_button = soup.find('button', {'id': 'btn'})
        response = requests.post(search_url, data={'btn': 'Search'})
        
        # Extract job details
        job_details = []
        for job in soup.find_all('div', class_='search_listing')[:num_jobs]:
            title = job.find('h3', class_='job_title').text.strip()
            company = job.find('span', class_='company_name').text.strip()
            location = job.find('li', class_='location').text.strip()
            experience = job.find('li', class_='experience').text.strip()
            
            job_details.append({
                'Title': title,
                'Company': company,
                'Location': location,
                'Experience': experience
            })
        
        return job_details
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Q3: Scrape data for Data Scientist jobs in Delhi/NCR with salary 3-6 lakhs
filtered_data_scientist_jobs = scrape_filtered_job_data("Data Scientist", "Delhi/NCR", "3-6", num_jobs=10)

# Create a dataframe for filtered Data Scientist jobs
filtered_data_scientist_df = pd.DataFrame(filtered_data_scientist_jobs)

# Display the filtered Data Scientist jobs dataframe
filtered_data_scientist_df


# In[12]:


# Function to scrape data from Flipkart for sunglasses or sneakers
def scrape_flipkart_data(product, num_items=10):
    base_url = "https://www.flipkart.com/"

    # Prepare the search URL
    search_url = f"{base_url}search?q={product}"

    # Container for scraped data
    data = []

    # Counter to keep track of the number of items scraped
    items_scraped = 0

    # Loop through multiple pages until the required number of items is scraped
    while items_scraped < num_items:
        # Send a GET request to the search results page
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting information based on the product type
        if product.lower() == 'sunglasses':
            items = soup.find_all('div', class_='_1AtVbE')[:num_items]
        elif product.lower() == 'sneakers':
            items = soup.find_all('div', class_='_1AtVbE')[:num_items]

        # Find the next page button and update the search URL
        next_button = soup.find('a', class_='ge-49M')
        if next_button:
            search_url = base_url + next_button['href']
        else:
            # Break if there are no more pages
            break

    return data

# Q4: Scrape data for the first 10 sunglasses listings
sunglasses_data = scrape_flipkart_data("sunglasses", num_items=10)
sunglasses_df = pd.DataFrame(sunglasses_data)

# Display the dataframe for sunglasses
print("Sunglasses Data:")
print(sunglasses_df)

# Q6: Scrape data for the first 10 sneakers listings
sneakers_data = scrape_flipkart_data("sneakers", num_items=10)
sneakers_df = pd.DataFrame(sneakers_data)

# Display the dataframe for sneakers
print("\nSneakers Data:")
print(sneakers_df)


# In[ ]:


Q6: Scrape data forfirst 100 sneakers you find whenyou visit flipkart.com and search for “sneakers” inthe
search field.
You have to scrape 3 attributes of each sneaker:
1. Brand
2. ProductDescription
3. Price
As shown in the below image, you have to scrape the above attributes. - 


# In[ ]:


Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
set CPU Type filter to “Intel Core i7” as shown in the below image: 


# In[ ]:


Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
The above task will be done in following steps:
1. First get the webpagehttps://www.azquotes.com/
2. Click on TopQuote


# In[ ]:


Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,
Term of office, Remarks) from https://www.jagranjosh.com/.
This task will be done in following steps:
1. First get the webpagehttps://www.jagranjosh.com/
2. Then You have to click on the GK option
3. Then click on the List of all Prime Ministers of India
4. Then scrap the mentioned data and make theDataFrame


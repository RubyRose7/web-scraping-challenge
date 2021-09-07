#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd 
from bs4 import BeautifulSoup as bs
import os 
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False) 


# In[3]:


# URL for web scraping 
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html

#Create BeautifulSoup object; parse with "html.parser"
soup = bs(html, "html.parser")
slide_elem = soup.select_one('ul.item_list li.slide')


# In[4]:


slide_elem.find("div", class_='content_title')


# In[5]:


# Scrape the Mars News Site and collect the latest News Title and Paragraph Text. 
# Assign the text to variables that you can reference later.
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[6]:


news_p = soup.find("div", class_= "article_teaser_body").get_text()
news_p


# In[7]:


# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url 
# string to a variable called featured_image_url.
# Make sure to find the image url to the full size .jpg image.
# Make sure to save a complete url string for this image.

jpl_url = 'https://spaceimages-mars.com/'
img_url = 'https://spaceimages-mars.com/image/mars/Icaria%20Fossae7.jpg'

browser.visit(img_url)

html = browser.html

img_soup = bs(html, 'html.parser')

# Retrieving image
image_path = img_soup.find_all('img')[0]['src']

featured_image_url = jpl_url + image_path
print(featured_image_url)


# In[8]:


# use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)
    
 # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

table_facts = slide_elem.find("div", class_="table table-striped")

news_title = slide_elem.find("div", class_='content_title').get_text()
print(news_title)


# # Mars Facts
# 

# In[9]:


url = "https://galaxyfacts-mars.com/"
browser.visit(url)
html = browser.html

#Create BeautifulSoup object; parse with "html.parser"
soup = bs(html, "html.parser")
slide_elem2 = soup.find_all("tr")
slide_elem2
pd.read_html(url)


# In[10]:


slide_elem2
table_info= soup.find("table", class_= "table table-striped")
table_rows = table_info.find_all("tr")

for table in table_rows:
    print('________________')
    print(table)
   


# # Mars Hemispheres
# * Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.
# * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
# 
# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 

# In[14]:


astro_url= 'https://astrogeology.usgs.gov'
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html= browser.html
soup= bs(html, 'html.parser')


# In[16]:


mars_hem = soup.find('div', class_='collapsible results')
mars_item = mars_hem.find_all('div', class_='item')

hemisphere_image_urls = []

# Create For Loop
for i in mars_item:
    # Title
    hem = i.find('div', class_="description")
    title = hem.h3.text
    
    # Collect image links
    hem_link = hem.a["href"]    
    browser.visit(astro_url + hem_link)
    
    img_html = browser.html
    img_soup = bs(img_html, 'html.parser')
    
    img_link = img_soup.find('div', class_='downloads')
    img_url = img_link.find('li').a['href']

    # Create Dictionary 
    img_dict = {}
    img_dict['title'] = title
    img_dict['img_url'] = img_url
    
    hemisphere_image_urls.append(img_dict)

print(hemisphere_image_urls)


# In[ ]:





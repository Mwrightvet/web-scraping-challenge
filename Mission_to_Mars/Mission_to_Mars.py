#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
#splinter is the package - browser is the tool/bot that we tell to remote control browser window
from bs4 import BeautifulSoup
#scraper tool raking into the site to fetch it (looks like a mess/soup)
#To create a time delay for clicking for the bot
import time


# In[2]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver.exe'}
fred = Browser('chrome', **executable_path)


# ## Visit the NASA mars news site

# In[4]:


fred.visit('https://mars.nasa.gov/news/')


# In[10]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
fred.visit(url)

# Optional delay for loading the page
fred.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[7]:


# Convert the browser html to a soup object and then quit the browser
#with the current browser (that we identified above under url,
#ALL of the html code is being into a pot of soup for us to pick from

html = fred.html

#We filter the tool siv/ladel 
news_soup = BeautifulSoup(html, 'html.parser') 

#we're grabbing newspost (like one of many noodles from the soup)
slide_elem = news_soup.select_one('ul.item_list li.slide')

#finding one of the list (li) because that's the list on the page
slide_elem


# In[11]:


slide_elem.find("div", class_='content_title')


# In[12]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[13]:


# Use the parent element to find the paragraph text
#use get text to get text 
#select the element first, then the class and then outside parens use .get text()
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ## JPL Space Images Featured Image

# In[14]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
fred.visit(url)


# In[16]:


# Find and click the full image button
full_image_elem = fred.find_by_id('full_image')
full_image_elem.click()


# In[18]:


# Find the more info button and click that
fred.is_element_present_by_text('more info', wait_time=1)
more_info_elem = fred.find_link_by_partial_text('more info')
more_info_elem.click()


# In[19]:


# Parse the resulting html with soup
html = fred.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[20]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[21]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ## Mars Weather Twitter

# In[40]:


url = 'https://twitter.com/marswxreport?lang=en'
fred.visit(url)


# In[56]:


# Create BeautifulSoup object

html = fred.html
weather_soup = BeautifulSoup(html, 'lxml')


# In[47]:


# First, find a tweet with the data-name `Mars Weather`
mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})


# In[58]:


mars_weather_tweet = weather_soup.find_all("li", {"data-item-type": "tweet"})


# In[59]:


print(mars_weather_tweet)


# In[63]:


#Tweet text
#tweets = weather_soup.find('ol', class_='stream-items')
#mars_weather = tweets.find('p', class_='tweet-text').text
#mars_weather = weather_soup.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').find('span').text
#print(tweets)


# In[ ]:





# ## Mars Weather Astropedia

# In[31]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
fred.visit(url)


# In[27]:


hemisphere_image_urls = []

# First, get a list of all of the hemispheres
links = fred.find_by_css("a.product-item h3")
links


# In[66]:




# Next, loop through those links, click the link, find the sample anchor, return the href
for i in range(len(links)):
    hemisphere = {}
    
    # We have to find the elements on each loop to avoid a stale element exception
    fred.find_by_css("a.product-item h3")[i].click()
    
    #create a delay
    time.sleep(3)
    
    # Next, we find the Sample image anchor tag and extract the href
    sample_elem = fred.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
    # Get Hemisphere title
    hemisphere['title'] = fred.find_by_css("h2.title").text
    
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    
    # Finally, we navigate backwards
    fred.back()
    
 


# In[ ]:





# In[67]:


hemisphere_image_urls


# ## Mars Facts

# In[ ]:


import pandas as pd
df = pd.read_html('https://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# In[ ]:


browser.quit()


# In[ ]:





# -*- coding: utf-8 -*-
"""Week 6 : Web Scraping with Python - Emmanuel Odenyire Anyira

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CO_4PBDzvLsLmKlRUuh-YXjzf2Vb5Dcy

<font color='#2F4F4F'>To use this notebook on Colaboratory, you will need to make a copy of it. Go to File > Save a Copy in Drive. You can then use the new copy that will appear in the new tab.</font>

# <font color='#2F4F4F'>AfterWork Data Science: Web Scraping with Python</font>

## <font color='#2F4F4F'>Prerequisites</font>
"""

# We first import the required libraries
# ---
#
import pandas as pd             # library for data manupation
import requests                 # library for fetching a web page 
from bs4 import BeautifulSoup   # library for extrating contents from a webpage

"""## <font color='#2F4F4F'>Step 1: Obtaining our Data</font>"""

# PigiaMe: https://www.pigiame.co.ke/it-software-jobs
# ---
#
pigia_me = requests.get('https://www.pigiame.co.ke/it-software-jobs')
pigia_me

# MyJobMag: https://www.myjobmag.co.ke/jobs-by-field/information-technology
# ---
my_job_mag = requests.get('https://www.myjobmag.co.ke/jobs-by-field/information-technology')
my_job_mag

# KenyanJob: https://www.kenyajob.com/job-vacancies-search-kenya?f%5B0%5D=im_field_offre_secteur%3A133
# ---
#
kenyan_job = requests.get('https://www.kenyajob.com/job-vacancies-search-kenya?f%5B0%5D=im_field_offre_secteur%3A133')
kenyan_job

"""## <font color='#2F4F4F'>Step 2: Parsing</font>"""

# Parsing our document: pigia_me
# ---
# 
pigia_me_soup = BeautifulSoup(pigia_me.text, 'html.parser')

# Parsing our document: my_job_mag
# ---
#  
my_job_mag_soup = BeautifulSoup(my_job_mag.text, 'html.parser')

# Parsing our document: kenyan_job
# ---
# 
kenyan_job_soup = BeautifulSoup(kenyan_job.text, 'html.parser')

"""## <font color='#2F4F4F'>Step 3: Extracting Required Elements</font>"""

# 1. Extracting job titles and links: pigia me
# ---
# 
# find the tag where the jobs are actually listed in the page
pigia_me_jobs = pigia_me_soup.find_all('div', class_ = "listings-cards__list-item ")

# create two lists to store the results of our job titles and link
pigia_me_job_title = []
pigia_me_job_link = []

# iterate through each job in the found jobs
for job in pigia_me_jobs:
  # find the job title text and strip for any whitespaces
  title = job.find('div', class_ = 'listing-card__header__title').text.strip()
  # find the link text in the a tag 
  link = job.a['href']
  # append our results to the respective lists
  pigia_me_job_title.append(title)
  pigia_me_job_link.append(link)

# Print the results in the two lists
print(pigia_me_job_title)
print(pigia_me_job_link)

# 2. Extracting job titles: my_job_mag
# ---
# 
# find the tag where the jobs are actually listed in the page
my_job_mag_jobs = my_job_mag_soup.find_all('li', class_ = "job-list-li")

# create two lists to store the results of our job titles and link
my_job_mag_job_title = []
my_job_mag_job_link = []

# iterate through each job in the found jobs
for job in my_job_mag_jobs:
    # check to confirm that the h2 tag in each job does not return a None type
    if job.h2:
      # find the job title text in the h2 tag and strip for any whitespaces
      title = job.h2.text.strip()
      # find the link text in the a tag inside h2 tag, concatinate this to the website url to get the complete link
      link = link = 'https://www.myjobmag.co.ke' + job.h2.a['href']
      
      # append our results to the respective lists
      my_job_mag_job_title.append(title)
      my_job_mag_job_link.append(link)

# Print the results in the two lists
print(my_job_mag_job_title)
print(my_job_mag_job_link)

# 3. Extracting job titles: kenyan_job
# ---
#
# find the tag where the jobs are actually listed in the page
kenya_jobs = kenyan_job_soup.find_all('div', class_ = "job-description-wrapper")

# create two lists to store the results of our job titles and link
kenyan_job_title = []
kenyan_job_link = []
# iterate through each job in the found jobs
for job in kenya_jobs:
  # find the link text
  link = job['data-href']
  # Find the title text, notice that we get the text property of the div class job-description-wrapper 
  # and strip it of any leading and trailing spaces, then split on the '\n' character, we can access the title as the 1st element
  title = job.text.strip().split('\n')[0]

  # append our results to the respective lists
  kenyan_job_link.append(link)
  kenyan_job_title.append(title)

# Print the results in the two lists
print(kenyan_job_link)
print(kenyan_job_title)

"""## <font color='#2F4F4F'>Step 4: Saving our Data</font>"""

# Saving the scraped contents in a dataframe and preview our data
# ---
#
# combine the lists from the three jobs into one list
job_titles = pigia_me_job_title + my_job_mag_job_title + kenyan_job_title
url_links = pigia_me_job_link + my_job_mag_job_link + kenyan_job_link

# create a pandas DataFrame using our combined lists
df = pd.DataFrame({"Job Title": job_titles, "link_url": url_links})

# get 20 random job from the DataFrame
df.head()
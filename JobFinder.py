import requests
from bs4 import BeautifulSoup
import csv
import random

Job=input("Enter job ")
url=requests.get(f'https://www.linkedin.com/jobs/search?keywords={Job}&location=India&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0').text 
Soup=BeautifulSoup(url,'html.parser')

titletag=Soup.find_all('h3',class_='base-search-card__title')
locationtag=Soup.find_all('span',class_='job-search-card__location')
postedtimetag=Soup.find_all('time',class_='job-search-card__listdate')
linktag=Soup.find_all('a',class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')
cantfindtag=Soup.find('h1',class_='core-section-container__main-title main-title')
#captiontag=Soup.find_all('h4',class_='base-search-card__subtitle')
      
jobtitle=[i.text.replace('\n','').strip() for i in titletag]
location=[i.text.replace('\n','').strip() for i in locationtag]
postedtime=[i.text.replace('\n','').strip() for i in postedtimetag]
link=[i.attrs['href'] for i in linktag]
#caption=[i.a.text.strip() for i in captiontag]

row=['JOB TITLE',"LOCATION","POSTED DATE","JOB LINK"]

jobdetails=list(zip(jobtitle,location,postedtime,link))

with open("Data.csv", 'a') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(row)
    # writing the data rows
    csvwriter.writerows(jobdetails)
print("File appended Sucessfully...")


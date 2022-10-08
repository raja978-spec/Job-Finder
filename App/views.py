from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
from App.models import Jobs,DefaultJobs
import requests
# Create your views here.

def App(request):
    if request.method=="POST":
        if Jobs.objects.all() != None:
            Jobs.objects.all().delete()
        print(Jobs.objects.all()==None)
        Job=request.POST.get('job') 
        Place=request.POST.get('place')
        url=requests.get(f'https://www.linkedin.com/jobs/search?keywords={Job}&location={Place}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0').text
        Soup=BeautifulSoup(url,'html.parser')

        titletag=Soup.find_all('h3',class_='base-search-card__title')
        locationtag=Soup.find_all('span',class_='job-search-card__location')
        postedtimetag=Soup.find_all('time',class_='job-search-card__listdate')
        linktag=Soup.find_all('a',class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')
        cantfindtag=Soup.find('h1',class_='core-section-container__main-title main-title')

        if cantfindtag != None:
            message=cantfindtag.text
        else:
            message=0
        
        jobtitle=[i.text.replace('\n','').strip() for i in titletag]
        location=[i.text.replace('\n','').strip() for i in locationtag]
        postedtime=[i.text.replace('\n','').strip() for i in postedtimetag]
        link=[i.attrs['href'] for i in linktag]
        
        jobdetails=list(zip(jobtitle,location,postedtime,link))
        
        for i in range(len(jobdetails)):
            Job_models=Jobs.objects.create(title=jobdetails[i][0],location=jobdetails[i][1],time=jobdetails[i][2],link=jobdetails[i][3])
            Job_models.save()
        print(Jobs.objects.all()==None)  
        return render(request,'job_listing.html',{'j':Jobs.objects.all(),'m':message})
    
    else:
        if DefaultJobs.objects.all() != None:
            DefaultJobs.objects.all().delete()
        print(DefaultJobs.objects.all())
        url=requests.get(f'https://www.linkedin.com/jobs/search?keywords=&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0').text
        Soup=BeautifulSoup(url,'html.parser')

        titletag=Soup.find_all('h3',class_='base-search-card__title')
        locationtag=Soup.find_all('span',class_='job-search-card__location')
        postedtimetag=Soup.find_all('time',class_='job-search-card__listdate')
        linktag=Soup.find_all('a',class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')
        imgtag=Soup.find_all('img',class_='artdeco-entity-image artdeco-entity-image--square-4 lazy-loaded')
        captiontag=Soup.find_all('h4',class_='base-search-card__subtitle')

        
        jobtitle=[i.text.replace('\n','').strip() for i in titletag]
        location=[i.text.replace('\n','').strip() for i in locationtag]
        postedtime=[i.text.replace('\n','').strip() for i in postedtimetag]
        link=[i.attrs['href'] for i in linktag]
        icon=[i.attrs['scr'] for i in imgtag]

        print(icon)
        jobdetails=list(zip(jobtitle,location,postedtime,link))
        
        for i in range(len(jobdetails)):
            Deafult_Job_models=DefaultJobs.objects.create(title=jobdetails[i][0],location=jobdetails[i][1],time=jobdetails[i][2],link=jobdetails[i][3])
            Deafult_Job_models.save()
        return render(request,'index.html',{'d':DefaultJobs.objects.all()})

def Job_list(request):
    if request.method=="POST":
        if Jobs.objects.all() != None:
            Jobs.objects.all().delete()
        print(Jobs.objects.all()==None)
        Job=request.POST.get('job') 
        Place=request.POST.get('place')
        url=requests.get(f'https://www.linkedin.com/jobs/search?keywords={Job}&location={Place}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0').text
        Soup=BeautifulSoup(url,'html.parser')

        titletag=Soup.find_all('h3',class_='base-search-card__title')
        locationtag=Soup.find_all('span',class_='job-search-card__location')
        postedtimetag=Soup.find_all('time',class_='job-search-card__listdate')
        linktag=Soup.find_all('a',class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')
        cantfindtag=Soup.find('h1',class_='core-section-container__main-title main-title')
        captiontag=Soup.find_all('h4',class_='base-search-card__subtitle')
        
        if cantfindtag != None:
            message=cantfindtag.text
        else:
            message=0
        
        jobtitle=[i.text.replace('\n','').strip() for i in titletag]
        location=[i.text.replace('\n','').strip() for i in locationtag]
        postedtime=[i.text.replace('\n','').strip() for i in postedtimetag]
        link=[i.attrs['href'] for i in linktag]
        caption=[i.a.text.strip() for i in captiontag]

        jobdetails=list(zip(jobtitle,location,postedtime,link,caption))
        
        for i in range(len(jobdetails)):
            Job_models=Jobs.objects.create(title=jobdetails[i][0],location=jobdetails[i][1],time=jobdetails[i][2],link=jobdetails[i][3],caption=caption)
            Job_models.save()
        print(Jobs.objects.all()==None)  
        return render(request,'job_listing.html',{'j':Jobs.objects.all(),'m':message})
    
    
    return render(request,'job_listing.html')
def About(request):
    return render(request,'about.html')
def Contact(request):
    return render(request,'contact.html')

def InterShipMethod(request):
    if request.method=="POST":
        pass   
    else:
       url=requests.get('https://www.linkedin.com/jobs/search?keywords=&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0').text
       Soup=BeautifulSoup(url,'html.parser')
       Soup.find_all('')
    return render(request,'index.html')

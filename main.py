
from bs4 import BeautifulSoup
import requests
import time
print('Put some skills that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out...{unfamiliar_skill}')


def find_jobs():
   html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
   soup = BeautifulSoup(html_text,'lxml')
   jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
   for index, job in enumerate(jobs):
      publishedDate = job.find('span',class_='sim-posted').span.text
      company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
      skills = job.find('span',class_='srp-skills').text.replace(' ','')
      moreInfo = job.header.h2.a['href']
      if unfamiliar_skill not in skills:
        with open(f'posts/{index}.txt', 'w') as f:
            f.write(f"company name:{company_name.strip()}")
            f.write('\n')
            f.write(f"skills required:{skills.strip()}")
            f.write('\n')
            f.write(f"published date: {publishedDate}")
            f.write('\n')
            f.write(f"link for moreInfo: {moreInfo}")
            
            print(f'file saved in {index}')
if  __name__ == '__main__':
   while True:
      find_jobs()
      time_wait = 10
      print(f"Waiting {time_wait}minutes...")
      time.sleep(time_wait*60)


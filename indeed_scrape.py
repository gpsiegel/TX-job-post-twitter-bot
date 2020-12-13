import random
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

def random_job_listing():
    jobs = ["cloud", "linux", "python", "kubernetes", \
    "information+security", "IoT", "solutions+architect", \
    "data+science", "azure", "aws", "gcp", "devops", \
    "software+developer", "backend+developer", "front+end", \
    "java", "c++", "javascript", "serverless", "it+support", "mongodb", \
    "node.js", "vmware", "active+directory", "terraform", "CCNA"]
    rando = ''
    rando = random.choice(jobs)
    return rando

def random_tx_city():
    cities = ["dallas", "fort+worth", "austin", "el+paso", "houston", "san+antonio"]
    rdm_city = ''
    rdm_city = random.choice(cities)
    return rdm_city

def get_tx_url(job, city):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    tx_url = f'https://www.indeed.com/jobs?q={job}&l={city}%2C%20tx&fromage=3'
    r = requests.get(tx_url, headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    jobcards = soup.find_all('div', 'jobsearch-SerpJobCard')
    card = jobcards[0]
    atag = card.h2.a
    job_title = atag.get('title')
    company = card.find('span', 'company').text.strip()
    location = card.find('div', 'recJobLoc').get('data-rc-loc')
    try:
        salary = card.find('span', 'salaryText').text.strip()
    except AttributeError:
        salary = ''
    indeed_results = {
        'job title': job_title,
        'company': company,
        'location': location,
        'salary': salary,
        'link': tx_url
    }
    job_result = []

    job_result.append(indeed_results)
    df = pd.DataFrame(job_result)
    print(df.head())
    df.to_csv('jobs.txt', header=None, index=None, sep=' ', mode='a')

def main():
    for x in range(0, 1):
        try:
            job = random_job_listing()
            city = random_tx_city()
            tx_url_made = get_tx_url(job, city)
        except IndexError:
            continue
        if IndexError:
            sleep(1)
        else:
            break
   
if __name__ == '__main__':
    main()

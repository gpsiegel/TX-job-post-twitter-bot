import random
import requests
from bs4 import BeautifulSoup

def random_job_listing():
    """returns a random tech-related job from list"""
    jobs = ["cloud", "linux", "python", "kubernetes", \
    "information security", "IoT", "solutions architect", \
    "data science", "azure", "aws", "gcp", "devops", \
    "software developer", "backend developer", "front end"]
    rando = ''
    rando = random.choice(jobs)
    return rando

def random_tx_city():
    """returns a random major Texas city"""
    cities = ["dallas", "fort+worth", "austin", "el+paso", "houston", "san+antonio"]
    rdm_city = ''
    rdm_city = random.choice(cities)
    return rdm_city

def get_tx_url(job, city):
    """random job and city for the link to get the records needed"""
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    tx_url = f'https://www.indeed.com/jobs?q={job}&l={city}%2C%20tx&fromage=1'
    r = requests.get(tx_url)
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
    record = (job_title, company, location, tx_url)
    print(record)

def main():
    job = random_job_listing()
    city = random_tx_city()
    tx_url_made = get_tx_url(job, city)

if __name__ == '__main__':
    main()

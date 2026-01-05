import requests
from bs4 import BeautifulSoup

# The URL of a job site (Example: a Python search on a tech job board)
url = "https://www.myjobmag.co.ke/jobs-by-field/it-software"

def find_jobs():
    headers = {'User-Agent': 'Chrome/Version 143.0.7499.170'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # This finds job listings based on the site's HTML structure
        jobs = soup.find_all('li', class_='job-info')
        
        print(f"--- Found {len(jobs)} Potential IT Leads ---")
        
        for job in jobs:
            title = job.find('h2').text.strip()
            link = "https://https://www.linkedin.com" + job.find('a')['href']
            print(f"Position: {title}")
            print(f"Apply here: {link}\n")
    else:
        print("Could not reach the site. Check your connection.")

if __name__ == "__main__":
    find_jobs()




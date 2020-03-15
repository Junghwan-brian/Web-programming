
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
    stack = requests.get(url)
    soup = BeautifulSoup(stack.text,features="html.parser")
    pagination = soup.find("div",{"class":"pagination"})
    pages = pagination.find_all('a')
    last_page = pages[-3].get_text(strip=True)
    return int(last_page)

def extract_info(html):
    title = html.a['title']
    locs = html.find("div",{"class":"fc-black-700"})
    company, location = locs.find_all("span",recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip('- \r\n')
    company_id = html.find("span",{"class":"fav-toggle"})['data-jobid']
    link = f"https://stackoverflow.com/jobs/{company_id}"
    return {"title":title, "company":company ,"location":location, "link":link}


def extract_so_jobs(last_page):
    jobs_list = []
    for page in range(last_page):
        print(f"Extract page: {page+1}")
        stack = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(stack.text,features="html.parser")
        jobs = soup.find_all("div",{"class":"-job-summary"})
        for job in jobs:
            job_info = extract_info(job)
            jobs_list.append(job_info)
    return jobs_list

def get_so_jobs():
    last_page = get_last_page()
    return extract_so_jobs(last_page)


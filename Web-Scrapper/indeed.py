#%%
import requests
from bs4 import BeautifulSoup
limit = 50
url = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={limit}"

def extract_indeed_pages():
    indeed = requests.get(url)
    soup = BeautifulSoup(indeed.text,features="html.parser")
    pagination = soup.find("div",{"class":"pagination"})
    pages = pagination.find_all('a')
    spans = []
    for page in pages[:-1]: # 마지막은 next이므로 제외시켜준다.
        spans.append(int(page.find('span').string)) # 그냥 page.string도 가능.
    last_page = spans[-1]
    return last_page

def extract_job(htmls,page):
    title = htmls.find('a')['title']
    company = htmls.find("span",{"class":"company"})
    if company.string == None:
        company = str(company.find('a').string)
    else:
        company = str(company.string)
    company = company.strip()
    location = htmls.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id = htmls["data-jk"]
    return {"title":title ,
            "company":company, 
            "location":location,
            "link":f"https://kr.indeed.com/jobs?q=python&limit=50&start={page*limit}&vjk={job_id}"}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Extract page: {page+1}")
        indeed = requests.get(f"{url}&start={page*limit}")
        soup = BeautifulSoup(indeed.text,features="html.parser")
        jobSearch = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})  
        for result in jobSearch:
            job = extract_job(result,page)
            jobs.append(job)
    return  jobs

def get_indeed_jobs():
    last_page = extract_indeed_pages()
    return extract_indeed_jobs(last_page)

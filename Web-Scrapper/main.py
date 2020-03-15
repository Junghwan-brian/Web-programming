#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
sys.path

#%%
# stackoveflow와 indeed를  'C:\\Users\\brian\\Anaconda3\\envs\\WebProgramming\\lib\\site-packages'
# 폴더안에 넣어주고 사용했다.
import stackoverflow
import indeed
# %%
stackoverflow_job = stackoverflow.get_so_jobs()
indeed_job = indeed.get_indeed_jobs()
jobs = stackoverflow_job + indeed_job 
print(jobs)
path = "jobs.csv"
job_df = pd.DataFrame(jobs)
job_df.to_csv(path)

# %%

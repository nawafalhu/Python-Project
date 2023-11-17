from bs4 import BeautifulSoup
import requests

print("put some skills that you are not familiar with")
ss = input(">")
print(f'Filtering out {ss}')

response = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
html_text = response.content
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')

for job in jobs :
    published_date = job.find('span', class_ = 'sim-posted').span.text.strip()
    if 'few' in published_date :
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href']
        
        if ss not in skills :
            print(f"Company Name: {company_name}. \nSkills: {skills}. \nPublished Date: {published_date}. \nMore info: {more_info}.")
            print()

# print(skill)
# print(company_name)
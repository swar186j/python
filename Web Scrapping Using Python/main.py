from bs4 import BeautifulSoup
import requests
import time

print('Enter the skill you are not familiar with: (Press 0 to stop)')
unfamiliar = input('>') 
#filter out unfamiliar skill of user
print(f'Filtering out {unfamiliar}')


def find_jobs():
    #check jobs for the domain filtered by user from TimesJob website
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Engineer%2Cdeveloper%2Cprogrammer&txtLocation=Pune&cboWorkExp1=0').text
    soup = BeautifulSoup(html_text, 'lxml')
    #find job posts
    jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
    #iterate through the list of all jobs posted
    for index, job in enumerate(jobs):
        published_dt = job.find('span', class_='sim-posted').span.text
        #if the post date is recent
        if 'few' in published_dt:
            #remove the spaces
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills= job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar not in skills:
              #generate files where each job posting is listed
                with open(f'D:\TechCS\webScrapping\JobWebsite\posts{index}.txt','w') as f: 
                    f.write(f'Company name: {company_name.strip()} \n')
                    f.write(f'Required skills: {skills.strip()} \n')
                    f.write(f'More Info: {more_info} \n')
                print(f'File saved: {index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_dur = 10
        #wait for 10 mins everytime to check for new job openings
        print(f'waiting for {time_dur} minutes')
        time.sleep(time_dur*60)

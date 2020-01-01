from bs4 import BeautifulSoup
import requests
import smtplib
import re

url = '<SAVED URL FOR THE WEB SITE YOU WANT TO SEARCH>'
link = requests.get(url)
soup = BeautifulSoup(link.content, 'html.parser')

fromaddr = '<YOUR EMAIL>'
toaddr = '<TO EMAIL>'
jobs = []
username = fromaddr
password = '<PASSWORD FOR EMAIL SERVER>'
server = smtplib.SMTP('smtp.gmail.com:587')

test = soup.find('p', text=re.compile('No search results found. Please try another search.'))


def mail():
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()

if test is not None:
    print('No Jobs found... :(')
else:
    for s in soup.find_all('h3'):
        jobs.append(str(s.text))

    msgbody = '\n'.join("New Job: %s" % job for job in jobs)
    print(str(msgbody))

    msg = '\r\n'.join([
        'From: AUTO JOB FINDER',
        'To: 'toaddr',
        'Subject: NEW JOB FOUND!!',
        '',
        'GO LOOK AT THE WEBSITE, FOOL.' + '\n\n' + str(msgbody),
    ])

    mail()

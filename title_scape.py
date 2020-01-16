from bs4 import BeautifulSoup
import requests


# URL of website
url = r'https://www.bbc.co.uk/news'

# Scraping the title
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find('title')
title = title.string

# Printing the title
title = soup.title.string
print(title)

# build a new project dir
# git init
# build a new github repo
# hook up travis to your git rep
# git remote add origin url_goes_here
# .gitignore with venv
# pip freeze to build a requirements.txt
# build the dockerfile
# build the .travis.yml file
# git push etc.
# test it to see if the travis build succeeds 

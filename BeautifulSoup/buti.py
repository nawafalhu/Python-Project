<<<<<<< HEAD
from bs4 import BeautifulSoup

with open(r"D:\HTMLCSSProject\index.html", 'r') as file :
    content = file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    tag = soup.find('h1') # first one
    print(tag.text)
    tags = soup.find_all("h1", class_ = 'link')
    for ta in tags :
=======
from bs4 import BeautifulSoup

with open(r"D:\HTMLCSSProject\index.html", 'r') as file :
    content = file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    tag = soup.find('h1') # first one
    print(tag.text)
    tags = soup.find_all("h1", class_ = 'link')
    for ta in tags :
>>>>>>> 40b695b7b8c1e383f5e04d5a00bb5c0d7e5c5353
        print("tags", ta.text)
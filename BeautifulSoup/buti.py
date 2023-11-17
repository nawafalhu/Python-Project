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
        print("tags", ta.text)
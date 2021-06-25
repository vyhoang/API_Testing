import requests
from bs4 import BeautifulSoup

# Create empty list to hold list movies
li = []

# send request to the imdb website
data = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")
# create bs object to get response with data
soup = BeautifulSoup(data.content, 'html.parser')
# display all content
# print(soup.prettify())

# find list of titles in the list searched by "thriller" on the website
moviesTable = soup.find('table', {'class': 'findList'})
# display moviesTable content
# print(moviesTable.prettify())


# get all rows with tag 'tr'
rows = moviesTable.findAll('tr')
# loop to find each movie title
for row in rows:
    rowData = row.findAll('td')
    # print(rowData[1].a.text)
    # access sub url, to extract genre by movie
    subUrl = rowData[1].a['href']
    subData = requests.get("https://www.imdb.com" + subUrl)
    # create child bs object for sub url
    childSoup = BeautifulSoup(subData.content, 'html.parser')

    # add condition to avoid AttributeError when no 'a' found
    if childSoup.find('div', {'class': 'see-more inline canwrap'}):
        # get data of movie genre
        genre = childSoup.find('div', {'class': 'see-more inline canwrap'})
        if genre.a.text == " Documentary":
            print(rowData[1].a.text)
            print(genre.a.text)
            li.append(rowData[1].a.text)

# display list of movie titles
print(li)

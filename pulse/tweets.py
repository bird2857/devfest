# this program parses through an html page and filters through tweets containing the hashtag, #schoolshooting

#import modules
import bs4 
import urllib.request

#let's create an empty string to store the tweet html page
loc ='https://twitter.com/search?q=%23schoolshooting&src=tyah'

#let's create a urllib object
page = urllib.request.urlopen(schoolShootings)

# let's create a BeautifulSoup object 
soup = bs4.BeautifulSoup(page,'html.parser')

#prettify alllows you to view the html page as a nested data structure (i.e. parse the page and locate specific html tags)
print(soup.prettify())

#an empty list to store the tweet links
l = [] # an empty list to store all the tweet 

# the find_all method allows you to isolate specific html tags 
for i in soup.find_all('link'):
    l.append(i)
    print(i.get('href'))

# the total number of tweets returned from the twitter API search 
print(len(l))


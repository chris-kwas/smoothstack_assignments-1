import requests
from bs4 import BeautifulSoup




if __name__ == '__main__':
    #Coding Exercise 10: Web scrapping exercise
    # Rules of this Project :
    # Extracting/Downloading the data from html page.
    # Extracting a particular content in the webpage.
    # Location of information of interest in the html page. Identify the common pattern.
    # Give instructions to the extractor which class is title column
    # Search by Tag and Tag by class.
    # Search the text file with beautiful soup object.
    #Problem Statement :
    #Count the total number of views for a given video in youtube for a given keyword.
    #Keyword :python
    with open('home.html', 'r') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'lxml')
        course_cards = soup.find_all('div', class_ = 'card' )
        for course in course_cards:
            print(course)
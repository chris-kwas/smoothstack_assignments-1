import requests
from bs4 import BeautifulSoup
import prettyprint



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
    # with open('home.html', 'r') as html_file:#home is just a generic html file not made yet
    #     content = html_file.read()
    #     soup = BeautifulSoup(content, 'lxml')#first arguement = html file to scrap, second arguement parse method to use
    #     #tags = soup.find_all('h5') returns all lines that are tagged with h5 (use find() for a single instance)
    #     # for course in tags:
    #     #     print(course.text)
        
    #     course_cards = soup.find_all('div', class_ = 'card' )#needs under score after class becase class is a python keyword
        
    #     for course in course_cards:
    #         print(course)
    #         #print(course.h5)#prints line taggede with h5
    #         #course_name = course.h5.text gets the text from each instance
    #         #course_price = course.a a tag stores the information to get the text use .text
    #         #course_price = course.a.text.split()[-1] gets the last string
    html_text = requests.get('https://www.youtube.com/watch?v=kqtD5dpn9C8&ab_channel=ProgrammingwithMosh').text
    #print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')#latter question why this parser and what other parsers there are
    title = soup.find("title")
    #print(soup.prettify())
    print(title.string)
    print("program finished")
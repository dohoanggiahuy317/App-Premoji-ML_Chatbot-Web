from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP


class MovieSuggBot:

    def __init__(self):
        print("How do you feel? joy, fear, anger, sadness, disgust, shame, guilt")

    def fetchingUrl(self, emotion):
        urlhere = 'https://www.imdb.com/search/keyword/?keywords='+emotion+'&ref_=fn_al_kw_2'

        # HTTP request to get the data of the whole page
        response = HTTP.get(urlhere)
        data = response.text

        # Parsing the data using BeautifulSoup
        soup = SOUP(data, "lxml")

        # Extract movie titles from the data using regex
        title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
        return title

    def prepareResponse(self, emotion):
        a_li = self.fetchingUrl(emotion)
        counter = 0
        ans = []

        for each_element in a_li:
            tag = str(each_element).split('>')

            if len(tag) == 3:
                ans.append(tag[1][:-3])
            if counter > 13:
                break
            counter += 1

        return ans

    def getResponse(self, emotion):
        movie_list = self.prepareResponse(emotion)
        response = "<div class='botText'><div>Maybe you can try: </div></div>"

        for eachMovie in movie_list:
            response += "<div class='botText'><div>" + eachMovie + "</div></div>"

        return response



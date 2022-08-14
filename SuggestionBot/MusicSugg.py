from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
import json


class MusicSuggBot:

    def __init__(self):
        print("How do you feel?")

    def fetchingUrl(self, emotion):
        urlhere = 'https://www.youtube.com/results?search_query=' + emotion + "+song"
        return urlhere

    def queryYouTubeSearch(self, emotion):
        # Create the search link
        urlhere = self.fetchingUrl(emotion)

        # Opening driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(urlhere)

        youtube_data = []
        count = 0

        while True:
            end_result = driver.find_element_by_css_selector('#message').is_displayed()
            driver.execute_script(
                "var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = "
                "scrollingElement.scrollHeight;")

            if end_result == True or count > 1:
                break
            count += 1

        # Processing result
        for result in driver.find_elements_by_css_selector('.text-wrapper.style-scope.ytd-video-renderer'):
            title = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer').text
            link = result.find_element_by_css_selector(
                '.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
            channel_name = result.find_element_by_css_selector('.long-byline').text
            channel_link = result.find_element_by_css_selector('#text > a').get_attribute('href')
            views = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[0]

            youtube_data.append({
                'title': title,
                'link': link,
                'channel': {'channel_name': channel_name, 'channel_link': channel_link},
                'views': views
            })

        # print(json.dumps(youtube_data, indent=2, ensure_ascii=False))
        driver.quit()

        return youtube_data

    def prepareResponse(self, emotion):
        a_li = self.queryYouTubeSearch(emotion)
        ans = []

        for each_song in a_li:
            ans.append({
                'title': each_song['title'],
                'link': each_song['link'],
            })

        return ans

    def getResponse(self, emotion):
        song_list = self.prepareResponse(emotion)
        response = "<div class='botText'> <div>I think you would like: </div></div>"

        for eachSong in song_list:
            response += "<div class='botText'><a href = \"" + eachSong["link"] + "\"><div>" + eachSong["title"] + "</div></a></div> "

        return response

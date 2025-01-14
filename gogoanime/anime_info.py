from bs4 import BeautifulSoup
from urllib.parse import urlparse

class GogoanimeInfo:
    def __init__(self, url, session):
        """
        Get information about an anime from a URL.
        args:
            url: The URL of the anime.
            session: The requests session to use for the request.
        """
        self.url = url
        self.session = session
        self.soup = self._get_soup()
        self._get_anime_name()
        self._get_anime_url()
        self._get_totalNumberOfEpisodes()
        parsed_url = urlparse(url)
        self.base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"


    def _get_soup(self):
        """
        Get the BeautifulSoup object of the anime page.
        """
        response = self.session.get(self.url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    

    def _get_anime_name(self):
        if 'category' not in self.url:
            self.anime_name = self.soup.find_all('div', {'class':'anime-info'})[0].find_all('a')[0].text.strip()
        else:
            self.anime_name = self.soup.find_all('div', {'class':'anime_info_body_bg'})[0].find_all('h1')[0].text.strip()

    def _get_totalNumberOfEpisodes(self):
        episode_page = self.soup.find('ul', id='episode_page')
        ep_end = 0
        if episode_page:
            a_tags = episode_page.find_all('a')
            for a_tag in a_tags:
                ep_end = a_tag.get('ep_end')

        self.totalNumberOfEpisodes = int(ep_end)


    def _get_anime_url(self):
        if 'category' in self.url:
            self.anime_url = f"{self.url.split('category/')[-1]}-episode-" 
        else:
            self.anime_url = f"{self.url.split('/')[-1].split('-episode-')[0]}-episode-"

    def get_anime_info(self):
        self._get_totalNumberOfEpisodes()
        return {
            'anime_name': self.anime_name,
            'anime_url': self.anime_url,
            'base_url': self.base_url,
            'totalNumberOfEpisodes': self.totalNumberOfEpisodes
        }
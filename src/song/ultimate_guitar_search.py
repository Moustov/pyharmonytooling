import urllib

from google.modules.utils import _get_search_url as google_search, get_html


class UltimateGuitarSearch:
    def __init__(self):
        self.html_parts = []

    def __extract_link(self, part: str) -> str:
        """
        retrieve the link from a search()
        :param part:
        :return:
        """
        res = part.split("&amp")
        return "https://tabs.ultimate-guitar.com/tab/" + res[0]

    def get_html_content(self, url: str) -> str:
        """
        retrieve the song from the URL and digest it into self
        :param url:
        """
        request_headers = {
            "headers": [
                {
                    "name": "Accept",
                    "value": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
                },
                {
                    "name": "Accept-Encoding",
                    "value": "gzip, deflate, br"
                },
                {
                    "name": "Accept-Language",
                    "value": "en-US,en;q=0.5"
                },
                {
                    "name": "Connection",
                    "value": "keep-alive"
                },
                {
                    "name": "Cookie",
                    "value": "CONSENT=YES+srp.gws-20220321-0-RC1.fr+FX+718; NID=511=SjLaEiAD8XieaPXzbvGRv6obDy5C2hl1t"
                             "38hYFhdZtUkAj5B3NXqcLJHFeObuMCHGQ0pFyGdqz4ZLreVi9dQL9d9vLirw7k1VvcpCfgrI22pIPQkEUPq_xng"
                             "Dp0sdevvrGl02RSD81yb3vRk02Ofcp0w1_eDJmGgciaxLtujX6sdf9R3cs4pPSifgMn6TYnJFXz6VYkdAw1pW3q"
                             "uyvAQ0nO5gKjacjdN4ONDRJRuWDsR0ylWatRx-WYv-hAbaH5V2Z2tjUNUB6fN-VxuGMGE26EkRzx5NA-yE9zgOr"
                             "h6E8loS2ApW3L57HRTxONcivR0p0tSxrQYj7aqKYBEscAVQP9YL5EASkLuFhq4va33_Jh0-BhmXwZmjpR2OjlsR"
                             "yUtbyzgpaJE2Me10SX3ryJK; 1P_JAR=2022-11-18-08; ANID=AHWqTUmZUm85ccpqw1SRuWEWgREkOPT2RAR"
                             "9J968nc1boHOlXfW9MAGliPggv80B; SEARCH_SAMESITE=CgQIjpYB; SID=PwiWTlLNHj_8SWBZpzmNAoR6TH"
                             "_oPFpJV5IRUfSZblwmD5IS5QDg09gsza6kaiatDXdKSA.; __Secure-1PSID=PwiWTlLNHj_8SWBZpzmNAoR6T"
                             "H_oPFpJV5IRUfSZblwmD5ISIxrk9qziX_4zAKqQ-c0Mcg.; __Secure-3PSID=PwiWTlLNHj_8SWBZpzmNAoR6"
                             "TH_oPFpJV5IRUfSZblwmD5ISHdSSdIzupiHJwSXwHFToDQ.; HSID=Alen3o4YYCcWDXg2n; SSID=ARWRdr36E"
                             "AiYDe_Fx; APISID=7HsDOitrJ-y7YtAj/AdxVaC1PRPdwdAe3r; SAPISID=YgNHLsMws4ctEC8j/AIFlW3VDa"
                             "LLUtJLgI; __Secure-1PAPISID=YgNHLsMws4ctEC8j/AIFlW3VDaLLUtJLgI; __Secure-3PAPISID=YgNHL"
                             "sMws4ctEC8j/AIFlW3VDaLLUtJLgI; SIDCC=AIKkIs2A63fUePFpjm3NO5LpNjp7TWEyjm4TVm1E308ZRjT4HQ"
                             "EG1t5mkzj71BY0_4Tf9rLP38E; __Secure-3PSIDCC=AIKkIs1-nEYmEcJ88hl4parr4tB18Q6O66_CoDJ6vUN"
                             "Mpy4RgWBDLdabW_9D1kwHGcOvfa-xHX5_; __Secure-1PSIDCC=AIKkIs1UoQ-tohs1I-7CeG8vx2kgQCYRrdL"
                             "6eIg5KwFeo6yItSX8WDBgX7JKEN7EKFUF3dOrekW7; AEC=AakniGP5-_SvkhUzwslNGYH0M8a3tfUHDAU2Kqi7"
                             "xx3uW6q9CA7KsgZcNso; OTZ=6758620_52_52_123900_48_436380; DV=k3F18yZsReBTcOIVpget2HdKubW"
                             "cSJhw4P5MyRCtQwAAAHAt_GefmwJYEAAAAARGBFEmR7V0LAAAACDi14a58OXZEAAAAA"
                },
                {
                    "name": "Host",
                    "value": "www.google.com"
                },
                {
                    "name": "Sec-Fetch-Dest",
                    "value": "document"
                },
                {
                    "name": "Sec-Fetch-Mode",
                    "value": "navigate"
                },
                {
                    "name": "Sec-Fetch-Site",
                    "value": "none"
                },
                {
                    "name": "Sec-Fetch-User",
                    "value": "?1"
                },
                {
                    "name": "TE",
                    "value": "trailers"
                },
                {
                    "name": "Upgrade-Insecure-Requests",
                    "value": "1"
                },
                {
                    "name": "User-Agent",
                    "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
                }
            ]
        }
        headers = {}
        for h in request_headers["headers"]:
            headers[h["name"]] = h["value"]
        req = urllib.request.Request(url, data=None, headers=headers)
        f = urllib.request.urlopen(req)
        response = f.read()
        html = response.decode('utf-8')
        return html

    def search(self, query: str, limit: int) -> [str]:
        """
        search from UG any string, not only the author / title
        WARNING: too many searches will result in a blocking HTTP ERROR 429
        https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python
        :param query:
        :param limit:
        :return:
        """
        query += " site:ultimate-guitar.com"
        res = []
        link_qty = 0
        page = 0
        more_songs = True
        while link_qty < limit and more_songs:
            url = google_search(query, page, lang='en', area='com', ncr=False, time_period=False, sort_by_date=False)
            # html = str(self.get_html_content(url))
            html = str(get_html(url))
            self.html_parts = html.split("=https://tabs.ultimate-guitar.com/tab/")
            more_songs = len(self.html_parts) > 1
            for part in self.html_parts[1:]:
                res.append(self.__extract_link(part))
                link_qty += 1
                if link_qty >= limit:
                    break
            page += 1
        return res

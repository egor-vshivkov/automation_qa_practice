import requests


class GetUrlEndpoint:
    def __init__(self):
        self.base_url = "https://tinyurl.com"
    def get_long_url(self, code):
        short_url = f"{self.base_url}/{code}"
        response = requests.head(short_url, allow_redirects=False)
        if response.status_code in (301, 302):
            return response.headers.get('Location')
        else:
            raise Exception(f"Не удалось получить длинный URL: {response.status_code} - {response.text}")
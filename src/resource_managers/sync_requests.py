import requests


class SyncAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = None

    def __enter__(self):
        self.session = requests.Session()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.session:
            self.session.close()

    def make_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url)
        return response.json()

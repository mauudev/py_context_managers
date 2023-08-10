import httpx


class AsyncAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def __aenter__(self):
        self.client = httpx.AsyncClient()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.client.aclose()

    async def make_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = await self.client.get(url)
        return response.json()

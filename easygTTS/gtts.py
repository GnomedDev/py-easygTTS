import aiohttp

offical_url = "http://easy-gtts.herokuapp.com/"

class NoContextManagerException(Exception): pass

class gtts:
    def __init__(self, base_url: str = offical_url, session: aiohttp.ClientSession = None):
        self.url = base_url
        self.used_session = None
        self.passed_session = session

    async def __aenter__(self):
        self.used_session = self.passed_session or aiohttp.ClientSession()
        return self

    async def __aexit__(self, *args):
        await self.used_session.close()

    @property
    def session(self):
        return self.passed_session or self.used_session

    async def get(self, **kwargs):
        if not self.session:
            raise NoContextManagerException("Session is not initialized, use context manager or pass aiohttp.ClientSession on init")

        if not kwargs.get("lang"):
            kwargs["lang"] = "en"

        async with self.session.get(f"{self.url}tts", params=kwargs) as resp:
            resp = await resp.read()
            return resp

    async def langs(self):
        async with self.session.get(f"{self.url}langs") as resp:
            return await resp.json()

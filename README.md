# py-easygTTS

Asynchronous interface to an [easy-gtts](https://github.com/Gnome-py/easy-gtts-api) server written with aiohttp.  
One class currently exists, easygTTS.gtts, which takes 2 optional args `base_url` (url to a easy-gtts server) and session (aiohttp.ClientSession)

## Examples

### One time use
```python
import easygTTS
import asyncio

async def main():
    async with easygTTS.gtts() as gtts:
        hello_uk = await gtts.get(text="Hello United Kingdom", lang="en-uk")
        hello_usa = await gtts.get(text="Hello USA", lang="en")
        langs = await gtts.langs()

    with open("u, "wb") as f:
        f.write(hello_uk)

asyncio.run(main())
```

### Using a global session
```python
import easygTTS
import asyncio
import aiohttp

async def main():
    session = aiohttp.ClientSession()
    gtts = easygTTS.gtts(session=session)

    await gtts.get(text="Hello World")

    # later in your code
    await gtts.get(text="even more to TTS")

    # at the end
    await session.close()

asyncio.run(main())
```
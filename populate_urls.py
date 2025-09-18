import asyncio
from main import URLMap, engine, Base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.example.com",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.amazon.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.linkedin.com",
    "https://www.reddit.com",
    "https://www.stackoverflow.com",
    "https://www.wikipedia.org",
    "https://www.netflix.com",
    "https://www.youtube.com",
    "https://www.instagram.com",
    "https://www.twitch.tv",
    "https://www.pinterest.com",
    "https://www.quora.com",
    "https://www.dropbox.com",
    "https://www.spotify.com",
    "https://www.adobe.com",
    "https://www.salesforce.com",
    "https://www.tesla.com",
    "https://www.nasa.gov",
    "https://www.cnn.com",
    "https://www.bbc.com",
    "https://www.nytimes.com",
    "https://www.espn.com",
    "https://www.imdb.com",
    "https://www.weather.com",
    "https://www.booking.com",
    "https://www.airbnb.com",
    "https://www.tripadvisor.com",
    "https://www.paypal.com",
    "https://www.wordpress.com",
    "https://www.medium.com",
    "https://www.bing.com",
    "https://www.yelp.com",
    "https://www.flickr.com",
    "https://www.tumblr.com",
    "https://www.slack.com",
    "https://www.shopify.com",
    "https://www.coursera.org",
    "https://www.udemy.com",
    "https://www.khanacademy.org",
    "https://www.edx.org",
    "https://www.duolingo.com",
    "https://www.ted.com",
    "https://www.wired.com",
    "https://www.forbes.com",
    "https://www.nationalgeographic.com"
]

SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def insert_urls():
    async with SessionLocal() as session:
        for i, url in enumerate(urls):
            short_code = f"ex{i+1:02d}"
            url_map = URLMap(short_code=short_code, long_url=url)
            session.add(url_map)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(insert_urls())

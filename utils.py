import requests
from newspaper import Article


HACKER_NEWS_TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HACKER_NEWS_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


def get_top_hacker_news(n=5):
    response = requests.get(HACKER_NEWS_TOP_STORIES_URL)
    top_story_ids = response.json()[:n]

    stories = []
    for story_id in top_story_ids:
        story = requests.get(HACKER_NEWS_ITEM_URL.format(story_id)).json()
        source_url = story.get("url")
        content = extract_story_content(source_url)
        if story:
            stories.append(
                {"title": story.get("title"), "url": source_url, "content": content}
            )

    return stories


def extract_story_content(url):
    article = Article(url)
    article.download()
    article.parse()

    return {"title": article.title, "content": article.text[:]}

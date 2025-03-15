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


def extract_story_content(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the article: {e}")
        return {"title": "", "content": f"Error: {e}"}

    article = Article(url)
    article.download(input_html=response.text)
    if not article.html:
        return {"title": "", "content": "Failed to download article content."}
    article.parse()
    return {"title": article.title, "content": article.text[:]}

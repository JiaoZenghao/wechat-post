import requests
HACKER_NEWS_TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HACKER_NEWS_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def get_top_hacker_news(n=5):
    response = requests.get(HACKER_NEWS_TOP_STORIES_URL)
    top_story_ids = response.json()[:n]

    stories = []
    for story_id in top_story_ids:
        story = requests.get(HACKER_NEWS_ITEM_URL.format(story_id)).json()
        print(story)
        if story:
            stories.append({"title": story.get("title"), "url": story.get("url")})

    return stories


# import openai


# def generate_post(topic):
#     """基于热点话题生成社交媒体文章"""
#     prompt = f"请基于以下科技新闻标题撰写一篇适合社交媒体的简短文章：{topic}"

#     chain = model | parser

#     messages=[{"role": "system", "content": "你是一个社交媒体内容创作者。"},
#              {"role": "user", "content": prompt}]

#     return chain.invoke(messages)

# def generate_posts_for_news(news_list):
#     """为多个新闻生成文章"""
#     posts = []
#     for news in news_list:
#         post = generate_post(news["title"])
#         posts.append({"title": news["title"], "url": news["url"], "post": post})
#     return posts

def main():
    stories = get_top_hacker_news()
    print(stories)


if __name__ == "__main__":
    main()

import time
import requests

url_top_stories = "https://hacker-news.firebaseio.com/v0/topstories.json"
url_item = "https://hacker-news.firebaseio.com/v0/item/"


def main():
    params = {"print": "pretty"}
    story_ids = requests.get(url_top_stories, params).json()

    for story_id in story_ids[:30]:
        time.sleep(1)
        response = requests.get(f"{url_item}{story_id}.json")
        story = response.json()
        if "title" in story:
            params = {"title": story.get("title"), "link": story.get("url")}
            print(params)


if __name__ == "__main__":
    main()

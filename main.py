import DrawFrame
import storyFetch
import json

if __name__ == '__main__':
	stories = json.loads(storyFetch.GetStories("entitledparents", "hot", 1))
	for story in stories.get("data").get("children"):
		DrawFrame.GenerateFrames(story.get("data").get("title"), story.get("data").get("selftext"), story.get("data").get("author_fullname"))
import DrawFrame
import storyFetch
import json
externalDadjokecounter = 0
if __name__ == '__main__':
	stories = json.loads(storyFetch.GetStories("entitledparents", "hot", 50))
	print("fetched " + str(storyFetch.NoOfStories(stories)) + " stories:")
	for story in stories.get("data").get("children"):
		DrawFrame.GenerateFrames(story.get("data").get("title"), story.get("data").get("selftext"), story.get("data").get("author_fullname"), externalDadjokecounter)
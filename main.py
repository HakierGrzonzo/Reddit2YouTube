import DrawFrame
import storyFetch
import json
from PIL import Image, ImageDraw, ImageFont
"""
	Naming variable for stories which titles are not compatible with OS file naming requirments,
	so they will be named e.g. "Dadjoke0"
"""
externalDadjokecounter = 0
subreddit = "entitledparents"
mode = "top"
limit = 10


if __name__ == '__main__':

	DrawFrame.settings = DrawFrame.TextFrame(TitleFont = ImageFont.truetype("fonts/Futura Bold font.ttf", 35), TextFont = ImageFont.truetype("fonts/Futura Light font.ttf", 35))
	"""Download .json file from specified subreddit"""
	stories = json.loads(storyFetch.GetStories(subreddit, mode, limit))
	print("fetched " + str(storyFetch.NoOfStories(stories)) + " stories:")
	"""Generate TextFrames for each post, some will not be generated due to errors"""
	for story in stories.get("data").get("children"):
		DrawFrame.GenerateFrames(story.get("data").get("title"), story.get("data").get("selftext"), story.get("data").get("author"), externalDadjokecounter)
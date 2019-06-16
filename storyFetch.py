
import http.client
import json
import time

debug = True

def GetStories(subreddit, mode, limit):
	"""	
		Get raw string json data from {subreddit}, mode specifies sorting (e.g. new, hot),
		limit sets the maximum number of posts returned
	"""
	connection = http.client.HTTPSConnection('www.reddit.com')
	headers = { b'User-Agent' : b'super moody reddit2youtube bot by /u/HakierGrzonzo' }
	connection.request('GET',"/r/" + subreddit + "/" + mode + "/.json?limit="+str(limit), headers)
	response = connection.getresponse()
	return response.read().decode()

def NoOfStories(stories):
	"""Returns number of stories in reddit's .json file"""
	return len(stories.get("data").get("children"))

def printTexts(stories):
	"""Prints post's Title and text to console"""
	print("fetched " + str(NoOfStories(stories)) + " stories:")
	for title in stories.get("data").get("children"):
		print("# " + title.get("data").get("title"))
		if title.get("data").get("selftext") != "":
 			print(title.get("data").get("selftext"))
		print("----------")


# legacy
if __name__ == '__main__':
	stories = json.loads(GetStories("entitledparents", "top", 200))
	if debug:
		print("fetched " + str(NoOfStories(stories)) + " stories:")
	for story in stories.get("data").get("children"):
		GenerateFrames(story.get("data").get("title"), story.get("data").get("selftext"))


	
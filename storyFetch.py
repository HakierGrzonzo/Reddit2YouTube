
import http.client
import json
import time

debug = True

def GetStories(subreddit, mode, limit):
	connection = http.client.HTTPSConnection('www.reddit.com')
	headers = { b'User-Agent' : b'super moody reddit2youtube bot by /u/HakierGrzonzo' }
	connection.request('GET',"/r/" + subreddit + "/" + mode + "/.json?limit="+str(limit), headers)
	response = connection.getresponse()
	return response.read().decode()

def NoOfStories(stories):
	return len(stories.get("data").get("children"))

def printTexts(stories):
	print("fetched " + str(NoOfStories(stories)) + " stories:")
	for title in stories.get("data").get("children"):
		print("# " + title.get("data").get("title"))
		if title.get("data").get("selftext") != "":
 			print(title.get("data").get("selftext"))
		print("----------")

if __name__ == '__main__':
	stories = json.loads(GetStories("tifu", "top", 10))
	printTexts(stories)


	
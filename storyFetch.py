
import http.client
import json
import time
import os
from PIL import Image, ImageDraw

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

def MakeTextFrame(text):
	img = Image.new('RGB', (1920, 1080), color = 'black')
 
	d = ImageDraw.Draw(img)
	d.text((10,10), text, fill= 'white')
 
	return img

def word_wrap(string, width=80, ind1=0, ind2=0, prefix=''):
    """ word wrapping function.
        string: the string to wrap
        width: the column number to wrap at
        prefix: prefix each line with this string (goes before any indentation)
        ind1: number of characters to indent the first line
        ind2: number of characters to indent the rest of the lines
    """
    string = prefix + ind1 * " " + string
    newstring = ""
    while len(string) > width:
        # find position of nearest whitespace char to the left of "width"
        marker = width - 1
        while not string[marker].isspace():
            marker = marker - 1

        # remove line from original string and add it to the new string
        newline = string[0:marker] + "\n"
        newstring = newstring + newline
        string = prefix + ind2 * " " + string[marker + 1:]

    return newstring + string

def GenerateFrames(title, selftext):
	paragraph = word_wrap(selftext, width = 120)
	counter = 0
	if not(os.path.exists("temp/" + title)):
		os.makedirs(("temp/" + title))
	MakeTextFrame(paragraph).save("temp/" + title + "/" + title + str(counter) + ".png")
	if debug:
		print("made paragraph: " + str(counter) + " with length of: " + str(len(paragraph)))

if __name__ == '__main__':
	stories = json.loads(GetStories("tifu", "top", 2))
	if debug:
		print("fetched " + str(NoOfStories(stories)) + " stories:")
	for story in stories.get("data").get("children"):
		GenerateFrames(story.get("data").get("title"), story.get("data").get("selftext"))


	
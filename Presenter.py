import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyttsx3, pickle
from multiprocessing import Process


def plot_graph(*args):
    plt.imshow(args)    
    plt.show()

def FindStories():
	path = "temp/"
	stories = []

	for r, d, f in os.walk(path):
		for file in f:
			if '.pkl' in file:
				stories.append(r)
	print("[INFO:FindStories] Found " +str(len(stories))+ " stories")
	return stories

def PresentStory(StoryPath):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[2].id)

	StoryPath = StoryPath+"/"

	with open(StoryPath+'text.pkl', 'rb') as f:
		Text = pickle.load(f).split("', ")
	count = 1
	engine.say(Text[0])
	try:
		for r, d, f in os.walk(StoryPath):
			for file in f:
				if '.png' in file:
					image = mpimg.imread(os.path.join(r,file))
					engine.say(Text[count])
					p = Process(target=plot_graph, args= image)
					p.start()	
					engine.runAndWait()			
					count = count+1
					p.join()
	except Exception as e:
		print(e)
	




if __name__ == '__main__':
	stories = FindStories()
	for story in stories:
		PresentStory(story)
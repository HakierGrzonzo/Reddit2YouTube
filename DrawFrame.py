import os

from PIL import Image, ImageDraw, ImageFont

debug = False


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

TitleFont = ImageFont.truetype("fonts/Futura Bold font.ttf", 35)
TextFont = ImageFont.truetype("fonts/Futura Light font.ttf", 35)

def MakeTextFrame(title, text, Op):
	"""returns frame with text"""
	img = Image.new('RGB', (1920, 1080), color = 'black')
	d = ImageDraw.Draw(img)
	d.text((20,10), word_wrap(title, width = 80), fill= 'white', font= TitleFont)
	d.text((10,100), text, fill= 'white', font= TextFont)
	d.text((1500,1040), "/u/"+Op+" Reddit2YT", font = TextFont)
 
	return img



def GenerateFrames(title, selftext, Op, externalDadjokecounter):
	"""Generate frames with title, post's text and OP at the bottom"""
	paragraphs = selftext.splitlines()
	counter = 0
	lastparagraph = ""
	print('Attempt to generate story: '+ title)
	try:
		try:
			if not(os.path.exists("temp/" + title)):
				os.makedirs(("temp/" + title))
			path = "temp/" + title + "/" + title
		except Exception as e:
			print("[warn:GenerateFrames] trying fallback dadjoke naming")
			if not(os.path.exists("temp/" + 'dadjoke' + str(externalDadjokecounter))):
				os.makedirs(("temp/" + 'dadjoke' + str(externalDadjokecounter)))
			path = "temp/" + 'dadjoke' + str(externalDadjokecounter) + "/" + 'dadjoke'
			externalDadjokecounter = externalDadjokecounter +1
		
		for paragraph in paragraphs:
			paragraph = word_wrap(paragraph, width = 150)
			if not(len(paragraph) == 0):
				if len(lastparagraph + '\n' + paragraph) > 600:
					MakeTextFrame(title, lastparagraph + '\n' + paragraph, Op).save(path + str(counter) + ".png")
					if debug:
						print("made paragraph: " + str(counter) + " with length of: " + str(len(lastparagraph + '\n' + paragraph)))
					counter = counter +1
					lastparagraph = ""
				else:
					lastparagraph = lastparagraph + '\n' + paragraph
		if lastparagraph != "":
			MakeTextFrame(title, lastparagraph, Op).save(path + str(counter) + ".png")
			if debug:
				print("made paragraph: " + str(counter) + " with length of: " + str(len(lastparagraph)))
			counter = counter +1
			lastparagraph = ""

	except Exception as e:
		print("[ERROR:GenerateFrames] story: '"+title+"' failed to generate frames")
		print(e)

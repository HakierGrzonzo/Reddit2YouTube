import os

from PIL import Image, ImageDraw, ImageFont

debug = True


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
class TextFrame(object):
	"""settings for textframes"""
	resolution = (1920, 1080)
	"""colors"""
	background = 'black'
	textcolor = 'white'
	"""fonts"""
	TitleFont = ImageFont.truetype("fonts/Futura Bold font.ttf", 35)
	TextFont = ImageFont.truetype("fonts/Futura Light font.ttf", 35)
	"""position of textelements"""
	TitlePos = (20, 10)
	TextPos = (10, 100)
	FootPos = (1500, 1040)
	"""Length of text lines in characters, reduce if it goes over the edge"""
	TitleRowLength = 80
	TextRowLength = 150
	TextParagraphLength = 600

	def __init__(self, resolution = (1920, 1080), background = 'black', textcolor = 'white', TitleFont = None, TextFont = None, TitlePos = (20, 10), TextPos = (10, 100) , FootPos = (1500, 1040), TitleRowLength = 80, TextRowLength = 150, TextParagraphLength = 600):
		super(TextFrame, self).__init__()
		self.resolution = resolution
		self.background = background
		self.textcolor = textcolor
		self.TitleFont = TitleFont
		self.TextFont = TextFont
		self.TitlePos = TitlePos
		self.TextPos = TextPos
		self.FootPos = FootPos
		self.TitleRowLength = TitleRowLength
		self.TextRowLength = TextRowLength
		self.TextParagraphLength = TextParagraphLength

settings = TextFrame()

def MakeTextFrame(title, text, Op):
	"""returns frame with text"""
	img = Image.new('RGB', settings.resolution, color = settings.background)
	d = ImageDraw.Draw(img)
	d.text(settings.TitlePos, word_wrap(title, width = settings.TitleRowLength), fill= settings.textcolor, font= settings.TitleFont)
	d.text(settings.TextPos, text, fill= settings.textcolor, font= settings.TextFont)
	d.text(settings.FootPos, "/u/"+Op+" Reddit2YT", fill= settings.textcolor, font = settings.TextFont)
 
	return img



def GenerateFrames(title, selftext, Op, externalDadjokecounter):
	"""Generate textframes with title, post's text and OP at the bottom"""
	"""split text to lines"""
	paragraphs = selftext.splitlines()
	counter = 0
	lastparagraph = ""
	print('Attempt to generate story: '+ title)
	"""Check if target directory exists, if not create it with post's title. If that fails then use dadjokeX naming scheme"""
	try:
		try:
			if not(os.path.exists("temp/" + title)):
				os.makedirs(("temp/" + title))
			path = "temp/" + title + "/" + title
		except Exception as e:
			print("[WARN:GenerateFrames] trying fallback dadjoke naming")
			if not(os.path.exists("temp/" + 'dadjoke' + str(externalDadjokecounter))):
				os.makedirs(("temp/" + 'dadjoke' + str(externalDadjokecounter)))
			path = "temp/" + 'dadjoke' + str(externalDadjokecounter) + "/" + 'dadjoke'
			externalDadjokecounter = externalDadjokecounter +1
		"""
			Group lines to paragraphs (so a minmum length of settings.TextParagraphLength is reached,
			Then wrap lines and than make and save the TextFrame
		"""
		for paragraph in paragraphs:
			paragraph = word_wrap(paragraph, width = settings.TextRowLength)
			if not(len(paragraph) == 0):
				if len(lastparagraph + '\n' + paragraph) > settings.TextParagraphLength:
					MakeTextFrame(title, lastparagraph + '\n' + paragraph, Op).save(path + str(counter) + ".png")
					if debug:
						print("made paragraph: " + str(counter) + " with length of: " + str(len(lastparagraph + '\n' + paragraph)))
					counter = counter +1
					lastparagraph = ""
				else:
					lastparagraph = lastparagraph + '\n' + paragraph
		"""if some text was left but it was to short to trigger previous if statment"""
		if lastparagraph != "":
			MakeTextFrame(title, lastparagraph, Op).save(path + str(counter) + ".png")
			if debug:
				print("made paragraph: " + str(counter) + " with length of: " + str(len(lastparagraph)))
			counter = counter +1
			lastparagraph = ""

	except Exception as e:
		print("[ERROR:GenerateFrames] story: '"+title+"' failed to generate frames")
		print(e)

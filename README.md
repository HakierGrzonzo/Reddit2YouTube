# Reddit2YouTube

* Are you killing yourself with taking screenshots of reddit posts? 
* Do you want to AUTOMATE the content stealing process?

Then this somewhat working thing is for you!

## Features:
- Downloads top Reddit posts from specified subreddit as a .json file
- Automatically make slides with the text, ready to be inserted into your M$ MovieMaker timeline!
- Just add music and voiceover!

## Planned features:
- Automatic Text to speech.
- Repost and duplicate detector.
- Automatic video generation.
- Automatic Youtube uploading, or even streaming!

## Known issues:
- Some random characters in slides.
- Errors due to some encoding errors. 

## How to use:
example implementation in Main.py just look at it
1. Create fonts folder, put some fonts there, declare them like so:
'''
DrawFrame.settings = DrawFrame.TextFrame(TitleFont = ImageFont.truetype("fonts/Futura Bold font.ttf", 35), TextFont = ImageFont.truetype("fonts/Futura Light font.ttf", 35))
"""For more settings look in class declaration!"""
'''
2. Specify target subreddit (without r/), mode (hot, new, top etc) and limit (maximal number of posts) and fetch some stories using 'storyFetch.GetStories'
3. Make some frames using 'DrawFrame.GenerateFrames'
 
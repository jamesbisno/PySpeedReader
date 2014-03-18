import pyglet
from pyglet.gl import *
import pyglet.app.base
import os
import time
import unicodedata
import string

window = pyglet.window.Window(width=335, height=70,resizable = True, vsync = 0)

pyglet.gl.glClearColor(1, 1, 1, 1)
pyglet.gl.glColor3f(0,0,0)
pyglet.gl.glLineWidth(2)
batch = pyglet.graphics.Batch()
batch2 = pyglet.graphics.Batch()

fontType =  'Arial' #'Times New Roman' 

#____________BATCH_1____________________________________

def readerOrient():
	center = int(window.width/2.9)
	lineGap = window.height/8
	pointLineL = int(lineGap * .9)
	fontSize = int(window.height * .37) 
	return center,lineGap,pointLineL,fontSize


center,lineGap,pointLineL,fontSize = readerOrient()

label = pyglet.text.Label("", font_name=fontType,font_size=fontSize,color=(0, 0, 0, 255), x=center - int(fontSize/2.5), y=(window.height//2) + 5, anchor_x='right', anchor_y='center',batch = batch)
label2 = pyglet.text.Label("", font_name=fontType, font_size=fontSize,color=(250, 65, 65,255), x=center, y=(window.height//2) + 5, anchor_x='center', anchor_y='center',batch = batch)
label3 = pyglet.text.Label("", font_name=fontType,font_size=fontSize,color=(0, 0, 0, 255), x= center + int(fontSize/2.5), y=(window.height//2) + 5, anchor_x='left', anchor_y='center',batch = batch)
readerLines = batch.add(8, GL_LINES, None, ('v2i', (lineGap, window.height - lineGap, window.width-lineGap, window.height - lineGap, lineGap, lineGap, window.width-lineGap,lineGap, center, lineGap, center, lineGap + pointLineL, center, window.height-lineGap, center, window.height - lineGap - pointLineL)))
left = pyglet.text.Label("", font_name=fontType,font_size=fontSize/2,color=(0, 0, 0, 255),x=window.width/17, y=window.height/2, anchor_x='center', anchor_y='center', batch = batch)
right = pyglet.text.Label("", font_name=fontType,font_size=fontSize/2,color=(0, 0, 0, 255),x=window.width-(window.width/17), y=window.height/2, anchor_x='center', anchor_y='center', batch = batch)
#____________BATCH_2____________________________________

fontSize2 = int(window.width * .02)

save = pyglet.text.Label("Save", font_name=fontType,font_size=fontSize2,color=(0, 0, 0, 255),x=window.width/5.3, y=window.height/2, anchor_x='right', anchor_y='center', batch = batch2)
load = pyglet.text.Label("Load", font_name=fontType,font_size=fontSize2,color=(0, 0, 0, 255),x=window.width/2.5, y=window.height/2, anchor_x='right', anchor_y='center', batch = batch2)
fontSize2 = fontSize2 * .2
back = pyglet.text.Label("<=100", font_name=fontType,font_size=fontSize2,color=(0, 0, 0, 255),x=window.width/1.625, y=window.height/2, anchor_x='right', anchor_y='center', batch = batch2)
WPMtag = pyglet.text.Label("wpm:", font_name=fontType,font_size=fontSize2,color=(0, 0, 0, 255),x=window.width/1.25, y=window.height/2.2, anchor_x='right', anchor_y='center', batch = batch2)
TrueWPMtag = pyglet.text.Label("", font_name=fontType,font_size=fontSize2,color=(0, 0, 0, 255),x=window.width/1.3, y=window.height/1.5, anchor_x='right', anchor_y='center', batch = batch2)
WPMdisplay = pyglet.text.Label("500", font_name=fontType,font_size=fontSize2*1.2,color=(0, 0, 0, 255),x=window.width/1.015, y=window.height/2.0, anchor_x='right', anchor_y='center', batch = batch2)
arrowKeys = pyglet.text.Label("Use Arrow Keys", font_name=fontType,font_size=fontSize2*.52,color=(0, 0, 0, 255),x=window.width/1.014, y=window.height/1.07, anchor_x='right', anchor_y='center', batch = batch2)

def verts():
	TRx = int((window.width/4.5))
	TRy = int(window.height-(window.height/4.5))

	TLx = int((window.width/20))
	TLy = int(window.height-(window.height/4.5))

	BRx = int((window.width/4.5))
	BRy = int(window.height/4.5)

	BLx = int((window.width/20))
	BLy = int(window.height/4.5)
	return TRx,TRy,TLx,TLy,BRx,BRy,BLx,BLy
	

green = [255,0,127,255,0,127,255,0,127,255,0,127,255,0,127,255,0,127,255,0,127,255,0,127,]
black = ('c3B', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
TRx,TRy,TLx,TLy,BRx,BRy,BLx,BLy = verts()

d = 0 # Distance between buttons
sq1 = batch2.add(8, GL_LINES, None, ('v2i', [TLx,TLy,TRx,TRy,BRx,BRy,BLx,BLy,TLx,TLy,BLx,BLy,TRx,TRy,BRx,BRy]),black)
d = window.width/5
sq2 =batch2.add(8, GL_LINES, None, ('v2i', [int(TLx+d),TLy,int(TRx+d),TRy,int(BRx+d),BRy,int(BLx+d),BLy,int(TLx+d),TLy,int(BLx+d),BLy,int(TRx+d),TRy,int(BRx+d),BRy]),black)
d = window.width/2.5
sq3 = batch2.add(8, GL_LINES, None, ('v2i', [int(TLx+d),TLy,int(TRx+d),TRy,int(BRx+d),BRy,int(BLx+d),BLy,int(TLx+d),TLy,int(BLx+d),BLy,int(TRx+d),TRy,int(BRx+d),BRy]),black)
d = window.width / 1.3
sq4 = batch2.add(8, GL_LINES, None, ('v2i', [int(TLx+d),TLy,int(TRx+d),TRy,int(BRx+d),BRy,int(BLx+d),BLy,int(TLx+d),TLy,int(BLx+d),BLy,int(TRx+d),TRy,int(BRx+d),BRy]),black)
progressBar = batch2.add(4, GL_LINES, None, ('v2i', [-1,3,-2,3,-1,1,-2,1]), ('c3B', [172, 214, 255, 102, 204, 255,172, 214, 255, 102, 204, 255]))

#______END_OF_GRAPHICS____________________________


class Application:
	def __init__(self):
		self.WPM = 500
		self.previousWPM = self.WPM
		self.WPMdivide = 50.0 #reps minutes and not fast enough
		self.count = 0
		
		self.state = False #True is read, False is Pause
		self.reverse = False
		self.brightButton = None
		self.wordslist = [0]
		self.showRealWPM = False
		self.fileLocation = None

	def timeSetter(self,newTime = False):
		if newTime == True:
			pyglet.clock.unschedule(app.timeSetter)
			self.countTracker = 0
			self.countTracker = self.count
			scheduleTimeSetter()
		elif self.state != False:
			if self.showRealWPM == True:
				WPMdisplay.text = str((self.WPM) - ((self.WPM/4) - (self.count - self.countTracker)))
			#print "WPM: ", self.WPM, "True WPM: ", (self.WPM) - ((self.WPM/4) - (self.count - self.countTracker))
			#print "Wordsleft: ", (self.WPM/4) - (self.count - self.countTracker)
			#print "Adjustmnent:", int(self.WPMdivide * ((((self.WPM/4) - (self.count - self.countTracker))/float(self.WPM))))/2
			#print "C: ",self.count, "T: ", self.countTracker
			if self.count - self.countTracker > 0:
				self.WPMdivide -= int(self.WPMdivide * ((((self.WPM/4) - (self.count - self.countTracker))/float(self.WPM))))/2
			#print "WPMdivide: ", self.WPMdivide
			changeClock()
			self.timeSetter(True)


	def makeSaveSpotFolder(self):
		filesList = os.listdir(self.fileLocation)
		if "Bookmarks" not in filesList:
			os.mkdir(self.fileLocation + "/Bookmarks")
		else:
			pass

	def update(self): #Updates Words
		mid = self.wordslist[self.count][1]

		center = int(window.width/2.9)
		fontSize = int(window.height * .37) *.9

		if mid == "i" or mid == "l" or mid == "w" or mid == "m" or mid == "f" or mid == "t" or mid == "r":
			if mid == "i" or mid == "l" or mid == "f" or mid == "t" or mid == "r":
				label.x = center - int(fontSize/4) 
				label3.x = center + int(fontSize/3.5) 
			else:
				label.x = center - int(fontSize/1.75) 
				label3.x = center + int(fontSize/1.75) 
		else:
			label.x = center - int(fontSize/2.5) 
			label3.x = center + int(fontSize/2.5) 
		label.text = self.wordslist[self.count][0]
		label2.text = self.wordslist[self.count][1]
		label3.text = self.wordslist[self.count][2]
		if self.reverse == False and self.count < len(self.wordslist)-1:
			self.count +=1
		elif self.reverse == True and self.WPM != 1 and self.count > 0:
			self.count -= 1
		else: #WPM = 0
			pass

	def PercentRead(self): 
		progress = int(window.width*(float(self.count)/len(self.wordslist)))
		progressBar.vertices = [1,3,progress,3,1,1,progress,1]


#_____Word_Splitting_Rules____________________________Working on file upload
	
#!!!! MUST EDIT !!!! IF WORD IS INSERTED THE FOR STURCTURE MESSES UP
	def ReadableText(self):
		vowels = ["a","e","i","o","u","A","E","I","O","U"]
		
		for root,dirs,files in os.walk(os.path.expanduser("~")):
			if "speed-reader.py" in files:
				self.fileLocation = root
				break
		print self.fileLocation
		os.chdir(self.fileLocation)
		filesList = os.listdir(os.getcwd()) 
		for file in filesList:
			print file
			if "SaveSpot" not in file and ".txt" in file:
					filename = file
					break
		self.filename = filename
		#Make file name an input from users 
		
		
		f = open(filename, 'r')
		w = f.read()
		f.close()
		w = w.decode('UTF-16','replace').encode('ascii', 'ignore')
		#w = w.decode('unicode_escape','replace').encode('ascii', 'ignore')
		w = string.replace(w,"\x00","")
		words = w.split()
		self.wordslist = []
		c = 0
		hyphen = False
		for word in words:
			if ("-" in word or "/" in word) and hyphen == False:
				if "-" in word:
					place = word.find("-")
					words.insert(c+1,word[place:])
					w = word[:place]
				else:
					place = word.find("/")
					words.insert(c+1,word[place:])
					w = word[:place]
				hyphen = True
			else:
				w = word
				if "," in word and hyphen == False: #hyphen is now used for comma detection if revised, add comma and hypen detection at end
					hyphen = True
					words.insert(c+1, word)
				else:
					hyphen = False
			if ("." in word or "?" in word or "!" in word or ":" in word or ";" in word) and hyphen == False:
				words.insert(c+1," ")
				words.insert(c+2," ")
			wordlist = []
			wordlength = len(w)
			# these are the rules the roughly seem to mimic spritz
			if wordlength == 1:
				wordlist = ["",w,""]
			elif wordlength == 2:
				wordlist = [w[0],w[1],""]
			elif 3 <= wordlength <=5:
				wordlist = [w[0],w[1],w[2:]]

			#elif wordlength == 5:
			#	if word[0] in vowels or (word[1] in vowels and word[2] in vowels) :
			#		wordlist = [w[0:2],w[2],w[3:]]
			#	else:
			#		wordlist = [w[0],w[1],w[2:]]
			elif 9 >= wordlength >=6 :
				if w[2] == w[1]:
					wordlist = [w[0:1],w[1],w[2:]]
				else:
					wordlist = [w[0:2],w[2],w[3:]]
			elif 13>= wordlength >= 10:
				if w[3] == w[2]:
					wordlist = [w[0:2],w[2],w[3:]]
				else:
					wordlist = [w[0:3],w[3],w[4:]]
			elif 17>= wordlength >= 14:
				if w[4] == w[3]:
					wordlist = [w[0:3],w[3],w[4:]]
				else:
					wordlist = [w[0:4],w[4],w[5:]]
			elif wordlength >= 18:
				if w[5] == w[4]:
					wordlist = [w[0:4],w[4],w[5:]]
				else:
					wordlist = [w[0:5],w[5],w[6:]]
					
			self.wordslist.append(wordlist)
			c += 1
		self.wordslist.append(["","","END"])

#_____ End_Of_Word_Splitting_______________________  	
    	
    	
    	
@window.event                        
def on_draw():
	if app.state == False:
		window.clear()
		batch2.draw()
	else:
		window.clear()
		pyglet.gl.glColor3f(0,0,0)
		batch.draw()
    
@window.event 
def on_mouse_press(x, y, button, modifiers):
	if app.state == False:
		if (window.width/20 < x < window.width/4.5) and window.height/4.5 < y < window.height-(window.height/4.5): #save
			sq1.colors = green
			s1 = open(app.fileLocation+"/Bookmarks/"+"SaveSpot" + app.filename,"w")
			s1.write(str(app.count-1))
			s1.close()
			app.brightButton = sq1

		elif (((window.width/20) + (window.width/5)) < x < ((window.width/5)+(window.width/4.5))) and window.height/4.5 < y < window.height-(window.height/4.5):#load
			sq2.colors = green
			app.brightButton = sq2
			if app.wordslist == [0]:
				fontSize = int(window.width * .05)
				load.text = "Loading"
				load.font_size = fontSize/1.5
				window.dispatch_event('on_draw')
				window.flip()
				app.ReadableText()
				app.makeSaveSpotFolder()
				load.text = "Load"
				load.font_size = fontSize
			if os.path.isfile(app.fileLocation+"/Bookmarks/"+"SaveSpot" + app.filename) == True:
				s2 = open(app.fileLocation+"/Bookmarks/"+"SaveSpot" + app.filename,"r")
				place = s2.read()
				s2.close()
				app.count = (int(place))
			app.brightButton = sq2
		elif ((window.width/20) + (window.width/2.5) < x < (window.width/2.5)+(window.width/4.5)) and window.height/4.5 < y < window.height-(window.height/4.5):
			sq3.colors = green
			if app.count -100 < 0:
				app.count = 0
			else:
				app.count -= 100
			app.brightButton = sq3
		elif ((window.width/20) + (window.width/1.3) < x < (window.width/1.3)+(window.width/4.5)) and window.height/4.5 < y < window.height-(window.height/4.5):
			fontSize = int(window.width * .05)
			if app.showRealWPM == False:
				app.showRealWPM = True
				TrueWPMtag.text = "True"
			else:
				TrueWPMtag.text = ""
				app.showRealWPM = False
				WPMdisplay.text = str(app.WPM)
		elif y <= 10:
			app.count = int((float(x)/window.width) * len(app.wordslist))
		elif app.wordslist != [0]:
			app.state = True
			if app.WPM != 0:
				app.timeSetter(True)
		else:
			pass
	else:
		if app.WPM == 0:
			if x < label2.x and app.count > 0:
				app.count -= 1
			elif x > label2.x and app.count < len(app.wordslist)-1:
				app.count += 1
			label.text = app.wordslist[app.count][0]
			label2.text = app.wordslist[app.count][1]
			label3.text = app.wordslist[app.count][2]
		else:
			app.state = False


@window.event 
def on_mouse_release(x, y, button, modifiers):
	if app.brightButton == None:
		pass
	else:
		app.brightButton.colors = black[1]
		app.brightButton = None
	
@window.event 
def on_key_press(symbol, modifiers):
	arrowKeys.delete()
	app.timeSetter(True)
	if symbol == 112:
		if app.WPM == 0:
			if app.previousWPM != 0:
				left.text = ""
				right.text = ""
			app.WPM = app.previousWPM
		else:
			app.previousWPM = app.WPM
			app.WPM = 0
		changeClock()
	elif symbol == 44 or symbol == 46:
		if symbol == 44 and app.count > 0:
			app.count -= 1
		elif symbol == 46 and app.count < len(app.wordslist)-1:
			app.count += 1
		label.text = app.wordslist[app.count][0]
		label2.text = app.wordslist[app.count][1]
		label3.text = app.wordslist[app.count][2]
	elif symbol == 65362 or symbol == 65363: #up and right arrow keys
		if app.WPM == 0:
			app.reverse = False
			left.text = ""
			right.text = ""
		app.WPM += 50
		app.previousWPM = app.WPM

		WPMdisplay.text = (str(app.WPM))
		changeClock()
	elif symbol == 65364 or symbol == 65361: #down and left arrow keys
		if app.WPM == 0:
			app.reverse = True 
			left.text = ""
			right.text = ""
		app.WPM += -50
		app.previousWPM = app.WPM

		WPMdisplay.text = (str(app.WPM))
		changeClock()
	if app.WPM == 0:
		app.timeSetter(True)
		pyglet.clock.unschedule(app.timeSetter)
		left.text = "<"
		right.text = ">"

#Working on it
@window.event
def on_resize(width, height):
	glViewport(0, 0, width, height)
	fontSize = int(window.width * .05)
	TRx,TRy,TLx,TLy,BRx,BRy,BLx,BLy= verts()
	d= 0 
	sq1.vertices = [int(TLx+d),TLy,int(TRx+d),TRy,int(BRx+d),BRy,int(BLx+d),BLy,int(TLx+d),TLy,int(BLx+d),BLy,int(TRx+d),TRy,int(BRx+d),BRy]
	d = window.width/5
	sq2.vertices = [int(TLx+d),TLy,int(TRx+d),TRy,int(BRx+d),BRy,int(BLx+d),BLy,int(TLx+d),TLy,int(BLx+d),BLy,int(TRx+d),TRy,int(BRx+d),BRy]
	d = window.width/2.5
	sq3.vertices = [int(TLx+d),TLy,int(TRx+d),TRy,int(BRx+d),BRy,int(BLx+d),BLy,int(TLx+d),TLy,int(BLx+d),BLy,int(TRx+d),TRy,int(BRx+d),BRy]
	d = window.width / 1.3
	sq4.vertices = [int(TLx+d),TLy,int(TRx+d),TRy,int(BRx+d),BRy,int(BLx+d),BLy,int(TLx+d),TLy,int(BLx+d),BLy,int(TRx+d),TRy,int(BRx+d),BRy]
	
	save.font_size = fontSize
	load.font_size = fontSize
	back.font_size = fontSize * .85
	WPMtag.font_size = fontSize *.9
	TrueWPMtag.font_size = fontSize *.9
	WPMdisplay.font_size = fontSize * 1.1
	arrowKeys.font_size = fontSize * .52
	
	save.x = window.width/4.85
	save.y =  window.height/2
	load.x = window.width/2.45
	load.y = window.height/2
	back.x =window.width/1.625
	back.y = window.height/2
	WPMtag.x = window.width/1.25
	WPMtag.y = window.height/2.2
	TrueWPMtag.x =window.width/1.3
	TrueWPMtag.y =window.height/1.5
	WPMdisplay.x = window.width/1.017
	WPMdisplay.y = window.height/2.0
	arrowKeys.x = window.width/1.014
	arrowKeys.y = window.height/1.07
	
	center,lineGap,pointLineL,fontSize = readerOrient()
	fontSize = fontSize*.9
	label.x = center - int(fontSize/2.5) 
	label2.x = center
	label3.x =  center + int(fontSize/2.5)
	label.y, label2.y, label3.y = (window.height/2) + 5,(window.height/2) + 5,(window.height/2) + 5
	label.font_size, label2.font_size, label3.font_size = fontSize,fontSize,fontSize
	readerLines.vertices = [lineGap, window.height - lineGap, window.width-lineGap, window.height - lineGap, lineGap, lineGap, window.width-lineGap,lineGap, center, lineGap, center, lineGap + pointLineL, center, window.height-lineGap, center, window.height - lineGap - pointLineL]
	left.x = window.width/17
	right.x = window.width-(window.width/17)
	left.y,right.y = window.height/2,window.height/2
	left.font_size = fontSize/2
	right.font_size = fontSize/2

def updateStart(dt):
	if app.wordslist == [0]:
		app.state == False
	else:
		pyglet.clock.schedule_interval(update, app.WPMdivide/500)
def update(dt):
	if app.state == True:
		app.update()
	else:
		app.PercentRead()

def scheduleTimeSetter():
	pyglet.clock.schedule_once(app.timeSetter,15)

app = Application()
	
def changeClock():
	pyglet.clock.unschedule(update)
	if app.WPM != 0:
		pyglet.clock.schedule_interval(update, abs(app.WPMdivide/app.WPM))
	
pyglet.clock.schedule_interval(update, app.WPMdivide/500)



class MyEventLoop(pyglet.app.base.EventLoop):

    def idle(self):
        dt = self.clock.update_time()
        redraw_all = self.clock.call_scheduled_functions(dt)
        for window in pyglet.app.windows:
            if redraw_all or (window._legacy_invalid and window.invalid):
                window.switch_to()
                window.dispatch_event('on_draw')
                window.flip()
                window._legacy_invalid = False 
        time.sleep(0.02)     
        return self.clock.get_sleep_time(False)
       
       
    def exit(self):
        pyglet.app.base.EventLoop.exit(self)


def run():
	
    pyglet.app.event_loop = MyEventLoop()
    pyglet.app.run()

run()

        

	

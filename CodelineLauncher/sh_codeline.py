"""
run editor with highlighted line
"""
LOGGING=1
EDITOR_PATH="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"


import sys, os,time
from Tkinter import *
import tkMessageBox
from subprocess import Popen

def log( s ):
     if LOGGING:
        print '[ %s ]  -  %s' % ( time.ctime(), s )
        sys.stdout.flush()

def dispatchButtonHead():
	if not entryWidget.get().strip()=="":
		openEditor(entryWidget.get().strip().replace(".cpp:",".h:").replace(".c:",".h:"))
		
def dispatchButtonCpp():
	if not entryWidget.get().strip()=="":
		openEditor(entryWidget.get().strip())
		
	

		
def drawBox():
	global entryWidget
	root = Tk()
	root.title("Source Code Viewer");
	root["padx"] = 40
	root["pady"] = 20
	
	textFrame = Frame(root)
	
	entryLabel = Label(textFrame)
	entryLabel["text"] = "Enter Path:line#"
	entryLabel.pack(side=LEFT)
	
	entryWidget=Entry(textFrame)
	entryWidget["width"]=50
	entryWidget.pack(side=LEFT)
	
	textFrame.pack()
	
	button_cpp = Button(root,text="cpp" ,default="active", command=dispatchButtonCpp)
	button_header = Button(root,text="header" , command=dispatchButtonHead)
	
	button_cpp.pack()
	button_header.pack()
	root.mainloop()
	
def openEditor(txtLine):
	if os.path.exists(EDITOR_PATH):
		src_line = txtLine.split(":")
		src_line_file=("%s:%s")%(src_line[0],src_line[1])
		src_line_nr=src_line[2]
		cmdParams = (("-n %s \"%s\"") % (src_line_nr,src_line_file))
		log(("%s -n %s %s") % (EDITOR_PATH,src_line_nr,src_line_file))
		syscmd=('""%s" %s"')%(EDITOR_PATH,cmdParams)
		#os.system(syscmd)
		cmd = [EDITOR_PATH,"-n %s" % src_line_nr, src_line_file]
		log( cmd)
		Popen([EDITOR_PATH,"-n %s" % src_line_nr, src_line_file])
		#call([syscmd])

        
		
if __name__ == '__main__':
	if len( sys.argv ) > 1:
		openEditor(sys.argv[1])
	else:
		drawBox()

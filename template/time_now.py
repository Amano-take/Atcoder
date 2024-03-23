import datetime
import pyperclip

pyperclip.copy(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(pyperclip.paste())
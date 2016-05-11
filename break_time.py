import webbrowser
import time

count = 0
print("This program started on "+time.ctime())
while (count < 3):
    time.sleep(5)
    webbrowser.open("http://www.youtube.com")
    count = count + 1

print ("Good bye!")

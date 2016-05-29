import urllib.request
import urllib.parse

def read_text():
    quotes = open("C:\github-repos\Python-Udacity-Programming-Foundations\movie_quotes.txt")
    contents_of_file = quotes.read()
##    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = 'http://www.wdylike.appspot.com'
    values = {'q': text_to_check}
    data = urllib.parse.urlencode(values)
    url = url + '/?' + data
    connection = urllib.request.urlopen(url)
    output = connection.read()
##    print(output)
    connection.close()
    output = output.decode(encoding='UTF-8')

    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document is clean! No curse words were found.")
    else:
        print("Could not scan the document properly.")
    
read_text()

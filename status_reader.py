import csv
import re
import subprocess
import time

def getText():
    searchlist = ['image 1']
    history =[]
    pattern = re.compile("|".join(searchlist))
    with open("conversation.log") as f:
    for line in f:
      if re.search(pattern, line):
        history.append(line)
      else:
        pass
    return history
    
while True:
    raw_history = getText()
    history = raw_history[-1].replace("image 1:", "")
    print history
    command = 'gtts-cli.py "%s" -l "en" -o convo.mp3 && play convo.mp3' % history
    subprocess.call(command, shell=True)
    time.sleep(1)

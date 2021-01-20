import schedule
from time import sleep


def join(subject):
    subject = str(subject)
    print("joined", subject)
    webbrowser.open(subject)


info = open("everyday joiner.txt", 'r+', encoding='ascii')
info = info.readlines()
infostr = ''
for i in range(len(info)):
    infostr += info[i]
infostr = infostr.replace(' ', '')
info = infostr
info = info.split('\n')
schedule.every().day.at(info[0]).do(join, info[1])


while True:
    schedule.run_pending()

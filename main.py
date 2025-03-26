import webbrowser
import time
import datetime
import pause
from datetime import datetime

hsc = "https://pcadobeconnect.stanford.edu/r4tu0gse1obp/"
wellness = "https://pcadobeconnect.stanford.edu/rpou6wauczx0/"
english = "https://pcadobeconnect.stanford.edu/rsvnaoo7tmpu/"
svc = "https://pcadobeconnect.stanford.edu/roskzg3ndq4u/"
physics = "https://pcadobeconnect.stanford.edu/rjep7k4p15q1/"
chem = "https://pcadobeconnect.stanford.edu/r9n6oldrue7v/"



chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'


year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
weekday = datetime.now().weekday

def open(url):
    webbrowser.get(chrome_path).open(url)


if weekday == 0 or weekday == 2: #monday or wednesday
    pause.until(datetime(year, month, day, 8, 55))
    open(hsc)
    if weekday == 0:
        pause.until(datetime(year, month, day, 10, 10))
        open(wellness)
    pause.until(datetime(year, month, day, 12, 40))
    open(english)

elif weekday == 1 or weekday == 3: #tuesday or thursday
    pause.until(datetime(year, month, day, 8, 55))
    open(svc)
    pause.until(datetime(year, month, day, 12, 40))
    open(physics)
    pause.until(datetime(year, month, day, 13, 55))
    open(chem)





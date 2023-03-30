import urllib.request, time, ssl
from bs4 import BeautifulSoup

one_88 = 'https://ttcbustracker.com/BusData.aspx?stopno=12120&busnum0=188&direction0=188-Kipling+South+Rocket&agency=ttc'
forty_four = 'https://ttcbustracker.com/BusData.aspx?stopno=12120&busnum0=44&direction0=44-Kipling+South&agency=ttc'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def grab_one_88():
    with urllib.request.urlopen(one_88, context=ctx) as url:
        s = url.read()

    express_web = BeautifulSoup(s, "html.parser")

    one_88_scraped = express_web.find_all('span', class_='ui-li-count ui-btn-up-c ui-btn-corner-all')

    one_88_times, filtered_times = [], []
    if len(one_88_scraped) > 0:
        for i in range(len(one_88_scraped)):
            one_88_times.append(str(one_88_scraped[i]))
        def filter (string):
            for i in range(len(string)):
                cut_string = string[i].split("\r\n                                ")
                new_string = cut_string[1].split(" ")
                if new_string[0] == '0':
                 filtered_times.append("DUE | ")
                elif i == 2:
                    filtered_times.append(new_string[0] + " min")
                else:
                    filtered_times.append(new_string[0] + " min | ")

        if filter(one_88_times) != None:
            filter(one_88_times)
        return filtered_times
    else:
        return "'Not Scheduled'"

def grab_forty_four():
    with urllib.request.urlopen(forty_four, context=ctx) as url:
        t = url.read()

    normal_web = BeautifulSoup(t, 'html.parser')

    forty_four_scraped = normal_web.find_all('span', class_='ui-li-count ui-btn-up-c ui-btn-corner-all')

    forty_four_times, filtered_times = [], []

    for i in range(len(forty_four_scraped)):
        forty_four_times.append(str(forty_four_scraped[i]))

    if len(forty_four_scraped) > 0:
        def filter (string):
            for i in range(len(string)):
                cut_string = string[i].split("\r\n                                ")
                new_string = cut_string[1].split(" ")
                if new_string[0] == '0':
                     filtered_times.append("DUE | ")
                elif i == 2:
                    filtered_times.append(new_string[0] + " min")
                else:
                    filtered_times.append(new_string[0] + " min | ")

        filter(forty_four_times)
        return filtered_times
    else:
        return "'Not Scheduled'"

while True:
    time.sleep(5)
    write_188 = open("188_times.txt", "w")
    write_44 = open("44_times.txt", "w")
    print(str(grab_one_88()))
    print(str(grab_forty_four()))
    write_188.write(str(grab_one_88()))
    write_44.write(str(grab_forty_four()))
    write_188.close()
    write_44.close()

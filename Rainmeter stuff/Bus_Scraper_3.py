import urllib.request, time
from bs4 import BeautifulSoup

nine_44 = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=ttc&stopId=12120&routeTag=944'
forty_four = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=ttc&stopId=12120&routeTag=44'

def grab_nine_44():
    nine_44_times, filtered_times = [], []
    with urllib.request.urlopen(nine_44) as url:
        s = url.read()
    express_web = BeautifulSoup(s, "html.parser")

    for data in express_web.find_all("prediction"):
        nine_44_times.append(data["minutes"])

    if len(nine_44_times) > 0:
        def filter (string):
            if len(string) >= 3:
                for i in range(3):
                    if string[i] == '0':
                         filtered_times.append("DUE | ")
                    elif i == 2:
                        filtered_times.append(string[i] + " min")
                    else:
                        filtered_times.append(string[i] + " min | ")
            else:
                for i in range(len(string)):
                    if string[i] == '0':
                         filtered_times.append("DUE | ")
                    elif i == 2:
                        filtered_times.append(string[i] + " min")
                    else:
                        filtered_times.append(string[i] + " min | ")


        if filter(nine_44_times) != None:
            filter(nine_44_times)
        return filtered_times
    else:
        return "'Not Scheduled'"

def grab_forty_four():
    forty_four_times, filtered_times = [], []
    with urllib.request.urlopen(forty_four) as url:
        t = url.read()
    normal_web = BeautifulSoup(t, 'html.parser')
    
    for data in normal_web.find_all("prediction"):
        forty_four_times.append(data["minutes"])

    if len(forty_four_times) > 0:
        def filter (string):
            if len(string) >= 3:
                for i in range(3):
                    if string[i] == '0':
                         filtered_times.append("DUE | ")
                    elif i == 2:
                        filtered_times.append(string[i] + " min")
                    else:
                        filtered_times.append(string[i] + " min | ")
            else:
                for i in range(len(string)):
                    if string[i] == '0':
                         filtered_times.append("DUE | ")
                    elif i == 2:
                        filtered_times.append(string[i] + " min")
                    else:
                        filtered_times.append(string[i] + " min | ")

        if filter(forty_four_times) != None:
            filter(forty_four_times)
        return filtered_times
    else:
        return "'Not Scheduled'"

write_944 = open("944_times.txt", "w")
write_44 = open("44_times.txt", "w")
print(str(grab_nine_44()))
print(str(grab_forty_four()))
write_944.write(str(grab_nine_44()))
write_44.write(str(grab_forty_four()))
write_944.close()
write_44.close()

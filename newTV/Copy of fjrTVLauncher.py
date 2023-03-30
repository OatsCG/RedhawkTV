import os
#command thats run: "/Program Files/Google/Chrome/Application/chrome.exe" file:///C:/Users/Redmond/Google%20Drive/School%20TV%20Things/newTV/tvs.html --allow-file-access-from-file --disable-web-security --user-data-dir=/Users/Redmond/chromeServerTest
os.popen('"/Program Files/Google/Chrome/Application/chrome.exe"' + " file:///C:/Users/Redmond/Google%20Drive/School%20TV%20Things/newTV/tvs.html --allow-file-access-from-file --disable-web-security --user-data-dir=" + "/Users/Redmond/chromeServerTest");
print("fjrTV loaded. you may close this window");
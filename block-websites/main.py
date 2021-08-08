'''This program is written for blocking the some specific URL for specific
    period, after that period is over you can access those wesites.'''


import time
from datetime import datetime

website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]   # sites you wanted to block
hosts_file = r"C:\Windows\System32\Drivers\etc\hosts"  # path of windows host file
redirect = "127.0.0.1"  # redirecting to some other local IP

while True:
    # fixed the time from when to when your blocker should work
    from_fixing = datetime.now().replace(hour=12, minute=00, second=00)
    to_fixing = datetime.now().replace(hour=17, minute=00, second=00)
    from_fixed, to_fixed = from_fixing.strftime("%X"), to_fixing.strftime("%X")
    current_time = datetime.now().strftime("%X")

    # ths condition will execute and block if you are in blocked time
    if from_fixed < current_time < to_fixed:
        with open(hosts_file, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    # this condition will remove the blocked website if you are not in blocked time
    else:
        with open(hosts_file, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(60)

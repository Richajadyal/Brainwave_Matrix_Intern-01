import re

def is_phishing(url):
    blacklist = [
        'phishingsite.com',
        'evilhackersite.org',
        'scammy.biz',
        'blackbox.ai'

    ]

    for domain in blacklist:
        if domain in url:
            return True
    
    patterns = [
        'https?:\/\/([^\s\.]+\.[^\s]{2,}|login\.|signin\.|secure\.|bank\.|account\.)'
    ]
    
    for pattern in patterns:
        if re.search(pattern, url, re.IGNORECASE):
            return True
    
    return False

url1 = "https://phishingsite.com/login"
url2 = "http://legit-site.com"
url3 = "https://secure.scammy.biz"
url4 = "https://www.blackbox.ai/chat/wNHVpuM"


print(f"{url1} is phishing: {is_phishing(url1)}")
print(f"{url2} is phishing: {is_phishing(url2)}")
print(f"{url3} is phishing: {is_phishing(url3)}")
print(f"{url4} is phishing: {is_phishing(url4)}")



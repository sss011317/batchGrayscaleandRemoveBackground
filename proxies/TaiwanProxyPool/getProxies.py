# coding=utf-8
 
import requests
import re
from bs4 import BeautifulSoup as bs
import Queue
import threading
import random
import re
 
headers_useragents = []
headers_referers = []
headers_referers.append('http://www.google.com/?q=')
headers_referers.append('http://www.usatoday.com/search/results?q=')
headers_referers.append('http://engadget.search.aol.com/search?q=')
headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
headers_useragents.append(
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
headers_useragents.append(
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
headers_useragents.append(
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
headers_useragents.append(
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
headers_useragents.append(
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
headers_useragents.append(
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
 
 
class proxyPick(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue
 
    def run(self):
        while not self._queue.empty():
            url = self._queue.get()
 
            proxy_spider(url)
 
 
def proxy_spider(url):
    headers = {
        #  .......
    }
    headers['User-Agent'] = random.choice(headers_useragents)
    headers['Cache-Control'] = 'no-cache'
    headers['Accept-Charset'] = 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
    headers['Referer'] = random.choice(headers_referers) + str(random.randint(5, 10))
    headers['Keep-Alive'] = str(random.randint(110, 120))
    headers['Connection'] = 'keep-alive'
    r = requests.get(url=url, headers=headers)
    soup = bs(r.content, "html.parser")
    data = soup.find_all(name='tr', attrs={'class': re.compile('|[^odd]')})
 
    for i in data:
        soup = bs(str(i), 'html.parser')
        data2 = soup.find_all(name='td')
        ip = str(data2[1].string)
        port = str(data2[2].string)
        types = str(data2[5].string).lower()
 
        proxy = {}
        proxy[types] = '%s:%s' % (ip, port)
        print proxy, " check proxy"
        try:
            proxy_check(proxy, ip)
        except Exception, e:
            print e
            pass
 
 
def proxy_check(proxy, ip):
    # url = 'http://1212.ip138.com/ic.asp'
    # url = 'https://www.ipip.net/ip.html'
    # url = 'http://www.baid.com'
    # url = 'http://ip138.com/'
    url = 'http://2018.ip138.com/ic.asp'
    r = requests.get(url=url, proxies=proxy, timeout=6)
    # r.encoding = 'gb2312' for url = 'http://ip138.com/'
    reip = r'\[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]'
    # print r.text
    f = open('ip_proxy.txt', 'a+')
    found = re.search(reip, r.text, re.M | re.I)
    if found:
        ip2 = found.group(1)
        print "ip==> : ", ip2
        if ip2 == ip:
            print "*" * 30
            print "ip is wanted:", ip
            f.write('%s' % proxy + '\n')
            print "*" * 30
    # import sys
    # sys.exit(0)
    f.close()
 
 
# proxy_spider()
 
def main():
    queue = Queue.Queue()
    for i in range(1, 2288):
        queue.put('http://www.xicidaili.com/nn/' + str(i))
 
    threads = []
    thread_count = 10
 
    for i in range(thread_count):
        spider = proxyPick(queue)
        threads.append(spider)
 
    for i in threads:
        i.start()
 
    for i in threads:
        i.join()
 
    print "It's down,sir!"
 
 
if __name__ == '__main__':
    main()
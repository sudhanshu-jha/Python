import urllib2
import re
import subprocess
import os

# URL to the product
flipkart_url = 'https://www.flipkart.com/redmi-note-5-pro-black-64-gb/p/itmf2fc3xgmxnhpx?pid=MOBF28FTQPHUPX83&srno=s_1_1&otracker=search&lid=LSTMOBF28FTQPHUPX83H7IIOZ&fm=SEARCH&iid=afc34371-4d80-444a-8d9a-77969cbdb9cc.MOBF28FTQPHUPX83.SEARCH&ppt=Search%20Page&ppn=Search%20Page&ssid=oqpty1bs2effc1z41524409085264&qH=987d10732f9d31f0'

flipkart_fetch = urllib2.urlopen(flipkart_url).read()

product = re.findall('This item is currently out of stock', flipkart_fetch);

if len(product) == 0: 
	message = "The Product is back in stock at Flipkart "
	os.system('spd-say "The Product is back in stock at Flipkart"')
	
else:
	message = "Product is not available yet"
	os.system('spd-say "Product is not available yet"')

subprocess.Popen(['notify-send', message])

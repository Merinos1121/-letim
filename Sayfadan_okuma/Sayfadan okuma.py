import urllib.request
import re

webUrl = urllib.request.urlopen('https://www.york.ac.uk/teaching/cws/wws/webpage1.html')

if webUrl.getcode() == 200:
	data = str(webUrl.read())

	reg_str = ">(.*?)</"
	res = re.findall(reg_str, data)

	print(str(res))

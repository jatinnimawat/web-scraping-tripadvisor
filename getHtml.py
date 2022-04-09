from urllib.request import urlopen

url = "https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html"
page = urlopen(url)
byteFormat = page.read()
htmlCode = byteFormat.decode("utf-8")

fp = open("newFile.txt", "w")
fp.write("This is a new file.")
fp.close()

print("\ndone\n")
import urllib2
import threading
import re
from bs4 import BeautifulSoup

Threads = []
f = open("DeceptionPoint",'ab+');
freq = open("DeceptionPointFreq",'ab+');
word_freq_hash = {}

def prepare_list_amazon(soup):
  pattern = re.compile('([a-zA-Z]+)')

	Rtable = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="productReviews").tr.td
	text = str(Rtable.encode('utf-8'))
	for rev in text.split("<!-- BOUNDARY -->"):
		for line in re.split('<.*>',rev):
			if len(line) is 0 or len(line) is 1:
				continue
			if line[0] is '\n':
				continue
			array = re.findall(pattern,line)
			for string in array:
				if string in word_freq_hash:
					word_freq_hash[string]+=1
				else :
					word_freq_hash[string]=1
				
				#print string
			
			f.write(line)
	
	
def crawl(addr):
	html = urllib2.urlopen(addr).read();
	prepare_list_amazon(BeautifulSoup(html))
	
	
if __name__ == "__main__":
	addr = raw_input()
	n = raw_input()	
	n = int(n)
	temp = addr.split("pageNumber=")[0]
	temp += "pageNumber="
	last = addr.split("pageNumber=")[1][1:]
	index = len(temp)
	
	m=1
	while m != n:
		for t in range(1, 10) :
			addr = temp + str(m) + last
			thread  = threading.Thread(target = crawl, args = (addr, ))
			thread.start()
			Threads.append(thread)
			print "\n From:Thread: " + str(t) + " and Web Address: "+addr+" \n "

			print "Waiting"
			
			for thread in Threads:
				thread.join()
				
			print "Complete"
			
			if(m == n):
				break
				
			m+=1
	for k,v in word_freq_hash.iteritems():
		print " %-45s %-15s %15s" % (k, "=>", str(v))
		freq.write(" %-45s %-15s %15s\n" % (k, "=>", str(v)))

	

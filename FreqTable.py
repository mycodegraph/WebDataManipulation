from bs4 import BeautifulSoup
import threading
import urllib2
import os
import time
import re
import stat
import sys


Threads = []
word_freq_hash = {}


def prepare_list_amazon(file, soup):
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
				string = string.lower()
				if string in word_freq_hash:
					word_freq_hash[string]+=1
				else :
					word_freq_hash[string]=1	
			file.write(line)
			
	
def crawl(file, addr):
	proxy_support = urllib2.ProxyHandler({"http":"http://xxx.xxx.xx.xx:80"}) #Proxy address
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	html = urllib2.urlopen(addr).read();
	prepare_list_amazon(file, BeautifulSoup(html))

	
	
if __name__ == "__main__":
	# Program start time
	start_time = time.clock()
	
	#Amazon product review page( > 2) URL and No. of pages to fetch
	addr = raw_input()
	n = int(raw_input())		
	
	#Creation of file
	temp = addr.split("/")[3]	
	flag = 0
	for folder in os.listdir('.'):
		if folder == temp:
			flag = 1
	
	if flag != 1:
		os.makedirs(temp)
		
	if flag == 1:
		os.remove(temp+"\\"+temp)
		os.remove(temp+"\\"+temp + "-Freq")
	
	file = open(temp+"\\"+temp,'ab+')
	freqFile = open(temp+"\\"+temp + "-Freq",'ab+')
	
	#Partitioning page URL to create new every time for every page
	temp = addr.split("pageNumber=")[0]
	temp += "pageNumber="
	last = addr.split("pageNumber=")[1][1:]
	
	
	m=0
	while m <= n:
		#Creating 10 threads to fetch network data and print it to the file
		for t in range(1, 10) :
			addr = temp + str(m) + last
			thread  = threading.Thread(target = crawl, args = (file, addr, ))
			thread.start()
			Threads.append(thread)
			
			print "\nFrom:Thread: " + str(t) + " and Web Address: " + addr
			print "Waiting"	
			m+=1
			if(m > n):
				break	
			
		#joining threads; although not required but generally with so many threads fetching data from amazon server,
		#leads to "Server blocking request"	
		for thread in Threads:
			thread.join()
			
		print "Complete"
			
			
	for k,v in word_freq_hash.iteritems():
		freqFile.write(" %-45s %-15s %15s\n" % (k, "=>", str(v)))
		
		
	# Following code might give error beacuase it has been added recently in this file without running locally.
	##	* Here for each product review, we are calculating "Document/review frequency for all the words"
	##	* Then we calculate "Inverse Document Frequency for all the words" using idf = log(N/df)
	##	* 
	##
	##
	##
	
		
	################################################################
	
	idfFile.write(" %-45s %-15s %15s %15s %15s %15s %15s\n" % ("String", "=>", "DF"," ", "Review No."," ","IDF"))
	for k,v in word_idf.iteritems():
		idfFile.write(" %-45s %-15s %15s %15s %15s %15s %15s\n" % (k, "=>", str(v[0])," ", str(v[1])," ", str(math.log(no_reviews[0]/v[0],10))))	
		
	rev_vec = []
	max = 0
	for h in rev_list:
		vec = []
		for k,v in h.iteritems():
			#print math.log(no_reviews[0]/word_idf[k][0],10)
			val = math.log(no_reviews[0]/word_idf[k][0],10)
			revFile.write(" %-45s %-15s %15s %15s %15s\n" % (k, "=>", str(v)," ",val));
			vec.append(val)
		if max < len(vec):
			max = len(vec)
		rev_vec.append(vec)
		revFile.write("\n\n")		
	
	final = []
	for i in range(0,no_reviews[0]):
		final.append([0 for _ in range(0,no_reviews[0])])
		if len(rev_vec[i]) != max:
			while len(rev_vec[i]) != max:
				rev_vec[i].append(0)
	
	for i in range(0,no_reviews[0]):
		magA = numpy.linalg.norm(rev_vec[i])
		for j in range(0,no_reviews[0]):
			if i != j:
				d = numpy.dot(rev_vec[i],rev_vec[j])
				magB = numpy.linalg.norm(rev_vec[j])
				den  = (magA*magB)
				if den != 0:
					final[j][i] = final[i][j] = d/(magA*magB)
				else:
					final[j][i] = final[i][j] = 0
					
	for row in range(0,no_reviews[0]):
		for col in range(0,no_reviews[0]):
			matFile.write("%s " % (str(final[row][col])));
		matFile.write(" \n ");
	
	################################################################
		
		
		
		
		
# The below code is part of Dictionary search and Spell Checker, which consider product reviews as corpus (just trial implementation) 
	
	
	# This code calculates the edit distance values for all strings in frequency table against the input string and 
	# prints the one with least "edit distance"
	string1 = raw_input()	
	min = sys.maxint
	temp=" "
	for k,v in word_freq_hash.iteritems():
		#print " %-45s %-15s %15s" % (k, "=>", str(v))
		
		string2 = k
		matrix = []
		val=0
		
		for row in range(0,len(string1)+1):
			matrix.append([0 for _ in range(0,len(string2)+1)])

		val =  edit_cost(string1, string2, len(string1)-1, len(string2)-1,matrix)
		if val < min:
			temp = string2
			min = val
				
	print temp +" "+str(min)
	
	#--------------------------------------------------------->
		
	#create_optimal_bst(len(word_freq_hash))
	print time.clock() - start_time

	

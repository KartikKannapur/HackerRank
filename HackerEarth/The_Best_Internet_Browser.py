__author__ = "Kartik Kannapur"

tc = raw_input()

for i in range(0, int(tc)):
	url = raw_input()[4:-4]
	
	n_browser = 4 + len(url) + 4
	
	url_no_vowel = (''.join(char for char in url if char not in set('aeiouAEIOU')))
	j_browser = len(url_no_vowel) + 4
	
	print str(j_browser) + "/" + str(n_browser)

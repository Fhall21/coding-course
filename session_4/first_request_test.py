import requests, bs4

with open('results.txt', 'w+') as file:
	file.write('Cineplex Movie Web Scrapper:')
for movie_num in range(2100, 2400):
	url = 'https://cineplex.com.au/movie/' + str(movie_num)

	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	body = soup.body

	try:
		h2_item = body.select(".movie-header > h2")[0]
		h2_item_str = str(h2_item)[4:-5]

	except:
		print ('something went wrong')
	else:
		print (h2_item_str)
		with open('results.txt', 'a+') as file:
			file.write('\n' + h2_item_str)
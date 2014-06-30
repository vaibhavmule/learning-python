def print_all_link(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break
	print get_page('http://xkcd.com/353')
	print_all_link(get_page('http://xkcd.com/353'))
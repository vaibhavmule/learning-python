def get_next_target(page):
	start_link = page.find('<a href=')
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote

print get_next_target('this is a <a href="http://udacity.com">link!</a>')
url, endpos = get_next_target('Not "good" at all!'>link!</a>)
if url:
	print "Here!"
else:
	print "Not here!"
print url
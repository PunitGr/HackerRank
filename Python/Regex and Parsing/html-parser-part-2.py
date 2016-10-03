#!/usr/local/bin/python3
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	def handle_comment(self, data):
		print(">>> Multi-line Comment" if "\r" in data else ">>> Single-line Comment")
		print(data.replace("\r","\n"))
	def handle_data(self, data):
		if data.strip():
			print(">>> Data")
			print(data)

parser = MyHTMLParser()
html = ''
for _ in range(int(input())):
	html += input()
parser.feed(html)
parser.close()


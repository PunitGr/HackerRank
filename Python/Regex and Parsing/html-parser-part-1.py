#!/usr/local/bin/python3
from html.parser import HTMLParser

class HTML_Parser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print("Start : "+ tag)
		for e in attrs: print("-> " + e[0] + " > " + str(e[1]))
	def handle_endtag(self, tag):
		print("End   : " + tag)
	def handle_startendtag(self, tag, attrs):
		print("Empty : " + tag)
		for e in attrs: print("-> " + e[0] + " > " + str(e[1]))

parser = HTML_Parser()
for _ in range(int(input())):
	parser.feed(input())

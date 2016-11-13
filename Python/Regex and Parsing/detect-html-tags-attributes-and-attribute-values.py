#!/usr/local/bin/python3
from html.parser import HTMLParser


class HtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print('->', ' > '.join(attr))


parser = HtmlParser()

html = ''
n = int(input())
for i in range(n):
    html += input() + '\n'
parser.feed(html)


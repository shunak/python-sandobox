import lxml.html
tree = lxml.html.parse('c_index.html')
html = tree.getroot()

for a in html.cssselect('A'):
    print(a.get('href'),a.text)

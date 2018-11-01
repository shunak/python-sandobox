import lxml.html
import cssselect

# input what you want to pase at #### 
tree = lxml.html.parse('./####.html')

html = tree.getroot()

for a in html.cssselect('a'):
    print(a.get('href'), a.text)







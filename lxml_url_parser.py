#################################
# parses inserted xml data and  #
# stores attributes (here URLs) #
# into a .txt file              #
#################################

from lxml import etree
xmllines = '''
  < **xml** >
'''

myfile = open('urls_total.txt', 'w') 

for line in xmllines.strip().splitlines():
    doc = etree.fromstring(line)
    urls = doc.xpath('/photo/@url_o')
    if urls:
        url = urls[0]
        print url
    else:
        print '------ no URL found ------'
    myfile.write('%s\n' % urls)

myfile.close()

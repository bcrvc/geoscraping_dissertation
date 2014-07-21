from lxml import etree
xmllines = '''
  < **xml** >
'''

for line in xmllines.strip().splitlines():
    doc = etree.fromstring(line)
    urls = doc.xpath('/photo/@url_n')
    if urls:
        url = urls[0]
        print url
    else:
        print '---no URL attribute found---'
